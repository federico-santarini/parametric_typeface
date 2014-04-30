###################
# Sandbox Roberto #
###################

# Importing modules
import robofab.world
import math
from robofab.world import *
from math import *

from calc import bezIntersection
from shapes import quarter

q = quarter.Quarter()

glyph = CurrentGlyph()

p_x1, p_y1 = 282, 413

cExt_x1, cExt_y1 = 149, 379
cExt_x2, cExt_y2 = 133, 185
cExt_x3, cExt_y3 = 247, 113

p_x2, p_y2 = 340, 220

cInt_x1, cInt_y1 = 255, 228
cInt_x2, cInt_y2 = 284, 351
cInt_x3, cInt_y3 = 358, 344

q.genericQuarter(glyph, 
                 (p_x1, p_y1),
                 (cExt_x1, cExt_y1), (cExt_x2, cExt_y2), (cExt_x3, cExt_y3),
                 (p_x2, p_y2),
                 (cInt_x1, cInt_y1), (cInt_x2, cInt_y2), (cInt_x3, cInt_y3))
