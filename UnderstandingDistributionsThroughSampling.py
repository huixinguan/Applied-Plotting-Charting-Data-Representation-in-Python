
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[3]:

import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib notebook')

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(figsize=(9,3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5);
plt.axis([-7,21,0,0.6])

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')


# In[6]:

import matplotlib.animation as animation
import numpy as np
import ipywidgets as widgets
from ipywidgets import interact,interactive,fixed,interact_manual

get_ipython().magic('matplotlib notebook')

x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

i=100

def update(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    
    if curr == i: 
        a.event_source.stop()
    plt.cla()
    for n in range(4):
        axes=([-7,2,0,0.6], [-1,11,0,0.6],[6,17,0,0.6],[14,21,0,0.6])
        titles=['x1 normal','x2 gamma','x3 exponential', 'x4 uniform']
        axs = [ax1,ax2,ax3,ax4]
        bins=20
        sample = [x1,x2,x3,x4]
        cols=['r','m','b','g']
        axs[n].hist(sample[n][:curr], bins=bins,normed=True, color=cols[n])
        axs[n].axis(axes[n])

        axs[n].axis(axes[n])
        axs[n].set_title(titles[n], size=9)
#         axs[n].text(sample[n].mean()-1.5, 0.5, '1')
        axs[n].annotate('n = {}'.format(curr), [19,0.53])
    plt.tight_layout() 
  

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=True)        
a = animation.FuncAnimation(fig, update, interval=100)
        

#     plt.annotate('n = {}'.format(curr), [3,3])
    


# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=True)

# axes=([-7,2,0,0.6], [-1,11,0,0.6],[6,17,0,0.6],[14,21,0,0.6])
# titles=['x1 normal','x2 gamma','x3 exponential', 'x4 uniform']
# axs = [ax1,ax2,ax3,ax4]
# bins=20
# sample = [x1,x2,x3,x4]
# cols=['r','m','b','g']
# for n in range(4):
#     axs[n].hist(sample[n], bins=bins,normed=True, color=cols[n])
#     axs[n].axis(axes[n])
#     axs[n].set_title(titles[n], size=9)

# plt.tight_layout() 



# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



