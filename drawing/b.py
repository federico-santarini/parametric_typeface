# coding = utf-8
#####
# b #
#####

import robofab.world
import math
from robofab.world import *
from math import *
from shapes import quarter, polygon
class lowercase_b():
    
    def __init__(self):
        pass
        
    def drawing(self):
        
        ## Testing quarter class
        
        q = quarter.Quarter()
        p = polygon.Polygon()
        
        # Chiamata del glifo
        font = CurrentFont ()
        glyph = font ['b']
        glyph.clear()
        
        ### upperLeft
        # punti di ancoraggio
        
        p_x1 = 230 
        p_y1 = 462
        cExt_x1 = 93
        cExt_y1 = 462
        cExt_x2 = 3
        cExt_y2 = 375
        cExt_x3 = 3 
        cExt_y3 = 238
        p_x2 = 138 
        p_y2 = 240
        cInt_x1 = 138
        cInt_y1 = 304
        cInt_x2 = 163
        cInt_y2 = 368
        cInt_x3 = 225 
        cInt_y3 = 368
        
        # Disegno
        q.genericQuarter(glyph,                      (p_x1, p_y1),                      (cExt_x1, cExt_y1), (cExt_x2, cExt_y2), (cExt_x3, cExt_y3),                      (p_x2, p_y2),                      (cInt_x1, cInt_y1), (cInt_x2, cInt_y2), (cInt_x3, cInt_y3))
                      
        
        ### bottomLeft
        # punti di ancoraggio
        
        p_x1 = 3 
        p_y1 = 218
        cExt_x1 = 3
        cExt_y1 = 81
        cExt_x2 = 98
        cExt_y2 = 0
        cExt_x3 = 222 
        cExt_y3 = 0
        p_x2 = 224
        p_y2 = 94
        cInt_x1 = 168
        cInt_y1 = 94
        cInt_x2 = 138
        cInt_y2 = 149
        cInt_x3 = 138 
        cInt_y3 = 221
        
        # Disegno
        q.genericQuarter(glyph,                      (p_x1, p_y1),                      (cExt_x1, cExt_y1), (cExt_x2, cExt_y2), (cExt_x3, cExt_y3),                      (p_x2, p_y2),                      (cInt_x1, cInt_y1), (cInt_x2, cInt_y2), (cInt_x3, cInt_y3))
                              
        
        ### bottomRight
        # punti di ancoraggio
        
        p_x1 = 243 
        p_y1 = 0
        cExt_x1 = 356
        cExt_y1 = 0
        cExt_x2 = 466
        cExt_y2 = 71
        cExt_x3 = 466 
        cExt_y3 = 225
        p_x2 = 329
        p_y2 = 222
        cInt_x1 = 329
        cInt_y1 = 146
        cInt_x2 = 297
        cInt_y2 = 94
        cInt_x3 = 245
        cInt_y3 = 94
        
        # Disegno
        q.genericQuarter(glyph,                      (p_x1, p_y1),                      (cExt_x1, cExt_y1), (cExt_x2, cExt_y2), (cExt_x3, cExt_y3),                      (p_x2, p_y2),                      (cInt_x1, cInt_y1), (cInt_x2, cInt_y2), (cInt_x3, cInt_y3))
  
  
        ### upperRight
        # punti di ancoraggio
        
        p_x1 = 465 
        p_y1 = 243
        cExt_x1 = 465
        cExt_y1 = 371
        cExt_x2 = 378
        cExt_y2 = 461
        cExt_x3 = 249 
        cExt_y3 = 461
        p_x2 = 243
        p_y2 = 366
        cInt_x1 = 303
        cInt_y1 = 366
        cInt_x2 = 328
        cInt_y2 = 302
        cInt_x3 = 328
        cInt_y3 = 239
        
        # Disegno
        q.genericQuarter(glyph,                      (p_x1, p_y1),                      (cExt_x1, cExt_y1), (cExt_x2, cExt_y2), (cExt_x3, cExt_y3),                      (p_x2, p_y2),                      (cInt_x1, cInt_y1), (cInt_x2, cInt_y2), (cInt_x3, cInt_y3))
        
        ### asta
        # punti di ancoraggio
        x1 = 138
        y1 = 750
        x2 = 3
        y2 = 750
        x3 = 3
        y3 = 0
        x4 = 138
        y4 = 0
                                              
        points_list = [(x1,y1) , (x2,y2) , (x3,y3) , (x4,y4)]
        
        #disegno
        p.drawPolyByPoints(glyph, points_list)
            
