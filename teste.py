from make_output import make_html, individuo_formatado

ind = """0  2  3  9  1  0  1  2  5  7  0  2  1 11  1  0  1  3  6 19  0  3  3  3
 18  3  8  0  3  0 15  7  0  2  4  0  1  0 10  0  0  0  0 14  1  0  3  0
  4 17  0  0  0  3 19  0  0  3 16  5  0  0  3 15  3  0  1  1  7  9  0  1
  3  1  5  0  2  3 17 11  0  0  0  8  0  0  2  0  7 12  0  1  2 15  6  0
  1  0  3 13  0  1  0  2 17  0  2  1  3  4  0  2  1 13  2  0  0  1 11  0
  0  2  2  1  6  0  1  3  9  8  0  2  2 18  5  0  3  3  1 13  0  3  2  9
 19  0  2  2  0  8  0  3  0 14  6  0  1  1 12  4""".split()

ind = [int(i) for i in ind]
ind_f = individuo_formatado(ind)
with open('individuo.py', mode='w', encoding='utf8') as f:
    f.write(ind_f)

html = make_html(ind)
with open('output.html', mode='w', encoding='utf8') as f:
    f.write(html)
