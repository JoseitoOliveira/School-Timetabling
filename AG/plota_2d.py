import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Plota_2D:
    '''
    Classe de apoio para vizualização dos resultados da otimização de funções 
    com 2D.
    '''

    def __init__(self):
        '''
        Executa testes no próprio construtor.
        '''
        pass

    def desenhar_funcao_2D(self, equacao, x, y, z):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        self._desenhar_plano(equacao, ax)
        self._desenhar_solucao(x, y, z, ax)
        plt.show()

    def _desenhar_plano(self, equacao, ax):
        x = np.linspace(-10, 10, 300)
        y = np.linspace(-10, 10, 300)
        xarray, yarray = np.meshgrid(x, y)
        zarray = equacao(xarray, yarray)[0]
        ax.plot_surface(xarray, yarray, zarray, rstride=1, cstride=1,
                        cmap='viridis', edgecolor='none', alpha=0.8)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

    def _desenhar_solucao(self, x, y, z, ax):
        scat, = ax.plot([], [], [], "o", markersize=7)
        posx_grafico = x
        posy_grafico = y
        posz_grafico = z
        scat.set_data(posx_grafico, posy_grafico)
        scat.set_3d_properties(posz_grafico)
