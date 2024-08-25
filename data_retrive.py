import pandas as pd
data={
    "Column1":["suhda","sunny"],
    "Column2":["konduru","midthur"]
    }
# Load the Excel file
df=pd.read_excel("C:\\Users\\sudarshan\\Desktop\\excel files\\file1.xlsx", sheet_name='Sheet1')

# Display the first few rows of the DataFrame
print(df)
