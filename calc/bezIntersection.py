########################
# Beziers intersection #
########################

class bezierIntersection:
    def __init__(self):
        pass
    

    def calc_bez_length (xI,yI,xII,yII,xIII,yIII,xIV,yIV,Delta_x_imput_max):
        """(xI,yI,xII,yII,xIII,yIII,xIV,yIV,Delta_x_imput_max)
        calculate the length of a bezier, and the t fraction needed to calulate the imput x precision
        example  for Delta_x_imput_max = 0.001   and a bezier with a length = 100 we will have a Delta_t_bez_cal = 0.00001
        return a tuple (x,y)"""
    
        Delta_t_bez_cal=0.1
    
        x_strt=xI
        y_strt=yI
    
        l_bex=0
    
        t_bez_cal=0

        cx = 3*(xII - xI)
        bx = 3*(xIII - xII) - cx
        ax = xIV - xI - cx - bx
        cy = 3*(yII - yI)
        by = 3*(yIII - yII) - cy
        ay = yIV - yI - cy - by

        while True:
            if t_bez_cal >= 1:
                break
            else:
                pass
            
                t_bez_cal3=t_bez_cal*t_bez_cal*t_bez_cal
                t_bez_cal2=t_bez_cal*t_bez_cal
            
                x_bez_cal = ax*(t_bez_cal3) + bx*(t_bez_cal2) + cx*t_bez_cal + xI
                y_bez_cal = ay*(t_bez_cal3) + by*(t_bez_cal2) + cy*t_bez_cal + yI

                t_bez_cal=t_bez_cal+Delta_t_bez_cal
            
                bez_dis=hypot((x_bez_cal-x_strt),(y_bez_cal-y_strt))

    
                x_strt=x_bez_cal
                y_strt=y_bez_cal
    
                l_bex=l_bex+bez_dis
            
        Delta_t_bez_cal= Delta_x_imput_max / l_bex            
        return l_bex, Delta_t_bez_cal
    
    
    def calc_bez_xy (XI,xI,yI,xII,yII,xIII,yIII,xIV,yIV,Delta_x_imput_max,Delta_t_bez_cal):
        
        """(XI,xI,yI,xII,yII,xIII,yIII,xIV,yIV,Delta_x_imput_max,Delta_t_bez_cal)
        calculate y coordinate on a bezier curve given a x value
        Delta_x_imput_max is the precision required es (0.001) 
        Delta_t_bez_cal is the scan precision es (0.001) 
        if Delta_t_bez_cal is == a sutable number will be calculated using calc_bez_length """
        
        if Delta_t_bez_cal== None:
            calc_bez= calc_bez_length (self,xI,yI,xII,yII,xIII,yIII,xIV,yIV,Delta_x_imput_max)
            Delta_t_bez_cal=calc_bez[1]
        x_imput=XI        
        t_bez_cal=0
    
        cx = 3*(xII - xI)
        bx = 3*(xIII - xII) - cx
        ax = xIV - xI - cx - bx
        cy = 3*(yII - yI)
        by = 3*(yIII - yII) - cy
        ay = yIV - yI - cy - by
    
        Delta_x_imput_eff=1000000000

        while True:
            if t_bez_cal>1 or Delta_x_imput_eff <= Delta_x_imput_max:
                break
            else:
                pass                    
            t_bez_cal=t_bez_cal+Delta_t_bez_cal    
            t_bez_cal3=t_bez_cal*t_bez_cal*t_bez_cal
            t_bez_cal2=t_bez_cal*t_bez_cal
            
            x_bez_cal = ax*(t_bez_cal3) + bx*(t_bez_cal2) + cx*t_bez_cal + xI
            y_bez_cal = ay*(t_bez_cal3) + by*(t_bez_cal2) + cy*t_bez_cal + yI

            Delta_x_imput_eff=fabs(x_imput-x_bez_cal)
            
        X_out=(x_imput+x_bez_cal)/2
        Y_out=y_bez_cal
    
        if    t_bez_cal>1.001:            
            return None
        else: 
            return X_out,Y_out
        
   
    def calc_bez_t (t_bez_cal,xI,yI,xII,yII,xIII,yIII,xIV,yIV):
        """(t_bez_cal,xI,yI,xII,yII,xIII,yIII,xIV,yIV)
        calculate the x,y on a bezier for a given t 0<1
        return a tuple (x,y)
        """
    
        if t_bez_cal<0 or t_bez_cal>1:
            return None
    
        cx = 3*(xII - xI)
        bx = 3*(xIII - xII) - cx
        ax = xIV - xI - cx - bx
        cy = 3*(yII - yI)
        by = 3*(yIII - yII) - cy
        ay = yIV - yI - cy - by
    
        t_bez_cal3=t_bez_cal*t_bez_cal*t_bez_cal
        t_bez_cal2=t_bez_cal*t_bez_cal

        x_bez_cal = ax*(t_bez_cal3) + bx*(t_bez_cal2) + cx*t_bez_cal + xI
        y_bez_cal = ay*(t_bez_cal3) + by*(t_bez_cal2) + cy*t_bez_cal + yI

        return x_bez_cal,y_bez_cal
