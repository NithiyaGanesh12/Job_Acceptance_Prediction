from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'data/raw/job_acceptance.csv'; OUT=ROOT/'data/processed/cleaned_data.csv'
if not RAW.exists(): raise FileNotFoundError(f'Dataset not found: {RAW}')
df=pd.read_csv(RAW); df.columns=[c.strip().lower().replace(' ','_') for c in df.columns]; before=len(df); df=df.drop_duplicates().copy()
for c in ['age','experience','current_salary','offered_salary']:
    df[c]=pd.to_numeric(df[c],errors='coerce'); df[c]=df[c].fillna(df[c].median())
for c in df.select_dtypes('object').columns:
    m=df[c].mode(); df[c]=df[c].fillna(m.iloc[0] if len(m) else 'Unknown').astype(str).str.strip()
OUT.parent.mkdir(parents=True,exist_ok=True); df.to_csv(OUT,index=False)
print(f'Removed duplicates: {before-len(df)}'); print('Saved:',OUT); print('Shape:',df.shape)
