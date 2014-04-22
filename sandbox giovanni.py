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


    

#inserimento dati
XI=583
YI=416
XII=875
YII=416
XIII=861
YIII=304
XIV=861
YIV=83

xI=650
yI=650
xII=650
yII=650
xIII=650
yIII=82
xIV=650
yIV=62


inter=bezTool.calc_int_bez (xI,yI,xII,yII,xIII,yIII,xIV,yIV,XI,YI,XII,YII,XIII,YIII,XIV,YIV)

##################################################
	
font = CurrentFont ()

glyph = font ['c']

glyph.clear ()

pen = glyph.getPen ()
pen.moveTo ((XI,YI))
pen.curveTo ((XII,YII),(XIII,YIII),(XIV,YIV))
pen.closePath()

pen.moveTo ((xI,yI))
pen.curveTo ((xII,yII),(xIII,yIII),(xIV,yIV))
pen.closePath()

pen.moveTo ((0,0))
pen.lineTo ((inter))
pen.closePath()
