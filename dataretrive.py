import pandas as pd

# Path to your .xlsm file
file_path = 'file6.xlsm'

# Load the Excel file
# You can specify the sheet name or index (0-based) if needed
df = pd.read_excel(file_path, engine='openpyxl', sheet_name='Sheet1')

# Display the first few rows of the dataframe
print(df.head())
