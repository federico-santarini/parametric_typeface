###################
# parametricoType #
###################

# Importing modules
from calc import bezIntersection


bezTool= bezIntersection.bezierIntersection()

length= bezTool.calc_bez_length(10,10,1,1,1,1,100,100,1)

print"length",length

xy= bezTool.calc_bez_xy(11,10,10,1,1,1,1,100,100,1,None)

print"xy",xy

t= bezTool.calc_bez_t(0.5,10,10,1,1,1,100,100,1)

print"t",t