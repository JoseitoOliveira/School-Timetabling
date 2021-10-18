from functools import partial

from deap import tools
from AG import AG

from AG.utilidades_AG import cruzamento_2pontos
from metadata import num_horarios, num_professores, num_salas, metadata
from fitness import fitness


definições = {
    'otimizacao': (1,),
    'npop': 100,
    'nger': 2000,
    'tam_elitismo': 1,
    'tam_memg': num_horarios + num_professores + num_salas,
    'taxa_cruzamento': 0.70,
    'taxa_mutacao': 0.10,
    'fitness': partial(fitness, metadata=metadata),
    'selecao': {
        'fcn': tools.selRoulette,
        'args': {
        }
    },
    'cromossomos': [
        {  # Horários
            'numero_genes': num_horarios,
            'tipo': int,
            'limite_inferior': 0,
            'limite_superior': len(metadata['horarios']) - 1,
            'mutacao': {
                'fcn': tools.mutFlipBit,
                'args': {
                    'indpb': 0.4,
                },
            },
            'cruzamento': {
                'fcn': cruzamento_2pontos,
                'args': {}
            }
        },
        {  # Professores
            'numero_genes': num_professores,
            'tipo': int,
            'limite_inferior': 0,
            'limite_superior': len(metadata['professores']) - 1,
            'mutacao': {
                'fcn': tools.mutFlipBit,
                'args': {
                    'indpb': 0.4,
                },
            },
            'cruzamento': {
                'fcn': cruzamento_2pontos,
                'args': {}
            }
        },
        {  # Salas
            'numero_genes': num_salas,
            'tipo': int,
            'limite_inferior': 0,
            'limite_superior': len(metadata['salas']) - 1,
            'mutacao': {
                'fcn': tools.mutFlipBit,
                'args': {
                    'indpb': 0.4,
                },
            },
            'cruzamento': {
                'fcn': cruzamento_2pontos,
                'args': {}
            }
        }
    ]
}

if __name__ == "__main__":
    obj = AG(definições)
    list_best_fit, hof = obj.executa(0)
    print(f'{list_best_fit=}')
    print(f'{hof=}')
