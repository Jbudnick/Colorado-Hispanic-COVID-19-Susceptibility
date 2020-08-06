import pandas as pd

if __name__ =='__main__':
    years = range(2006, 2020)
    for year in years:
        df = pd.read_csv('data/Environmental/aqireport{}.csv'.format(str(year)))
        df['County'] = df['County'].apply(lambda x: x.replace(', CO', ''))
        df.to_csv('data/Environmental/aqireport{}.csv'.format(str(year)))
