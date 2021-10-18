metadata = {
    "professores": [
        {
            "nome": "Prof A",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {  # nome: afinidade
                "Física": 1,
                "Cálculo 1": 2
            }
        },
        {
            "nome": "Prof B",
            "hrs_min": 8,
            "hrs_max": 12,
            "disciplinas": {
                "Química": 1,
                "Cálculo 2": 1
            }
        },
        {
            "nome": "Prof C",
            "hrs_min": 8,
            "hrs_max": 8,
            "disciplinas": {
                "Introdução a Computação": 2
            }
        }],
    "salas": [
        {
            "nome": "CTM1",
            "capacidade": 30
        },
        {
            "nome": "CTM2",
            "capacidade": 45
        }],
    "grades": [
        "p1",
        "p2"],
    "disciplinas:": [
        {
            "nome": "Física",
            "grade": "p1",
            "num_alunos": 10,
            "horas": [
                2,
                3
            ]
        },
        {
            "nome": "Cálculo 1",
            "grade": "p1",
            "num_alunos": 20,
            "horas": [
                2,
                3
            ]
        },
        {
            "nome": "Química",
            "grade": "p2",
            "num_alunos": 15,
            "horas": [
                2,
                3
            ]
        },
        {
            "nome": "Cálculo 2",
            "grade": "p2",
            "num_alunos": 12,
            "horas": [
                2,
                3
            ]
        },
        {
            "nome": "Introdução a Computação",
            "grade": "p2",
            "num_alunos": 35,
            "horas": [
                2,
                3
            ]
        }],
    "horarios": [
        "2M1",
        "2M2",
        "2M3",
        "2M4",
        "2M5",
        "2T1",
        "2T2",
        "2T3",
        "2T4",
        "2T5",
        "3M1",
        "3M2",
        "3M3",
        "3M4",
        "3M5",
        "3T1",
        "3T2",
        "3T3",
        "3T4",
        "3T5",
        "4M1",
        "4M2",
        "4M3",
        "4M4",
        "4M5",
        "4T1",
        "4T2",
        "4T3",
        "4T4",
        "4T5",
        "5M1",
        "5M2",
        "5M3",
        "5M4",
        "5M5",
        "5T1",
        "5T2",
        "5T3",
        "5T4",
        "5T5",
        "6M1",
        "6M2",
        "6M3",
        "6M4",
        "6M5",
        "6T1",
        "6T2",
        "6T3",
        "6T4",
        "6T5",
        "7M1",
        "7M2",
        "7M3",
        "7M4",
        "7M5",
        "7T1",
        "7T2",
        "7T3",
        "7T4",
        "7T5"]
}


num_horarios = sum([len(diciplina["horas"])
                   for diciplina in metadata["disciplinas"]])

num_professores = len(metadata["disciplinas"])
num_salas = num_horarios
