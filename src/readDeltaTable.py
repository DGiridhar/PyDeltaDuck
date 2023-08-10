import duckdb
from deltalake import DeltaTable

delta_table_path = '../data/deltapond/chipotle_usa/chipotle_usa_stores/'

# Get table as pyarrow table
arrowDeltaTable = DeltaTable(delta_table_path).to_pyarrow_table()

# Query arrow table as an ordinary SQL Table.
duckdbConnection = duckdb.connect()
duckdbDf = duckdbConnection.execute(''' Select * from arrowDeltaTable where state='Georgia'  and location='Alpharetta' ''').fetch_df()
# arrowResults =duckdbConnection.execute(''' Select count(*) from arrowDeltaTable ''').arrow()
# pandaResults = arrowResults.to_pandas()

#print(results)
print(duckdbDf)