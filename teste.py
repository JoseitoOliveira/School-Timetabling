from fitness import fitness_meta
from make_pdf import make_html

ind = [0.,  2.,  0., 17., 40.,  0.,  2.,  1., 27., 41.,  0.,  1.,
       2.,  2., 46.,  0.,  0.,  1., 37., 46.,  0.,  1.,  0., 18.,
       30.,  0.,  2.,  2., 48., 16.,  0.,  0.,  2., 30., 18.,  0.,
       0.,  0., 18., 27.,  0.,  1.,  1., 36., 45.,  0.,  0.,  0.,
       15., 42.,  0.,  2.,  1., 33., 40.,  0.,  2.,  2., 40., 38.]

html = make_html(ind)
with open('output.html', mode='w', encoding='utf8') as f:
    f.write(html)
print(fitness_meta(ind))
