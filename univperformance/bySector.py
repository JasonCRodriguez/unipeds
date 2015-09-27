'''
Created on Jul 26, 2015

@author: J4ROD2
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

class bySector():
    '''
    classdocs
    '''

    def __init__(self, df, sector='sector_revised'):
        '''
        Constructor
        '''
        self.sector = sector
        self.df_by_sector = df.groupby(self.sector)
        
    def summary(self, target_var):
        # basic table with summary stats by some target variable
        print(self.df_by_sector[target_var].agg([np.sum, np.mean, np.std, len]))
        
    def plot(self, target_var):
        self.column = self.df_by_sector[target_var]

#         fs = 10 # fontsize
#          
#         # demonstrate how to toggle the display of different elements:
#         fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6,6))
#         axes.boxplot(self.column)
#         axes.set_title('Default', fontsize=fs)
        
#        plt.show()
        return self.column
    #self.df_by_sector.boxplot(column = target_var, subplots=False)
        
    def createBands(self, model_var):
        '''
        Code to create bands for a given model variable (model_var)
        '''
            # specify the bins for each category based on the percentiles
        self.bins = list(np.percentile(model_var,range(0,101,10), interpolation='linear'))
        return pd.cut(model_var, self.bins, include_lowest=True, right=True) 
            