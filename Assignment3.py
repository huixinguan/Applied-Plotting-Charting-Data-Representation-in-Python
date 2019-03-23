
# coding: utf-8

# # Assignment 3 - Building a Custom Visualization
# 
# ---
# 
# In this assignment you must choose one of the options presented below and submit a visual as well as your source code for peer grading. The details of how you solve the assignment are up to you, although your assignment must use matplotlib so that your peers can evaluate your work. The options differ in challenge level, but there are no grades associated with the challenge level you chose. However, your peers will be asked to ensure you at least met a minimum quality for a given technique in order to pass. Implement the technique fully (or exceed it!) and you should be able to earn full grades for the assignment.
# 
# 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ferreira, N., Fisher, D., & Konig, A. C. (2014, April). [Sample-oriented task-driven visualizations: allowing users to make better, more confident decisions.](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf) 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 571-580). ACM. ([video](https://www.youtube.com/watch?v=BI7GAs-va-Q))
# 
# 
# In this [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf) the authors describe the challenges users face when trying to make judgements about probabilistic data generated through samples. As an example, they look at a bar chart of four years of data (replicated below in Figure 1). Each year has a y-axis value, which is derived from a sample of a larger dataset. For instance, the first value might be the number votes in a given district or riding for 1992, with the average being around 33,000. On top of this is plotted the 95% confidence interval for the mean (see the boxplot lectures for more information, and the yerr parameter of barcharts).
# 
# <br>
# <img src="readonly/Assignment3Fig1.png" alt="Figure 1" style="width: 400px;"/>
# <h4 style="text-align: center;" markdown="1">  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 1 from (Ferreira et al, 2014).</h4>
# 
# <br>
# 
# A challenge that users face is that, for a given y-axis value (e.g. 42,000), it is difficult to know which x-axis values are most likely to be representative, because the confidence levels overlap and their distributions are different (the lengths of the confidence interval bars are unequal). One of the solutions the authors propose for this problem (Figure 2c) is to allow users to indicate the y-axis value of interest (e.g. 42,000) and then draw a horizontal line and color bars based on this value. So bars might be colored red if they are definitely above this value (given the confidence interval), blue if they are definitely below this value, or white if they contain this value.
# 
# 
# <br>
# <img src="readonly/Assignment3Fig2c.png" alt="Figure 1" style="width: 400px;"/>
# <h4 style="text-align: center;" markdown="1">  Figure 2c from (Ferreira et al. 2014). Note that the colorbar legend at the bottom as well as the arrows are not required in the assignment descriptions below.</h4>
# 
# <br>
# <br>
# 
# **Easiest option:** Implement the bar coloring as described above - a color scale with only three colors, (e.g. blue, white, and red). Assume the user provides the y axis value of interest as a parameter or variable.
# 
# 
# **Harder option:** Implement the bar coloring as described in the paper, where the color of the bar is actually based on the amount of data covered (e.g. a gradient ranging from dark blue for the distribution being certainly below this y-axis, to white if the value is certainly contained, to dark red if the value is certainly not contained as the distribution is above the axis).
# 
# **Even Harder option:** Add interactivity to the above, which allows the user to click on the y axis to set the value of interest. The bar colors should change with respect to what value the user has selected.
# 
# **Hardest option:** Allow the user to interactively set a range of y values they are interested in, and recolor based on this (e.g. a y-axis band, see the paper for more details).
# 
# ---
# 
# *Note: The data given for this assignment is not the same as the data used in the article and as a result the visualizations may look a little different.*

# In[4]:

# Use the following data for this assignment:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import mpl_toolkits.axes_grid1.inset_locator as mpl_il
import matplotlib.colors

get_ipython().magic('matplotlib notebook')

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df


# In[5]:

dfT=df.T.describe()
columns=dfT.columns.tolist()

yerr=[]
for i in range(len(columns)):
    error_bar=dfT.loc['std'][columns[i]]*1.96//dfT.loc['count'][columns[i]]**0.5
    yerr.append(error_bar)

yerr=np.array(yerr)
yerr.reshape(-1,1)

dfT=dfT.T
dfT['yerr']=yerr

dfT=dfT.T
dfT


# In[11]:

plt.figure()
mean_list=dfT.loc['mean'].tolist()


barlist=plt.bar(range(4),[ dfT.loc['mean'][1992],dfT.loc['mean'][1993],dfT.loc['mean'][1994],dfT.loc['mean'][1995]],
        yerr=yerr,)

plt.xticks(np.linspace(0,3, num=4),('1992','1993','1994','1995'),);
for bar in barlist:
    bar.set_color((0,0,0,0.1))

y=30000
x1, x2 = plt.xlim()
line, = plt.plot([x1,x2], [y,y], '-', color=(0,0,1,.5), lw=1)    




def onclick(event):

    plt.gca().set_title('y-axis value: {}'.format(event.ydata))
    line.set_ydata([event.ydata,event.ydata])
    yPick = event.ydata
    for b, m, e in zip(barlist, mean_list, yerr.tolist()):
        redVal =0
        blueVal =0
        alpha =1
        if yPick > m :
            blueVal = 1 #min(1, (yPick-yMean-yErr)/yErr)
            alpha = min(1, (yPick-m)/e)
        if yPick < m :
            redVal = 1 #min(1, (yMean-yPick-yErr)/yErr) 
            alpha = min(1, (m-yPick)/e) 
        b.set_color((redVal, 0, blueVal, alpha)) #rgba
        b.set_edgecolor('black')

# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
cmap = plt.cm.rainbow
norm = matplotlib.colors.Normalize(vmin=10000, vmax=40000)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])


# In[12]:

# Use the following data for this assignment:
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn
from matplotlib import cm

get_ipython().magic('matplotlib notebook')

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(33500,150000,3650), 
                   np.random.normal(41000,90000,3650), 
                   np.random.normal(41000,120000,3650), 
                   np.random.normal(48000,55000,3650)], 
                  index=[1992,1993,1994,1995])

y = (df.mean(axis = 1)) - 36000 + 3515.919393
plt.figure()
colors = cm.hsv(y / float(max(y)))
plot = plt.scatter(y, y, c = y, cmap = 'hsv')
plt.clf()
plt.colorbar(plot)
plt.bar(list(df.index), list(df.mean(axis = 1)), width = 0.5, yerr = ([150000, 90000, 120000, 55000]/np.sqrt(3650)), color = colors);
plt.xticks(list(df.index), list(df.index))
plt.axhline(y=36000, color='black', linestyle='-')
plt.yticks(list(plt.yticks()[0]) + [36000]);


# In[ ]:




# In[ ]:



