###################
# parametricoType #
###################

# Importing modules
from calc import bezIntersection


bezTool= bezIntersection.bezierIntersection()

length= bezTool.calc_bez_length( ((10,10),(1,1),(1,1),(100,100)),1)

print"length",length

xy= bezTool.calc_bez_xy(11,((10,10),(1,1),(1,1),(100,100)),1,None)

print"xy",xy

t= bezTool.calc_bez_t(0.5,((10,10),(1,1),(1,100),(100,1)))


oDraw = lowercase_o.drawing()
nDraw = lowercase_n.drawing()


pen.moveTo ((xI,yI))
pen.curveTo ((xII,yII),(xIII,yIII),(xIV,yIV))
pen.closePath()

pen.moveTo ((0,0))
pen.lineTo ((inter))
pen.closePath()