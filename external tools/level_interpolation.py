#################################
# Robofont levels interpolation #
#################################

# Apertura librerie
from robofab.world import *

# Funzioni

# Variabili

# Istruzioni
glyph = CurrentGlyph()
print glyph

value = 0.2

estremo01 = glyph.getLayer('01', clear = False)
estremo02 = glyph.getLayer('02', clear = False)

print estremo01.isCompatible(estremo02, False)

glyph.interpolate(value, estremo01, estremo02)

# Visualizzare automaticamente i punti intermedi dell'interpolazione