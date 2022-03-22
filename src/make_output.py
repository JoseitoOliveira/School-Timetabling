from src.metadata import metadata, extrair_dados
from src.fitness import Fitness

TEMPLATE_HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grades</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css"
        integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js"
        integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/"
        crossorigin="anonymous"></script>
</head>

<body>
    <div class="container-fluid flex-row mx-auto">
    <strong>{fitness:.2f}</strong><br>
    {stats} <br>
    <hr style="width:50%;text-align:left;margin-left:0">
    {professores}
    <hr style="width:50%;text-align:left;margin-left:0">
    {tables}
    </div>
</body>

</html>
"""

TEMPLATE_TABLE = """
<center><h3>{grade}</h3></center>
<table class="table table-bordered">
    <thead>
        <th>Hora</th><th>Segunda</th><th>Terça</th><th>Quarta</th><th>Quinta</th><th>Sexta</th><th>Sábado</th>
    </thead>
    <tbody>
        <tr><td>M1</td><td>{_0}</td><td>{_10}</td><td>{_20}</td><td>{_30}</td><td>{_40}</td><td>{_50}</tr>
        <tr><td>M2</td><td>{_1}</td><td>{_11}</td><td>{_21}</td><td>{_31}</td><td>{_41}</td><td>{_51}</tr>
        <tr><td>M3</td><td>{_2}</td><td>{_12}</td><td>{_22}</td><td>{_32}</td><td>{_42}</td><td>{_52}</tr>
        <tr><td>M4</td><td>{_3}</td><td>{_13}</td><td>{_23}</td><td>{_33}</td><td>{_43}</td><td>{_53}</tr>
        <tr><td>M5</td><td>{_4}</td><td>{_14}</td><td>{_24}</td><td>{_34}</td><td>{_44}</td><td>{_54}</tr>
        <tr><td>T1</td><td>{_5}</td><td>{_15}</td><td>{_25}</td><td>{_35}</td><td>{_45}</td><td>{_55}</tr>
        <tr><td>T2</td><td>{_6}</td><td>{_16}</td><td>{_26}</td><td>{_36}</td><td>{_46}</td><td>{_56}</tr>
        <tr><td>T3</td><td>{_7}</td><td>{_17}</td><td>{_27}</td><td>{_37}</td><td>{_47}</td><td>{_57}</tr>
        <tr><td>T4</td><td>{_8}</td><td>{_18}</td><td>{_28}</td><td>{_38}</td><td>{_48}</td><td>{_58}</tr>
        <tr><td>T5</td><td>{_9}</td><td>{_19}</td><td>{_29}</td><td>{_39}</td><td>{_49}</td><td>{_59}</tr>
    </tbody>
</table>
"""
TEMPLATE_PROFESSOR = """
Professor: {nome}<br>
Horas mínimas: {hrs_min}<br>
Horas máximas: {hrs_max}<br>
Horas totais: <span style="color:{color}">{hrs_tot}</span><br>
Disciplinas: {disciplinas}<br>
"""

empty_table_args = {f'_{i}': '' for i in range(60)}


def make_html(ind):

    grades = metadata.grades
    tables_args = [empty_table_args.copy() for _ in grades]
    [tables_args[i].__setitem__('grade', grade)
     for i, grade in enumerate(grades)]

    sum_fit, fit = Fitness(metadata)(ind)

    professores = {}

    for disciplina in metadata.disciplinas.values():

        (i_p, i_s, i_l, i_h,
         salas, laboratorios,
         qtd_horas, horarios,
         grades, professor) = extrair_dados(disciplina, ind)

        if not professor.sem_professor:
            if professor.nome not in professores:
                professores[professor.nome] = {
                    'nome': professor.nome,
                    'hrs_min': professor.hrs_min,
                    'hrs_max': professor.hrs_max,
                    'hrs_tot': sum(disciplina.horas),
                    'disciplinas': f"{disciplina.nome} | ",
                }
            else:
                professores[professor.nome]['hrs_tot'] += sum(disciplina.horas)
                professores[professor.nome]['disciplinas'] += f"{disciplina.nome} | "

        for grade in grades:
            i_grade = metadata.grades.index(grade)
            for i, sala in enumerate(salas):
                for h in range(i_h[i], i_h[i]+qtd_horas[i]):
                    args = (
                        f"{disciplina.nome}<br>"
                        f"{professor.nome}<br>"
                        f"{sala.nome}<br>"
                        f"{laboratorios[i].nome if laboratorios else ''}"
                    )
                    tables_args[i_grade][f'_{h}'] += args

    stats = '<br>'.join(
        [f'{field} = {getattr(fit, field)}' for field in fit.__dataclass_fields__])

    tables = '<br>'.join([TEMPLATE_TABLE.format(**args)
                         for args in tables_args])

    profes_html = '<br>'.join([TEMPLATE_PROFESSOR.format(
        color='red' if not (args['hrs_min'] <= args['hrs_tot'] and
                            args['hrs_tot'] <= args['hrs_max']) else 'black',
        **args)
        for args in professores.values()]
    )

    return TEMPLATE_HTML.format(tables=tables, stats=stats, fitness=sum_fit, professores=profes_html)


TEMPLATE_INDIVIDUO = """
from src.make_output import make_html

ind = [
{cromossomos}
]

html = make_html(ind)
with open('output.html', mode='w', encoding='utf8') as f:
    f.write(html)
"""


def individuo_formatado(ind):
    str_cromossomos = []
    for disciplina in metadata.disciplinas.values():

        (i_p, i_s, i_l, i_h,
         salas, laboratorios,
         qtd_horas, horarios,
         grades, professor) = extrair_dados(disciplina, ind)

        cromo = i_p + i_s + i_h
        header = (
            "    # {disciplina}\n"
            "    # p: {professores}\n"
            "    # s: {salas}\n"
            "{horarios}\n"
            "  #{cabeçalho}\n"
        ).format(
            disciplina=disciplina.nome,
            professores=[profe.nome for profe in disciplina.professores],
            salas=[sala.nome for sala in disciplina.salas],
            horarios='\n'.join(['    # h{}:{}'.format(i, h)
                               for i, h in enumerate(disciplina.horarios)]),
            cabeçalho=' p, ' * len(i_p) + ' s, ' * len(i_s) +
            ', '.join([f'h{i}' for i in range(len(i_h))])
        )

        str_cromossomos.append(
            f"{header}"
            f"   {', '.join([f'{x:2}' for x in cromo])},\n"
        )
    return TEMPLATE_INDIVIDUO.format(cromossomos='\n'.join(str_cromossomos))
