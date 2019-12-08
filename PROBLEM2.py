def PROBLEM2():
    import math as mh
    import numpy as np
    x1 = int(input("First x coordinate: "))
    y1 = int(input("First y coordinate: "))
    x2 = int(input("Second x coordinate: "))
    y2 = int(input("Second y coordinate: "))
    x3 = int(input("Third x coordinate: "))
    y3 = int(input("Third y coordinate: "))
    
    #slope
    s12 = (y2-y1)/(x2-x1)
    s23 = (y3-y2)/(x3-x2)
    
    if s12 == s23:
        print("ERROR: No possible solution because indicated points are collinear")
    else:
        A = np.array([(x1,y1,1),(x2,y2,1),(x3,y3,1)])
        D = np.array([((mh.pow(x1,2)+mh.pow(y1,2)),y1,1),
                      ((mh.pow(x2,2)+mh.pow(y2,2)),y2,1),
                      ((mh.pow(x3,2)+mh.pow(y3,2)),y3,1)])
    
        E = np.array([((mh.pow(x1,2)+mh.pow(y1,2)),x1,1),
                      ((mh.pow(x2,2)+mh.pow(y2,2)),x2,1),
                      ((mh.pow(x3,2)+mh.pow(y3,2)),x3,1)])
    
        F = np.array([((mh.pow(x1,2)+mh.pow(y1,2)),x1,y1),
                      ((mh.pow(x2,2)+mh.pow(y2,2)),x2,y2),
                      ((mh.pow(x3,2)+mh.pow(y3,2)),x3,y3)])
        
        a = np.linalg.det(A)
        m = -(np.linalg.det(D))
        n = np.linalg.det(E)
        o = -(np.linalg.det(F))
        
        d = m/a
        e = n/a
        f = o/a
        
        h = -m/(2*a)
        k = -n/(2*a)
        
        r = np.round((mh.sqrt(mh.pow(h-x1,2)+mh.pow(k-y1,2))),2)
        
        cent = np.round([h,k],2)
        vecDEF = np.round([d,e,f],2)
        
        print("The center of the circle (h,k) is at point: ", cent)
        print("Radius of the circle: ",r)
        print("Vector [D,E,F]: ", vecDEF)
        