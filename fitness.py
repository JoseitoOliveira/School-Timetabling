from functools import partial, lru_cache
from metadata import num_horarios, metadata

CHOQUE_SALA = -10
CHOQUE_PROF = -10
CHOQUE_GRADE = -10
AVERSAO_DISCIPLINA = -10
INCAPACIDADE_SALA = -10
HORAS_DIAS_DISTINTOS = -8
AULAS_MESMO_DIA = -8
AULAS_AOS_SABADOS = -5
AULAS_EM_DOIS_TURNOS = -5


def fitness(ind, metadata):
    num_d = len(metadata['disciplinas'])
    num_h = num_horarios

    cromo_horas = [int(x) for x in ind[:num_h]]
    cromo_profe = [int(x) for x in ind[num_h: num_h+num_d]]
    cromo_salas = [int(x) for x in ind[num_h+num_d:]]

    sala_horas = []

    def fit_choque_salas(salas, ini_horas, qtd_horas):
        """Verifica se a sala está ocupada no horário"""
        fit = 0
        for i, sala in enumerate(salas):
            for h in range(ini_horas[i], ini_horas[i]+qtd_horas[i], 1):
                tag = f'{sala}{h}'
                if tag in sala_horas:
                    fit += CHOQUE_SALA
                else:
                    sala_horas.append(tag)
        return fit

    prof_horas = []

    def fit_choque_profe(profe, ini_horas, qtd_horas):
        """Verifica se o professor está ocupada no horário"""
        fit = 0
        for i, ini_h in enumerate(ini_horas):
            for h in range(ini_h, ini_h+qtd_horas[i], 1):
                tag = f'{profe}{h}'
                if tag in prof_horas:
                    fit += CHOQUE_PROF
                else:
                    prof_horas.append(tag)
        return fit

    grade_horas = []

    def fit_choque_grade(grade, ini_horas, qtd_horas):
        """Verifica se a turma está com 2 ou mais aulas no horário"""
        fit = 0
        for i, ini_h in enumerate(ini_horas):
            for h in range(ini_h, ini_h+qtd_horas[i], 1):
                tag = f'{grade}{h}'
                if tag in grade_horas:
                    fit += CHOQUE_GRADE
                else:
                    prof_horas.append(tag)
        return fit

    def fit_afinidade_disciplina(i_prof, disciplina):
        """Verifica se o professor tem afinidade com a disciplina"""
        fit = 0
        profe = metadata['professores'][i_prof]
        nome_disciplina = disciplina['nome']
        if nome_disciplina in profe['disciplinas'].keys():
            fit += profe['disciplinas'][nome_disciplina]
        else:
            fit += AVERSAO_DISCIPLINA
        return fit

    def fit_capacidade_salas(disciplina, i_salas: list):
        """Verifica se a sala comporta os alunos matriculados na disciplina"""
        fit = 0
        salas = [metadata['salas'][i] for i in i_salas]
        for sala in salas:
            dif = sala['capacidade'] - disciplina['num_alunos']
            if dif >= 0:
                fit += dif
            else:
                fit += dif * INCAPACIDADE_SALA
        return fit

    def fit_horas_em_dias_distintos(ini_horas, qtd_horas):
        """Verifica se uma aula começa em um dia e termina em outro"""
        fit = 0
        for h, q in zip(ini_horas, qtd_horas):
            if h % 10 + q > 10:
                fit += HORAS_DIAS_DISTINTOS
        return fit

    def fit_aulas_no_mesmo_dia(ini_horas):
        """Verifica se há duas aulas ou mais de uma mesma diciplina no mesmo dia"""
        fit = 0
        dias = []
        for h in ini_horas:
            dia = int(h/10)
            if dia in dias:
                fit += AULAS_MESMO_DIA
            else:
                dias.append(dia)
        return fit

    def fit_aulas_aos_sabados(ini_horas):
        """Verifica se há aulas aos sábados"""
        fit = 0
        for h in ini_horas:
            dia = int(h/10)
            if dia == 5:
                fit += AULAS_AOS_SABADOS
        return fit

    def fit_aula_em_dois_turnos(ini_horas, qtd_horas):
        """Verifica se uma aula ocupa dois turnos"""
        fit = 0
        for h, q in zip(ini_horas, qtd_horas):
            i_h = h % 10
            if i_h < 5 and i_h + q >= 5:
                fit += AULAS_EM_DOIS_TURNOS
        return fit

    fit = 0
    ultimo = 0
    for i_d, disciplina in enumerate(metadata['disciplinas']):
        num_h = len(disciplina['horas'])
        horas = cromo_horas[ultimo:ultimo+num_h]
        salas = cromo_salas[ultimo:ultimo+num_h]
        profe = cromo_profe[i_d]
        qtd_horas = disciplina['horas']
        grade = disciplina["grade"]

        fit += fit_choque_salas(salas, horas, qtd_horas)
        fit += fit_choque_profe(profe, horas, qtd_horas)
        fit += fit_choque_grade(grade, horas, qtd_horas)
        fit += fit_afinidade_disciplina(profe, disciplina)
        fit += fit_capacidade_salas(disciplina, salas)
        fit += fit_horas_em_dias_distintos(horas, qtd_horas)
        fit += fit_aulas_no_mesmo_dia(horas)
        fit += fit_aulas_aos_sabados(horas)
        fit += fit_aula_em_dois_turnos(horas, qtd_horas)

        ultimo += num_h

    return fit,


fitness_meta = partial(fitness, metadata=metadata)

_fitness_cache = lru_cache(maxsize=32)(fitness_meta)


def fitness_cache(ind):
    return _fitness_cache(tuple(ind))
