import pandas as pd
data={
    'Column1':["sudha","sinchan","sunny"],
    'Column2':["konduru","kovvuru","ananthapuram"]
}
df=pd.DataFrame(data)
df.to_excel("C:\\Users\\sudarshan\\OneDrive\\Documents\\FILE2.xlsx", sheet_name='Sheet1', index=False)