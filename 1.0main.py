import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# adding the dataset
df = pd.read_csv('1data.csv')

# Converting numeric columns
df['Financial_Loss_USD'] = pd.to_numeric(df['Financial_Loss_USD'], errors='coerce')
df['Total_Cybercrimes'] = pd.to_numeric(df['Total_Cybercrimes'], errors='coerce')

# figure 
plt.figure(figsize=(22, 14))
plt.suptitle('Cybercrime Statistics by Country', fontsize=17)

# -------------------- Dataset Table --------------------
table_ax = plt.subplot2grid((2, 3), (0, 0), colspan=3)
table_ax.axis('off')  # Hide axis borders for table
data_table = table_ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center'
)
data_table.scale(1, 2)

# -------------------- Chart 1: Cybercrimes --------------------
ax1 = plt.subplot2grid((2, 3), (1, 0))
sns.barplot(x='Country', y='Total_Cybercrimes', data=df, ax=ax1, palette='Blues')
ax1.set_title('Total Cybercrimes')
ax1.set_xlabel('Country')
ax1.set_ylabel('Reported Cases')
ax1.tick_params(axis='x', rotation=90)

# -------------------- Chart 2: Financial Loss --------------------
ax2 = plt.subplot2grid((2, 3), (1, 1))
sns.barplot(x='Country', y='Financial_Loss_USD', data=df, ax=ax2, palette='Oranges')
ax2.set_title('Estimated Financial Loss (USD)')
ax2.set_xlabel('Country')
ax2.set_ylabel('Loss in USD')
ax2.tick_params(axis='x', rotation=90)

# -------------------- Chart 3: Prevention Method --------------------
ax3 = plt.subplot2grid((2, 3), (1, 2))
df['Prevention_Method_Taken'].value_counts().plot.pie(
    autopct='%1.1f%%',
    labels=['Yes', 'No'],
    colors=['#66bb6a', '#ef5350'],
    ax=ax3,
    startangle=90
)
ax3.set_title('Prevention Method Taken')
ax3.set_ylabel('')  # it will remove default y-label for pie chart

# Adjust space
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()