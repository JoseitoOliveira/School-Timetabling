from deap import base
from deap import creator
from deap import tools
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

import random
import numpy as np


class AG():
    '''
    Classe usada para executar um Algoritmo Genético.
    '''

    def __init__(self, metadados):
        '''
        Cria uma instância da classe.
        O único argumento é metadados, em que devem estar todos os dados 
        necessários para realizar a otimização.
        Atenção: 
            Não foi feita uma cópia de metadados, apenas uma referência!
        '''

        self.metadados = metadados

    def _cria_individuo(self):
        '''
        Retorna um individuo completo conforme definido pela lista:
        self.metadados['cromossomos']
        '''

        individuo = np.array([])

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

    def _selecao(self, pop, k):
        '''
        '''
        selecao_fcn = self.metadados['selecao']['fcn']
        selecao_args = self.metadados['selecao']['args']
        selecionado = selecao_fcn(pop, k, **selecao_args)
        return selecionado

    def _cruzamento_numpy(self, ind1, ind2):
        '''
        Essa rotina opera por cromossomo.
        Retorno: os dois indivíduos recebidos com alterações.
        '''

        pos = 0
        for item in self.metadados['cromossomos']:
            genes = item['numero_genes']
            cruzamento_fcn = item['cruzamento']['fcn']
            cruzamento_args = item['cruzamento']['args']
            cruzamento_fcn(ind1[pos:pos+genes],
                           ind2[pos:pos+genes], **cruzamento_args)
            pos += genes
        return ind1, ind2

    def _mutacao_numpy(self, ind):
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
            mutacao_fcn(ind[pos:pos+genes], **mutacao_args)
            ind[pos:pos+genes] = np.clip(ind[pos:pos+genes],
                                         limite_inf, limite_sup)
            pos += genes
        return ind,

    def _cria_memg(self, populacao):
        '''
        Criação das listas de memórias (individuos e seus respectivos fitness).
        Argumentos:
        > populacao: populacao de individuos
        Atenção: supõe-se que tam_mem <= tamanho de população. Não é feito teste!
        '''

        tam_memg = self.metadados['tam_memg']
        fcn_fitness = self.metadados['fitness']

        mem_ind, mem_fit = [], []
        for i in range(tam_memg):
            mem_ind.append(populacao[i].copy())
            mem_fit.append(fcn_fitness(populacao[i]))

        return mem_ind, mem_fit

    def _memg_fitness(self, individuo, mem_ind, mem_fit):
        '''
        Avaliação dos indivíduos acrescida do operador de memória genética.
        > individuo: individuo da populacao cuja fitness desejamos calcular.
        > mem_ind: lista de individuos armazenados na memoria
        > mem_fit: lista de tuplas com fitness armazenados na memoria
        Retorno: tupla com a aptidão calculada para "individuo".
        '''

        def array_eq_in_list(myarr, list_arrays):
            for idx, elem in enumerate(list_arrays):
                if(np.array_equal(elem, myarr)):
                    return idx, True
            return -1, False

        fcn_fitness = self.metadados['fitness']
        if(len(mem_ind) == 0):
            return fcn_fitness(individuo)

        # chegando aqui, sabemos que há memória genética...

        fit_individuo = None
        idx, flag = array_eq_in_list(individuo, mem_ind)
        if flag:
            fit_individuo = mem_fit[idx]
            mem_ind.pop(idx)
            mem_fit.pop(idx)
        else:
            del mem_ind[-1]
            del mem_fit[-1]
            fit_individuo = fcn_fitness(individuo)

        mem_ind.insert(0, individuo)
        mem_fit.insert(0, fit_individuo)

        return fit_individuo

    def _print_pop(self, pop, name):
        '''
        Imprime a população na tela para depuração.
        '''

        print(f'{name} = ')
        for ind in pop:
            for gene in ind:
                print(f'{gene:8.4f},', end='')
            print('')
        print('-----\n')

    def _print_pop_fit(self, pop, fits, name):
        '''
        Imprime a população com fitness na tela para depuração.
        '''

        print(f'{name} = ')
        for ind, fit in zip(pop, fits):
            for gene in ind:
                print(f'{gene:8.4f},', end='')
            print(f' ==> fit:{fit[0]:12.4f}')
        print('-----\n')

    def executa(self, habilita_depuracao=0):
        '''
        > habilita_depuracao: 0 para não e 1 para sim.
        Retorna:
        > Melhor fitness ao longo das gerações
        > Melhor indivíduo encontrado no algoritmo
        > Tempo de execução do algoritmo
        '''

        # Formulação do problema e definição da classe base dos indivíduos
        pesos = self.metadados['otimizacao']
        creator.create("Problema", base.Fitness, weights=pesos)
        creator.create("Individual", np.ndarray, fitness=creator.Problema)

        # Cria o pool de processos
        mp = Pool(cpu_count() - 1)
        fnc_fitness = self.metadados['fitness']

        def multi_fitness(pop):
            _pop = [[int(x) for x in ind] for ind in pop]
            return mp.map(fnc_fitness, _pop, chunksize=100)

        # Registro das estruturas

        toolbox = base.Toolbox()
        toolbox.register("map", mp.map)
        toolbox.register("attr", self._cria_individuo)
        toolbox.register("individual", tools.initIterate,
                         creator.Individual, toolbox.attr)
        toolbox.register("population", tools.initRepeat,
                         list, toolbox.individual)
        toolbox.register("mate", self._cruzamento_numpy)
        toolbox.register("mutate", self._mutacao_numpy)
        toolbox.register("select", self._selecao)

        # Inicia hall of fame: hof
        tam_elitismo = self.metadados['tam_elitismo']
        tam_hof = tam_elitismo if (tam_elitismo > 0) else 1

        # Cria a população inicial
        pop = toolbox.population(n=self.metadados['npop'])

        # Registra "_memg_fitness" como a função fitness
        toolbox.register("evaluate", self.metadados['fitness'])

        # Avalia a população
        #fitnesses = list(map(toolbox.evaluate, pop))
        fitnesses = multi_fitness(pop)

        for ind, fit in zip(pop, fitnesses):
            ind.fitness.values = fit

        # Inicializa o hof
        hof = tools.HallOfFame(tam_hof, similar=np.array_equal)
        hof.update(pop)

        # Cria a lista que armazenará a melhor fitness ao longo das gerações
        list_best_fit = []
        if pesos[0] < 0:
            list_best_fit.append(min(fitnesses))
        else:
            list_best_fit.append(max(fitnesses))

        # Loop principal de gerações
        geracoes = self.metadados['nger']
        taxa_cruzamento = self.metadados['taxa_cruzamento']
        taxa_mutacao = self.metadados['taxa_mutacao']

        pbar_geracoes = tqdm(range(geracoes))
        for g in pbar_geracoes:

            # Seleciona "npop-tam_elitismo" indivíduos
            offspring = toolbox.select(pop, len(pop) - tam_elitismo)
            offspring = list(map(toolbox.clone, offspring))

            # Aplica cruzamento
            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < taxa_cruzamento:
                    toolbox.mate(child1, child2)
                    del child1.fitness.values
                    del child2.fitness.values

            # Aplica mutação
            for mutant in offspring:
                if random.random() < taxa_mutacao:
                    toolbox.mutate(ind=mutant)
                    del mutant.fitness.values

            # Avalia indivíduos (apenas aqueles que foram modificados)
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            # fitnesses = list(map(toolbox.evaluate, invalid_ind))
            fitnesses = multi_fitness(invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit

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

            # Atualiza o hall da fama
            hof.update(pop)

            pbar_geracoes.set_description(f'Melhor fit={list_best_fit[-1]}')

        del creator.Problema
        del creator.Individual

        return (list_best_fit, hof)
