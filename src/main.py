import pandas as pd

def load_and_clean_data(save = False):
    aqi_df = pd.read_csv('data/aqireport2019.csv')
    aqi_df['County'] = aqi_df['County'].apply(lambda x: x.replace(' County, CO', ''))
    pop_perc_df = pd.read_csv(
        'data/PopulationByRaceEthnicity2019/Share of Total Population-Table 1.csv')
    pop_num_df = pd.read_csv(
        'data/PopulationByRaceEthnicity2019/PopulationTotals-Table 1.csv')
    if save == True:
        aqi_df.to_csv('data/aqiCO_2019.csv')
    return aqi_df, pop_perc_df, pop_num_df

def load_and_clean_census_data():
    pass

if __name__ == '__main__':
    # aqi_df, pop_perc_df, pop_num_df = load_and_clean_data()

    census_clean_df = pd.DataFrame()
    census_df = pd.read_csv(
        'data/ACSDP5Y2018.DP02_2020-07-30T180026/ACSDP5Y2018.DP02_data_with_overlays_2020-07-30T175726.csv', header = 1)
    wanted_data = ['Geographic Area Name', 'EDUCATIONAL ATTAINMENT',
                   'LANGUAGE SPOKEN AT HOME', 'U.S. CITIZENSHIP STATUS']
    for col in census_df.columns:
        if 'Margin of Error' in col:
            continue
        else:
            for wanted in wanted_data:
                if wanted in col:
                    census_clean_df[col] = census_df[col].copy()

    census_clean_df.rename(
        columns=lambda x: x.replace('!!', ' '), inplace=True)
    census_clean_df.rename(columns=lambda x: x.replace(
        'Estimate', ''), inplace=True)
    census_clean_df.rename(columns={'Geographic Area Name': 'County'}, inplace = True)
    census_clean_df['County'] = census_clean_df['County'].apply(lambda x: x.replace(', Colorado', ''))
    census_clean_df.to_csv('data/Educational/Clean_Census.csv')
