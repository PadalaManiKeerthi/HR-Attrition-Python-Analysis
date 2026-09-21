import pandas as pd
import numpy as np
np.random.seed(42)
n=500
df = pd.DataFrame({
    'EmployeeID': range(1, n+1),
    'Age': np.random.randint(22, 60, n),
    'Salary': np.random.randint(30000, 90000, n),
    'Satisfaction': np.random.randint(1, 6, n),
    'YearsAtCompany': np.random.randint(0, 15, n),
    'Attrition': np.random.choice(['Yes','No'], n, p=[0.25, 0.75])
})
df.loc[df['Satisfaction'] <= 2, 'Attrition'] = np.random.choice(['Yes','No'], len(df[df['Satisfaction'] <= 2]), p=[0.6, 0.4])
df.to_csv('hr_dataset.csv', index=False)
print("csv ready!")
