from deap import tools
from ttictoc import tic, toc

from AG.AG import AG
from fitness import fitness_cache
from make_pdf import make_html
from metadata import criar_cromossomos, metadata
TAM_POP = 200
NUM_GEN = 1000


definições = {
    'otimizacao': (1,),
    'npop': TAM_POP,
    'nger': NUM_GEN,
    'tam_elitismo': 10,
    'tam_memg': 0,
    'taxa_cruzamento': 0.50,
    'taxa_mutacao': 0.20,
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

    s = 0
    L = 10
    tic()
    list_best_fit, hof = obj.executa(0)
    print(toc())
    print(f'{list_best_fit=}')
    print(f'{hof[0]=}')
    html = make_html(hof[0])
    with open('output.html', mode='w', encoding='utf8') as f:
        f.write(html)
