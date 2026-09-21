import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('hr_dataset.csv')

plt.figure(figsize=(6,4))
sns.countplot(x='Attrition', data=df)
plt.title('Attrition Count')
plt.savefig('attrition_count.png')
plt.close()

plt.figure(figsize=(6,4))
sns.boxplot(x='Attrition', y='Salary', data=df)
plt.title('Salary vs Attrition')
plt.savefig('salary_vs_attrition.png')
plt.close()

plt.figure(figsize=(6,4))
sns.countplot(x='Satisfaction', hue='Attrition', data=df)
plt.title('Satisfaction vs Attrition')
plt.savefig('satisfaction_vs_attrition.png')
plt.close()
print("3 images ready!")
