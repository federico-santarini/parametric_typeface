###################
# parametricoType #
###################

# Importing modules
from drawing import a, b, c, d, e, i, l, m, n, o, p, q, u
from relations import extractor
from calc import bezIntersection
from shapes import quarter

# Constructors
lowercase_a = a.lowercase_a()
lowercase_b = b.lowercase_b()
lowercase_c = c.lowercase_c()
lowercase_d = d.lowercase_d()
lowercase_e = e.lowercase_e()
lowercase_i = i.lowercase_i()
lowercase_l = l.lowercase_l()
lowercase_m = m.lowercase_m()
lowercase_n = n.lowercase_n()
lowercase_o = o.lowercase_o()
lowercase_p = p.lowercase_p()
lowercase_q = q.lowercase_q()
lowercase_u = u.lowercase_u()

# Intersezione bezier
bezIntersection = bezIntersection.bezierIntersection()

input_path = u"/Users/robertoarista/Documents/Repositories/parametric_typeface/relations/data.ufo"

e = extractor.Extractor()
print e
values = e.extractValues(input_path, 'test_wgt_exp')
print values

print bezIntersection.calc_bez_t(0.5, 22, 327, 22, 164, 145, 29, 293, 8)


### Testing quarter class

## Si parte dal punto più in basso a sinistra
#q = quarter.Quarter()

## Chiamata del glifo
#glyph = CurrentGlyph()
#glyph.clear()

#### upperLeft
## Punti di ancoraggio
#x1 = 3 
#y1 = 238
#x2 = 138 
#y2 = 240
#x3 = 225 
#y3 = 368
#x4 = 230 
#y4 = 462

## Manipolatori
#hnd_int_ver = 64
#hnd_int_hor = 62
#hnd_ext_ver = 137
#hnd_ext_hor = 137

## Disegno
#q.upperLeft(glyph, 
#          x1, y1, x2, y2, x3, y3, x4, y4, 
#          hnd_int_ver, hnd_int_hor, 
#          hnd_ext_ver, hnd_ext_hor)
          

#### upperRight
## Punti di ancoraggio
#x1 = 328 
#y1 = 239
#x2 = 465 
#y2 = 243
#x3 = 249 
#y3 = 461
#x4 = 243 
#y4 = 366

## Manipolatori
#hnd_int_ver = 63
#hnd_int_hor = 60
#hnd_ext_ver = 128
#hnd_ext_hor = 129

## Disegno
#q.upperRight(glyph, 
#          x1, y1, x2, y2, x3, y3, x4, y4,
#          hnd_int_ver, hnd_int_hor, 
#          hnd_ext_ver, hnd_ext_hor)

#### bottomLeft
## Punti di ancoraggio
#x1 = 222
#y1 = 0
#x2 = 224
#y2 = 94
#x3 = 138
#y3 = 221
#x4 = 3
#y4 = 218

## Manipolatori
#hnd_int_ver = 72
#hnd_int_hor = 56
#hnd_ext_ver = 137
#hnd_ext_hor = 124

## Disegno
#q.bottomLeft(glyph,
#          x1, y1, x2, y2, x3, y3, x4, y4,
#          hnd_int_ver, hnd_int_hor, 
#          hnd_ext_ver, hnd_ext_hor)
          
          
#### bottomRight
## Punti di ancoraggio
#x1 = 243
#y1 = 0
#x2 = 466
#y2 = 225
#x3 = 329
#y3 = 222
#x4 = 245
#y4 = 94

## Manipolatori
#hnd_int_ver = 76
#hnd_int_hor = 52
#hnd_ext_ver = 154
#hnd_ext_hor = 113

## Disegno
#q.bottomRight(glyph,
#          x1, y1, x2, y2, x3, y3, x4, y4,
#          hnd_int_ver, hnd_int_hor, 
#          hnd_ext_ver, hnd_ext_hor)

