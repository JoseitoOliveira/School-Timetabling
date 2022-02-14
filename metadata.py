from typing import Tuple
from AG.utilidades_AG import cruzamento_uniforme, mutUniformInt
from modelos import *
from horarios import *

from dataclasses import asdict

professores = [
    Professor(
        nome='Rafael',
        afinidade_disciplinas={
            "Dispositivos": 0,
        },
    ),
    Professor(
        nome='Prof Eletromag',
        afinidade_disciplinas={
            "Eletromagnetismo": 0,
        },
    ),
    Professor(
        nome='Prof Mec. Solidos II',
        afinidade_disciplinas={
            "Mec. dos Sólidos II": 0,
        },
    ),
    Professor(
        nome='Prof. Economia I',
        afinidade_disciplinas={
            "Economia I": 0,
        },
    ),
    Professor(
        nome='Prof. Sociologia do Trabalho',
        afinidade_disciplinas={
            "Sociologia do Trabalho": 0,
        },
    ),
    Professor(
        nome='Prof. Complexas',
        afinidade_disciplinas={
            "Complexas": 0,
        },
    ),
    Professor(
        nome='Prof. Estocásticos',
        afinidade_disciplinas={
            "Estocásticos": 0,
        },
    ),
    Professor(
        nome='Prof. Cálculo Numérico',
        afinidade_disciplinas={
            "Cálculo Numérico": 0,
        },
    ),
    Professor(
        nome='Prof Mec. Sólidos I',
        afinidade_disciplinas={
            "Mec. dos Sólidos I": 0,
        }
    ),
    Professor(
        nome="Prof Física Experimental II",
        afinidade_disciplinas={
            "Física Experimental II": 0,
        }
    ),
    Professor(
        nome="Alexandre",
        afinidade_disciplinas={
            "Circuitos I": 2,
            "Conversão": 2,
        }
    ),
    Professor(
        nome="Cícero",
        afinidade_disciplinas={
            "Instrumentação Eletrônica": 2,
            "Materiais Elétricos": 2
        }
    ),
    Professor(
        nome="Rômulo",
        afinidade_disciplinas={
            "Mecânica dos Flúidos": 2,
        }
    ),
    Professor(
        nome="Darlan",
        afinidade_disciplinas={
            "Teoria do Controle": 2,
        }
    ),
    Professor(
        nome="Fabiano",
        afinidade_disciplinas={
            "Máquinas Elétricas": 2,
            "Conversão": 1
        },
        afinidade_horarios={
            "2M5": -10,
            "2T1": -10,
            "3M5": -10,
            "3T1": -10,
            "4M5": -10,
            "4T1": -10,
            "5M5": -10,
            "5T1": -10,
            "6M5": -10,
            "6T1": -10,
            "7M5": -10,
            "7T1": -10
        }
    ),
    Professor(
        nome="Jéssica",
        afinidade_disciplinas={
            "Pesquisa": 2
        }
    ),
    Professor(

        nome="Alexsandro",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Controle I": 2
        }
    ),
    Professor(
        nome="Fabrício",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Princípios de Comunicações": 2
        }
    ),
    Professor(
        nome="Clivaldo",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Sistemas Elétricos": 2
        }
    ),
    Professor(
        nome="Romero",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Eletrônica de Potência": 2
        }
    ),
    Professor(
        nome="Yuri",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Técnicas de Medição": 2
        }
    ),
    Professor(
        nome="Helon",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Análise de Sistemas Elétricos": 2
        }
    ),
    Professor(
        nome="Euler",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Filtros": 2,
            "Eletrônica": 2
        }
    ),
    Professor(
        nome="Carlos",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Instrumentação Industrial": 2
        }
    ),
    Professor(
        nome="Isaac",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Acionamentos e Circuitos Elétricos": 2,
            "Circuitos II": 2
        }
    ),
    Professor(
        nome="Waslon",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Análise de Sinais e Sistemas": 2,
        }
    ),
    Professor(
        nome="Protásio",
        hrs_min=8,
        hrs_max=8,
        afinidade_disciplinas={
            "Microc e Microp": 2,
            "Técnicas de Programação": 2
        }
    )
]

salas = [
    Sala(

        nome="CTM1",
        capacidade=30
    ),
    Sala(
        nome="CTM2",
        capacidade=30
    ),
    Sala(
        nome="CTM3",
        capacidade=30
    ),
    Sala(
        nome="CTM4",
        capacidade=30,
    ),
    Sala(
        nome="LMI",
        capacidade=30,
        laboratorio=True
    ),
    Sala(
        nome="LMA",
        capacidade=30,
        laboratorio=True
    )
]

disciplinas = {
    "Circuitos I": Disciplina(
        nome="Circuitos I",
        grades=["p4"],
        num_alunos=22,
        horas=[2, 3],
        aulas_aos_sabados=False
    ),
    "Sociologia do Trabalho": Disciplina(
        nome="Sociologia do Trabalho",
        grades=["p4"],
        num_alunos=22,
        horas=[2, 3],
        aulas_aos_sabados=False
    ),
    "Complexas": Disciplina(
        nome="Complexas",
        grades=["p4"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Estocásticos": Disciplina(
        nome="Estocásticos",
        grades=["p4"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Mec. dos Sólidos I": Disciplina(
        nome="Mec. dos Sólidos I",
        grades=["p4"],
        num_alunos=22,
        horas=[2, 2, 2],
        aulas_aos_sabados=False
    ),
    "Cálculo Numérico": Disciplina(
        nome="Cálculo Numérico",
        grades=["p4"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Física Experimental II": Disciplina(
        nome="Física Experimental II",
        grades=["p4"],
        num_alunos=22,
        horas=[2],
        aulas_aos_sabados=False
    ),
    "Dispositivos": Disciplina(
        nome="Dispositivos",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Eletromagnetismo": Disciplina(
        nome="Eletromagnetismo",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Circuitos II": Disciplina(
        nome="Circuitos II",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Técnicas de Programação": Disciplina(
        nome="Técnicas de Programação",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False,
        salas=[sala for sala in salas if sala.nome in ["LMI", "LMA"]]
    ),
    "Análise de Sinais e Sistemas": Disciplina(
        nome="Análise de Sinais e Sistemas",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Mec. dos Sólidos II": Disciplina(
        nome="Mec. dos Sólidos II",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 3],
        aulas_aos_sabados=False
    ),
    "Economia I": Disciplina(
        nome="Economia I",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 3],
        aulas_aos_sabados=False
    ),
    "Mecânica dos Flúidos": Disciplina(
        nome="Mecânica dos Flúidos",
        grades=["p6"],
        num_alunos=22,
        horas=[3, 3],
        aulas_aos_sabados=False
    ),
    "Teoria do Controle": Disciplina(
        nome="Teoria do Controle",
        grades=["p6"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Eletrônica": Disciplina(
        nome="Eletrônica",
        grades=["p6"],
        num_alunos=22,
        horas=[3, 2],
        aulas_aos_sabados=False,
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    "Materiais Elétricos": Disciplina(
        nome="Materiais Elétricos",
        grades=["p6"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False,
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    "Conversão": Disciplina(
        nome="Conversão",
        grades=["p6"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False,
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    "Pesquisa": Disciplina(
        nome="Pesquisa",
        grades=["p6"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False,
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    "Instrumentação Eletrônica": Disciplina(
        nome="Instrumentação Eletrônica",
        grades=["p7"],
        num_alunos=10,
        horas=[2, 2],
        aulas_aos_sabados=False,
        salas=[sala for sala in salas if sala.nome in ["LMI", "LMA"]]
    ),
    "Máquinas Elétricas": Disciplina(
        nome="Máquinas Elétricas",
        grades=["p7"],
        num_alunos=20,
        horas=[2, 3],
        aulas_aos_sabados=False,
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    "Controle I": Disciplina(
        nome="Controle I",
        grades=["p7"],
        num_alunos=15,
        horas=[2, 3],
        aulas_aos_sabados=False,
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    "Princípios de Comunicações": Disciplina(
        nome="Princípios de Comunicações",
        grades=["p7"],
        num_alunos=12,
        horas=[2, 3],
        aulas_aos_sabados=False,
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    "Sistemas Elétricos": Disciplina(
        nome="Sistemas Elétricos",
        grades=["p7"],
        num_alunos=20,
        horas=[2, 3],
        aulas_aos_sabados=False
    ),
    "Eletrônica de Potência": Disciplina(
        nome="Eletrônica de Potência",
        grades=["p7", "p8"],
        num_alunos=25,
        horas=[2, 3],
        aulas_aos_sabados=False
    ),
    "Técnicas de Medição": Disciplina(
        nome="Técnicas de Medição",
        grades=["p8"],
        num_alunos=22,
        horas=[2, 2],
        aulas_aos_sabados=False,
    ),
    "Análise de Sistemas Elétricos": Disciplina(
        nome="Análise de Sistemas Elétricos",
        grades=["p8"],
        num_alunos=15,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Filtros": Disciplina(
        nome="Filtros",
        grades=["p8"],
        num_alunos=15,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Instrumentação Industrial": Disciplina(
        nome="Instrumentação Industrial",
        grades=["p8"],
        num_alunos=15,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Acionamentos e Circuitos Elétricos": Disciplina(
        nome="Acionamentos e Circuitos Elétricos",
        grades=["p8"],
        num_alunos=15,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    "Microc e Microp": Disciplina(
        nome="Microc e Microp",
        grades=["p8"],
        num_alunos=15,
        horas=[2, 2],
        aulas_aos_sabados=False,
        salas=[sala for sala in salas if sala.nome in ["LMI", "LMA"]]
    )
}


distancias = {
    "CTM1": {"CTM1": 00, "CTM2": 10, "CTM3": 20, "CTM4": 30, "LMI": 40, "LMA": 50},
    "CTM2": {"CTM1": 10, "CTM2": 00, "CTM3": 10, "CTM4": 20, "LMI": 40, "LMA": 50},
    "CTM3": {"CTM1": 20, "CTM2": 10, "CTM3": 00, "CTM4": 10, "LMI": 40, "LMA": 50},
    "CTM4": {"CTM1": 30, "CTM2": 20, "CTM3": 10, "CTM4": 00, "LMI": 40, "LMA": 50},
    "LMI": {"CTM1": 30, "CTM2": 20, "CTM3": 10, "CTM4": 00, "LMI": 00, "LMA": 50},
    "LMA": {"CTM1": 30, "CTM2": 20, "CTM3": 10, "CTM4": 00, "LMI": 50, "LMA": 00},
}


metadata = MetaData(
    professores=professores,
    salas=salas,
    grades=["p4", "p5", "p6", "p7", "p8"],
    disciplinas=disciplinas,
    horarios=horarios_str,
    distancias=distancias,
    choques={
        "Conversão": [
            "Sistemas Elétricos",
            "Princípios de Comunicações",
            "Controle I",
            "Instrumentação Eletrônica",
            "Eletrônica de Potência"
        ],
        "Circuitos I": [
            "Dispositivos",
            "Eletromagnetismo",
            "Técnicas de Programação",
            "Análise de Sistemas Elétricos",
            "Mec. dos Sólidos II",
            "Economia I",
        ]

    }
)


def completar_professores(disciplina: Disciplina):
    professores: list[Professor] = metadata.professores
    disciplina.professores = [
        Prof_Disciplina(
            nome=profe.nome,
            afinidade=profe.afinidade_disciplinas[disciplina.nome],
            horarios=profe.afinidade_horarios
        )

        for profe in professores
        if disciplina.nome in profe.afinidade_disciplinas.keys()
    ]

    if disciplina.professores == []:
        raise Exception(
            f'Não há professores para a disciplina {disciplina.nome}.'
        )
    return disciplina


def completar_salas(disciplina: Disciplina):
    salas: list[Sala] = metadata.salas
    if disciplina.salas == []:
        disciplina.salas = [
            sala for sala in salas
            if sala.capacidade >= disciplina.num_alunos
            if not sala.laboratorio
        ]

    if disciplina.salas == []:
        raise Exception(
            f'Não há sala que comporte a disciplina {disciplina.nome} '
            f'que possui {disciplina.num_alunos} alunos matriculados.'
        )
    return disciplina


def completar_cromossomos(disciplina: Disciplina, ultimo_gene):
    num_genes_p = 1
    num_genes_s = len(disciplina.horas)
    num_genes_l = len(disciplina.horas) if disciplina.laboratorios else 0

    cromossomos = []
    cromossomos.append(Cromossomo(   # Professores
        numero_genes=num_genes_p,
        limite_inferior=0,
        limite_superior=len(disciplina.professores),
        slice_i=ultimo_gene,
        slice_f=ultimo_gene+num_genes_p
    ))
    ultimo_gene += num_genes_p
    cromossomos.append(Cromossomo(   # Salas
        numero_genes=num_genes_s,
        limite_inferior=0,
        limite_superior=len(disciplina.salas),
        slice_i=ultimo_gene,
        slice_f=ultimo_gene+num_genes_s
    ))
    ultimo_gene += num_genes_s

    cromossomos.append(Cromossomo(   # Laboratórios
        numero_genes=num_genes_l,
        limite_inferior=0,
        limite_superior=len(disciplina.laboratorios),
        slice_i=ultimo_gene,
        slice_f=ultimo_gene+num_genes_l
    ))
    ultimo_gene += num_genes_l

    num_genes_h = 1
    for horarios in disciplina.horarios:
        cromossomos.append(Cromossomo(   # Horiários
            numero_genes=num_genes_h,
            limite_inferior=0,
            limite_superior=len(horarios),
            slice_i=ultimo_gene,
            slice_f=ultimo_gene+num_genes_h
        ))
        ultimo_gene += num_genes_h

    disciplina.cromossomos = cromossomos
    return disciplina, ultimo_gene


def get_horarios(disciplina: Disciplina, ind):
    qtd_horas = disciplina.horas
    cromos_h = disciplina.cromossomos[3:]
    i_h = []
    for i, horarios in enumerate(disciplina.horarios):
        cromo_h = cromos_h[i]
        index_h = ind[cromo_h.slice_i: cromo_h.slice_f][0]
        horario = horarios[index_h]
        i_h.append(metadata.horarios.index(horario))

    horarios = [
        [h for h in range(ini_h, ini_h+qtd_horas[i], 1)]
        for i, ini_h in enumerate(i_h)
    ]
    return horarios, i_h


def extrair_dados(disciplina: Disciplina, ind: list[int]) -> Tuple[
    list[int], list[int], list[int], list[int], list[Sala],
    list[Sala], list[int], list[list[int]], list[str], Prof_Disciplina
]:

    cromo_p = disciplina.cromossomos[0]
    cromo_s = disciplina.cromossomos[1]
    cromo_l = disciplina.cromossomos[2]
    i_p: list = ind[cromo_p.slice_i: cromo_p.slice_f]
    i_s: list = ind[cromo_s.slice_i: cromo_s.slice_f]
    i_l: list = ind[cromo_l.slice_i: cromo_l.slice_f]

    salas = [disciplina.salas[i] for i in i_s]
    laboratorios = [disciplina.laboratorios[i] for i in i_l]

    qtd_horas = disciplina.horas
    grades: list = disciplina.grades
    professor = disciplina.professores[i_p[0]]
    horarios, i_h = get_horarios(disciplina, ind)

    return (
        i_p,
        i_s,
        i_l,
        i_h,
        salas,
        laboratorios,
        qtd_horas,
        horarios,
        grades,
        professor
    )


def completar_metadata(metadata: MetaData):

    ultimo_gene = 0
    for nome, disciplina in metadata.disciplinas.items():
        disciplina = completar_professores(disciplina)
        disciplina = completar_salas(disciplina)
        disciplina, ultimo_gene = completar_cromossomos(disciplina,
                                                        ultimo_gene)

    return metadata


def dummy_mut(ind, *args, **kargs):
    return ind,


def dummy_cruz(ind1, ind2, *args, **kargs):
    return ind2, ind1


def criar_cromossomos(metadata: MetaData):

    cromossomos = []
    for disciplina in metadata.disciplinas.values():
        disciplina: Disciplina
        for cromo in disciplina.cromossomos:
            numero_genes = cromo.numero_genes
            limite_inferior = cromo.limite_inferior
            limite_superior = cromo.limite_superior
            diff_limite = limite_superior - limite_inferior
            if diff_limite > 1:
                fcn_cruzamento = cruzamento_uniforme
            else:
                fcn_cruzamento = dummy_cruz

            cromossomos.append({
                'numero_genes': numero_genes,
                'tipo': int,
                'limite_inferior': limite_inferior,
                'limite_superior': limite_superior,
                'mutacao': {
                    'fcn': mutUniformInt if diff_limite > 1 else dummy_mut,
                    'args': {
                        'indpb': 0.15,
                        'low': 0,
                        'up': limite_superior - 1
                    },
                },
                'cruzamento': {
                    'fcn': fcn_cruzamento,
                    'args': {}
                }
            })
    return cromossomos


metadata = completar_metadata(metadata)

with open('metadata_c.py', mode='w', encoding='utf8') as f:
    from pprint import pprint
    pprint(asdict(metadata), stream=f)
