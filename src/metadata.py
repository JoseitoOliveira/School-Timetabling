from dataclasses import asdict
from tkinter import N
from typing import Tuple

from src.AG.utilidades_AG import cruzamento_uniforme, mutUniformInt
from src.horarios import *
from src.modelos import *

P8_SE = "p8_se"
P8_CA = "p8_ca"
P8_EL = "p8_el"
P8_GE = "p8_ge"

professores = [
    # Professor(
    #     nome='Rafael',
    #     afinidade_disciplinas={
    #         "Dispositivos": 1,
    #         "Projeto de CI": 1,
    #     },
    #     afinidade_salas={
    #         "CTM1": 10
    #     }
    # ),
    Professor(
        nome='Lucas Hartmann',
        afinidade_salas={"CTJ201": 10, "CTJ202": 10, "CTJ203": 10},
        afinidade_disciplinas={
            "ASD": 2,
            "Arquitetura Avançada": 1,
            "Tempo Real": 2,
            "Filtros": 1,
            "Microc e Microp": 1,
            "Eventos Discretos": 1,
        }
    ),
    Professor(
        nome='Ademar',
        hrs_min=4,
        afinidade_disciplinas={
            "Informática Industrial": 1,
            "Técnicas de Programação": 1,
            "Circuitos Lógicos": 3,
            "Instrumentação Industrial": 1,
        }
    ),
    Professor(
        nome='Rogerio Gaspar',
        afinidade_disciplinas={
            "Equipamentos": 2,
            "Geração": 2,
            "Sistemas Elétricos": 2,
            "Proteção de Sistemas": 1,
        }
    ),
    Professor(
        nome="Nady Rocha",
        afinidade_salas={"CTJ201": 10, "CTJ202": 10, "CTJ203": 10},
        afinidade_disciplinas={
            "Instalações Elétricas": 2,
            "Acionamentos e Controles Elétricos": 2,
            "ACIONAMENTOS DE MÁQUINAS ELÉTRICAS PÓS": 1,
        }
    ),
    Professor(
        nome="Alexandre",
        afinidade_salas={"CTJ201": 10, "CTJ202": 10, "CTJ203": 10},
        afinidade_disciplinas={
            "Circuitos I": 2,
            "Conversão": 2,
            "Equipamentos": 1,
        }
    ),
    Professor(
        nome="Camila Gehrke",
        afinidade_salas={"CTJ201": 10, "CTJ202": 10, "CTJ203": 10},
        hrs_min=4,
        afinidade_disciplinas={
            "Circuitos Lógicos": 2,
            "Fontes": 2,
        }
    ),
    Professor(
        nome="José Maurício",
        afinidade_disciplinas={
            "Circuitos Lógicos": 2,
            "PDS": 1,
            "Microc e Microp": 2,
            "Arquitetura Avançada": 2,
        }
    ),
    Professor(
        nome="Cícero",
        afinidade_disciplinas={
            "Instrumentação Eletrônica": 2,
            "Materiais Elétricos": 2
        }
    ),
    Professor(
        nome="Darlan",
        afinidade_disciplinas={
            "Teoria do Controle": 2,
            "Controle I": 2,
            "Métodos Numéricos": 2,
        }
    ),
    Professor(
        nome="Fabiano",
        hrs_min=4,
        afinidade_salas={"CTJ201": 10, "CTJ202": 10, "CTJ203": 10},
        afinidade_disciplinas={
            "Máquinas Elétricas": 2,
            "Conversão": 1,
            "FONTES RENOVÁVEIS E QUALIDADE DE ENERGIA PÓS": 1,
        },
        afinidade_horarios={
            "2M5": -10,
            "2T1": -10,
            "3M5": -10,
            "3T1": -10,
            "4M5": -10,
            "4T1": -10,
            "5M5": -10,
            "5T1": -10,
            "6M5": -10,
            "6T1": -10,
            "7M5": -10,
            "7T1": -10
        }
    ),
    Professor(
        nome="Alexsandro",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Controle I": 2,
            "Audio e Vídeo": 2,
            "Filtros": 2,
            "Eletrônica": 2,
        }
    ),
    Professor(
        nome="Fabrício",
        hrs_min=8,
        hrs_max=12,
        afinidade_salas={"CTJ201": 10, "CTJ202": 10, "CTJ203": 10},
        afinidade_disciplinas={
            "Princípios de Comunicações": 2,
            "Comunicação Digital": 2,
            "Pesquisa": 2
        }
    ),
    Professor(
        nome="Romero",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Eletrônica de Potência": 2,
            "Conversores Estaticos e Eletromecânicos": 2,
        }
    ),
    Professor(
        nome="Yuri",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Técnicas de Medição": 2,
            "Gestão": 2,
            "Cálcudo de Fluxo de Potência": 2,
            "Otimização Aplicada": 2,
        }
    ),
    Professor(
        nome="Helon",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Análise de Sistemas Elétricos": 2,
            "Distribuição": 2
        }
    ),
    Professor(
        nome="Felipe Vigolvino",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Proteção de Sistemas": 2,
            "Gestão": 2
        }
    ),
    Professor(
        nome="Antônio Augusto",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Concepção de CI": 2,
            "Circuitos para Comunicações": 2,
            "Dispositivos": 1,
            "Projeto de CI": 1,
        }
    ),
    Professor(
        nome="Euler",
        hrs_min=4,
        afinidade_salas={"CTJ201": 10, "CTJ202": 10, "CTJ203": 10},
        afinidade_disciplinas={
            "Filtros": 2,
            "Eletrônica": 2
        }
    ),
    Professor(
        nome="Juan",
        hrs_min=8,
        afinidade_disciplinas={
            "Eventos Discretos": 2,
            "Controle I": 2,
            "Automação Inteligente": 2,
            "Controle de Processos": 2,
            "Audio e Vídeo": 2,
            "Técincas Aplicadas de IA": 2,
        }
    ),
    Professor(
        nome="Carlos",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Instrumentação Industrial": 2,
            "Sistemas de Automação Industrial": 2,
            "Sistemas de Aquisição": 2,
        }
    ),
    Professor(
        nome="Isaac",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Acionamentos e Circuitos Elétricos": 2,
            "Circuitos II": 2
        }
    ),
    Professor(
        nome="Waslon",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Análise de Sinais e Sistemas": 2,
            "PDS": 1,
            "Circuitos para Comunicações": 1,
            "Técnicas de Programação": 2,
        }
    ),
    Professor(
        nome="Protásio",
        hrs_min=8,
        hrs_max=12,
        afinidade_disciplinas={
            "Microc e Microp": 2,
            "Técnicas de Programação": 2
        }
    )
]

salas = [
    Sala(
        nome="CTJ201",
        capacidade=40,
    ),
    Sala(
        nome="CTJ202",
        capacidade=40,
    ),
    Sala(
        nome="CTJ203",
        capacidade=40,
    ),
    Sala(
        nome="CTM1",
        capacidade=30,
    ),
    Sala(
        nome="CTM2",
        capacidade=30
    ),
    Sala(
        nome="CTM3",
        capacidade=30
    ),
    Sala(
        nome="CTM4",
        capacidade=30,
    ),
    Sala(
        nome="LMI",
        capacidade=30,
        laboratorio=True
    ),
    Sala(
        nome="LMA",
        capacidade=30,
        laboratorio=True
    )
]

disciplinas = [
    Disciplina(
        nome="Física I",
        grades=["p1"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Vetorial I",
        grades=["p1"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Cálculo I",
        grades=["p1"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Português",
        grades=["p1"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Inglês",
        grades=["p1"],
        num_alunos=20,
        horas=[2, 2, 1],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Metodologia",
        grades=["p1"],
        num_alunos=20,
        horas=[3],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Técincas Aplicadas de IA",
        grades=["pós"],
        num_alunos=20,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Desenho",
        grades=["p1"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Física II",
        grades=["p2"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Cálculo II",
        grades=["p2"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Linear",
        grades=["p2"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Cálcudo de Fluxo de Potência",
        grades=["pós"],
        num_alunos=20,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Otimização Aplicada",
        grades=["pós"],
        num_alunos=20,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Química",
        grades=["p2"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="IC",
        grades=["p2"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Administração",
        grades=["p2"],
        num_alunos=20,
        horas=[3],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Circuitos Lógicos",
        grades=["p2"],
        num_alunos=20,
        horas=[2, 3],
    ),
    Disciplina(
        nome="Física III",
        grades=["p3"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Experimental I",
        grades=["p3"],
        num_alunos=20,
        horas=[2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Equações",
        grades=["p3"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Cálculo III",
        grades=["p3"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Probabilidades",
        grades=["p3"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="ICM",
        grades=["p3"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="ASD",
        grades=["p3"],
        num_alunos=20,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Experimental II",
        grades=["p4"],
        num_alunos=20,
        horas=[2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Complexas",
        grades=["p4"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Numérico",
        grades=["p4"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Estocásticos",
        grades=["p4"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Sociologia",
        grades=["p4"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Sólidos I",
        grades=["p4"],
        num_alunos=20,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Circuitos I",
        grades=["p4"],
        num_alunos=22,
        horas=[2, 3],
    ),
    Disciplina(
        nome="Dispositivos",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Eletromagnetismo",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Circuitos II",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Técnicas de Programação",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
        salas=[sala for sala in salas if sala.nome in ["LMI", "LMA"]]
    ),
    Disciplina(
        nome="FONTES RENOVÁVEIS E QUALIDADE DE ENERGIA PÓS",
        grades=["pós"],
        num_alunos=22,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Análise de Sinais e Sistemas",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Sólidos II",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 3],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Economia I",
        grades=["p5"],
        num_alunos=22,
        horas=[2, 3],
        professores=[sem_professor],
        salas=[sem_sala],
    ),
    Disciplina(
        nome="Mecânica dos Flúidos",
        grades=["p6"],
        num_alunos=22,
        horas=[3, 3],
        professores=[sem_professor]
    ),
    Disciplina(
        nome="Ciências do Ambiente",
        grades=["p6"],
        num_alunos=22,
        horas=[3],
        professores=[sem_professor],
    ),
    Disciplina(
        nome="Teoria do Controle",
        grades=["p6"],
        num_alunos=22,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Eletrônica",
        grades=["p6"],
        num_alunos=22,
        horas=[3, 2],
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    Disciplina(
        nome="Materiais Elétricos",
        grades=["p6"],
        num_alunos=22,
        horas=[2, 2],
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    Disciplina(
        nome="Conversão",
        grades=["p6"],
        num_alunos=22,
        horas=[2, 3],
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    Disciplina(
        nome="Pesquisa",
        grades=["p6"],
        num_alunos=22,
        horas=[3],
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    Disciplina(
        nome="Instrumentação Eletrônica",
        grades=["p7"],
        num_alunos=10,
        horas=[2, 2],
        salas=[sala for sala in salas if sala.nome in ["LMI", "LMA"]]
    ),
    Disciplina(
        nome="Máquinas Elétricas",
        grades=["p7"],
        num_alunos=20,
        horas=[2, 3],
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    Disciplina(
        nome="Controle I",
        grades=["p7"],
        num_alunos=15,
        horas=[2, 3],
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    Disciplina(
        nome="Princípios de Comunicações",
        grades=["p7"],
        num_alunos=12,
        horas=[2, 3],
        laboratorios=[sala for sala in salas if sala.nome in ["LMA"]]
    ),
    Disciplina(
        nome="Sistemas Elétricos",
        grades=["p7"],
        num_alunos=20,
        horas=[2, 3],
        aulas_aos_sabados=False,
    ),
    Disciplina(
        nome="Eletrônica de Potência",
        grades=["p7"],
        num_alunos=25,
        horas=[2, 3],
        aulas_aos_sabados=False
    ),
    Disciplina(
        nome="Instalações Elétricas",
        grades=[P8_GE, P8_SE],
        horas=[2, 2],
        num_alunos=20,
    ),
    Disciplina(
        nome="Técnicas de Medição",
        grades=[P8_GE, P8_SE],
        num_alunos=22,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Análise de Sistemas Elétricos",
        grades=[P8_SE],
        num_alunos=15,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    Disciplina(
        nome="Filtros",
        grades=[P8_EL, P8_CA],
        num_alunos=15,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    Disciplina(
        nome="Métodos Numéricos",
        grades=["pós"],
        num_alunos=22,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Instrumentação Industrial",
        grades=[P8_EL, P8_CA],
        num_alunos=15,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    Disciplina(
        nome="Acionamentos e Circuitos Elétricos",
        grades=[P8_GE, P8_CA],
        num_alunos=15,
        horas=[2, 2],
        aulas_aos_sabados=False
    ),
    Disciplina(
        nome="Microc e Microp",
        grades=[P8_EL],
        num_alunos=15,
        horas=[2, 2],
        salas=[sala for sala in salas if sala.nome in ["LMI", "LMA"]]
    ),
    Disciplina(
        nome="Automação Inteligente",
        grades=[P8_SE],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Conversores Estaticos e Eletromecânicos",
        grades=[P8_SE, P8_CA],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Informática Industrial",
        grades=[P8_CA],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Sistemas de Aquisição",
        grades=[P8_EL, P8_CA],
        num_alunos=15,
        horas=[2, 2]
    ),
    Disciplina(
        nome="Sistemas de Automação Industrial",
        grades=[P8_CA],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Eventos Discretos",
        grades=[P8_CA],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Tempo Real",
        grades=[P8_CA],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="PDS",
        grades=[P8_EL],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Audio e Vídeo",
        grades=[P8_EL],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Concepção de CI",
        grades=[P8_EL],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Comunicação Digital",
        grades=[P8_EL],
        num_alunos=15,
        horas=[2, 2],
    ),
    # Disciplina(
    #     nome="Projeto de CI",
    #     grades=[P8_EL],
    #     num_alunos=15,
    #     horas=[2, 2],
    # ),
    Disciplina(
        nome="Arquitetura Avançada",
        grades=[P8_EL],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Circuitos para Comunicações",
        grades=[P8_SE],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Proteção de Sistemas",
        grades=[P8_SE],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Distribuição",
        grades=[P8_SE],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Equipamentos",
        grades=[P8_SE],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Gestão",
        grades=[P8_SE],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Geração",
        grades=[P8_SE],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="Fontes",
        grades=[P8_SE],
        num_alunos=15,
        horas=[2, 2],
    ),
    # Disciplina(
    #     nome="Controle de Processos",
    #     grades=[P8_CA],
    #     num_alunos=15,
    #     horas=[2, 2],
    # ),
    Disciplina(
        nome="Acionamentos e Controles Elétricos",
        grades=[P8_GE, P8_CA],
        num_alunos=15,
        horas=[2, 2],
    ),
    Disciplina(
        nome="ACIONAMENTOS DE MÁQUINAS ELÉTRICAS PÓS",
        grades=["pós"],
        num_alunos=15,
        horas=[2, 2],
    ),
]


distancias = {
    "CTJ201": {"CTM1": 100, "CTM2": 100, "CTM3": 100, "CTM4": 100, "LMI": 100, "LMA": 100, "CTJ201": 00, "CTJ202": 10, "CTJ203": 20},
    "CTJ202": {"CTM1": 100, "CTM2": 100, "CTM3": 100, "CTM4": 100, "LMI": 100, "LMA": 100, "CTJ201": 10, "CTJ202": 00, "CTJ203": 10},
    "CTJ203": {"CTM1": 100, "CTM2": 100, "CTM3": 100, "CTM4": 100, "LMI": 100, "LMA": 100, "CTJ201": 20, "CTJ202": 10, "CTJ203": 00},
    "CTM1": {"CTM1": 00, "CTM2": 10, "CTM3": 20, "CTM4": 30, "LMI": 40, "LMA": 50, "CTJ201": 100, "CTJ202": 100, "CTJ203": 100},
    "CTM2": {"CTM1": 10, "CTM2": 00, "CTM3": 10, "CTM4": 20, "LMI": 40, "LMA": 50, "CTJ201": 100, "CTJ202": 100, "CTJ203": 100},
    "CTM3": {"CTM1": 20, "CTM2": 10, "CTM3": 00, "CTM4": 10, "LMI": 40, "LMA": 50, "CTJ201": 100, "CTJ202": 100, "CTJ203": 100},
    "CTM4": {"CTM1": 30, "CTM2": 20, "CTM3": 10, "CTM4": 00, "LMI": 40, "LMA": 50, "CTJ201": 100, "CTJ202": 100, "CTJ203": 100},
    "LMI": {"CTM1": 30, "CTM2": 20, "CTM3": 10, "CTM4": 00, "LMI": 00, "LMA": 50, "CTJ201": 100, "CTJ202": 100, "CTJ203": 100},
    "LMA": {"CTM1": 40, "CTM2": 30, "CTM3": 20, "CTM4": 10, "LMI": 00, "LMA": 00, "CTJ201": 100, "CTJ202": 100, "CTJ203": 100},
}


metadata = MetaData(
    professores=professores,
    salas=salas,
    disciplinas={disciplina.nome: disciplina for disciplina in disciplinas},
    horarios=horarios_str,
    distancias=distancias,
    choques={}
)


def completar_professores(disciplina: Disciplina):
    if not disciplina.professores:
        professores: list[Professor] = metadata.professores
        disciplina.professores = [
            profe
            for profe in professores
            if disciplina.nome in profe.afinidade_disciplinas.keys()
        ]

    if disciplina.professores == []:
        raise Exception(
            f'Não há professores para a disciplina {disciplina.nome}.'
        )
    return disciplina


def completar_salas(disciplina: Disciplina):
    salas: list[Sala] = metadata.salas
    if disciplina.salas == []:
        disciplina.salas = [
            sala for sala in salas
            if sala.capacidade >= disciplina.num_alunos
            if not sala.laboratorio
        ]

    if disciplina.salas == []:
        raise Exception(
            f'Não há sala que comporte a disciplina {disciplina.nome} '
            f'que possui {disciplina.num_alunos} alunos matriculados.'
        )
    return disciplina


def completar_cromossomos(disciplina: Disciplina, ultimo_gene):
    num_genes_p = 1
    num_genes_s = len(disciplina.horas)
    num_genes_l = len(disciplina.horas) if disciplina.laboratorios else 0

    cromossomos = []
    cromossomos.append(Cromossomo(   # Professores
        numero_genes=num_genes_p,
        limite_inferior=0,
        limite_superior=len(disciplina.professores),
        slice_i=ultimo_gene,
        slice_f=ultimo_gene+num_genes_p
    ))
    ultimo_gene += num_genes_p
    cromossomos.append(Cromossomo(   # Salas
        numero_genes=num_genes_s,
        limite_inferior=0,
        limite_superior=len(disciplina.salas),
        slice_i=ultimo_gene,
        slice_f=ultimo_gene+num_genes_s
    ))
    ultimo_gene += num_genes_s

    cromossomos.append(Cromossomo(   # Laboratórios
        numero_genes=num_genes_l,
        limite_inferior=0,
        limite_superior=len(disciplina.laboratorios),
        slice_i=ultimo_gene,
        slice_f=ultimo_gene+num_genes_l
    ))
    ultimo_gene += num_genes_l

    num_genes_h = 1
    for horarios in disciplina.horarios:
        cromossomos.append(Cromossomo(   # Horiários
            numero_genes=num_genes_h,
            limite_inferior=0,
            limite_superior=len(horarios),
            slice_i=ultimo_gene,
            slice_f=ultimo_gene+num_genes_h
        ))
        ultimo_gene += num_genes_h

    disciplina.cromossomos = cromossomos
    return disciplina, ultimo_gene


def get_horarios(disciplina: Disciplina, ind):
    qtd_horas = disciplina.horas
    cromos_h = disciplina.cromossomos[3:]
    i_h = []
    for i, horarios in enumerate(disciplina.horarios):
        cromo_h = cromos_h[i]
        index_h = ind[cromo_h.slice_i: cromo_h.slice_f][0]
        horario = horarios[index_h]
        i_h.append(metadata.horarios.index(horario))

    horarios = [
        [h for h in range(ini_h, ini_h+qtd_horas[i], 1)]
        for i, ini_h in enumerate(i_h)
    ]
    return horarios, i_h


def extrair_dados(disciplina: Disciplina, ind: list[int]) -> Tuple[
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
    professor = disciplina.professores[i_p[0]]
    horarios, i_h = get_horarios(disciplina, ind)

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


def completar_metadata(metadata: MetaData):
    ultimo_gene = 0
    for nome, disciplina in metadata.disciplinas.items():
        disciplina = completar_professores(disciplina)
        disciplina = completar_salas(disciplina)
        disciplina, ultimo_gene = completar_cromossomos(disciplina,
                                                        ultimo_gene)

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


metadata = completar_metadata(metadata)

with open('out/metadata_c.py', mode='w', encoding='utf8') as f:
    from pprint import pprint
    pprint(asdict(metadata), stream=f)
