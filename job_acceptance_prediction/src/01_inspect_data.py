from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'data/raw/job_acceptance.csv'
if not RAW.exists(): raise FileNotFoundError(f'Dataset not found: {RAW}')
df=pd.read_csv(RAW)
print('Shape:',df.shape); print('\nColumns:',df.columns.tolist()); print('\nData types:\n',df.dtypes); print('\nMissing values:\n',df.isnull().sum()); print('\nDuplicates:',df.duplicated().sum()); print('\nFirst 5 rows:\n',df.head())
