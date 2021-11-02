from fitness import fitness_meta
from make_pdf import make_html

ind = [0.,  1.,  3., 24., 30.,  0.,  1.,  3., 32., 57.,  0.,  2.,
       3., 34., 46.,  0.,  2.,  1.,  6., 27.,  0.,  0.,  0., 21.,
       37.,  0.,  2.,  2., 10., 42.,  0.,  1.,  2., 49., 24.,  0.,
       3.,  1., 12., 46.,  0.,  2.,  2., 38., 58.,  0.,  3.,  0.,
       20.,  4.,  0.,  0.,  3., 26., 44.,  0.,  1.,  3., 54., 15.]

html = make_html(ind)
with open('output.html', mode='w', encoding='utf8') as f:
    f.write(html)
print(fitness_meta(ind))
