'''
Created on Jul 26, 2015

@author: J4ROD2
'''

class bySector(object):
    '''
    classdocs
    '''

    def __init__(self, df, sector='sector_revised'):
        '''
        Constructor
        '''
        self.df_by_sector = df.groupby(sector)
        
    def summary(self, target_var):
        # basic table with summary stats by some target variable
        self.df_by_sector[target_var].agg([np.sum, np.mean, np.std, len])
        
    def plot(self, target_var):
        self.df_by_sector.boxplot(by=sector, column = target_var)