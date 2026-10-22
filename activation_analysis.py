import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate a realistic 100-member mock dataset for the portfolio
np.random.seed(42)
data = {
    'watched_welcome_video': np.random.choice([True, False], 100, p=[0.9, 0.1]),
    'booked_onboarding_call': np.random.choice([True, False], 100, p=[0.7, 0.3]),
    'selected_schedule': np.random.choice(['Schedule A', 'Schedule B', 'Schedule C', 'Pending'], 100, p=[0.4, 0.2, 0.2, 0.2]),
    'completed_first_week': np.random.choice([True, False], 100, p=[0.6, 0.4])
}
df = pd.DataFrame(data)

# Chart 1: The Onboarding Funnel (Where do members drop off?)
funnel_data = {
    'Stage': ['Watched Video', 'Booked Call', 'Completed Week 1'],
    'Users': [df['watched_welcome_video'].sum(), df['booked_onboarding_call'].sum(), df['completed_first_week'].sum()]
}
funnel_df = pd.DataFrame(funnel_data)

plt.figure(figsize=(8, 5))
sns.barplot(x='Stage', y='Users', data=funnel_df, palette='magma')
plt.title('Customer Success Onboarding Funnel Drop-off')
plt.ylabel('Number of Active Members')
plt.savefig('onboarding_funnel.png')

# Chart 2: Activation Rate by Schedule
plt.figure(figsize=(8, 5))
sns.countplot(x='selected_schedule', hue='completed_first_week', data=df, palette='coolwarm', 
              order=['Schedule A', 'Schedule B', 'Schedule C', 'Pending'])
plt.title('First Week Completion by Schedule Cohort')
plt.xlabel('Availability Schedule')
plt.ylabel('User Count')
plt.legend(title='Completed Week 1', labels=['No', 'Yes'])
plt.savefig('schedule_activation.png')

print("Analysis complete. Charts saved as onboarding_funnel.png and schedule_activation.png.")
