import pandas as pd
import pyarrow as pa
from deltalake import DeltaTable
from deltalake.writer import write_deltalake


csv_file_path = '../data/staging/chipotle_us/chipotle_usa_stores.csv'
delta_pond_path = '../data/deltapond/chipotle_usa/chipotle_usa_stores/'

# Read CSV file
# /Users/DAYANGX/Dev/Projects/Playground/PyDeltaDuck/data/staging/chipotle_us/chipotle_usa_stores.csv
pandaDf = pd.read_csv(csv_file_path)
# Remove empty spaces in State column so that the Delta Partition is clean.
pandaDf['state'] = pandaDf['state'].apply(lambda x: x.replace(' ', ''))
print(pandaDf.head())

# Convert Pandas df to Arrow Table
arrowTable = pa.Table.from_pandas(pandaDf, preserve_index=False)
# Convert String Columns to appropriate Data type
arrow_schema = pa.schema([
    pa.field('state', pa.string()),
    pa.field('location', pa.string()),
    pa.field('address', pa.string()),
    pa.field('latitude', pa.float64()),
    pa.field('longitude', pa.float64())
])
newArrowTable = arrowTable.cast(target_schema=arrow_schema)

# write to Deltapond
write_deltalake(delta_pond_path, newArrowTable,mode='append',partition_by=['state'])