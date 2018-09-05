
# coding: utf-8

# In[102]:


import numpy as np



# In[114]:


def show_histogram(array):
    plt.plot(range(len(array)), array)


# In[115]:





# In[110]:


channels = [list(), list(), list()]

for i in range(3):
    for j in range(len(pix)):
        channels[i].append(pix[j][i])


# In[116]:


chanels_handler = ChannelHandler()
histogram = chanels_handler.get_histogram(channels[0])

show_histogram(channels[0])

