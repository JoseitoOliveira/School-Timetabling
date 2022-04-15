from typing import Tuple

from tqdm import tqdm


from src.AG.utilidades_AG import cruzamento_uniforme, mutUniformInt
from src.modelos import Cromossomo, Disciplina, MetaData, Professor, Sala


def completar_professores(metadata, disciplina: Disciplina):
    if disciplina.professores == [] and not disciplina.sem_professor:
        professores: list[Professor] = metadata.professores
        disciplina.professores = [
            profe
            for profe in professores
            if disciplina.nome in profe.afinidade_disciplinas.keys()
        ]

    if disciplina.professores == [] and not disciplina.sem_professor:
        raise Exception(
            f'Não há professores para a disciplina {disciplina.nome}.'
        )
    return disciplina


def completar_salas(metadata, disciplina: Disciplina):
    salas: list[Sala] = metadata.salas
    if disciplina.salas == [] and not disciplina.sem_sala:
        disciplina.salas = [
            sala for sala in salas
            if sala.capacidade >= disciplina.num_alunos
            if not sala.laboratorio
        ]

    if disciplina.salas == [] and not disciplina.sem_sala:
        raise Exception(
            f'Não há sala que comporte a disciplina {disciplina.nome} '
            f'que possui {disciplina.num_alunos} alunos matriculados.'
        )
    return disciplina


def completar_cromossomos(disciplina: Disciplina, ultimo_gene):
    num_genes_p = 1 if not disciplina.sem_professor else 0
    num_genes_s = len(disciplina.horas) if not disciplina.sem_sala else 0
    num_genes_l = len(disciplina.horas) if disciplina.laboratorios else 0

    cromossomos = []
    cromossomos.append(Cromossomo(   # Professores
        numero_genes=num_genes_p,
        limite_inferior=0,
        limite_superior=len(disciplina.professores),
        slice_i=ultimo_gene,
        slice_f=ultimo_gene + num_genes_p
    ))
    ultimo_gene += num_genes_p
    cromossomos.append(Cromossomo(   # Salas
        numero_genes=num_genes_s,
        limite_inferior=0,
        limite_superior=len(disciplina.salas),
        slice_i=ultimo_gene,
        slice_f=ultimo_gene + num_genes_s
    ))
    ultimo_gene += num_genes_s

    cromossomos.append(Cromossomo(   # Laboratórios
        numero_genes=num_genes_l,
        limite_inferior=0,
        limite_superior=len(disciplina.laboratorios),
        slice_i=ultimo_gene,
        slice_f=ultimo_gene + num_genes_l
    ))
    ultimo_gene += num_genes_l

    num_genes_h = 1
    for horarios in disciplina.horarios:
        cromossomos.append(Cromossomo(   # Horiários
            numero_genes=num_genes_h,
            limite_inferior=0,
            limite_superior=len(horarios),
            slice_i=ultimo_gene,
            slice_f=ultimo_gene + num_genes_h
        ))
        ultimo_gene += num_genes_h

    disciplina.cromossomos = cromossomos
    return disciplina, ultimo_gene


def get_horarios(metadata, disciplina: Disciplina, ind):
    qtd_horas = disciplina.horas
    cromos_h = disciplina.cromossomos[3:]
    i_h = []
    for i, horarios in enumerate(disciplina.horarios):
        cromo_h = cromos_h[i]
        index_h = ind[cromo_h.slice_i: cromo_h.slice_f][0]
        horario = horarios[index_h]
        i_h.append(metadata.horarios.index(horario))

    horarios = [
        [h for h in range(ini_h, ini_h + qtd_horas[i], 1)]
        for i, ini_h in enumerate(i_h)
    ]
    return horarios, i_h


def extrair_dados(metadata, disciplina: Disciplina, ind: list[int]) -> Tuple[
    list[int], list[int], list[int], list[int], list[Sala],
    list[Sala], list[int], list[list[int]], list[str], Professor
]:

    cromo_p = disciplina.cromossomos[0]
    cromo_s = disciplina.cromossomos[1]
    cromo_l = disciplina.cromossomos[2]
    i_p: list = ind[cromo_p.slice_i: cromo_p.slice_f]
    i_s: list = ind[cromo_s.slice_i: cromo_s.slice_f]
    i_l: list = ind[cromo_l.slice_i: cromo_l.slice_f]

    salas = [disciplina.salas[i] for i in i_s]
    laboratorios = [disciplina.laboratorios[i] for i in i_l]

    qtd_horas = disciplina.horas
    grades: list = disciplina.grades
    if not disciplina.sem_professor:
        professor = disciplina.professores[i_p[0]]
    else:
        professor = None

    horarios, i_h = get_horarios(metadata=metadata,
                                 disciplina=disciplina,
                                 ind=ind)

    return (
        i_p,
        i_s,
        i_l,
        i_h,
        salas,
        laboratorios,
        qtd_horas,
        horarios,
        grades,
        professor
    )


def completar_distancias(metadata: MetaData):
    nomes_salas = [s.nome for s in metadata.salas]

    for sala, distancias in metadata.distancias.items():
        for outra_sala in nomes_salas:
            if sala == outra_sala:
                distancias[outra_sala] = 0
            elif outra_sala not in distancias:
                distancias[outra_sala] = 1000

    return metadata


def processar_metadata(metadata: MetaData):
    ultimo_gene = 0
    for nome, disc in tqdm(metadata.disciplinas.items()):
        disc.atualizar_laboratorios()
        disc.atualizar_salas()
        disc.atualizar_professores()
        disc = completar_professores(metadata, disc)
        disc = completar_salas(metadata, disc)
        disc, ultimo_gene = completar_cromossomos(disc, ultimo_gene)

    metadata = completar_distancias(metadata)

    return metadata


def dummy_mut(ind, *args, **kargs):
    return ind,


def dummy_cruz(ind1, ind2, *args, **kargs):
    return ind2, ind1


def criar_cromossomos(metadata: MetaData):
    cromossomos = []
    for disciplina in metadata.disciplinas.values():
        disciplina: Disciplina
        for cromo in disciplina.cromossomos:
            numero_genes = cromo.numero_genes
            limite_inferior = cromo.limite_inferior
            limite_superior = cromo.limite_superior
            diff_limite = limite_superior - limite_inferior
            if diff_limite > 1:
                fcn_cruzamento = cruzamento_uniforme
            else:
                fcn_cruzamento = dummy_cruz

            cromossomos.append({
                'numero_genes': numero_genes,
                'tipo': int,
                'limite_inferior': limite_inferior,
                'limite_superior': limite_superior,
                'mutacao': {
                    'fcn': mutUniformInt if diff_limite > 1 else dummy_mut,
                    'args': {
                        'indpb': 0.15,
                        'low': 0,
                        'up': limite_superior - 1
                    },
                },
                'cruzamento': {
                    'fcn': fcn_cruzamento,
                    'args': {}
                }
            })
    return cromossomos
