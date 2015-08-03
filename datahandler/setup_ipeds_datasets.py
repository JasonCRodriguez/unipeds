# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:16:26 2015

@author: takahirodoi
"""

import pandas as pd
import numpy as np

class SetupIPEDSData:
    '''
    Read, filter, merge two IPEDS datasets:     
    1) IPEDS Analytics Delta Cost Analytics Data 1987-2012 
    2) Distance data
    
    Also, detect nan in the retentionrate entry and add that info to
    the main dataframe
    '''

    def __init__(self):
        '''
        Create data frames for main dataset and distance dataset
        '''
        self.df_main = pd.DataFrame()
        self.df_dist = pd.DataFrame()
        
       
    def read_maindata(self):
        self.df_main = pd.read_csv(self.__filein_main, 
             sep = ',',
             # read the specified variables as object     
             dtype = {'academicyear':'object',
                      'groupid':'object',
                      'unitid':'object',
                      'sector':'object',
                      'sector_revised':'object'
                      },
             usecols = [
             "groupid",
             "unitid",
             "academicyear",
             "acadsupp01",
             "liabilities07",
             "assets11",
             "ftretention_rate",
             "ptretention_rate",
             "fall_cohort_num",
             "fall_cohort_pct",
             "fall_cohort_num_indistrict",
             "fall_cohort_pct_indistrict",
             "fall_cohort_num_instate",
             "fall_cohort_pct_instate",
             "fall_cohort_num_outofstate",
             "fall_cohort_pct_outofstate",
             "fall_cohort_num_resunknown",
             "fall_cohort_pct_resunknown",
             "fall_total_undergrad",
             "total_enrollment_amin_tot",
             "total_enrollment_asian_tot",
             "total_enrollment_black_tot",
             "total_enrollment_hisp_tot",
             "total_enrollment_white_tot",
             "total_enrollment_multi_tot",
             "total_enrollment_unkn_tot",
             "total_enrollment_nonres_tot",
             "any_aid_num",
             "any_aid_pct",
             "tuitionfee02_tf",
             "total01",
             "eandg01_sum",
             "grad_rate_150_p",
             "all_employees",
             "ft_faculty_salary",
             "full_time_employee_100fte",
             "sector",
             "sector_revised"
        ])

    def filter_maindata(self):
        '''
        Filter the main data based on 
        1) year 2012
        2) sectors: 1='Public 4-year or above', 2='Private nonprofit 4-year or above',
                    3='Private for-profit 4-year or above'
           (we use sector_revised, where 4-year univs that don't grant diplomas are removed)
        '''

        tmp = self.df_main
        tmp = tmp[tmp['academicyear']=='2012']
        tmp = tmp[tmp['sector_revised'].isin(['1','2','3'])] # note that sector is read as object
        self.df_main = tmp

    def detect_nan_retrate(self):
        '''
        detect nan elements in ftretention_rate column
        and put it into newly created 'not_missing' column
        '''
        self.df_main['missing_ret'] = np.isnan(self.df_main.ftretention_rate)

    def read_distdata(self):
        self.df_dist = pd.read_csv(self.__filein_dist)
        
    def filter_distdata(self):
        '''
        Filter the distance data base on level of student (undergrad)
        '''
        
        
        
        
        
    # private variables
    __filein_main = '../data/IPEDS_Analytics_DCP_87_12_CSV/delta_public_00_12.csv'
#    __filein_dist = '../data/EF2012A_DIST/ef2012a_dist_rv.csv'
    __filein_dist = '../data/EF2013A_DIST/ef2013a_dist.csv'

