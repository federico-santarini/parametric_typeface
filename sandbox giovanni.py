###################
# parametricoType #
###################

# Importing modules
from calc import bezIntersection


bezierIntersection= bezIntersection.bezierIntersection()
length= bezierIntersection.calc_bez_length(10,10,1,1,1,1,100,100,1)

print"length",length

xy= bezierIntersection.calc_bez_xy(11,10,10,1,1,1,1,100,100,1,None)

print"xy",xy

t= bezierIntersection.calc_bez_t(0.5,10,10,1,1,1,100,100,1)

print"t",t