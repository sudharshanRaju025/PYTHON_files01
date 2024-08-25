import pandas as pd 
data={
    "Column1":['sudha','sinchan'],
    "Column2":["kondrur","midthur"]

}
df=pd.DataFrame(data)
df.to_excel("C:/Users/sudarshan/OneDrive/Documents/file9.xlsx")
print(df)