import pandas as pd
import glob

# Load and combine all CSV files for 2021-2025
file_paths = glob.glob("data\raw\demanddata_202*.csv")
df_list = [pd.read_csv(f) for f in file_paths]
df = pd.concat(df_list, ignore_index=True)

# Clean up column names and inspect
print(df.head())