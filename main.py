from deap import tools
from ttictoc import tic, toc
from functools import lru_cache

from AG2 import AG
from fitness import fitness_meta
from make_pdf import make_html
from metadata import criar_cromossomos, metadata

TAM_POP = 2**12
TAM_CACHE = TAM_POP
NUM_GER = 10_000


_fitness_cache = lru_cache(maxsize=TAM_CACHE)(fitness_meta)


def fitness_cache(ind):
    return _fitness_cache(tuple(ind))


definições = {
    'otimizacao': (1,),
    'npop': TAM_POP,
    'nger': NUM_GER,
    'tam_elitismo': 1,
    'tam_memg': 0,
    'taxa_cruzamento': 0.75,
    'taxa_mutacao': 0.10,
    'fitness': fitness_cache,
    'selecao': {
        'fcn': tools.selRoulette,
        'args': {
        }
    },
    'cromossomos': criar_cromossomos(metadata)
}

if __name__ == "__main__":
    obj = AG(definições)

    list_best_fit, hof = obj.executa()
    print(f'{list_best_fit[-1]=}')
    print(f'{len(list_best_fit)=}')
    print(f'{hof[0]=}')
    html = make_html(hof[0])
    with open('output.html', mode='w', encoding='utf8') as f:
        f.write(html)
