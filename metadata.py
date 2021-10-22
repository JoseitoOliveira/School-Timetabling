from deap import tools

from AG.utilidades_AG import cruzamento_2pontos

metadata = {
    "professores": [
        {
            "nome": "Cícero",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {  # nome: afinidade
                "Instrumentação Eletrônica": 2,
            }
        },
        {
            "nome": "Fabiano",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Máquinas Elétricas": 1,
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
                "Filtros": 2
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
                "Acionamentos e Circuitos Elétricos": 2
            }
        },
        {
            "nome": "Protásio",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Microc e Microp": 2
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
            "capacidade": 30
        }
    ],
    "grades": [
        "p7",
        "p8"
    ],
    "disciplinas": [
        {
            "nome": "Instrumentação Eletrônica",
            "grade": "p7",
            "num_alunos": 10,
            "horas": [2, 2]
        },
        {
            "nome": "Máquinas Elétricas",
            "grade": "p7",
            "num_alunos": 20,
            "horas": [2, 3]
        },
        {
            "nome": "Controle I",
            "grade": "p7",
            "num_alunos": 15,
            "horas": [2, 3]
        },
        {
            "nome": "Princípios de Comunicações",
            "grade": "p7",
            "num_alunos": 12,
            "horas": [2, 3]
        },
        {
            "nome": "Sistemas Elétricos",
            "grade": "p7",
            "num_alunos": 20,
            "horas": [2, 3]
        },
        {
            "nome": "Eletrônica de Potência",
            "grade": "p7",
            "num_alunos": 25,
            "horas": [2, 3]
        },
        {
            "nome": "Técnicas de Medição",
            "grade": "p8",
            "num_alunos": 22,
            "horas": [2, 2]
        },
        {
            "nome": "Análise de Sistemas Elétricos",
            "grade": "p8",
            "num_alunos": 15,
            "horas": [2, 2]
        },
        {
            "nome": "Filtros",
            "grade": "p8",
            "num_alunos": 15,
            "horas": [2, 2]
        },
        {
            "nome": "Instrumentação Industrial",
            "grade": "p8",
            "num_alunos": 15,
            "horas": [2, 2]
        },
        {
            "nome": "Acionamentos e Circuitos Elétricos",
            "grade": "p8",
            "num_alunos": 15,
            "horas": [2, 2]
        },
        {
            "nome": "Microc e Microp",
            "grade": "p8",
            "num_alunos": 15,
            "horas": [2, 2]
        },
    ],
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
        "7T5"]
}


def completar_metadata(metadata):

    professores = metadata['professores']
    salas = metadata['salas']
    nomes_salas_válidos = [sala['nome'] for sala in salas]
    ultimo_gene = 0
    for disciplina in metadata['disciplinas']:

        disciplina['professores'] = [
            {'nome': profe['nome'],
             'afinidade': profe['disciplinas'][disciplina['nome']]}
            for profe in professores
            if disciplina['nome'] in profe['disciplinas'].keys()
        ]

        if disciplina['professores'] == []:
            raise Exception(
                f'Não há professores para a disciplina {disciplina["nome"]}.'
            )

        if 'salas' not in disciplina:
            disciplina['salas'] = [
                sala for sala in salas
                if sala['capacidade'] >= disciplina['num_alunos']
            ]
        else:
            nomes_salas = disciplina['salas']

            for nome_sala in nomes_salas:
                if nome_sala not in nomes_salas_válidos:
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

        num_genes_p = 1
        num_genes_s = len(disciplina['horas'])
        num_genes_h = len(disciplina['horas'])

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
        cromossomos.append({  # Horiários
            'numero_genes': num_genes_h,
            'limite_inferior': 0,
            'limite_superior': len(metadata['horarios']),
            'slice_i': ultimo_gene,
            'slice_f': ultimo_gene+num_genes_h
        })
        ultimo_gene += num_genes_h

        disciplina['cromossomos'] = cromossomos

    return metadata


def criar_cromossomos(metadata):
    def dummy_mut(ind, *args, **kargs):
        return ind,

    def dummy_cruz(ind1, ind2, *args, **kargs):
        return ind1, ind2

    cromossomos = []
    for disciplina in metadata['disciplinas']:
        for cromo in disciplina['cromossomos']:
            numero_genes = cromo['numero_genes']
            limite_inferior = cromo['limite_inferior']
            limite_superior = cromo['limite_superior']
            diff_limite = limite_superior - limite_inferior
            cromossomos.append({
                'numero_genes': numero_genes,
                'tipo': int,
                'limite_inferior': limite_inferior,
                'limite_superior': limite_superior,
                'mutacao': {
                    'fcn': tools.mutUniformInt if diff_limite > 1 else dummy_mut,
                    'args': {
                        'indpb': 0.4,
                        'low': 0,
                        'up': limite_superior - 1
                    },
                },
                'cruzamento': {
                    'fcn': cruzamento_2pontos if diff_limite > 1 else dummy_cruz,
                    'args': {}
                }
            })
    return cromossomos


metadata = completar_metadata(metadata)

with open('metadata_c.py', mode='w', encoding='utf8') as f:
    from pprint import pprint
    pprint(metadata, f)
