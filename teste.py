from make_output import make_html, individuo_formatado

ind = """0  2  3  1 11  0  3  1 10 18  0  2  3  5 13  0  3  0 19  2  0  0  2 14
  3  0  0  1 15  3  0  3  3  0  4  0  2  2  9  3  0  2  3 10 17  0  1  1
  2 12  0  2  2 16  2  0  3  2  1 11  0  1  3 19  7  0  1  0  8  3  0  1
  0 14  0  0  0  2  5  6  0  1  3 17  3  0  2  0 13  2  0  1  1  9  1  0
  3  3 14  4  0  0  0  1 13  0  0  0 19  7  0  0  0  6 12  0  1  3  0 16
  0  3  3  3 15""".split()

ind = [int(i) for i in ind]
ind_f = individuo_formatado(ind)
with open('individuo.py', mode='w', encoding='utf8') as f:
    f.write(ind_f)

html = make_html(ind)
with open('output.html', mode='w', encoding='utf8') as f:
    f.write(html)
