import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


# Importing the dataset
pd.set_option("display.float_format", "{:.5f}".format)
df = pd.read_csv("Q1_property.csv", sep=";")

# Ensure the validation and correction of any inconsistent data formats
df = df.dropna()
# Identify and address missing values in the dataset
df = df.fillna(0)

# Identify and manage potential outliers within the data.
df["price"] = pd.to_numeric(df["price"], errors="coerce")
zscores = stats.zscore(df["price"])
threshold = 3

df = df[(zscores < threshold) & (zscores > -threshold)]

# Overall correlation structure within the dataset
numeric_columns = ["price", "latitude", "longitude", "baths", "bedrooms"]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")
correlation_matrix = df[numeric_columns].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# correlation between the number of properties listed by an agent and the average property price
agent_stats = (
    df.groupby("agent").agg({"property_id": "count", "price": "mean"}).reset_index()
)
agent_stats.columns = ["agent", "num_properties", "avg_price"]
correlation = agent_stats["num_properties"].corr(agent_stats["avg_price"])

plt.figure(figsize=(10, 6))
sns.scatterplot(x="num_properties", y="avg_price", data=agent_stats)
plt.title("Correlation between Number of Properties and Average Price")
plt.xlabel("Number of Properties Listed")
plt.ylabel("Average Property Price")
plt.show()

# New column indicating the price per square meter
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["area"] = pd.to_numeric(df["area"].str.extract("(\d+\.\d+|\d+)")[0], errors="coerce")
df["price_per_sqm"] = df["price"] / df["area"]
print(df[["price", "area", "price_per_sqm"]])

# additional temporal features, including month, quarter, and day of the week
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["month_added"] = df["date_added"].dt.month
df["quarter_added"] = df["date_added"].dt.quarter
df["day_of_week_added"] = df["date_added"].dt.dayofweek
print(df[["date_added", "month_added", "quarter_added", "day_of_week_added"]])

# Standardising the numerical variables using StandardScaler
scaler = StandardScaler()
df_standardized = pd.DataFrame(
    scaler.fit_transform(df[numeric_columns]), columns=numeric_columns
)
print(df_standardized)

# Encoding the categorical variables using LabelEncoder
categorical_columns = [
    "page_url",
    "property_type",
    "location",
    "city",
    "province_name",
    "purpose",
    "agency",
    "agent",
]

label_encoder = LabelEncoder()
for column in categorical_columns:
    df[column + "_encoded"] = label_encoder.fit_transform(df[column])
print(df)
