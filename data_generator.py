import pandas as pd
import random

print("Creating dataset...")

data = []
for i in range(500):
    age = random.randint(22, 55)
    salary = random.randint(25000, 90000)
    years = random.randint(0, 10)
    satisfaction = random.randint(1, 5)
    
    # Logic: Low salary + low satisfaction = high chance to leave
    if satisfaction <= 2 and salary < 40000:
        attrition = "Yes" if random.random() < 0.7 else "No"
    elif years <= 2:
        attrition = "Yes" if random.random() < 0.4 else "No"
    else:
        attrition = "Yes" if random.random() < 0.1 else "No"
    
    data.append([i+1, age, salary, years, satisfaction, attrition])

df = pd.DataFrame(data, columns=["EmployeeID","Age","Salary","YearsAtCompany","Satisfaction","Attrition"])
df.to_csv("hr_dataset.csv", index=False)

print("✅ hr_dataset.csv created with 500 rows!")
print(df.head())
