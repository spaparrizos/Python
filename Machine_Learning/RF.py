#!/usr/bin/env python
#########################################################
# Spyros Paparrizos										#		       
# spyridon.paparrizos@lsce.ipsl.fr       				#              
# Random Forest Regressor (RF)							#		       
#########################################################
#  More info here: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html

# Python libraries
from sklearn.ensemble import RandomForestRegressor as RFR
import numpy as np, numpy.ma as ma
import pandas as pd
import matplotlib.pyplot as plt
import cPickle
import matplotlib.gridspec as gridspec

# Preconditions
step = 0.5											# in degrees



#################################
###  CREATE SOME FAKE VALUES  ###
#################################

# Independent variables (regressors)
a_train = np.random.rand(2000)
b_train = np.random.rand(2000)
c_train = np.random.rand(2000)

# Dependent variable (target)
y_train = np.random.rand(2000)


##############################################################
###  PREPARE DATAFRAMES TO INTRODUCE TO THE RF REGRESSION  ###
##############################################################

# Prepare the common dataframe for all regressors
vars_clim = np.array(["a_train", "b_train", "c_train"])
nvars_clim = len(vars_clim)
vals_clim = np.array([a_train, b_train, c_train])

X = pd.DataFrame()
for i in np.arange(nvars_clim):
    X[vars_clim[i]] = vals_clim[i]

# Prepare the dependent variable 
Y = ma.masked_array(y_train)

# Print to check (validate) common shape 
print "Initial X mean values and shape is: ", X.mean(), X.shape 
print "Initial Y mean value and shape is:     ", Y.mean(), Y.shape

 
######################
###  RF algorithm  ###
######################
 
# RF pre-conditions
n_estimators = 100
max_depth = 10

# Executing the RF algorithm
forest = RFR(n_estimators=n_estimators, criterion='mse', max_depth=max_depth, max_features='auto', oob_score=True)
forest.fit(X,Y)

# Estimating R-Squared
r2_train = forest.score(X,Y)
r2_OOB = forest.oob_score_
print "r2_train = ", r2_train, "r2_OOB = ", r2_OOB 

# Estimating simulated values (predict)
ymod = forest.oob_prediction_
print "ymod.min is: ", ymod.min(), "  -  ", "ymod.mean is: ", ymod.mean(), "  -  ", "ymod.max is: ", ymod.max()
print "ymod.shape is: ", ymod.shape


# Save (and Open to re-use) the algorithm
pathout = "./RF_algorithm"
with open(pathout, 'wb') as f:
  cPickle.dump(forest, f)

######################################
###  			  IMPORTANCE PLOT  ###
######################################

# Importance
imps = forest.feature_importances_ 
indices = np.argsort(imps)

# Importance Plot
fig = plt.figure(figsize=[20,28]) 
plt.subplots_adjust(left=0.13, bottom=0.1, right=0.95, top=0.95, wspace=0, hspace=0.) 
plt.rcParams.update({'font.size': 14})
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

ax = plt.subplot(111)
# ax.set_title('Importance', loc='left')
x = np.arange(len(vars_clim))
y = imps[indices]*100
ax.barh(x, y, color='deepskyblue')
ax.set_yticks(x)
ax.set_yticklabels(vars_clim[indices], rotation=0)
ax.set_xlabel('Contribution (%)')
ax.set_xlim(0,100)
for i in np.arange(len(x)):
    ax.text(y[i]+1, x[i],'%.1f'%y[i], size=14, va='center')
    
# Save figure   
plt.savefig("Importance_RF.png")
plt.close()


######################################
###        COMPARISON PLOT         ###
######################################

# FIGURE
fig = plt.figure()
gs = gridspec.GridSpec(1,1)
fig.subplots_adjust(hspace = .25, wspace = 0.15) 

area = 2 * 6.371229E6**2 * np.repeat(step, 360/step)[None,:] * np.pi/180 * np.sin(0.5 * np.repeat(step, 180/step)[:,None] * np.pi/180) * np.cos(np.arange(90 - step/2., -90, -step)[:,None] * np.pi/180)

# Re-name the variables
Simulated = ymod
Observed = Y

# Subplot 1
ax1 = plt.subplot(gs[0])
r2 = np.corrcoef(Observed, Simulated)[1,0]   
print "r2 correlation between the 2 examined datasets is: ", r2

# Title
ax1.set_title("Title", fontweight = 'bold', fontsize = 10)

# Variables to be plotted
ax1.plot(range(len(Y)), Observed, color = "red",linestyle = '-',linewidth = 0.3, label = "Observed")
ax1.plot(range(len(Y)), Simulated, color = "green", linestyle = '-',linewidth = 0.3, label = "Simulated")

# Labels
ax1.set_ylabel("y_label", fontsize = 7, fontweight = 'bold')
ax1.set_xlabel("x_label", fontsize = 7, fontweight = 'bold')

# Legend
legend = ax1.legend(fontsize = 8)

# Grid
plt.grid()
ax1.grid(which = 'major', linestyle = ':',alpha = 0.5, color = "grey")

# Info
info2 = "test"
plt.annotate(info2, xy=(0.01, 0.03), xycoords='axes fraction', color='black', fontsize = 12, fontweight = 'bold')

# Save figure
plt.savefig("Obs-sim_RF.png", dpi=150)
plt.close()
