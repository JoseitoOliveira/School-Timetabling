from functools import lru_cache
from statistics import mean, pvariance
from typing import Union

import click
import numpy as np
from tqdm.std import trange

from src.AG.AG2 import AG
from src.AG.utilidades_AG import selTournament
from src.fitness import Fitness
from src.make_output import make_html
from src.metadata import criar_cromossomos, processar_metadata
from src.modelos import get_metadata
from multiprocessing import freeze_support
import webbrowser


class Cached_Fitness():

    def __init__(self) -> None:
        self.fitness = Fitness()

    def apply_metadata(self, metadata):
        self.fitness.metadata = metadata

    @lru_cache(maxsize=2048)
    def _fitness(self, ind):
        return self.fitness(ind)

    def __call__(self, individuo: np.ndarray) -> float:
        return self._fitness(tuple(individuo))


fitness = Cached_Fitness()


class Otimizador:

    def __init__(
        self,
        metadata,
        tam_pop,
        num_ger,
        taxa_cruzamento: Union[float, list[float]] = 0.9,
        taxa_mutacao: Union[float, list[float]] = 0.3,
        num_repeticoes=1,
        tournsize=3
    ):
        if isinstance(taxa_cruzamento, float):
            assert 0 <= taxa_cruzamento <= 1
            self.taxa_cruzamento = [taxa_cruzamento, taxa_cruzamento]
        elif isinstance(taxa_cruzamento, list):
            assert len(taxa_cruzamento) == 2
            for t in taxa_cruzamento:
                assert 0 <= t <= 1
            self.taxa_cruzamento = taxa_cruzamento
        else:
            raise ValueError(f'Taxa de cruzamento inválida: {taxa_cruzamento}')

        if isinstance(taxa_mutacao, float):
            assert 0 <= taxa_mutacao <= 1
            self.taxa_mutacao = [taxa_mutacao, taxa_mutacao]
        elif isinstance(taxa_mutacao, list):
            assert len(taxa_mutacao) == 2
            for t in taxa_mutacao:
                assert 0 <= t <= 1
            self.taxa_mutacao = taxa_mutacao
        else:
            raise ValueError(f'Taxa de mutação inválida: {taxa_mutacao}')

        self.metadata = metadata
        self.tam_pop = tam_pop
        self.num_ger = num_ger
        self.num_repeticoes = num_repeticoes
        self.tournsize = tournsize

    def run(self):
        global fitness

        fitness.apply_metadata(self.metadata)

        definicoes = {
            'otimizacao': (1,),
            'npop': self.tam_pop,
            'nger': self.num_ger,
            'tam_elitismo': 1,
            'tam_memg': 0,
            'taxa_cruzamento': self.taxa_cruzamento,
            'taxa_mutacao': self.taxa_mutacao,
            'fitness': fitness,
            'selecao': {
                'fcn': selTournament,
                'args': {
                    'tournsize': self.tournsize
                }
            },
            'cromossomos': criar_cromossomos(self.metadata)
        }

        obj = AG(definicoes)

        lists_bests_fits = []
        list_best_ind = []
        for _ in trange(max(self.num_repeticoes, 1)):
            list_best_fit, hof = obj.executa()
            lists_bests_fits.append(list_best_fit)
            list_best_ind.append(hof[-1])

        for g in [
            1,
            int(1 / 10 * self.num_ger),
            int(2 / 10 * self.num_ger),
            int(3 / 10 * self.num_ger),
            int(5 / 10 * self.num_ger),
            int(7.5 / 10 * self.num_ger),
            self.num_ger - 1,
        ]:
            aux = [x[g] for x in lists_bests_fits]
            print(f'{g + 1:^3} | {mean(aux):^6.1f} | {pvariance(aux):0.1f}')

        obj2 = AG(definicoes, 'Indivíduos_b.txt')
        for ind in list_best_ind:
            obj2.save_ind(ind)

        best_ind = max(list_best_ind, key=lambda x: x.fitness)
        return best_ind


@click.command()
@click.option('--num_repeticoes', default=1, help='Número de repeticoes')
@click.option('--tam_pop', default=100, help='Tamanho da população')
@click.option('--num_ger', default=100, help='Número de gerações')
@click.option('--taxa_cruzamento', default=0.9, help='Taxa de cruzamento')
@click.option('--taxa_mutacao', default=0.3, help='Taxa de mutação')
@click.option('--tournsize', default=3, help='Tamanho do torneio')
def run_otimizador(
    tam_pop: int,
    num_ger: int,
    taxa_cruzamento: Union[float, list[float]] = 0.9,
    taxa_mutacao: Union[float, list[float]] = 0.3,
    num_repeticoes: int = 1,
    tournsize: int = 3
):
    print('Construindo metadata...')
    metadata = get_metadata()
    print('Processando metadata...')
    metadata = processar_metadata(metadata)
    otimizador = Otimizador(metadata,
                            tam_pop,
                            num_ger,
                            taxa_cruzamento,
                            taxa_mutacao,
                            num_repeticoes,
                            tournsize)
    print('Iniciando otimização...')
    best_ind = otimizador.run()

    html = make_html(best_ind, metadata)
    with open('output.html', mode='w', encoding='utf8') as f:
        f.write(html)

    webbrowser.open('output.html')
    input('Otimização concluída! O resultado foi salvo em output.html')


if __name__ == '__main__':
    freeze_support()
    run_otimizador()
