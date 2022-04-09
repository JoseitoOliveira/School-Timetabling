from dataclasses import dataclass, field

from tinydb import where

from src.data import disciplinas, professores, salas
from src.horarios import horarios_2, horarios_2_str, horarios_3, horarios_3_str
from src.horarios import horarios_str
from src.horarios import horarios_str as horarios_1_str
from src.horarios import sabado, todos


@dataclass
class Professor:
    nome: str
    afinidade_disciplinas: dict[str, int]
    hrs_min: int = 8
    hrs_max: int = 12
    afinidade_horarios: dict[str, int] = field(default_factory=lambda: {})
    afinidade_salas: dict[str, int] = field(default_factory=lambda: {})

    __sem_professor__: bool = False

    def set_nome(self, nome):
        professores.update({'nome': nome}, where('nome') == self.nome)
        self.nome = nome

    def set_hrs_min(self, hrs_min):
        self.hrs_min = hrs_min
        professores.update({'hrs_min': hrs_min}, where('nome') == self.nome)

    def set_hrs_max(self, hrs_max):
        self.hrs_max = hrs_max
        professores.update({'hrs_max': hrs_max}, where('nome') == self.nome)

    def set_afinidade_disciplinas(self, disciplina, afinidade):
        if afinidade == 0 and disciplina in self.afinidade_disciplinas:
            del self.afinidade_disciplinas[disciplina]
        else:
            self.afinidade_disciplinas[disciplina] = afinidade
        professores.update({'afinidade_disciplinas': self.afinidade_disciplinas},
                           where('nome') == self.nome)

    def set_afinidade_horarios(self, horario, afinidade):
        if afinidade == 0 and horario in self.afinidade_horarios:
            del self.afinidade_horarios[horario]
        else:
            self.afinidade_horarios[horario] = afinidade
        professores.update({'afinidade_horarios': self.afinidade_horarios},
                           where('nome') == self.nome)

    def set_afinidade_salas(self, sala, afinidade):
        if afinidade == 0 and sala in self.afinidade_salas:
            del self.afinidade_salas[sala]
        else:
            self.afinidade_salas[sala] = afinidade
        professores.update({'afinidade_salas': self.afinidade_salas},
                           where('nome') == self.nome)

    @property
    def sem_professor(self):
        return self.__sem_professor__

    def as_json(self):
        return {
            'nome': self.nome,
            'afinidade_disciplinas': self.afinidade_disciplinas,
            'hrs_min': self.hrs_min,
            'hrs_max': self.hrs_max,
            'afinidade_horarios': self.afinidade_horarios,
            'afinidade_salas': self.afinidade_salas,
        }

    @classmethod
    def from_json(cls, d):
        return cls(
            nome=d['nome'],
            afinidade_disciplinas=d['afinidade_disciplinas'],
            hrs_min=d['hrs_min'],
            hrs_max=d['hrs_max'],
            afinidade_horarios=d['afinidade_horarios'],
            afinidade_salas=d['afinidade_salas'],
        )


@dataclass
class Sala:
    nome: str
    capacidade: int
    laboratorio: bool = False
    afinidade_horarios: dict[str, int] = field(default_factory=lambda: {})

    __sem_sala__: bool = False

    @property
    def sem_sala(self):
        return self.__sem_sala__

    def as_json(self):
        return {
            'nome': self.nome,
            'capacidade': self.capacidade,
            'laboratorio': self.laboratorio,
            'afinidade_horarios': self.afinidade_horarios,
        }

    @classmethod
    def from_json(cls, d):
        return cls(
            nome=d['nome'],
            capacidade=d['capacidade'],
            laboratorio=d['laboratorio'],
            afinidade_horarios=d['afinidade_horarios'],
        )


@dataclass
class Cromossomo:
    numero_genes: int
    limite_inferior: int
    limite_superior: int
    slice_i: int
    slice_f: int

    def as_json(self):
        return {
            'numero_genes': self.numero_genes,
            'limite_inferior': self.limite_inferior,
            'limite_superior': self.limite_superior,
            'slice_i': self.slice_i,
            'slice_f': self.slice_f
        }

    @classmethod
    def from_json(cls, d):
        return cls(
            d['numero_genes'],
            d['limite_inferior'],
            d['limite_superior'],
            d['slice_i'],
            d['slice_f']
        )


class Disciplina:
    nome: str
    num_alunos: int
    grades: list[str]
    horas: list[int]
    horarios: list[list[str]] = field(default_factory=lambda: [])
    laboratorios: list[Sala] = field(default_factory=lambda: [])
    salas: list[Sala] = field(default_factory=lambda: [])
    professores: list[Professor] = field(default_factory=lambda: [])
    cromossomos: list[Cromossomo] = field(default_factory=lambda: [])
    aulas_aos_sabados: bool = False
    sem_professor: bool = False
    sem_sala: bool = False

    def __init__(self,
                 nome: str,
                 num_alunos: int,
                 grades: list[str],
                 horas: list[int],
                 horarios: list[list[str]],
                 laboratorios: list[Sala],
                 salas: list[Sala],
                 professores: list[Professor],
                 cromossomos: list[Cromossomo],
                 aulas_aos_sabados: bool,
                 sem_professor: bool,
                 sem_sala: bool):
        self._nome = nome
        self._num_alunos = num_alunos
        self._grades = grades
        self._horas = horas
        self._horarios = horarios
        self._laboratorios = laboratorios
        self._salas = salas
        self._professores = professores
        self._cromossomos = cromossomos
        self._aulas_aos_sabados = aulas_aos_sabados
        self._sem_professor = sem_professor
        self._sem_sala = sem_sala

        if self.horarios == []:
            self.make_horarios()

        assert len(self.horarios) == len(self.horas)

    def set_nome(self, nome):
        disciplinas.update({'nome': nome}, where('nome') == self.nome)
        self.nome = nome

    def set_grades(self, grades):
        self.grades = grades
        disciplinas.update({'grades': grades}, where('nome') == self.nome)

    def set_num_alunos(self, num_alunos):
        self.num_alunos = num_alunos
        disciplinas.update({'num_alunos': num_alunos},
                           where('nome') == self.nome)

    def set_sem_sala(self, sem_sala):
        self.sem_sala = sem_sala
        disciplinas.update({'sem_sala': sem_sala},
                           where('nome') == self.nome)

    def set_sem_professor(self, sem_professor):
        self.sem_professor = sem_professor
        disciplinas.update({'sem_professor': sem_professor},
                           where('nome') == self.nome)

    def add_aula(self, creditos):
        creditos_horarios = {
            1: horarios_1_str,
            2: horarios_2_str,
            3: horarios_3_str
        }
        self.horas.append(creditos)
        self.horarios.append(creditos_horarios[creditos])
        disciplinas.update({'horas': self.horas, 'horarios': self.horarios},
                           where('nome') == self.nome)

    def rmv_aula(self, index):
        self.horas.pop(index)
        self.horarios.pop(index)
        disciplinas.update({'horas': self.horas, 'horarios': self.horarios},
                           where('nome') == self.nome)

    def add_horario(self, aula, horario_str):
        if horario_str not in self.horarios[aula]:
            self.horarios[aula].append(horario_str)
            disciplinas.update({'horarios': self.horarios},
                               where('nome') == self.nome)

    def rmv_horario(self, aula, horario_str):
        if horario_str in self.horarios[aula]:
            self.horarios[aula].remove(horario_str)
            disciplinas.update({'horarios': self.horarios},
                               where('nome') == self.nome)

    def add_laboratorio(self, sala_nome):
        labs_nomes = [lab['nome'] for lab in self.laboratorios]
        if sala_nome not in labs_nomes:
            sala = salas.get(where('nome') == sala_nome)
            self.laboratorios.append(sala)
            disciplinas.update({'laboratorios': self.laboratorios},
                               where('nome') == self.nome)

    def rmv_laboratorio(self, sala_nome):
        for lab in self.laboratorios:
            if lab['nome'] == sala_nome:
                self.laboratorios.remove(lab)
                break
        disciplinas.update({'laboratorios': self.laboratorios},
                           where('nome') == self.nome)

    def make_horarios(self):
        for h in self.horas:
            if h == 2:
                horarios_binarios = (horarios_2
                                     if self.aulas_aos_sabados
                                     else horarios_2 & ~sabado)
                self.horarios.append(
                    [
                        horario_str
                        for i, horario_str in enumerate(horarios_str)
                        if horarios_binarios & (0x1 << i)
                    ]
                )
            elif h == 3:
                horarios_binarios = (horarios_3
                                     if self.aulas_aos_sabados
                                     else horarios_3 & ~sabado)

                self.horarios.append(
                    [
                        horario_str
                        for i, horario_str in enumerate(horarios_str)
                        if horarios_binarios & (0x1 << i)
                    ]
                )
            else:
                horarios_binarios = (todos
                                     if self.aulas_aos_sabados
                                     else todos & ~sabado)
                self.horarios.append(
                    [
                        horario_str
                        for i, horario_str in enumerate(horarios_str)
                        if horarios_binarios & (0x1 << i)
                    ]
                )

    def as_json(self):
        return {
            'nome': self.nome,
            'num_alunos': self.num_alunos,
            'grades': self.grades,
            'horas': self.horas,
            'aulas_aos_sabados': self.aulas_aos_sabados,
            'horarios': self.horarios,
            'laboratorios': [s.as_json() for s in self.laboratorios],
            'salas': [s.as_json() for s in self.salas],
            'professores': [p.as_json() for p in self.professores],
            'cromossomos': [c.as_json() for c in self.cromossomos],
            'sem_professor': self.sem_professor,
            'sem_sala': self.sem_sala,
        }

    @classmethod
    def from_json(cls, d):
        return cls(
            nome=d['nome'],
            num_alunos=d['num_alunos'],
            grades=d['grades'],
            horas=d['horas'],
            aulas_aos_sabados=d['aulas_aos_sabados'],
            horarios=d['horarios'],
            laboratorios=[Sala.from_json(s) for s in d['laboratorios']],
            salas=[Sala.from_json(s) for s in d['salas']],
            professores=[Professor.from_json(p) for p in d['professores']],
            cromossomos=[Cromossomo.from_json(c) for c in d['cromossomos']],
            sem_professor=d['sem_professor'],
            sem_sala=d['sem_sala'],
        )


@dataclass
class MetaData:
    professores: list[Professor]
    salas: list[Sala]
    disciplinas: dict[str, Disciplina]
    horarios: list[str]
    distancias: dict[str, dict[str, int]]
    choques: dict

    def __post_init__(self):
        self.__grades__ = list(set([
            grade
            for disciplina in self.disciplinas.values()
            for grade in disciplina.grades
        ]))

    @property
    def grades(self):
        return self.__grades__

    def as_json(self):
        return {
            'professores': [p.as_json() for p in self.professores],
            'salas': [s.as_json() for s in self.salas],
            'disciplinas': {
                d.nome: d.as_json()
                for d in self.disciplinas.values()
            },
            'horarios': self.horarios,
            'distancias': self.distancias,
            'choques': self.choques
        }

    @classmethod
    def from_json(cls, d):
        return cls(
            professores=[Professor.from_json(p) for p in d['professores']],
            salas=[Sala.from_json(s) for s in d['salas']],
            disciplinas={
                d['nome']: Disciplina.from_json(d)
                for d in d['disciplinas'].values()
            },
            horarios=d['horarios'],
            distancias=d['distancias'],
            choques=d['choques']
        )
