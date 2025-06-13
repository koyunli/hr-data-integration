import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
df = pd.read_csv("data/merged_users_attendance.csv")
# Extract the department from the 'company' column
df['department'] = df['company'].apply(eval).apply(lambda x: x['department'])
# Group by department and calculate average hours worked
avg_hours = df.groupby('department')['hours_worked'].mean()
# Plot the average working hours by department
plt.figure(figsize=(10, 6))
avg_hours.sort_values().plot(kind='barh', color='skyblue')
plt.title("Average Working Hours by Department")
plt.xlabel("Hours Worked")
plt.ylabel("Department")
plt.tight_layout()
plt.show()


# Group by gender and calculate average hours worked
gender_avg = df.groupby('gender')['hours_worked'].mean()

# Plot average working hours by gender
plt.figure(figsize=(6, 5))
gender_avg.plot(kind='bar', color=['lightpink', 'lightblue'])
plt.title("Average Working Hours by Gender")
plt.xlabel("Gender")
plt.ylabel("Hours Worked")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
