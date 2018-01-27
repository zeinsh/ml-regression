def write_to_file(report,filename):
    f=open("output/"+filename,"w")
    f.write(str(report))
    f.close()

def getLine(w,bias,fig_boundary):
    import numpy as np
    x_min,x_max=fig_boundary["x_min"],fig_boundary["x_max"]
    y_min,y_max=fig_boundary["y_min"],fig_boundary["y_max"]
    if w[0]!=0 and abs(w[0])>abs(w[1]):
        yy=np.array([y_min,y_max])
        xx=(-bias-yy*w[1])/w[0]
    else:
        xx=np.array([x_min,x_max])
        yy=(-bias-xx*w[0])/w[1]
    return xx,yy
