import pandas as pd

# Create a DataFrame with sample data
data = {
    'Column1': [1, 2, 3],
    'Column2': ['sudharshan raju', 'sinchan', 'roger'],
    'Column3':['9392486441','7337205326','8790363405'],
    'Column4':['konduru','kukkatpally','ammerpet']
}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('C:\\Users\\sudarshan\\OneDrive\\Documents\\file7.xlsx', sheet_name='Sheet1', index=False)
