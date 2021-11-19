from make_output import make_html, individuo_formatado

ind = """0  0  3  7  7  0  2  1 16  4  0  3  0  9 19  0  2  1 18  4  0  1  0  2
  3 17  6  0  1  2  2 11  0  0 13  0  3  2  8 17  0  2  0  3 15  0  3  3
 11 18  0  0  1  9  1  0  1  3 13  0  0  0  0  5  1  0  1  1 16  3  0  3
  3  5  1  0  2  1  9  1  0  2  3  0  0  6  6  0  1  1  0  0 14  5  0  3
  0  0  0  3 11  0  2  1  0  0  8  0  0  0  0  1 12  0  2  2  0  0 15  2
  0  1  2  0  0 17  5  0  3  0  0  0 13  3  0  3  0  7  9  0  2  2 19  1
  0  2  0 14  3  0  0  1  1 18  0  0  3  9 17  0  1  3  7 15  0  2  0 13
  0  0  0  0 16 11""".split()

ind = [int(i) for i in ind]
ind_f = individuo_formatado(ind)
with open('individuo.py', mode='w', encoding='utf8') as f:
    f.write(ind_f)

html = make_html(ind)
with open('output.html', mode='w', encoding='utf8') as f:
    f.write(html)
