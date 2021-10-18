from AG import AG, Plota_2D
from AG.utilidades_AG import (Ackley_function, Beale_function,
                              BukinN6_function, Easom_function,
                              Eggholder_function, Goldstein_function,
                              Himmelblau_function, Min_max_one_function,
                              Rosenbrock_function, ScafferN2_function,
                              Sphere_function, cria_metadados_2D,
                              cria_metadados_min_max_one)

print(f'Min_max_one_function...')
metadados = cria_metadados_min_max_one(Min_max_one_function)
obj = AG(metadados)
list_best_fit, hof = obj.executa(0)
print(f'best_fit = {list_best_fit[-1]}')

print(f'hof = {hof}')
funcoes_de_teste = {
    'Ackley_function': Ackley_function,
    'Rosenbrock_function': Rosenbrock_function,
    'Beale_function': Beale_function,
    'Goldstein_function': Goldstein_function,
    'BukinN6_function': BukinN6_function,
    'Easom_function': Easom_function,
    'Eggholder_function': Eggholder_function,
    'ScafferN2_function': ScafferN2_function,
    'Himmelblau_function': Himmelblau_function,
    'Sphere_function': Sphere_function,
}
for key, value in funcoes_de_teste.items():
    print(f'{key}...')
    metadados = cria_metadados_2D(lambda ind: value(ind[0], ind[1]))
    obj = AG(metadados)
    list_best_fit, hof = obj.executa(0)
    print(f'best_fit = {list_best_fit[-1]}')
    print(f'hof = {hof}')

    # Como são funções 2D, podemos plotar...
    Plota_2D().desenhar_funcao_2D(
        value, hof[0][0], hof[0][1], list_best_fit[-1])

# Espera enter...
wait = input('Pressione uma tecla para continuar...')
