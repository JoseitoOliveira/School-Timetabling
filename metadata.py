from AG.utilidades_AG import cruzamento_uniforme, mutUniformInt

metadata = {
    "professores": [
        {
            "nome": "Rafael",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Dispositivos": 0,
            }
        },
        {
            "nome": "Prof Eletromag",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Eletromagnetismo": 0,
            }
        },
        {
            "nome": "Prof Mec. Sólidos II",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Mec. dos Sólidos II": 0,
            }
        },
        {
            "nome": "Prof Economia I",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Economia I": 0,
            }
        },
        {
            "nome": "Prof Sociologia do Trabalho",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Sociologia do Trabalho": 0,
            }
        },
        {
            "nome": "Prof Complexas",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Complexas": 0,
            }
        },
        {
            "nome": "Prof Estocásticos",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Estocásticos": 0,
            }
        },
        {
            "nome": "Prof Cálculo Numério",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Cálculo Numério": 0,
            }
        },
        {
            "nome": "Prof Mec. Sólidos I",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Mec. dos Sólidos I": 0,
            }
        },
        {
            "nome": "Prof Física Experimental II",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Física Experimental II": 0,
            }
        },
        {
            "nome": "Alexandre",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Circuitos I": 2,
                "Conversão": 2,
            }
        },
        {
            "nome": "Cícero",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Instrumentação Eletrônica": 2,
                "Materiais Elétricos": 2
            }
        },
        {
            "nome": "Rômulo",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Mecânica dos Flúidos": 2,
            }
        },
        {
            "nome": "Darlan",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Teoria do Controle": 2,
            }
        },
        {
            "nome": "Fabiano",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Máquinas Elétricas": 2,
                "Conversão": 1
            },
            "horarios": {
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
        },
        {
            "nome": "Jéssica",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Pesquisa": 2
            }
        },
        {
            "nome": "Alexsandro",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Controle I": 2
            }
        },
        {
            "nome": "Fabrício",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Princípios de Comunicações": 2
            }
        },
        {
            "nome": "Clivaldo",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Sistemas Elétricos": 2
            }
        },
        {
            "nome": "Romero",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Eletrônica de Potência": 2
            }
        },
        {
            "nome": "Yuri",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Técnicas de Medição": 2
            }
        },
        {
            "nome": "Helon",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Análise de Sistemas Elétricos": 2
            }
        },
        {
            "nome": "Euler",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Filtros": 2,
                "Eletrônica": 2
            }
        },
        {
            "nome": "Carlos",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Instrumentação Industrial": 2
            }
        },
        {
            "nome": "Isaac",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Acionamentos e Circuitos Elétricos": 2,
                "Circuitos II": 2
            }
        },
        {
            "nome": "Waslon",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Análise de Sinais e Sistemas": 2,
            }
        },
        {
            "nome": "Protásio",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Microc e Microp": 2,
                "Técnicas de Programação": 2
            }
        },
    ],
    "salas": [
        {
            "nome": "CTM1",
            "capacidade": 30
        },
        {
            "nome": "CTM2",
            "capacidade": 30
        },
        {
            "nome": "CTM3",
            "capacidade": 30
        },
        {
            "nome": "CTM4",
            "capacidade": 30,
            "especial": False
        },
        {
            "nome": "LMI",
            "capacidade": 30,
            "especial": True
        },
        {
            "nome": "LMA",
            "capacidade": 30,
            "especial": True
        },
    ],
    "grades": ["p4", "p5", "p6", "p7", "p8"],
    "disciplinas": {
        "Circuitos I": {
            "grades": ["p4"],
            "num_alunos": 22,
            "horas": [2, 3],
            "aulas_aos_sabados": False
        },
        "Sociologia do Trabalho": {
            "grades": ["p4"],
            "num_alunos": 22,
            "horas": [2, 3],
            "aulas_aos_sabados": False
        },
        "Complexas": {
            "grades": ["p4"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Estocásticos": {
            "grades": ["p4"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Mec. dos Sólidos I": {
            "grades": ["p4"],
            "num_alunos": 22,
            "horas": [2, 2, 2],
            "aulas_aos_sabados": False
        },
        "Cálculo Numério": {
            "grades": ["p4"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Física Experimental II": {
            "grades": ["p4"],
            "num_alunos": 22,
            "horas": [2],
            "aulas_aos_sabados": False
        },
        "Dispositivos": {
            "grades": ["p5"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Eletromagnetismo": {
            "grades": ["p5"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Circuitos II": {
            "grades": ["p5"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Técnicas de Programação": {
            "grades": ["p5"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False,
            "salas": ["LMA", "LMI"]
        },
        "Análise de Sinais e Sistemas": {
            "grades": ["p5"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Mec. dos Sólidos II": {
            "grades": ["p5"],
            "num_alunos": 22,
            "horas": [2, 3],
            "aulas_aos_sabados": False
        },
        "Economia I": {
            "grades": ["p5"],
            "num_alunos": 22,
            "horas": [2, 3],
            "aulas_aos_sabados": False
        },
        "Mecânica dos Flúidos": {
            "grades": ["p6"],
            "num_alunos": 22,
            "horas": [3, 3],
            "aulas_aos_sabados": False
        },
        "Teoria do Controle": {
            "grades": ["p6"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Eletrônica": {
            "grades": ["p6"],
            "num_alunos": 22,
            "horas": [3, 2],
            "aulas_aos_sabados": False,
            "laboratorios": ["LMA", "LMI"]
        },
        "Materiais Elétricos": {
            "grades": ["p6"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Conversão": {
            "grades": ["p6"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Pesquisa": {
            "grades": ["p6"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Instrumentação Eletrônica": {
            "grades": ["p7"],
            "num_alunos": 10,
            "horas": [2, 2],
            "aulas_aos_sabados": False,
            "salas": ["LMA", "LMI"]
        },
        "Máquinas Elétricas": {
            "grades": ["p7"],
            "num_alunos": 20,
            "horas": [2, 3],
            "aulas_aos_sabados": False
        },
        "Controle I": {
            "grades": ["p7"],
            "num_alunos": 15,
            "horas": [2, 3],
            "aulas_aos_sabados": False
        },
        "Princípios de Comunicações": {
            "grades": ["p7"],
            "num_alunos": 12,
            "horas": [2, 3],
            "aulas_aos_sabados": False
        },
        "Sistemas Elétricos": {
            "grades": ["p7"],
            "num_alunos": 20,
            "horas": [2, 3],
            "aulas_aos_sabados": False
        },
        "Eletrônica de Potência": {
            "grades": ["p7"],
            "num_alunos": 25,
            "horas": [2, 3],
            "aulas_aos_sabados": False
        },
        "Técnicas de Medição": {
            "grades": ["p8"],
            "num_alunos": 22,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Análise de Sistemas Elétricos": {
            "grades": ["p8"],
            "num_alunos": 15,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Filtros": {
            "grades": ["p8"],
            "num_alunos": 15,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Instrumentação Industrial": {
            "grades": ["p8"],
            "num_alunos": 15,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Acionamentos e Circuitos Elétricos": {
            "grades": ["p8"],
            "num_alunos": 15,
            "horas": [2, 2],
            "aulas_aos_sabados": False
        },
        "Microc e Microp": {
            "grades": ["p8"],
            "num_alunos": 15,
            "horas": [2, 2],
            "aulas_aos_sabados": False,
            "salas": ["LMA", "LMI"]
        }
    },
    "horarios": [
        "2M1",
        "2M2",
        "2M3",
        "2M4",
        "2M5",
        "2T1",
        "2T2",
        "2T3",
        "2T4",
        "2T5",
        "3M1",
        "3M2",
        "3M3",
        "3M4",
        "3M5",
        "3T1",
        "3T2",
        "3T3",
        "3T4",
        "3T5",
        "4M1",
        "4M2",
        "4M3",
        "4M4",
        "4M5",
        "4T1",
        "4T2",
        "4T3",
        "4T4",
        "4T5",
        "5M1",
        "5M2",
        "5M3",
        "5M4",
        "5M5",
        "5T1",
        "5T2",
        "5T3",
        "5T4",
        "5T5",
        "6M1",
        "6M2",
        "6M3",
        "6M4",
        "6M5",
        "6T1",
        "6T2",
        "6T3",
        "6T4",
        "6T5",
        "7M1",
        "7M2",
        "7M3",
        "7M4",
        "7M5",
        "7T1",
        "7T2",
        "7T3",
        "7T4",
        "7T5"],
    "distancias": {
        "CTM1": {"CTM1": 00, "CTM2": 10, "CTM3": 20, "CTM4": 30, "LMI": 40, "LMA": 50},
        "CTM2": {"CTM1": 10, "CTM2": 00, "CTM3": 10, "CTM4": 20, "LMI": 40, "LMA": 50},
        "CTM3": {"CTM1": 20, "CTM2": 10, "CTM3": 00, "CTM4": 10, "LMI": 40, "LMA": 50},
        "CTM4": {"CTM1": 30, "CTM2": 20, "CTM3": 10, "CTM4": 00, "LMI": 40, "LMA": 50},
        "LMI": {"CTM1": 30, "CTM2": 20, "CTM3": 10, "CTM4": 00, "LMI": 00, "LMA": 50},
        "LMA": {"CTM1": 30, "CTM2": 20, "CTM3": 10, "CTM4": 00, "LMI": 50, "LMA": 00},
    },
    "choques": {
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
}


horarios_3 = {
    "2M1",
    "2T1",
    "3M1",
    "3T1",
    "4M1",
    "4T1",
    "5M1",
    "5T1",
    "6M1",
    "6T1",
    "7M1",
    "7T1"}
horarios_2 = {
    "2M2",
    "2T2",
    "3M2",
    "3T2",
    "4M2",
    "4T2",
    "5M2",
    "5T2",
    "6M2",
    "6T2",
    "7M2",
    "7T2",
    "2M4",
    "2T4",
    "3M4",
    "3T4",
    "4M4",
    "4T4",
    "5M4",
    "5T4",
    "6M4",
    "6T4",
    "7M4",
    "7T4"}
horarios_s = {
    "7M1",
    "7M2",
    "7M3",
    "7M4",
    "7M5",
    "7T1",
    "7T2",
    "7T3",
    "7T4",
    "7T5"}
horarios_t = {
    "2M1",
    "2M2",
    "2M3",
    "2M4",
    "2M5",
    "2T1",
    "2T2",
    "2T3",
    "2T4",
    "2T5",
    "3M1",
    "3M2",
    "3M3",
    "3M4",
    "3M5",
    "3T1",
    "3T2",
    "3T3",
    "3T4",
    "3T5",
    "4M1",
    "4M2",
    "4M3",
    "4M4",
    "4M5",
    "4T1",
    "4T2",
    "4T3",
    "4T4",
    "4T5",
    "5M1",
    "5M2",
    "5M3",
    "5M4",
    "5M5",
    "5T1",
    "5T2",
    "5T3",
    "5T4",
    "5T5",
    "6M1",
    "6M2",
    "6M3",
    "6M4",
    "6M5",
    "6T1",
    "6T2",
    "6T3",
    "6T4",
    "6T5",
    "7M1",
    "7M2",
    "7M3",
    "7M4",
    "7M5",
    "7T1",
    "7T2",
    "7T3",
    "7T4",
    "7T5"}


def completar_professores(disciplina):
    professores = metadata['professores']
    disciplina['professores'] = [
        {
            'nome': profe['nome'],
            'afinidade': profe['disciplinas'][disciplina['nome']],
            'horarios': profe.setdefault('horarios', dict())
        }
        for profe in professores
        if disciplina['nome'] in profe['disciplinas'].keys()
    ]

    if disciplina['professores'] == []:
        raise Exception(
            f'Não há professores para a disciplina {disciplina["nome"]}.'
        )
    return disciplina


def completar_salas(disciplina):
    salas = metadata['salas']
    nomes_salas_validos = [sala['nome'] for sala in salas]
    if 'salas' not in disciplina:
        disciplina['salas'] = [
            sala for sala in salas
            if sala['capacidade'] >= disciplina['num_alunos']
            if 'especial' not in sala or sala['especial'] is False
        ]
    else:
        nomes_salas = disciplina['salas']

        for nome_sala in nomes_salas:
            if nome_sala not in nomes_salas_validos:
                raise Exception(
                    f'A sala {nome_sala} definida na disciplina '
                    f'{disciplina["nome"]} não é uma sala válida.'
                )

        disciplina['salas'] = [
            sala for sala in salas
            if sala['nome'] in nomes_salas
            if sala['capacidade'] >= disciplina['num_alunos']
        ]

    if disciplina['salas'] == []:
        raise Exception(
            f'Não há sala que comporte a disciplina {disciplina["nome"]} '
            f'que possui {disciplina["num_alunos"]} alunos matriculados.'
        )
    return disciplina


def completar_laboratorios(disciplina):
    salas = metadata['salas']
    nomes_salas_validos = [sala['nome'] for sala in salas]
    if 'laboratorios' not in disciplina:
        disciplina['laboratorios'] = []
    else:
        nomes_labs = disciplina['laboratorios']

        disciplina['laboratorios'] = [
            sala for sala in salas
            if sala['nome'] in nomes_labs
            if sala['capacidade'] >= disciplina['num_alunos']
        ]
        for nome_lab in nomes_labs:
            if nome_lab not in nomes_salas_validos:
                raise Exception(
                    f'O laboratório {nome_lab} definido na disciplina '
                    f'{disciplina["nome"]} não é um laboratório válida.'
                )

        disciplina['laboratorios'] = [
            lab for lab in salas
            if lab['nome'] in nomes_labs
        ]

    return disciplina


def completar_nome_disciplina(nome, disciplina):
    disciplina['nome'] = nome
    return disciplina


def completar_horarios(disciplina):
    if "aulas_aos_sabados" in disciplina:
        aulas_aos_sabados = disciplina['aulas_aos_sabados']
    else:
        aulas_aos_sabados = True

    if 'horarios' not in disciplina:
        disciplina['horarios'] = []

        for i, h in enumerate(disciplina['horas']):
            if h == 2:
                disciplina['horarios'].append(
                    sorted(list(horarios_2))
                    if aulas_aos_sabados
                    else sorted(list(horarios_2 - horarios_s))
                )
            elif h == 3:
                disciplina['horarios'].append(
                    sorted(list(horarios_3))
                    if aulas_aos_sabados
                    else sorted(list(horarios_3 - horarios_s))
                )
            else:
                disciplina['horarios'].append(
                    sorted(list(horarios_t))
                    if aulas_aos_sabados
                    else sorted(list(horarios_t - horarios_s))
                )

    assert len(disciplina['horarios']) == len(disciplina['horas'])
    return disciplina


def completar_cromossomos(disciplina, ultimo_gene):
    num_genes_p = 1
    num_genes_s = len(disciplina['horas'])

    cromossomos = []
    cromossomos.append({   # Professores
        'numero_genes': num_genes_p,
        'limite_inferior': 0,
        'limite_superior': len(disciplina['professores']),
        'slice_i': ultimo_gene,
        'slice_f': ultimo_gene+num_genes_p
    })
    ultimo_gene += num_genes_p
    cromossomos.append({  # Salas
        'numero_genes': num_genes_s,
        'limite_inferior': 0,
        'limite_superior': len(disciplina['salas']),
        'slice_i': ultimo_gene,
        'slice_f': ultimo_gene+num_genes_s
    })
    ultimo_gene += num_genes_s

    num_genes_h = 1
    for horarios in disciplina['horarios']:
        cromossomos.append({  # Horiários
            'numero_genes': num_genes_h,
            'limite_inferior': 0,
            'limite_superior': len(horarios),
            'slice_i': ultimo_gene,
            'slice_f': ultimo_gene+num_genes_h
        })
        ultimo_gene += num_genes_h

    disciplina['cromossomos'] = cromossomos
    return disciplina, ultimo_gene


def completar_metadata(metadata):

    ultimo_gene = 0
    for nome, disciplina in metadata['disciplinas'].items():
        disciplina = completar_nome_disciplina(nome, disciplina)
        disciplina = completar_professores(disciplina)
        disciplina = completar_salas(disciplina)
        disciplina = completar_horarios(disciplina)
        disciplina = completar_laboratorios(disciplina)
        disciplina, ultimo_gene = completar_cromossomos(disciplina,
                                                        ultimo_gene)

    return metadata


def dummy_mut(ind, *args, **kargs):
    return ind,


def dummy_cruz(ind1, ind2, *args, **kargs):
    return ind2, ind1


def criar_cromossomos(metadata):

    cromossomos = []
    for disciplina in metadata['disciplinas'].values():
        for cromo in disciplina['cromossomos']:
            numero_genes = cromo['numero_genes']
            limite_inferior = cromo['limite_inferior']
            limite_superior = cromo['limite_superior']
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
    pprint(metadata, f)
