from dataclasses import dataclass

from tinydb import where

from src.data import disciplinas, professores, salas
from src.horarios import horarios_2_str, horarios_3_str
from src.horarios import horarios_str as horarios_1_str


class Professor:

    def __init__(
        self,
        nome: str,
        afinidade_disciplinas: dict[str, int] = None,
        hrs_min: int = 8,
        hrs_max: int = 12,
        afinidade_horarios: dict[str, int] = None,
        afinidade_salas: dict[str, int] = None
    ):
        self._nome = nome
        self._afinidade_disciplinas = afinidade_disciplinas or {}
        self._hrs_min = hrs_min
        self._hrs_max = hrs_max
        self._afinidade_horarios = afinidade_horarios or {}
        self._afinidade_salas = afinidade_salas or {}

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        professores.update({'nome': nome}, where('nome') == self.nome)
        self._nome = nome

    @property
    def afinidade_disciplinas(self):
        return self._afinidade_disciplinas

    @property
    def afinidade_horarios(self):
        return self._afinidade_horarios

    @property
    def afinidade_salas(self):
        return self._afinidade_salas

    @property
    def hrs_min(self):
        return self._hrs_min

    @hrs_min.setter
    def hrs_min(self, hrs_min):
        self._hrs_min = hrs_min
        professores.update({'hrs_min': hrs_min}, where('nome') == self.nome)

    @property
    def hrs_max(self):
        return self._hrs_max

    @hrs_max.setter
    def hrs_max(self, hrs_max):
        self._hrs_max = hrs_max
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


class Sala:

    def __init__(
        self,
        nome: str,
        capacidade: int,
        laboratorio: bool = False,
        afinidade_horarios: dict[str, int] = None,
        distancias: dict[str, int] = None
    ):
        self._nome = nome
        self._capacidade = capacidade
        self._laboratorio = laboratorio
        self._afinidade_horarios = afinidade_horarios or {}
        self._distancias = distancias or {}

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome) -> None:
        salas.update({'nome': nome}, where('nome') == self.nome)
        self._nome = nome

    @property
    def capacidade(self) -> int:
        return self._capacidade

    @capacidade.setter
    def capacidade(self, capacidade) -> None:
        self._capacidade = capacidade
        salas.update({'capacidade': self.capacidade},
                     where('nome') == self.nome)

    @property
    def laboratorio(self) -> bool:
        return self._laboratorio

    @laboratorio.setter
    def laboratorio(self, laboratorio) -> None:
        self._laboratorio = laboratorio
        salas.update({'laboratorio': self.laboratorio},
                     where('nome') == self.nome)

    @property
    def afinidade_horarios(self) -> dict[str, int]:
        return self._afinidade_horarios

    @afinidade_horarios.setter
    def afinidade_horarios(self, afinidade_horarios):
        self._afinidade_horarios = afinidade_horarios
        salas.update({'afinidade_horarios': self.afinidade_horarios},
                     where('nome') == self.nome)

    @property
    def distancias(self) -> dict[str, int]:
        return self._distancias

    @distancias.setter
    def distancias(self, distancias) -> None:
        self._distancias = distancias
        salas.update({'distancias': self.distancias},
                     where('nome') == self.nome)

    def set_afinidade_horarios(self, horario, afinidade) -> None:
        if afinidade == 0 and horario in self.afinidade_horarios:
            del self.afinidade_horarios[horario]
        else:
            self.afinidade_horarios[horario] = afinidade
        salas.update({'afinidade_horarios': self.afinidade_horarios},
                     where('nome') == self.nome)

    def set_distancia(self, nome_outra_sala, distancia) -> None:
        self.distancias[nome_outra_sala] = distancia
        salas.update({'distancias': self.distancias},
                     where('nome') == self.nome)

        outra_sala = salas.get(where('nome') == nome_outra_sala)
        outra_sala['distancias'][self.nome] = distancia
        salas.update({'distancias': outra_sala['distancias']},
                     where('nome') == nome_outra_sala)

    def as_json(self) -> dict:
        return {
            'nome': self.nome,
            'capacidade': self.capacidade,
            'laboratorio': self.laboratorio,
            'afinidade_horarios': self.afinidade_horarios,
            'distancias': self.distancias,
        }

    @classmethod
    def from_json(cls, d) -> 'Sala':
        return cls(
            nome=d['nome'],
            capacidade=d['capacidade'],
            laboratorio=d['laboratorio'],
            afinidade_horarios=d['afinidade_horarios'],
            distancias=d['distancias'],
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

    def __init__(
            self,
            nome: str,
            num_alunos: int,
            grades: list[str],
            horas: list[int],
            horarios: list[list[str]] = None,
            laboratorios: list[Sala] = None,
            salas: list[Sala] = None,
            professores: list[Professor] = None,
            cromossomos: list[Cromossomo] = None,
            sem_professor: bool = False,
            sem_sala: bool = False
    ):
        self._nome = nome
        self._num_alunos = num_alunos
        self._grades = grades
        self._horas = horas
        self._horarios = horarios or []
        self._laboratorios = laboratorios or []
        self._salas = salas or []
        self._professores = professores or []
        self._cromossomos = cromossomos or []
        self._sem_professor = sem_professor
        self._sem_sala = sem_sala

        if self.horarios == []:
            self.make_horarios()

        assert len(self.horarios) == len(self.horas)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        disciplinas.update({'nome': nome}, where('nome') == self.nome)
        self._nome = nome

    @property
    def num_alunos(self):
        return self._num_alunos

    @num_alunos.setter
    def num_alunos(self, num_alunos):
        self._num_alunos = num_alunos
        disciplinas.update({'num_alunos': self.num_alunos},
                           where('nome') == self.nome)

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, grades):
        self._grades = grades
        disciplinas.update({'grades': self.grades},
                           where('nome') == self.nome)

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, horas):
        self._horas = horas
        disciplinas.update({'horas': self.horas},
                           where('nome') == self.nome)

    @property
    def horarios(self):
        return self._horarios

    @horarios.setter
    def horarios(self, horarios):
        self._horarios = horarios
        disciplinas.update({'horarios': self.horarios},
                           where('nome') == self.nome)

    @property
    def laboratorios(self):
        return self._laboratorios

    @laboratorios.setter
    def laboratorios(self, laboratorios):
        self._laboratorios = laboratorios
        disciplinas.update(
            {'laboratorios': [lab.as_json for lab in self.laboratorios]},
            where('nome') == self.nome)

    @property
    def salas(self):
        return self._salas

    @salas.setter
    def salas(self, salas):
        self._salas = salas
        disciplinas.update({'salas': [s.as_json() for s in self.salas]},
                           where('nome') == self.nome)

    @property
    def professores(self):
        return self._professores

    @professores.setter
    def professores(self, professores):
        self._professores = professores
        disciplinas.update({'professores': [p.as_json() for p in self.professores]},
                           where('nome') == self.nome)

    @property
    def cromossomos(self):
        return self._cromossomos

    @cromossomos.setter
    def cromossomos(self, cromossomos):
        self._cromossomos = cromossomos
        disciplinas.update({'cromossomos': [c.as_json() for c in self.cromossomos]},
                           where('nome') == self.nome)

    @property
    def sem_professor(self):
        return self._sem_professor

    @sem_professor.setter
    def sem_professor(self, sem_professor):
        self._sem_professor = sem_professor
        disciplinas.update({'sem_professor': self.sem_professor},
                           where('nome') == self.nome)

    @property
    def sem_sala(self):
        return self._sem_sala

    @sem_sala.setter
    def sem_sala(self, sem_sala):
        self._sem_sala = sem_sala
        disciplinas.update({'sem_sala': self.sem_sala},
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
            horarios_str = {
                1: horarios_1_str,
                2: horarios_2_str,
                3: horarios_3_str
            }
            self.horarios.append(horarios_str.get(h, horarios_str))

    def as_json(self):
        return {
            'nome': self.nome,
            'num_alunos': self.num_alunos,
            'grades': self.grades,
            'horas': self.horas,
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
