from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data/processed/cleaned_data.csv'; FIG=ROOT/'outputs/figures'; FIG.mkdir(parents=True,exist_ok=True)
if not DATA.exists(): raise FileNotFoundError('Run 02_clean_data.py first')
df=pd.read_csv(DATA); print(df['acceptance'].value_counts())
df['acceptance'].value_counts().plot(kind='bar'); plt.title('Job Acceptance Distribution'); plt.xlabel('Acceptance'); plt.ylabel('Candidates'); plt.tight_layout(); plt.savefig(FIG/'acceptance_distribution.png'); plt.close()
df.boxplot(column='offered_salary',by='acceptance'); plt.suptitle(''); plt.title('Offered Salary by Acceptance'); plt.tight_layout(); plt.savefig(FIG/'salary_by_acceptance.png'); plt.close()
print('Figures saved:',FIG)
