###########
# Polygon #
###########

class Polygon:

    def __init__(self):
        pass
        
    def drawPolyByPoints(self, glyph, points_list):
        pen = glyph.getPen()
    
        # Starting point
        pen.moveTo(points_list[0])
    
        #Extremes
        for point_coordinates in points_list[1:]:
            pen.lineTo(point_coordinates)
    
        # Closing path
        pen.closePath()