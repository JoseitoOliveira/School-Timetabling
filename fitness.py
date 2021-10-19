from typing import Dict
from metadata import num_horarios

CHOQUE_SALA = 1
CHOQUE_PROF = 1
AVERSAO_DISCIPLINA = -10
INCAPACIDADE_SALA = -10


def fitness(ind, metadata):
    num_d = len(metadata['disciplinas'])
    num_h = num_horarios

    cromo_horas = [int(x) for x in ind[:num_h]]
    cromo_profe = [int(x) for x in ind[num_h: num_h+num_d]]
    cromo_salas = [int(x) for x in ind[num_h+num_d:]]

    sala_horas = []
    prof_horas = []

    def fit_choque_salas(salas, ini_horas, qtd_horas):
        fit = 0
        for i, sala in enumerate(salas):
            for h in range(ini_horas[i], ini_horas[i]+qtd_horas[i], 1):
                tag = f'{sala}{h}'
                if tag in sala_horas:
                    fit -= CHOQUE_SALA
                else:
                    sala_horas.append(tag)
                    fit += CHOQUE_SALA
        return fit

    def fit_choque_profe(profe, ini_horas, qtd_horas):
        fit = 0
        for i, ini_h in enumerate(ini_horas):
            for h in range(ini_h, ini_h+qtd_horas[i], 1):
                tag = f'{profe}{h}'
                if tag in prof_horas:
                    fit -= CHOQUE_PROF
                else:
                    prof_horas.append(tag)
                    fit += CHOQUE_PROF
        return fit

    def fit_afinidade_disciplina(i_prof, disciplina):
        fit = 0
        profe = metadata['professores'][i_prof]
        nome_disciplina = disciplina['nome']
        if nome_disciplina in profe['disciplinas'].keys():
            fit += profe['disciplinas'][nome_disciplina]
        else:
            fit += AVERSAO_DISCIPLINA
        return fit

    def fit_capacidade_salas(disciplina, i_salas: list):
        fit = 0
        salas = [metadata['salas'][i] for i in i_salas]
        for sala in salas:
            dif = sala['capacidade'] - disciplina['num_alunos']
            if dif >= 0:
                fit += dif
            else:
                fit += dif * INCAPACIDADE_SALA
        return fit

    fit = 0
    ultimo = 0
    for i_d, disciplina in enumerate(metadata['disciplinas']):
        num_h = len(disciplina['horas'])
        horas = cromo_horas[ultimo:num_h]
        salas = cromo_salas[ultimo:num_h]
        profe = cromo_profe[i_d]

        fit += fit_choque_salas(salas, horas, disciplina['horas'])
        fit += fit_choque_profe(profe, horas, disciplina['horas'])
        fit += fit_afinidade_disciplina(profe, disciplina)
        fit += fit_capacidade_salas(disciplina, salas)

        ultimo += num_h

    return fit,
