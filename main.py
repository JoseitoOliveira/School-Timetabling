from functools import lru_cache
from statistics import mean, pvariance

from tqdm.std import tqdm, trange

from src.AG.AG2 import AG
from src.AG.utilidades_AG import selTournament
from src.fitness import fitness
from src.make_output import make_html
from src.metadata import criar_cromossomos, metadata

TAM_POP = 2**4
NUM_GER = 2**3
NUM_REPETICOES = 2
TAM_CACHE = TAM_POP


_fitness_cache = lru_cache(maxsize=TAM_CACHE)(fitness)


def fitness_cache(ind):
    return _fitness_cache(tuple(ind))


def taxa_mutacao(ger):
    return 0.10


def taxa_cruzamento(ger):
    return 0.90


definicoes = {
    'otimizacao': (1,),
    'npop': TAM_POP,
    'nger': NUM_GER,
    'tam_elitismo': 1,
    'tam_memg': 0,
    'taxa_cruzamento': taxa_cruzamento,
    'taxa_mutacao': taxa_mutacao,
    'fitness': fitness_cache,
    'selecao': {
        'fcn': selTournament,
        'args': {
            'tournsize': 3
        }
    },
    'cromossomos': criar_cromossomos(metadata)
}

if __name__ == "__main__":
    obj = AG(definicoes)

    lists_bests_fits = []
    list_best_ind = []
    for _ in trange(max(NUM_REPETICOES, 1)):
        list_best_fit, hof = obj.executa()
        lists_bests_fits.append(list_best_fit)
        list_best_ind.append(hof[-1])

    for g in [
        1,
        int(1/10 * NUM_GER),
        int(2/10 * NUM_GER),
        int(3/10 * NUM_GER),
        int(5/10 * NUM_GER),
        int(7.5/10 * NUM_GER),
        NUM_GER - 1,
    ]:
        aux = [x[g] for x in lists_bests_fits]
        print(f'{g + 1:^3} | {mean(aux):^6.1f} | {pvariance(aux):0.1f}')

    obj2 = AG(definicoes, 'out/Indivíduos_b.txt')
    for ind in list_best_ind:
        obj2.save_ind(ind)

    best_ind = max(list_best_ind, key=lambda x: x.fitness)
    html = make_html(best_ind)
    with open('out/output.html', mode='w', encoding='utf8') as f:
        f.write(html)
