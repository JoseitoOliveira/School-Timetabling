from functools import reduce
MUDANÇA_DE_TURNO = -1


def fit_mesmo_turno(ini_horas):
    """ Verifica se os horários da aula são no mesmo turno """
    turnos = map(lambda i: bool(int(i/5) % 2), ini_horas)
    mudança_turno = reduce(lambda x, y: x != y, turnos,)
    return MUDANÇA_DE_TURNO if mudança_turno else 0


fit_mesmo_turno([0, 0])
fit_mesmo_turno([0, 1])
fit_mesmo_turno([0, 5])
fit_mesmo_turno([0, 10])
fit_mesmo_turno([0, 15])
