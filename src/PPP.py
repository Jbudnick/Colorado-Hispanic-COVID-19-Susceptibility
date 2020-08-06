import pandas as pd


def combine_cols(df, cols_eliminate, col_sum='untitled'):
    df[col_sum] = 0
    for col_eliminate in cols_eliminate:
        df[col_sum] += df[col_eliminate]
        df.drop(columns=col_eliminate, inplace=True)
    return df

def convert_to_boolean(df, col, def_1, with_unknown = False):
    df[col][df[col] == def_1] = 1
    if with_unknown != False:
        df[col][df[col] == with_unknown] = -1
        df[col][(df[col] != 1) & (df[col] != -1)] = 0
    else:
        df[col][df[col] != 1] = 0
    df[col].apply(int)
    return df

def import_PPP_data():
    PPP_df = pd.read_csv('data/PPPDataupto150k-CO.csv')
    PPP2_df = pd.read_csv('data/PPP_Data_150kplus.csv')
    PPP2_df = PPP2_df[PPP2_df['State'] == 'CO']

    PPP2_df.drop(['BusinessName', 'Address'], axis = 1, inplace = True)
    PPP2_df.rename(columns = {'LoanRange': 'LoanAmount'}, inplace = True)

    PPP_df = PPP_df.append(PPP2_df)

    PPP_df[['City', 'BusinessType']] = PPP_df[['City', 'BusinessType']].fillna('Unanswered')
    #Unknown = -1
    PPP_df[['Zip', 'NAICSCode', 'JobsRetained']] = PPP_df[['Zip', 'NAICSCode', 'JobsRetained']].fillna(-1)

    #Assume nonprofit NaNs are No
    PPP_df['NonProfit'] = PPP_df['NonProfit'].fillna(0)
    PPP_df['NonProfit'] = PPP_df['NonProfit'].replace('Y', 1)
    return PPP_df

if __name__ == '__main__':
    PPP_df = import_PPP_data()
