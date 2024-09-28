import pandas as pd

# Load data from a CSV file
data = pd.read_csv("people.csv")

# Display the first few rows
print(data.head())

# Filter data based on a condition
filtered_data = data[data["Age"] > 30]

# Calculate summary statistics
mean_age = filtered_data["Age"].mean()
print(f"Mean age: {mean_age}")

# Select 'Name' and 'Country' columns
name_country_df = data[['Name', 'Country']]

# Display the selected columns
print(name_country_df)

# Filter rows where age is greater than 30
older_than_30 = data[data['Age'] > 30]

# Display the filtered data
print(older_than_30)

# Add a new column 'Income'
data['Income'] = [50000, 45000, 60000, 48000]

# Display the updated DataFrame
print(data)






