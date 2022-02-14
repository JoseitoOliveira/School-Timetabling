from dataclasses import dataclass, field
from horarios import *


@dataclass
class Professor:
    nome: str
    afinidade_disciplinas: dict[str, int]
    hrs_min: int = 8
    hrs_max: int = 12
    afinidade_horarios: dict[str, int] = field(default_factory=lambda: {})


@dataclass
class Sala:
    nome: str
    capacidade: int
    laboratorio: bool = False


@dataclass
class Prof_Disciplina:
    nome: str
    afinidade: int
    horarios: dict[str, int]


@dataclass
class Cromossomo:
    numero_genes: int
    limite_inferior: int
    limite_superior: int
    slice_i: int
    slice_f: int


@dataclass
class Disciplina:
    nome: str
    num_alunos: int
    grades: list[str]
    horas: list[int]
    aulas_aos_sabados: bool = False
    horarios: list[list[str]] = field(default_factory=lambda: [])
    laboratorios: list[Sala] = field(default_factory=lambda: [])
    salas: list[Sala] = field(default_factory=lambda: [])
    professores: list[Prof_Disciplina] = field(default_factory=lambda: [])
    cromossomos: list[Cromossomo] = field(default_factory=lambda: [])

    def __post_init__(self):
        if self.horarios == []:
            self.make_horarios()

        assert len(self.horarios) == len(self.horas)

    def make_horarios(self):
        for h in self.horas:
            if h == 2:
                horarios_binarios = (horarios_2
                                     if not self.aulas_aos_sabados
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
                                     if not self.aulas_aos_sabados
                                     else horarios_3 & ~sabado)

                self.horarios.append(
                    [
                        horario_str
                        for i, horario_str in enumerate(horarios_str)
                        if horarios_binarios & (0x1 << i)
                    ]
                )
            else:
                horarios_binarios = todos
                self.horarios.append(
                    [
                        horario_str
                        for i, horario_str in enumerate(horarios_str)
                        if horarios_binarios & (0x1 << i)
                    ]
                )


@dataclass
class MetaData:
    professores: list[Professor]
    salas: list[Sala]
    grades: list[str]
    disciplinas: dict[str, Disciplina]
    horarios: list[str]
    distancias: dict[str, dict[str, int]]
    choques: dict
