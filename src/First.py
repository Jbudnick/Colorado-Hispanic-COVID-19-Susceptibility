'''
Assuming blank confirmed/probable/death columns are 0
'''
from src.PPP import combine_cols, convert_to_boolean

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

def load_and_clean_data():
    date_cols = ['Date illnesses were determined to be an outbreak']
    outbreak_df = pd.read_csv(
        'data/Outbreak_List.csv', parse_dates= date_cols)
    col_rename_dict = {'Date outbreak was considered closed:': 'Closed Date',
                       'If setting type is other, specify': 'Location Info',
                       'Colorado county (exposure location)': 'Exposure County',
                       'Date illnesses were determined to be an outbreak': 'Start Date',
                       'Number of residents positive for COVID-19 (lab confirmed)': 'Residents Confirmed Positive',
                       'Number of residents with probable COVID-19 (NOT lab confirmed)' : 'Residents Probable Positive',
                       'Number of COVID-19 deaths (lab confirmed/confirmed)' : 'Residents Confirmed Deaths',
                       'Number of COVID-19 deaths (NOT lab confirmed/probable)' : 'Residents Probable Deaths',
                       'Number of staff who are positive for COVID-19 (lab confirmed)' : 'Staff Confirmed Positive',
                       'Number of staff with probable COVID-19 (NOT lab confirmed)' : 'Staff Probable Positive',
                       'Number of COVID-19 staff deaths (lab confirmed/confirmed)' : 'Staff Confirmed Deaths',
                       'Number of COVID-19 staff deaths (NOT lab confirmed/probable)' : 'Staff Probable Deaths',
                       'Number of attendees who are positive for COVID-19 (lab confirmed)' : 'Attendees Confirmed Positive',
                       'Number of attendees with probable COVID-19 (NOT lab confirmed)' : 'Attendees Probable Positive',
                       'Number of COVID-19 attendee deaths (lab confirmed/confirmed)' : 'Attendees Confirmed Deaths',
                       'Number of COVID-19 attendee deaths (NOT lab confirmed/probable)' : 'Attendees Probable Deaths'
                       }
    outbreak_df.rename(columns = col_rename_dict, inplace = True)
    # desired_col_order = ['Setting name',
    #                      'Location Info', 'Exposure County', 'Investigation status', 'Start Date', 'Closed Date'].extend()
    # outbreak_df.reindex(['Setting name', 'Investigation status', 'Location Info', 'Exposure County', 'Start Date', 'Closed Date'].extend()
        # columns=['Location Info', 'Exposure County', 'Start Date', 'Closed Date'])
    no_end_date = '2200-1-1'
    outbreak_df['Closed Date'].fillna(no_end_date, inplace = True)
    outbreak_df['Closed Date'] = pd.to_datetime(outbreak_df['Closed Date'])
    
    
    other_loc_df = outbreak_df[outbreak_df['Location Info'].isnull() == False].copy()
    outbreak_df.drop(columns = 'Location Info', inplace = True)


    outbreak_df.fillna(0, inplace=True)
    outbreak_df[outbreak_df.columns[6:]] = outbreak_df[outbreak_df.columns[6:]].astype(int)
    other_loc_df.fillna(0, inplace=True)
    other_loc_df[outbreak_df.columns[6:]] = outbreak_df[outbreak_df.columns[6:]].astype(int)

    return outbreak_df, other_loc_df

if __name__ == '__main__':
    # PPP_df = 
    outbreak_df, other_loc_df = load_and_clean_data()
