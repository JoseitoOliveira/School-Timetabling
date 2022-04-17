from src.AG.utilidades_AG import HallOfFame
from src.AG.classes import Individual
from tqdm import tqdm
import numpy as np
from typing import List
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from copy import deepcopy
from functools import partial
from multiprocessing import cpu_count


class AG():
    '''
    Classe usada para executar um Algoritmo Genético.
    '''

    def __init__(self, metadados: dict, filename: str = 'Indivíduos.txt'):
        '''
        Cria uma instância da classe.
        O único argumento é metadados, em que devem estar todos os dados
        necessários para realizar a otimização.
        Atenção:
            Não foi feita uma cópia de metadados, apenas uma referência!
        '''
        self.filename = filename
        with open(self.filename, mode='w', encoding='utf8') as f:
            f.write('')

        self.metadados = metadados

    def _cria_individuo(self):
        '''
        Retorna um individuo completo conforme definido pela lista:
        self.metadados['cromossomos']
        '''

        individuo = np.array([], 'I')

        for item in self.metadados['cromossomos']:

            nro_genes = item['numero_genes']
            tipo = item['tipo']
            limite_inf = item['limite_inferior']
            limite_sup = item['limite_superior']

            fcn = None
            if tipo is float:
                fcn = np.random.uniform
            elif tipo is int:
                fcn = np.random.randint
            else:
                raise Exception('Tipo de gene não suportado.')

            aux = fcn(limite_inf, limite_sup, nro_genes)
            individuo = np.concatenate((individuo, aux))

        return individuo

    def _selecao(self, pop: list, k):
        '''
        '''
        selecao_fcn = self.metadados['selecao']['fcn']
        selecao_args = self.metadados['selecao']['args']

        selecionado = selecao_fcn(pop, k, **selecao_args)
        return selecionado

    def _cruzamento_numpy(self, ind1: Individual, ind2: Individual):
        '''
        Essa rotina opera por cromossomo.
        Retorno: os dois indivíduos recebidos com alterações.
        '''

        pos = 0
        for item in self.metadados['cromossomos']:
            genes = item['numero_genes']
            cruzamento_fcn = item['cruzamento']['fcn']
            cruzamento_args = item['cruzamento']['args']
            cruzamento_fcn(ind1[pos:pos + genes],
                           ind2[pos:pos + genes], **cruzamento_args)
            pos += genes
        return ind1, ind2

    def _mutacao_numpy(self, ind: Individual):
        '''
        Implementa a mutação de ind, conforme especificado em metadados.

        OBS:
        A mutação inteira permite fornecer os limites inf e sup, mas são ambos
        "inclusivos". Por isso, nos cromossomos inteiros vamos mandar:
            "up = limsup_2-1".

        Retorna um individuo após mutação "inplace".
        '''

        pos = 0
        for item in self.metadados['cromossomos']:
            mutacao_fcn = item['mutacao']['fcn']
            mutacao_args = item['mutacao']['args']
            genes = item['numero_genes']
            limite_inf = item['limite_inferior']
            limite_sup = item['limite_superior']
            mutacao_fcn(ind[pos:pos + genes], **mutacao_args)
            ind[pos:pos + genes] = np.clip(ind[pos:pos + genes],
                                           limite_inf, limite_sup)
            pos += genes
        return ind,

    def _population(self, n):
        return [Individual(self._cria_individuo()) for _ in range(n)]

    def worker(self, pop: list, npop,
               n_workers,
               taxa_cruzamento,
               taxa_mutacao,
               fnc_fitness):

        # Seleciona "npop-tam_elitismo" indivíduos
        offspring: List[Individual] = self.metadados['selecao']['fcn'](
            individuals=pop,
            k=int(npop / n_workers),
            **self.metadados['selecao']['args']
        )
        offspring = [deepcopy(ind) for ind in offspring]

        # Aplica cruzamento
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < taxa_cruzamento:
                self._cruzamento_numpy(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        # Aplica mutação
        for mutant in offspring:
            if random.random() < taxa_mutacao:
                self._mutacao_numpy(ind=mutant)
                del mutant.fitness.values

        # Avalia indivíduos (apenas aqueles que foram modificados)
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = [fnc_fitness(ind) for ind in invalid_ind]
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        return offspring

    def save_ind(self, ind: np.ndarray):
        fit_sum, fit = self.metadados['fitness'](ind)
        with open(self.filename, mode='a', encoding='utf8') as f:
            f.write(f'{fit}\n{ind}\n\n')

    def executa(self):

        n_workers = cpu_count()

        pesos = self.metadados['otimizacao']

        # Inicia hall of fame: hof
        tam_elitismo = self.metadados['tam_elitismo']
        tam_hof = tam_elitismo if (tam_elitismo > 0) else 1

        # Cria a população inicial
        npop = self.metadados['npop']
        pop: list = self._population(n=npop)

        fitnesses: list = [self.metadados['fitness'](ind) for ind in pop]
        for ind, fit in zip(pop, fitnesses):
            ind.fitness.values = fit

        # Inicializa o hof
        hof = HallOfFame(tam_hof, similar=np.array_equal)
        hof.update(pop)

        # Cria a lista que armazenará a melhor fitness ao longo das gerações
        list_best_fit = []

        # Loop principal de gerações
        geracoes = self.metadados['nger']

        worker = partial(self.worker,
                         npop=npop,
                         n_workers=n_workers,
                         fnc_fitness=self.metadados['fitness'])

        taxa_cruzamento = self.metadados['taxa_cruzamento']
        taxa_mutacao = self.metadados['taxa_mutacao']

        def fun_cruzamento(g):
            x1, x2 = 0, geracoes
            y1, y2 = taxa_cruzamento
            a = (y2 - y1) / (x2 - x1)
            b = y1 - a * x1
            return a * g + b

        def fun_mutacao(g):
            x1, x2 = 0, geracoes
            y1, y2 = taxa_mutacao
            a = (y2 - y1) / (x2 - x1)
            b = y1 - a * x1
            return a * g + b

        with ProcessPoolExecutor(n_workers) as mp:
            pbar_geracoes = tqdm(range(geracoes))
            for g in pbar_geracoes:
                offspring = []
                futures = [
                    mp.submit(
                        worker,
                        pop=pop,
                        taxa_cruzamento=fun_cruzamento(g),
                        taxa_mutacao=fun_mutacao(g),
                    )
                    for _ in range(n_workers)
                ]
                for result in as_completed(futures):
                    offspring.extend(result.result())

                # Adiciona hall da fama (elitismo)
                if tam_elitismo > 0:
                    offspring.extend(hof.items)

                # Atualiza a população
                pop = offspring

                # Salva a melhor fitness da população atual
                fits = [ind.fitness.values[0] for ind in pop]
                if pesos[0] < 0:
                    list_best_fit.append(min(fits))
                else:
                    list_best_fit.append(max(fits))

                if (
                    len(list_best_fit) == 1 or
                    list_best_fit[-1] != list_best_fit[-2]
                ):
                    ind = pop[fits.index(list_best_fit[-1])]
                    self.save_ind(ind)

                # Atualiza o hall da fama
                hof.update(pop)

                pbar_geracoes.set_description(
                    f'Melhor fit={list_best_fit[-1]:0.2f} {len(pop)}')

        return (list_best_fit, hof)
