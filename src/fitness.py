from dataclasses import dataclass
from functools import reduce
from itertools import chain
from typing import Tuple

from more_itertools import pairwise

from src.metadata import extrair_dados, get_horarios
from src.modelos import Disciplina, MetaData, Professor, Sala

CHOQUE_SALA = -30
CHOQUE_PROF = -30
CHOQUE_GRADE = -30
AULAS_MESMO_DIA = -30
CHOQUE_LABORATORIOS = -30
AULAS_DIAS_SEGUIDOS = -20
CHOQUE_DISCIPLINAS = -10
AULAS_AOS_SABADOS = -10
MAX_MIN_HORAS = -10
MUDANCA_DE_TURNO = -8
NUM_DISCIPLINA_POR_LAB = 2
DISTANCIA_ENTRE_SALAS = -2e-3


@dataclass
class Partial_Fitnesses:
    choque_salas: int = 0
    choque_professor: int = 0
    choque_grade: int = 0
    choque_laboratorios: int = 0
    choque_disciplinas: int = 0
    mesmo_turno: int = 0
    max_min_horas_professor: int = 0
    afinidade_professor_disciplina: int = 0
    afinidade_professor_horarios: int = 0
    afinidade_professor_salas: int = 0
    afinidade_salas_horarios: int = 0
    aulas_no_mesmo_dia: int = 0
    aulas_em_dias_seguidos: int = 0
    aulas_aos_sabados: int = 0
    distancia_percorrida: float = 0

    def sum(self):
        acumulador = 0
        for key in self.__dataclass_fields__:
            acumulador += getattr(self, key)
        return acumulador

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return self.sum() <= other.sum()

    def __lt__(self, other):
        return self.sum() < other.sum()

    def __eq__(self, other):
        return self.sum() == other.sum()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self) -> str:
        rep = 'Fitnesses: {}\n'.format(self.sum())
        fields = [f'{field}: {getattr(self, field)}'
                  for field in self.__dataclass_fields__]
        return rep + '\n'.join(fields)


class Fitness:

    def __init__(self, metadata: MetaData = None):
        if metadata is not None:
            self.metadata = metadata

    def __call__(self, individuo) -> Tuple[int, Partial_Fitnesses]:
        """
        Calcula o fitness de um indivíduo.
        """
        self.prof_horas = []
        self.grade_horas = []
        self.horas_professor = {
            prof.nome: 0 for prof in self.metadata.professores
        }
        self.salas_hora_disciplinas = {
            lab.nome: {
                hora: []
                for hora in range(60)
            } for lab in self.metadata.salas
        }
        self.grade_dia_sala = {
            grade: {
                turno: []
                for turno in range(12)
            } for grade in self.metadata.grades
        }

        fit = Partial_Fitnesses()
        for disciplina in self.metadata.disciplinas.values():
            disciplina: Disciplina

            (i_p, i_s, i_l, i_h,
             salas, laboratorios,
             qtd_horas, horarios,
             grades, professor) = extrair_dados(self.metadata, disciplina, individuo)

            fit.choque_grade += self.fit_choque_grade(grades, horarios)
            fit.choque_laboratorios += self.fit_choque_laboratorios(laboratorios,
                                                                    horarios,
                                                                    disciplina.nome)

            fit.mesmo_turno += self.fit_mesmo_turno(i_h)
            fit.aulas_no_mesmo_dia += self.fit_aulas_no_mesmo_dia(i_h)
            fit.aulas_aos_sabados += self.fit_aulas_aos_sabados(i_h)
            fit.aulas_em_dias_seguidos += self.fit_aulas_em_dias_seguidos(i_h)

            if not disciplina.sem_sala:
                fit.choque_salas += self.fit_choque_salas(salas,
                                                          horarios,
                                                          disciplina.nome)
                fit.afinidade_salas_horarios += self.fit_afinidade_salas_horarios(
                    salas, horarios)
                self.adicionar_grade_dia_sala(salas, horarios, grades)

            if not disciplina.sem_professor:
                fit.afinidade_professor_disciplina += self.fit_afinidade_professor_disciplina(
                    professor, disciplina.nome)
                fit.choque_professor += self.fit_choque_profe(professor,
                                                              horarios)
                fit.afinidade_professor_horarios += self.fit_afinidade_professor_horarios(
                    professor, horarios)
                fit.afinidade_professor_salas += self.fit_afinidade_professor_salas(
                    professor, salas)
                self.contabilizar_horas_professor(professor, disciplina.horas)

        fit.distancia_percorrida += self.fit_distancia_percorrida()
        fit.choque_disciplinas += self.fit_choque_disciplinas(individuo)
        fit.max_min_horas_professor += self.fit_max_min_horas_professor()

        return fit.sum(), fit

    def fit_max_min_horas_professor(self):
        fit = 0
        for prof in self.metadata.professores:
            if self.horas_professor[prof.nome] < prof.hrs_min:
                error = abs(self.horas_professor[prof.nome] - prof.hrs_min)
                fit += MAX_MIN_HORAS * error
            elif self.horas_professor[prof.nome] > prof.hrs_max:
                error = abs(self.horas_professor[prof.nome] - prof.hrs_max)
                fit += MAX_MIN_HORAS * error
        return fit

    def contabilizar_horas_professor(self, professor: Professor, horas):
        self.horas_professor[professor.nome] += sum(horas)

    def fit_choque_profe(self, profe: Professor, horarios: list[list[int]]):
        """Verifica se o professor está ocupada no horário"""
        fit = 0
        nome_professor = profe.nome
        for h in chain(*horarios):
            tag = f'{nome_professor}{h}'
            if tag in self.prof_horas:
                fit += CHOQUE_PROF
            else:
                self.prof_horas.append(tag)
        return fit

    def fit_choque_grade(self, grades: list[str], horarios: list[list[int]]):
        """Verifica se a turma está com 2 ou mais aulas no horário"""
        fit = 0
        for h in chain(*horarios):
            for grade in grades:
                tag = f'{grade}{h}'
                if tag in self.grade_horas:
                    fit += CHOQUE_GRADE
                else:
                    self.grade_horas.append(tag)
        return fit

    def fit_mesmo_turno(self, ini_horas):
        """ Verifica se os horários da aula são no mesmo turno """
        turnos = map(lambda i: bool(int(i / 5) % 2), ini_horas)
        mudanca_turno = reduce(lambda x, y: x != y, turnos,)
        return MUDANCA_DE_TURNO if mudanca_turno else 0

    def fit_choque_laboratorios(self, laboratorios: list[Sala],
                                horarios: list[list[int]],
                                nome_disciplina: str):
        """
        Verifica se o laboratório está ocupado no horário por
        mais de NUM_DISCIPLINA_POR_LAB disciplinas
        """
        fit = 0
        for lab, _horarios in zip(laboratorios, horarios):
            for h in _horarios:
                sala_hora_disciplinas = self.salas_hora_disciplinas[lab.nome][h]
                if nome_disciplina not in sala_hora_disciplinas:
                    sala_hora_disciplinas.append(nome_disciplina)
                if len(sala_hora_disciplinas) > NUM_DISCIPLINA_POR_LAB:
                    fit += CHOQUE_LABORATORIOS
        return fit

    def fit_choque_salas(self, salas: list[Sala], horarios: list[list[int]], nome_disciplina: str):
        """Verifica se a sala está ocupada no horário"""
        fit = 0
        for sala, _horarios in zip(salas, horarios):
            nome_sala = sala.nome
            for h in _horarios:
                sala_hora_disciplinas = self.salas_hora_disciplinas[nome_sala][h]
                if nome_disciplina not in sala_hora_disciplinas:
                    sala_hora_disciplinas.append(nome_disciplina)
                if len(sala_hora_disciplinas) > 1:
                    fit += CHOQUE_SALA
        return fit

    def fit_choque_disciplinas(self, ind):
        """
        Verifica se disciplinas que não devem chocar se choram no mesmo horário.
        Essas disciplinas são definidas na chave "choques" no metadada.
        """
        fit = 0
        for nome_disciplina, nome_outras in self.metadata.choques.items():
            disciplina = self.metadata.disciplinas[nome_disciplina]
            horarios, _ = get_horarios(self.metadata, disciplina, ind)
            horarios = list(chain(*horarios))
            for nome_outra in nome_outras:
                outra_disciplina = self.metadata.disciplinas[nome_outra]
                horarios_outra, _ = get_horarios(outra_disciplina, ind)
                horarios_outra = list(chain(*horarios_outra))
                for horario in horarios:
                    if horario in horarios_outra:
                        fit += CHOQUE_DISCIPLINAS
        return fit

    def fit_afinidade_professor_disciplina(self, profe: Professor, nome_disciplina: str):
        """Verifica se o professor tem afinidade com a disciplina"""
        return profe.afinidade_disciplinas[nome_disciplina]

    def fit_afinidade_professor_horarios(self, professor: Professor, horarios: list[list[int]]):
        """Verifica a afinidade do professor com o horário"""
        fit = 0
        for i in chain(*horarios):
            horario = self.metadata.horarios[i]
            fit += professor.afinidade_horarios.get(horario, 0)
        return fit

    def fit_afinidade_professor_salas(self, professor: Professor, salas: list[Sala]):
        fit = 0
        for sala in salas:
            fit += professor.afinidade_salas.setdefault(sala.nome, 0)
        return fit

    def fit_afinidade_salas_horarios(self, salas: list[Sala], horarios: list[list[int]]):
        fit = 0
        for sala, horarios_sala in zip(salas, horarios):
            for i in horarios_sala:
                horario = self.metadata.horarios[i]
                fit += sala.afinidade_horarios.setdefault(horario, 0)
        return fit

    def fit_aulas_em_dias_seguidos(self, ini_horas):
        """
        Verifica se há dois ou mais dias sequenciais com aulas
        de uma mesma disciplina.
        """
        fit = 0
        for h1, h2 in pairwise(sorted(ini_horas)):
            dia1 = int(h1 / 10)
            dia2 = int(h2 / 10)
            if abs(dia1 - dia2) <= 1:
                fit += AULAS_DIAS_SEGUIDOS
        return fit

    def fit_aulas_no_mesmo_dia(self, ini_horas):
        """Verifica se há duas aulas ou mais de uma mesma diciplina no mesmo dia"""
        fit = 0
        dias = []
        for h in ini_horas:
            dia = int(h / 10)
            if dia in dias:
                fit += AULAS_MESMO_DIA
            else:
                dias.append(dia)
        return fit

    def fit_aulas_aos_sabados(self, ini_horas):
        """Verifica se há aulas aos sábados"""
        fit = 0
        for h in ini_horas:
            if h > 49:
                fit += AULAS_AOS_SABADOS
        return fit

    def adicionar_grade_dia_sala(self, salas: list[Sala],
                                 horarios: list[list[int]],
                                 grades: list[str]):
        for _horarios, sala in zip(horarios, salas):
            for h in _horarios:
                turno = int(h / 5)
                for grade in grades:
                    self.grade_dia_sala[grade][turno].append((h, sala))

    def fit_distancia_percorrida(self):
        distancia = 0
        for grade in self.metadata.grades:
            _grade = self.grade_dia_sala[grade]
            for turno in range(12):
                h_salas = sorted(_grade[turno], key=lambda x: x[0])
                if h_salas != []:
                    distancia += 1000
                for (_, s1), (_, s2) in pairwise(h_salas):
                    if s1 == s2:
                        continue
                    distancia += self.metadata.distancias[s1.nome][s2.nome]

        return distancia * DISTANCIA_ENTRE_SALAS
