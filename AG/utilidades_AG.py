import random
import numpy as np
from numba import jit

from deap import tools


@jit
def cruzamento_1ponto(ind1, ind2):
    '''
    Rotina de apoio para cruzamento em 1 ponto.
    '''

    pos_ini = 0
    pos_fim = len(ind1)
    size = pos_fim - pos_ini
    p1 = pos_ini + random.randint(1, size)
    ind1[p1:pos_fim], ind2[p1:pos_fim] = ind2[p1:pos_fim].copy(
    ), ind1[p1:pos_fim].copy()
    return ind1, ind2


@jit
def cruzamento_2pontos(ind1, ind2):
    '''
    Rotina de apoio para cruzamento em 2 pontos.
    '''
    pos_ini = 0
    pos_fim = len(ind1)
    size = pos_fim - pos_ini
    p1 = pos_ini + random.randint(1, size)
    p2 = pos_ini + random.randint(1, size - 1)
    if p2 >= p1:
        p2 += 1
    else:
        p1, p2 = p2, p1

    ind1[p1:p2], ind2[p1:p2] = ind2[p1:p2].copy(), ind1[p1:p2].copy()
    return ind1, ind2


def Min_max_one_function(ind):
    return sum(ind),


def Ackley_function(x, y):
    return -20*np.exp(-0.2*np.sqrt(0.5*(x**2+y**2))) - np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y))) + np.exp(1)+20,


def Rosenbrock_function(x, y):
    return (100*(y-x**2)**2+(1 - x)**2),


def Beale_function(x, y):
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2,


def Goldstein_function(x, y):
    return (1+((x+y+1)**2)*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+((2*x-3*y)**2)*(18-32*x+12*x**2+48*y-36*x*y+27*y**2)),


def BukinN6_function(x, y):
    return 100*np.sqrt(abs(y-0.01*x**2))+0.01*abs(x+10),


def Easom_function(x, y):
    return -np.cos(x)*np.cos(y)*np.e**(-((x-np.pi)**2+(y-np.pi)**2)),


def Eggholder_function(x, y):
    return -(y+47)*np.sin(np.sqrt(abs(x/2 + y+47)))-x*np.sin(np.sqrt(abs(x-y-47))),


def ScafferN2_function(x, y):
    return 0.5 + ((np.sin(x**2-y**2)**2 - 0.5)/(1+0.001*(x**2+y**2))**2),


def Himmelblau_function(x, y):
    return (x**2+y-11)**2 + (x+y**2-7)**2,


def Sphere_function(x, y):
    return x**2 + y**2,


def cria_metadados_min_max_one(fitness):
    '''
    Monta o dicionário para a função de teste min_max_one.
    ATENÇÃO: o método de seleção escolhido aqui foi a roleta, logo o 
    problema precisa ser de maximização em pesos.
    '''

    num_genes = 20

    return {
        'otimizacao': (1,),
        'npop': num_genes * 10,
        'nger': 200,
        'tam_elitismo': 1,
        'tam_memg': num_genes,
        'taxa_cruzamento': 0.70,
        'taxa_mutacao': 0.10,
        'fitness': fitness,
        'selecao': {
            'fcn': tools.selRoulette,
            'args': {
            }
        },
        'cromossomos': [
            {
                'numero_genes': num_genes,
                'tipo': int,
                'limite_inferior': 0,
                'limite_superior': 2,
                'mutacao': {
                    'fcn': tools.mutFlipBit,
                    'args': {
                        'indpb': 0.4,
                    },
                },
                'cruzamento': {
                    'fcn': cruzamento_2pontos,
                    'args': {
                    }
                },
            }
        ],
    }


def cria_metadados_2D(fitness):
    '''
    Monta o dicionário para as funções de teste de 2D.
    '''

    num_genes = 2
    limite_inferior = -10
    limite_superior = 10

    return {
        'otimizacao': (-1,),
        'npop': num_genes * 10,
        'nger': 100,
        'tam_elitismo': 1,
        'tam_memg': num_genes,
        'taxa_cruzamento': 0.70,
        'taxa_mutacao': 0.10,
        'fitness': fitness,
        'selecao': {
            'fcn': tools.selSPEA2,
            'args': {
            },
        },
        'cromossomos': [
            {
                'numero_genes': num_genes,
                'tipo': float,
                'limite_inferior': limite_inferior,
                'limite_superior': limite_superior,
                'mutacao': {
                    'fcn': tools.mutGaussian,
                    'args': {
                        'mu': 0.0,
                        'sigma': (limite_superior - limite_inferior)/10,
                        'indpb': 0.50,
                    },
                },
                'cruzamento': {
                    'fcn': tools.cxBlend,
                    'args': {
                        'alpha': random.random(),
                    },
                },
            },
        ],
    }
