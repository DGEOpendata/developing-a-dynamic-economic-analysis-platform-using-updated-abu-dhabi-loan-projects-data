python
import pandas as pd
import matplotlib.pyplot as plt

# Load the updated dataset
loan_data = pd.read_csv('Updated_Active_Entities_Ranking.csv')

# Example: Visualize loan amounts by sector
sector_loan_totals = loan_data.groupby('sector')['loan_amount'].sum()

plt.figure(figsize=(10, 6))
sector_loan_totals.plot(kind='bar', color='skyblue')
plt.title('Total Loan Amounts by Sector')
plt.xlabel('Sector')
plt.ylabel('Total Loan Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
