h2M1 = 0x1 << 0
h2M2 = 0x1 << 1
h2M3 = 0x1 << 2
h2M4 = 0x1 << 3
h2M5 = 0x1 << 4
h2T1 = 0x1 << 5
h2T2 = 0x1 << 6
h2T3 = 0x1 << 7
h2T4 = 0x1 << 8
h2T5 = 0x1 << 9
h3M1 = 0x1 << 10
h3M2 = 0x1 << 11
h3M3 = 0x1 << 12
h3M4 = 0x1 << 13
h3M5 = 0x1 << 14
h3T1 = 0x1 << 15
h3T2 = 0x1 << 16
h3T3 = 0x1 << 17
h3T4 = 0x1 << 18
h3T5 = 0x1 << 19
h4M1 = 0x1 << 20
h4M2 = 0x1 << 21
h4M3 = 0x1 << 22
h4M4 = 0x1 << 23
h4M5 = 0x1 << 24
h4T1 = 0x1 << 25
h4T2 = 0x1 << 26
h4T3 = 0x1 << 27
h4T4 = 0x1 << 28
h4T5 = 0x1 << 29
h5M1 = 0x1 << 30
h5M2 = 0x1 << 31
h5M3 = 0x1 << 32
h5M4 = 0x1 << 33
h5M5 = 0x1 << 34
h5T1 = 0x1 << 35
h5T2 = 0x1 << 36
h5T3 = 0x1 << 37
h5T4 = 0x1 << 38
h5T5 = 0x1 << 39
h6M1 = 0x1 << 40
h6M2 = 0x1 << 41
h6M3 = 0x1 << 42
h6M4 = 0x1 << 43
h6M5 = 0x1 << 44
h6T1 = 0x1 << 45
h6T2 = 0x1 << 46
h6T3 = 0x1 << 47
h6T4 = 0x1 << 48
h6T5 = 0x1 << 49
h7M1 = 0x1 << 50
h7M2 = 0x1 << 51
h7M3 = 0x1 << 52
h7M4 = 0x1 << 53
h7M5 = 0x1 << 54
h7T1 = 0x1 << 55
h7T2 = 0x1 << 56
h7T3 = 0x1 << 57
h7T4 = 0x1 << 58
h7T5 = 0x1 << 59
segunda = h2M1 | h2M2 | h2M3 | h2M4 | h2M5 | h2T1 | h2T2 | h2T3 | h2T4 | h2T5
terca = h3M1 | h3M2 | h3M3 | h3M4 | h3M5 | h3T1 | h3T2 | h3T3 | h3T4 | h3T5
quarta = h4M1 | h4M2 | h4M3 | h4M4 | h4M5 | h4T1 | h4T2 | h4T3 | h4T4 | h4T5
quinta = h5M1 | h5M2 | h5M3 | h5M4 | h5M5 | h5T1 | h5T2 | h5T3 | h5T4 | h5T5
sexta = h6M1 | h6M2 | h6M3 | h6M4 | h6M5 | h6T1 | h6T2 | h6T3 | h6T4 | h6T5
sabado = h7M1 | h7M2 | h7M3 | h7M4 | h7M5 | h7T1 | h7T2 | h7T3 | h7T4 | h7T5
todos = segunda | terca | quarta | quinta | sexta | sabado
horarios_2 = h2M2 | h2M4 | h2T2 | h2T4 | h3M2 | h3M4 | h3T2 | h3T4 | h4M2 | h4M4 | h4T2 | h4T4 | h5M2 | h5M4 | h5T2 | h5T4 | h6M2 | h6M4 | h6T2 | h6T4 | h7M2 | h7M4 | h7T2 | h7T4
horarios_3 = h2M1 | h2T1 | h3M1 | h3T1 | h4M1 | h4T1 | h5M1 | h5T1 | h6M1 | h6T1 | h7M1 | h7T1


horarios_str = [
    "2M1", "2M2", "2M3", "2M4", "2M5", "2T1", "2T2", "2T3", "2T4", "2T5",
    "3M1", "3M2", "3M3", "3M4", "3M5", "3T1", "3T2", "3T3", "3T4", "3T5",
    "4M1", "4M2", "4M3", "4M4", "4M5", "4T1", "4T2", "4T3", "4T4", "4T5",
    "5M1", "5M2", "5M3", "5M4", "5M5", "5T1", "5T2", "5T3", "5T4", "5T5",
    "6M1", "6M2", "6M3", "6M4", "6M5", "6T1", "6T2", "6T3", "6T4", "6T5",
    "7M1", "7M2", "7M3", "7M4", "7M5", "7T1", "7T2", "7T3", "7T4", "7T5",
]
