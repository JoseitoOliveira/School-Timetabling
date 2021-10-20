from deap import tools
import json

from AG.utilidades_AG import cruzamento_2pontos

metadata = {
    "professores": [
        {
            "nome": "Prof A",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {  # nome: afinidade
                "Física": 1,
                "Cálculo 1": 2
            }
        },
        {
            "nome": "Prof B",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Química": 1,
                "Cálculo 2": 1
            }
        },
        {
            "nome": "Prof C",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Introdução a Computação": 2
            }
        }],
    "salas": [
        {
            "nome": "CTM1",
            "capacidade": 30
        },
        {
            "nome": "CTM2",
            "capacidade": 45
        }],
    "grades": [
        "p1",
        "p2"],
    "disciplinas": [
        {
            "nome": "Física",
            "grade": "p1",
            "num_alunos": 10,
            "horas": [
                2,
                3
            ]
        },
        {
            "nome": "Cálculo 1",
            "grade": "p1",
            "num_alunos": 20,
            "horas": [
                2,
                3
            ]
        },
        {
            "nome": "Química",
            "grade": "p2",
            "num_alunos": 15,
            "horas": [
                2,
                3
            ]
        },
        {
            "nome": "Cálculo 2",
            "grade": "p2",
            "num_alunos": 12,
            "horas": [
                2,
                3
            ]
        },
        {
            "nome": "Introdução a Computação",
            "grade": "p2",
            "num_alunos": 35,
            "horas": [
                2,
                3
            ]
        }],
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

    return metadata


def dummy_mut(ind, *args, **kargs):
    return ind,


def dummy_cruz(ind1, ind2, *args, **kargs):
    return ind1, ind2


def criar_cromossomos(metadata):
    cromossomos = []
    for disciplina in metadata['disciplinas']:
        limite_superior = {
            'horas': len(metadata['horarios']),
            'professores': len(disciplina['professores']),
            'salas': len(disciplina['salas'])
        }
        for tipo in ['horas', 'professores', 'salas']:
            numero_genes = len(disciplina[tipo])
            cromossomos.append({
                'numero_genes': numero_genes if tipo != 'profesores' else 1,
                'tipo': int,
                'limite_inferior': 0,
                'limite_superior': limite_superior[tipo],
                'mutacao': {
                    'fcn': tools.mutUniformInt if limite_superior[tipo] > 1 else dummy_mut,
                    'args': {
                        'indpb': 0.4,
                        'low': 0,
                        'up': limite_superior[tipo] - 1
                    },
                },
                'cruzamento': {
                    'fcn': cruzamento_2pontos if limite_superior[tipo] > 1 else dummy_cruz,
                    'args': {}
                }
            })
    return cromossomos


metadata = completar_metadata(metadata)

with open('metadata.json', mode='w', encoding='utf8') as f:
    json.dump(metadata, f)
