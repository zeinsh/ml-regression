
# coding: utf-8

# In[ ]:




# In[2]:

def scatterData(X,y,classmap):
    import matplotlib.pyplot as plt
    for c,label in classmap.iteritems():
        pltdata=X[(y==c)]
        plt.scatter(pltdata[:,0], pltdata[:,1] ,label=label) 

def plotDecisionBoundary(w,bias,fig_boundary):
    import matplotlib.pyplot as plt
    from helpersmd import getLine
    xline,yline=getLine(w,bias,fig_boundary)
    plt.plot(xline,yline, 'k-',label="Decision Boundary")

import matplotlib.pyplot as plt
import numpy as np


# In[9]:


def saveFigure(desc,TUT_NUM,FIG_COUNT):
    plt.savefig('figures/c%s-%d-%s'%(TUT_NUM,FIG_COUNT,desc))
def plotVector(Y,desc,xlabel="x",ylabel="f(x)",showMean=False,X=None):
    if showMean:
        N=X.shape[0]
        xmean=np.mean(X)
        plt.plot([0,N-1],[xmean,xmean])
    if X==None:
        plt.plot(Y)
    else:
	plt.plot(X,Y)
    plt.title(desc)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
def plotHistogram(X,desc):
    import matplotlib.pyplot as plt
    plt.hist(X)
    plt.title(desc)
    plt.xlabel("x")
    plt.ylabel("f(x)")
def plotDistribution(X,desc):
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set(color_codes=True)
    sns.distplot(X)
    plt.title(desc)
    plt.xlabel("x")
    plt.ylabel("f(x)")


# In[2]:


def plot2D(X,Y,desc,xlabel="x",ylabel="f(x)"):
    plt.plot(X,Y)
    plt.grid()
    plt.title(desc)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

