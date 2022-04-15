from setuptools import setup

NAME = "UFPB School Timetabling"
VERSION = "0.3.0"
DESCRIPTION = """Software para planejamento ótimo de períodos, \
horários das turmas, professores e salas no DEE/UFPB"""
AUTHOR = "Joseíto Oliveira"
AUTHOR_EMAIL = "joseito.junior@cear.ufpb.br"

setup(
    name=NAME,
    version=VERSION,
    package_data={
        '': ['*.txt', '*.rst'],
    },

    # metadata for upload
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    install_requires=[
        'PyQt5==5.15.6',
        'PyQt5-Qt5==5.15.2',
        'PyQt5-sip==12.9.1',
        'qt-material==2.8.19',
        'tqdm==4.62.3',
        'numpy==1.22.2',
        'deap==1.3.1',
        'more-itertools==8.12.0',
        'fire==0.4.0',
    ]
)
