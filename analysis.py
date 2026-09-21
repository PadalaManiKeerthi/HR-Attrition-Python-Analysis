import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("hr_dataset.csv")

print(f"Total Employees: {len(df)}")
yes_count = len(df[df['Attrition'] == 'Yes'])
print(f"Left Company: {yes_count} ({yes_count/len(df)*100:.1f}%)")

# Graph 1
plt.figure(figsize=(6,4))
sns.countplot(x='Attrition', data=df, palette='Set2')
plt.title("How many left vs stayed")
plt.savefig("attrition_count.png", dpi=150)
plt.close()
print("✅ Graph 1 saved")

# Graph 2
plt.figure(figsize=(6,4))
sns.boxplot(x='Attrition', y='Salary', data=df, palette='Set3')
plt.title("Salary vs Attrition")
plt.savefig("salary_vs_attrition.png", dpi=150)
plt.close()
print("✅ Graph 2 saved")

# Graph 3
plt.figure(figsize=(6,4))
sns.countplot(x='Satisfaction', hue='Attrition', data=df, palette='coolwarm')
plt.title("Satisfaction vs Attrition")
plt.savefig("satisfaction_vs_attrition.png", dpi=150)
plt.close()
print("✅ Graph 3 saved")

print("\nAll done! 3 images ready for GitHub")
