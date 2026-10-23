import pandas as pd

# Problem 1
data = {
    "Student": ["David", "Samuel", "Terry", "Evan"],
    "Age": [27, 24, 22, 32],
    "Country": ["UK", "Canada", "China", "USA"],
    "Course": ["Python", "Data Structures", "Machine Learning", "Web Development"],
    "Marks": [85, 72, 89, 76]
}

df = pd.DataFrame(data)

print(df)


# Problem 2
b = df["Marks"]

print("\nMarks column:")
print(b)


# Problem 3
c = df[["Country", "Course"]]

print("\nCountry and Course:")
print(c)


# Problem 4
customer_data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Aarav", "Diya", "Rohan", "Anaya", "Kabir",
             "Meera", "Arjun", "Isha", "Vivaan", "Sara"],
    "Age": [25, 34, 29, 41, 36, 28, 45, 31, 39, 27],
    "Gender": ["Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female"],
    "Purchase_Amount": [1200, 2500, 1800, 3200, None,
                        1500, 4100, 2200, 2800, 1700]
}

customers = pd.DataFrame(customer_data)

print("\nFirst 5 rows:")
print(customers.head())

print("\nSummary:")
print(customers.describe())

print("\nMissing values:")
print(customers.isnull().sum())

# Fill missing value with the mean
customers["Purchase_Amount"] = customers["Purchase_Amount"].fillna(
    customers["Purchase_Amount"].mean()
)

print("\nData after handling missing value:")
print(customers)


# Problem 5

# Customers whose age is greater than 30
result = customers[customers["Age"] > 30]

print("\nCustomers with age greater than 30:")
print(result)

# Total purchase amount for male customers
male_total = customers[customers["Gender"] == "Male"]["Purchase_Amount"].sum()

# Total purchase amount for female customers
female_total = customers[customers["Gender"] == "Female"]["Purchase_Amount"].sum()

print("\nMale total:", male_total)
print("Female total:", female_total)

# Select required columns
result = customers[["Customer_ID", "Name", "Purchase_Amount"]]

print("\nSelected columns:")
print(result)


# Problem 6

# Add 10% discounted price
customers["Discounted_Price"] = customers["Purchase_Amount"] * 0.90

print("\nData with discounted price:")
print(customers)

# Average purchase amount according to gender
avg_purchase = customers.groupby("Gender")["Purchase_Amount"].mean()

print("\nAverage purchase amount by gender:")
print(avg_purchase)

# Sort by purchase amount from highest to lowest
sorted_data = customers.sort_values(
    "Purchase_Amount",
    ascending=False
)

print("\nSorted data:")
print(sorted_data)
