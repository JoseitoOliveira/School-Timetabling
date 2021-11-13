
from make_output import make_html

#     2|  3|  4|  5|  6|  7
# M1  0| 10| 20| 30| 40| 50
# M2  1| 11| 21| 31| 41| 51
# M3  2| 12| 22| 32| 42| 52
# M4  3| 13| 23| 33| 43| 53
# M5  4| 14| 24| 34| 44| 54
# T1  5| 15| 25| 35| 45| 55
# T2  6| 16| 26| 36| 46| 56
# T3  7| 17| 27| 37| 47| 57
# T4  8| 18| 28| 38| 48| 58
# T5  9| 19| 29| 39| 49| 59

ind = [
    # Dispositivos
    # p:['Rafael']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  2,  3,  3, 28,

    # Eletromagnetismo
    # p:['Prof Eletromag']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  3,  1, 26, 46,

    # Circuitos 2
    # p:['Isaac']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  2,  3, 13, 33,

    # Técnicas de Programação
    # p:['Protásio']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  3,  0, 48,  6,

    # Análise de Sinais e Sistemas
    # p:['Waslon']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  0,  2, 36,  8,

    # Mec. dos Sólidos II
    # p:['Prof Mec. Sólidos']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  0,  1, 38, 15,

    # Economia I
    # p:['Prof Economia I']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  3,  3,  1, 20,

    # Mecânica dos Flúidos
    # p:['Rômulo']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  2,  2, 45, 15,

    # Teoria do Controle
    # p:['Darlan']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  2,  3, 26, 43,

    # Eletrônica
    # p:['Euler']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  1,  1, 10, 31,

    # Materiais Elétricos
    # p:['Cícero']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  2,  2, 41,  6,

    # Conversão
    # p:['Fabiano']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  3,  2,  3, 28,

    # Pesquisa
    # p:['Jéssica']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  1,  3, 48, 18,

    # Instrumentação Eletrônica
    # p:['Cícero']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  1,  0, 21,  8,

    # Máquinas Elétricas
    # p:['Fabiano']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  1,  0, 36,  0,

    # Controle I
    # p:['Alexsandro']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  0,  2, 13, 30,

    # Princípios de Comunicações
    # p:['Fabrício']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  1,  3, 43, 15,

    # Sistemas Elétricos
    # p:['Clivaldo']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  2,  0, 33, 10,

    # Eletrônica de Potência
    # p:['Romero']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  1,  1, 23,  5,

    # Técnicas de Medição
    # p:['Yuri']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  3,  3, 36, 11,

    # Análise de Sistemas Elétricos
    # p:['Helon']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  0,  0,  3, 33,

    # Filtros
    # p:['Euler']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  0,  0, 48, 18,

    # Instrumentação Industrial
    # p:['Carlos']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  0,  0, 16, 31,

    # Acionamentos e Circuitos Elétricos
    # p:['Isaac']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  1,  3,  1, 41,

    # Microc e Microp
    # p:['Protásio']
    # s:['CTM1', 'CTM2', 'CTM3', 'CTM4']
  # p,  s,  s,  h,  h, 
    0,  3,  3,  8, 38,

]

html = make_html(ind)
with open('output.html', mode='w', encoding='utf8') as f:
    f.write(html)
