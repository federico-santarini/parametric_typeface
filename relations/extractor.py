############################
# Extraction from ufo file #
############################

from robofab.world import OpenFont

class Extractor():
    
    def __init__(self):
        pass
        
    def extractValues(self, UFOpath, glyphName):
        
        font = OpenFont(UFOpath, showUI = False)
        glyph = font[glyphName]
        
        valuesList = []
        for p in glyph[0].points:
            valuesList.append((p.x, p.y))
            
        return valuesList
        

input_path = u"/Users/robertoarista/Documents/Repositories/parametric_typeface/relations/data.ufo"
        
t = Extractor()
print t.extractValues(input_path, 'test_wgt_exp')