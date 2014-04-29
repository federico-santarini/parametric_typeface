###############################
# Quarter drawing test script #
###############################

### Apertura librerie
from robofab.world import *

class Quarter:
    
    def __init__(self):
        pass

    def upperRight(self, glyph, 
                   x1, y1, x2, y2, x3, y3, x4, y4, 
                   hnd_int_ver, hnd_int_hor, 
                   hnd_ext_ver, hnd_ext_hor):
        
        pen = glyph.getPen()        pen.moveTo((x1, y1))        pen.lineTo((x2, y2))        pen.curveTo((x2, y2 + hnd_ext_ver),(x3 + hnd_ext_hor, y3),(x3, y3))        pen.lineTo((x4, y4))        pen.curveTo((x4 + hnd_int_hor, y4),(x1, y1 + hnd_int_ver),(x1, y1))        pen.closePath()
        
    
    def upperLeft(self, glyph, 
                  x1, y1, x2, y2, x3, y3, x4, y4, 
                  hnd_int_ver, hnd_int_hor, 
                  hnd_ext_ver, hnd_ext_hor):
        
        pen = glyph.getPen()
        pen.moveTo((x1, y1))
        pen.lineTo((x2, y2))
        pen.curveTo((x2, y2 + hnd_int_ver),(x3 - hnd_int_hor, y3),(x3, y3))
        pen.lineTo((x4, y4))
        pen.curveTo((x4 - hnd_ext_hor, y4),(x1 , y1+ hnd_ext_ver),(x1, y1))
        pen.closePath()
    
    
    def bottomLeft(self, glyph, 
                   x1, y1, x2, y2, x3, y3, x4, y4, 
                   hnd_int_ver, hnd_int_hor, 
                   hnd_ext_ver, hnd_ext_hor):
        
        pen = glyph.getPen()
        pen.moveTo((x1, y1))
        pen.lineTo((x2, y2))
        pen.curveTo((x2 - hnd_int_hor, y2),(x3, y3 - hnd_int_ver),(x3, y3))
        pen.lineTo((x4, y4))
        pen.curveTo((x4, y4 - hnd_ext_ver),(x1 - hnd_ext_hor, y1),(x1, y1))
        pen.closePath()


    def bottomRight(self, glyph, 
                    x1, y1, x2, y2, x3, y3, x4, y4, 
                    hnd_int_ver, hnd_int_hor, 
                    hnd_ext_ver, hnd_ext_hor):
        
        pen = glyph.getPen()
        pen.moveTo((x1, y1))        pen.curveTo((x1 + hnd_ext_hor, y1),(x2, y2 - hnd_ext_ver),(x2, y2))        pen.lineTo((x3, y3))        pen.curveTo((x3, y3 - hnd_int_ver),(x4 + hnd_int_hor, y4),(x4, y4))        pen.lineTo((x1, y1))        pen.closePath()