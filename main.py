from functools import partial

from deap import tools
from ttictoc import tic, toc

from AG.AG import AG
from AG.utilidades_AG import cruzamento_2pontos
from fitness import fitness, fitness_cache, fitness_meta
from make_pdf import make_html
from metadata import metadata, num_horarios, num_professores, num_salas

TAM_POP = 100
NUM_GEN = 200

definições = {
    'otimizacao': (1,),
    'npop': TAM_POP,
    'nger': NUM_GEN,
    'tam_elitismo': 1,
    'tam_memg': 0,
    'taxa_cruzamento': 0.50,
    'taxa_mutacao': 0.10,
    'fitness': fitness_cache,
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
            'limite_superior': len(metadata['horarios']),
            'mutacao': {
                'fcn': tools.mutUniformInt,
                'args': {
                    'indpb': 0.4,
                    'low': 0,
                    'up': len(metadata['horarios']) - 1
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
            'limite_superior': len(metadata['professores']),
            'mutacao': {
                'fcn': tools.mutUniformInt,
                'args': {
                    'indpb': 0.4,
                    'low': 0,
                    'up': len(metadata['professores']) - 1
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
            'limite_superior': len(metadata['salas']),
            'mutacao': {
                'fcn': tools.mutUniformInt,
                'args': {
                    'indpb': 0.4,
                    'low': 0,
                    'up': len(metadata['salas']) - 1
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

    s = 0
    L = 10
    tic()
    list_best_fit, hof = obj.executa(0)
    print(toc())
    print(f'{list_best_fit=}')
    html = make_html(hof[0])
    with open('output.html', mode='w', encoding='utf8') as f:
        f.write(html)
