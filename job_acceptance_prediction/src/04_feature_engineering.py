from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data/processed/cleaned_data.csv'; OUT=ROOT/'data/processed/features.csv'
if not DATA.exists(): raise FileNotFoundError(f'Dataset not found: {DATA}. Run 02_clean_data.py first.')
df=pd.read_csv(DATA); target='acceptance'; mapping={'accepted':1,'yes':1,'1':1,'rejected':0,'no':0,'0':0}; df[target]=df[target].astype(str).str.lower().map(mapping)
if df[target].isna().any(): raise ValueError('Unknown acceptance values found')
X=df.drop(columns=[target,'candidate_id'],errors='ignore'); y=df[target].astype(int); X=pd.get_dummies(X,drop_first=True).astype(float); out=X.copy(); out[target]=y.values; OUT.parent.mkdir(parents=True,exist_ok=True); out.to_csv(OUT,index=False)
print('Feature matrix:',X.shape); print('Saved:',OUT)
