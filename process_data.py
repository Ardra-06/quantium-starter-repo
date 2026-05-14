import os

print(os.getcwd())
print(os.listdir())
import pandas as pd

# List of CSV files
files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

# Empty list to store dataframes
dataframes = []

# Read each CSV file
for file in files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Combine all files into one dataframe
combined_df = pd.concat(dataframes, ignore_index=True)

# Keep only Pink Morsels
pink_df = combined_df[combined_df['product'] == 'pink morsel']

# Remove $ sign from price and convert to float
pink_df['price'] = pink_df['price'].replace(r'[\$,]', '', regex=True).astype(float)

# Create sales column
pink_df['sales'] = pink_df['quantity'] * pink_df['price']

# Keep only required columns
final_df = pink_df[['sales', 'date', 'region']]

# Rename columns
final_df.columns = ['Sales', 'Date', 'Region']

# Save output file
final_df.to_csv('formatted_output.csv', index=False)

print("formatted_output.csv created successfully!")