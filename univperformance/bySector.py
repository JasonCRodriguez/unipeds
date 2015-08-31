'''
Created on Jul 26, 2015

@author: J4ROD2
'''
import numpy as np
import matplotlib.pyplot as p
import pandas as pd 

class bySector(object):
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
        return self.df_by_sector[target_var].agg([np.sum, np.mean, np.std, len])
        
    def plot(self, target_var):
        self.df_by_sector.boxplot(by=self.sector, column = target_var)
        
    def createBands(self, model_var):
        '''
        Code to create bands for a given model variable (model_var)
        '''
            # specify the bins for each category based on the percentiles
        self.bins = list(np.percentile(model_var,range(0,101,10), interpolation='linear'))
        return pd.cut(model_var, self.bins, include_lowest=True, right=True) 
            