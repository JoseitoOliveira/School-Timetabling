from functools import partial, reduce
from itertools import chain
from metadata import metadata
from more_itertools import pairwise
from dataclasses import dataclass

CHOQUE_SALA = -20
CHOQUE_PROF = -20
CHOQUE_GRADE = -20
CHOQUE_LABORATORIOS = -20
CHOQUE_DISCIPLINAS = -5
AULAS_MESMO_DIA = -20
AULAS_AOS_SABADOS = -10
AULAS_DIAS_SEGUIDOS = -10
DISTANCIA_ENTRE_SALAS = -1e-3
MUDANÇA_DE_TURNO = -4


@dataclass
class Partial_Fitnesses:
    choque_salas: int = 0
    choque_professor: int = 0
    choque_grade: int = 0
    choque_laboratorios: int = 0
    choque_disciplinas: int = 0
    mesmo_turno: int = 0
    afinidade_disciplina: int = 0
    horarios_professor: int = 0
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
        return (f'Fitness: {self.sum()}\n' +
                '\n'.join([f'{field}: {getattr(self, field)}'
                           for field in self.__dataclass_fields__]))


def fitness(ind, metadata):

    sala_horas = []

    def fit_choque_salas(salas, horarios):
        """Verifica se a sala está ocupada no horário"""
        fit = 0
        for sala, _horarios in zip(salas, horarios):
            nome_sala = sala['nome']
            for h in _horarios:
                tag = f'{nome_sala}{h}'
                if tag in sala_horas:
                    fit += CHOQUE_SALA
                else:
                    sala_horas.append(tag)
        return fit

    prof_horas = []

    def fit_choque_profe(profe, horarios):
        """Verifica se o professor está ocupada no horário"""
        fit = 0
        nome_professor = profe['nome']
        for h in chain(*horarios):
            tag = f'{nome_professor}{h}'
            if tag in prof_horas:
                fit += CHOQUE_PROF
            else:
                prof_horas.append(tag)
        return fit

    grade_horas = []

    def fit_choque_grade(grades, horarios):
        """Verifica se a turma está com 2 ou mais aulas no horário"""
        fit = 0
        for h in chain(*horarios):
            for grade in grades:
                tag = f'{grade}{h}'
                if tag in grade_horas:
                    fit += CHOQUE_GRADE
                else:
                    grade_horas.append(tag)
        return fit

    laboratorios_horas = []

    def fit_mesmo_turno(ini_horas):
        """ Verifica se os horários da aula são no mesmo turno """
        turnos = map(lambda i: bool(int(i/5) % 2), ini_horas)
        mudança_turno = reduce(lambda x, y: x != y, turnos,)
        return MUDANÇA_DE_TURNO if mudança_turno else 0

    def fit_choque_laboratorios(laboratorios, horarios):
        """Verifica se a sala está ocupada no horário"""
        fit = 0
        for lab, _horarios in zip(laboratorios, horarios):
            nome_lab = lab['nome']
            for h in _horarios:
                tag = f'{nome_lab}{h}'
                if tag in laboratorios_horas:
                    fit += CHOQUE_SALA
                else:
                    laboratorios_horas.append(tag)
        return fit

    def fit_choque_disciplinas():
        fit = 0
        for nome_disciplina, nome_outras in metadata['choques'].items():
            disciplina = metadata['disciplinas'][nome_disciplina]
            horarios, _ = get_horarios(disciplina)
            horarios = list(chain(*horarios))
            for nome_outra in nome_outras:
                outra_disciplina = metadata['disciplinas'][nome_outra]
                horarios_outra, _ = get_horarios(outra_disciplina)
                horarios_outra = list(chain(*horarios_outra))
                for horario in horarios:
                    if horario in horarios_outra:
                        fit += CHOQUE_DISCIPLINAS
        return fit

    def fit_afinidade_disciplina(profe):
        """Verifica se o professor tem afinidade com a disciplina"""
        return profe['afinidade']

    def fit_aulas_em_dias_seguidos(ini_horas):
        """
        Verifica se há dois ou mais dias sequenciais com aulas
        de uma mesma disciplina.
        """
        fit = 0
        for h1, h2 in pairwise(sorted(ini_horas)):
            dia1 = int(h1/10)
            dia2 = int(h2/10)
            if abs(dia1 - dia2) <= 1:
                fit += AULAS_DIAS_SEGUIDOS
        return fit

    def fit_aulas_no_mesmo_dia(ini_horas):
        """Verifica se há duas aulas ou mais de uma mesma diciplina no mesmo dia"""
        fit = 0
        dias = []
        for h in ini_horas:
            dia = int(h/10)
            if dia in dias:
                fit += AULAS_MESMO_DIA
            else:
                dias.append(dia)
        return fit

    def fit_horarios_professores(professor, horarios):
        """Verifica a afinidade do professor com o horário"""
        fit = 0
        for i in chain(*horarios):
            h = metadata['horarios'][i]
            fit += professor['horarios'].setdefault(h, 0)
        return fit

    def fit_aulas_aos_sabados(ini_horas):
        """Verifica se há aulas aos sábados"""
        fit = 0
        for h in ini_horas:
            if h > 49:
                fit += AULAS_AOS_SABADOS
        return fit

    grade_dia_sala = {
        grade: {
            turno: []
            for turno in range(12)
        } for grade in metadata['grades']
    }

    def adicionar_grade_dia_sala(salas, horarios, grades):
        for _horarios, sala in zip(horarios, salas):
            for h in _horarios:
                turno = int(h/5)
                for grade in grades:
                    grade_dia_sala[grade][turno].append((h, sala))

    def fit_distancia_percorrida():
        def calc_distancia(s1, s2):
            return metadata['distancias'][s1['nome']][s2['nome']]
        distancia = 0
        for grade in metadata['grades']:
            _grade = grade_dia_sala[grade]
            for turno in range(12):
                h_salas = sorted(_grade[turno], key=lambda x: x[0])
                if h_salas != []:
                    distancia += 1000
                for (_, s1), (_, s2) in pairwise(h_salas):
                    distancia += calc_distancia(s1, s2)
        return distancia * DISTANCIA_ENTRE_SALAS

    def get_horarios(disciplina):
        cromos_h = disciplina['cromossomos'][2:]
        i_h = []
        for i, horarios in enumerate(disciplina['horarios']):
            cromo_h = cromos_h[i]
            index_h = ind[cromo_h['slice_i']:cromo_h['slice_f']][0]
            horario = horarios[index_h]
            i_h.append(metadata['horarios'].index(horario))

        horarios = [
            [h for h in range(ini_h, ini_h+qtd_horas[i], 1)]
            for i, ini_h in enumerate(i_h)
        ]
        return horarios, i_h

    fit = Partial_Fitnesses()
    for disciplina in metadata['disciplinas'].values():
        cromo_p = disciplina['cromossomos'][0]
        cromo_s = disciplina['cromossomos'][1]
        i_p = ind[cromo_p['slice_i']:cromo_p['slice_f']]
        i_s = ind[cromo_s['slice_i']:cromo_s['slice_f']]

        salas = [disciplina['salas'][i] for i in i_s]

        qtd_horas = disciplina['horas']
        grades: list = disciplina['grades']
        professor = disciplina['professores'][i_p[0]]
        horarios, i_h = get_horarios(disciplina)

        fit.choque_salas += fit_choque_salas(salas, horarios)
        fit.choque_professor += fit_choque_profe(professor, horarios)
        fit.choque_grade += fit_choque_grade(grades, horarios)
        fit.afinidade_disciplina += fit_afinidade_disciplina(professor)
        fit.horarios_professor += fit_horarios_professores(professor, horarios)
        fit.mesmo_turno += fit_mesmo_turno(i_h)
        fit.aulas_no_mesmo_dia += fit_aulas_no_mesmo_dia(i_h)
        fit.aulas_aos_sabados += fit_aulas_aos_sabados(i_h)
        fit.aulas_em_dias_seguidos += fit_aulas_em_dias_seguidos(i_h)

        adicionar_grade_dia_sala(salas, horarios, grades)

    fit.distancia_percorrida += fit_distancia_percorrida()
    fit.choque_disciplinas += fit_choque_disciplinas()

    return fit.sum(), fit


fitness_meta = partial(fitness, metadata=metadata)
