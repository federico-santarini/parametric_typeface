#####
# c #
#####

import robofab.world
import math
from robofab.world import *
from math import *
from shapes import quarter
from calc import bezIntersection

bezTool= bezIntersection.bezierIntersection()

class lowercase_c():
    
    def __init__(self):
        pass
    
    def drawing(self):
        
        ## Testing quarter class
        
        q = quarter.Quarter()
        
        # Chiamata del glifo
        font = CurrentFont ()
        glyph = font ['c']
        glyph.clear()
        
        
        ### cut
        # Punti di ancoraggio
        x1cutUp = 240
        y1cutUp  = 266
        x2cutUp = 464
        y2cutUp  = 423
        
        # Punti di ancoraggio
        x1cutDw = 240
        y1cutDw  = 185
        x2cutDw = 483
        y2cutDw = 12
        
        
        
        

        ### upperLeft
        # Punti di ancoraggio
        x1 = 3 
        y1 = 238
        x2 = 138 
        y2 = 240
        x3 = 225 
        y3 = 368
        x4 = 230 
        y4 = 462

        # Manipolatori
        hnd_int_ver = 64
        hnd_int_hor = 62
        hnd_ext_ver = 137
        hnd_ext_hor = 137

        # Disegno
        q.upperLeft(glyph, 
                  x1, y1, x2, y2, x3, y3, x4, y4, 
                  hnd_int_ver, hnd_int_hor, 
                  hnd_ext_ver, hnd_ext_hor)
          

        ### upperRight
        # Punti di ancoraggio
        x1 = 328 
        y1 = 239
        x2 = 465 
        y2 = 243
        x3 = 249 
        y3 = 461
        x4 = 243 
        y4 = 366
        
        interUp=bezTool.calc_int_bez (  ((x1cutUp,y1cutUp),(x1cutUp,y1cutUp),(x2cutUp,y2cutUp),(x2cutUp,y2cutUp)), ((x1,y1),(x2,y2),(x3,y3),(x4,y4)) )

        # Manipolatori
        hnd_int_ver = 63
        hnd_int_hor = 60
        hnd_ext_ver = 128
        hnd_ext_hor = 129

        # Disegno
        q.upperRight(glyph, 
                  x1, y1, x2, y2, x3, y3, x4, y4,
                  hnd_int_ver, hnd_int_hor, 
                  hnd_ext_ver, hnd_ext_hor)

        ### bottomLeft
        # Punti di ancoraggio
        x1 = 222
        y1 = 0
        x2 = 224
        y2 = 94
        x3 = 138
        y3 = 221
        x4 = 3
        y4 = 218

        # Manipolatori
        hnd_int_ver = 72
        hnd_int_hor = 56
        hnd_ext_ver = 137
        hnd_ext_hor = 124

        # Disegno
        q.bottomLeft(glyph,
                  x1, y1, x2, y2, x3, y3, x4, y4,
                  hnd_int_ver, hnd_int_hor, 
                  hnd_ext_ver, hnd_ext_hor)
          
          
        ### bottomRight
        # Punti di ancoraggio
        x1 = 243
        y1 = 0
        x2 = 466
        y2 = 225
        x3 = 329
        y3 = 222
        x4 = 245
        y4 = 94

        # Manipolatori
        hnd_int_ver = 76
        hnd_int_hor = 52
        hnd_ext_ver = 154
        hnd_ext_hor = 113

        # Disegno
        q.bottomRight(glyph,
                  x1, y1, x2, y2, x3, y3, x4, y4,
                  hnd_int_ver, hnd_int_hor, 
                  hnd_ext_ver, hnd_ext_hor)

        
