import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("hospital_data.csv")

# Convert dates
df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])

# Hospital stay duration
df['Hospital_Stay'] = (df['Discharge_Date'] - df['Admission_Date']).dt.days

# --- Basic Analysis ---
print("Most common diseases:\n", df['Disease'].value_counts())
print("\nAverage cost per disease:\n", df.groupby('Disease')['Treatment_Cost'].mean())
print("\nAverage hospital stay by disease:\n", df.groupby('Disease')['Hospital_Stay'].mean())

# --- Visualizations ---

# 1. Disease distribution
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Disease', order=df['Disease'].value_counts().index)
plt.title("Top Diseases Distribution")
plt.xticks(rotation=45)
plt.show()

# 2. Gender vs Disease
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Disease', hue='Gender')
plt.title("Disease Distribution by Gender")
plt.xticks(rotation=45)
plt.show()

# 3. Admissions trend per month
df['Month'] = df['Admission_Date'].dt.month_name()
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Month', order=df['Month'].value_counts().index)
plt.title("Patient Admissions per Month")
plt.xticks(rotation=45)
plt.show()

# 4. Age vs Disease
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='Disease', y='Age')
plt.title("Age Distribution per Disease")
plt.xticks(rotation=45)
plt.show()
