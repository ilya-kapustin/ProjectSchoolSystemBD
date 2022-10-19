from sqlalchemy import create_engine
import pandas as pd

Server = 'LAPTOP-70KT4M65\SQLEXPRESS'
Database = 'School'
Driver = 'SQL Server'
Database_Con = f'mssql://@{Server}/{Database}?driver={Driver}'

if __name__ == '__main__':
    engine = create_engine(Database_Con)
    con = engine.connect()
    df = pd.read_sql_query("Select * from [School].[dbo].[Students]", con)
    print(df.head(), df.shape)
