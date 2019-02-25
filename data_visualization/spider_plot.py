#!/usr/bin/env python
########################################################
# Spyros Paparrizos								      
# spipap@gmail.com					              
# Line customization: 15 (Generate data)
########################################################

# Python libraries
import numpy as np, sys, os
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import seaborn as sns

# Generate data
df = pd.DataFrame({
'group': ['label 1','label 2'],
'var1':  [0.0000086,    0.0000103],
'var2':   [0.0000036,  0.0000013],
'var3':  [0.0000015,   0.0000025],
'var4':  [0.0000035,  0.0000065]
})


MSD_MLR = 0.0000013 + 0.0000025 + 0.0000065     # = 0.0000103
MSD_RF  = 0.0000036 + 0.0000015 + 0.0000035		# = 0.0000086


# Labels
labels=np.array(['var1', 'var2', 'var3', 'var4'])
stats=df.loc[0,labels].values

# Figure preparation
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)#. # Set the angle
stats=np.concatenate((stats,[stats[0]]))  # Closed
angles=np.concatenate((angles,[angles[0]]))  # Closed

# FIGURE
fig=sns.plt.figure()

ax = fig.add_subplot(111, polar=True)   # Set polar axis
fig.subplots_adjust(hspace = .25, wspace = 0.25) 
ax.set_thetagrids(angles * 180/np.pi, labels)  # Set the label for each axis

ttl = ax.title
ttl.set_position([.5, 1.05])
ax.set_title("Title", fontsize = 14, fontweight = 'bold', y = 1.1)

# Grid
ax.grid(True)

# Ind1
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=0.4, linestyle='solid', color = 'red', label="label 1")
ax.fill(angles, values, 'r', alpha=0.2)
 
# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=0.4, linestyle='solid', color = 'blue', label="label 2")
ax.fill(angles, values, 'b', alpha=0.2)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), framealpha = 0.5, fontsize = 12, frameon = True)

# Exponential form
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0), color = 'white', size = 4)

# Save figure
plt.savefig("./Spider_plot.png", dpi=150)
plt.close()
