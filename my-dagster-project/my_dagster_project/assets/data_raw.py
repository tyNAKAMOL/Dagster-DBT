
import glob
import pandas as pd
from dagster import asset,Output
from sqlalchemy import create_engine

@asset(key_prefix=["public"])
def data_raw():
    folder_path = 'C:/Users/beaut/Documents/dagater_dbt/my-dagster-project/my_dagster_project/data'
    dataFrame = []
    first_file = True
    for file_path in glob.glob(f'{folder_path}/raw*.csv'):
        if first_file is True:
            df = pd.read_csv(file_path,sep=",",header=0)
            first_file = False
        else:
            df = pd.read_csv(file_path,skiprows=0,sep=",",)
        dataFrame.append(df)

    merged_df = pd.concat(dataFrame)
    return merged_df

    # engine = create_engine('postgresql://localdbt:password@localhost:54325/testdbt', echo=False) 
    #postgresql://username:password@host:port/database
    # merged_df.to_sql('data_raw', con = engine, if_exists='replace',index_label='id')