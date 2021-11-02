from functools import partial
from metadata import metadata
from more_itertools import pairwise

CHOQUE_SALA = -20
CHOQUE_PROF = -20
CHOQUE_GRADE = -20
AULAS_AOS_SABADOS = -20
HORAS_DIAS_DISTINTOS = -15
AULAS_MESMO_DIA = -8
AULAS_EM_DOIS_TURNOS = -10
AULAS_EM_M1_T1 = -10
PESO_DISTANCIA_ENTRE_SALAS = -2 * 1e-1


def fitness(ind, metadata):

    sala_horas = []

    def fit_choque_salas(salas, ini_horas, qtd_horas):
        """Verifica se a sala está ocupada no horário"""
        fit = 0
        for i, sala in enumerate(salas):
            nome_sala = sala['nome']
            for h in range(ini_horas[i], ini_horas[i]+qtd_horas[i], 1):
                tag = f'{nome_sala}{h}'
                if tag in sala_horas:
                    fit += CHOQUE_SALA
                else:
                    sala_horas.append(tag)
        return fit

    prof_horas = []

    def fit_choque_profe(profe, ini_horas, qtd_horas):
        """Verifica se o professor está ocupada no horário"""
        fit = 0
        nome_professor = profe['nome']
        for i, ini_h in enumerate(ini_horas):
            for h in range(ini_h, ini_h+qtd_horas[i], 1):
                tag = f'{nome_professor}{h}'
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
                    grade_horas.append(tag)
        return fit

    def fit_afinidade_disciplina(i_prof, disciplina):
        """Verifica se o professor tem afinidade com a disciplina"""
        return disciplina['professores'][i_prof]['afinidade']

    def fit_capacidade_salas(disciplina, salas: list):
        """Verifica se a sala comporta os alunos matriculados na disciplina"""
        fit = 0
        for sala in salas:
            dif = sala['capacidade'] - disciplina['num_alunos']
            if dif >= 0:
                fit += dif
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
            if h > 49:
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

    def fit_aulas_M1_T1(ini_horas, qtd_horas):
        """Verifica se há aulas nos horários M1 e T1"""
        fit = 0
        for ini_h, qtd_hora in zip(ini_horas, qtd_horas):
            for h in range(ini_h, ini_h+qtd_hora, 1):
                if h % 5 == 0:
                    fit += AULAS_EM_M1_T1
        return fit

    grade_dia_sala = {
        grade: {
            dia: []
            for dia in range(7)
        } for grade in metadata['grades']
    }

    def adicionar_grade_dia_sala(salas, ini_horas, qtd_horas, grade):
        for ini_h, qtd_hora, sala in zip(ini_horas, qtd_horas, salas):
            for h in range(ini_h, ini_h+qtd_hora, 1):
                dia = int(h/10)
                grade_dia_sala[grade][dia].append((h, sala))

    def fit_distancia_percorrida():
        def calc_distancia(s1, s2):
            return metadata['distancias'][s1['nome']][s2['nome']]
        distancia = 0
        for grade in metadata['grades']:
            _grade = grade_dia_sala[grade]
            for dia in range(6):
                h_salas = sorted(_grade[dia], key=lambda x: x[0])
                for (_, s1), (_, s2) in pairwise(h_salas):
                    distancia += calc_distancia(s1, s2)
        return distancia * PESO_DISTANCIA_ENTRE_SALAS

    fit = 0
    for disciplina in metadata['disciplinas']:
        cromo_p = disciplina['cromossomos'][0]
        cromo_s = disciplina['cromossomos'][1]
        cromos_h = disciplina['cromossomos'][2:]
        i_p = ind[cromo_p['slice_i']:cromo_p['slice_f']]
        i_s = ind[cromo_s['slice_i']:cromo_s['slice_f']]

        i_h = []
        for i, horarios in enumerate(disciplina['horarios']):
            cromo_h = cromos_h[i]
            index_h = ind[cromo_h['slice_i']:cromo_h['slice_f']][0]
            horario = horarios[index_h]
            i_h.append(metadata['horarios'].index(horario))

        salas = [disciplina['salas'][i] for i in i_s]

        qtd_horas = disciplina['horas']
        grade = disciplina['grade']
        profe = disciplina['professores'][i_p[0]]
        fit += fit_choque_salas(salas, i_h, qtd_horas)
        fit += fit_choque_profe(profe, i_h, qtd_horas)
        fit += fit_choque_grade(grade, i_h, qtd_horas)
        fit += fit_afinidade_disciplina(i_p[0], disciplina)
        # fit += fit_capacidade_salas(disciplina, salas)
        fit += fit_horas_em_dias_distintos(i_h, qtd_horas)
        fit += fit_aulas_no_mesmo_dia(i_h)
        fit += fit_aulas_aos_sabados(i_h)
        fit += fit_aula_em_dois_turnos(i_h, qtd_horas)
        fit += fit_aulas_M1_T1(i_h, qtd_horas)

        adicionar_grade_dia_sala(salas, i_h, qtd_horas, grade)

    fit += fit_distancia_percorrida()

    return fit,


fitness_meta = partial(fitness, metadata=metadata)
