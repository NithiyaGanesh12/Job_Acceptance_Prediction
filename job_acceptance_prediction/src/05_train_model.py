from pathlib import Path
import pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data/processed/features.csv'; OUT=ROOT/'models/job_acceptance_model.pkl'
if not DATA.exists(): raise FileNotFoundError('Run 04_feature_engineering.py first')
df=pd.read_csv(DATA); X=df.drop(columns='acceptance'); y=df.acceptance.astype(int); Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42,stratify=y); model=RandomForestClassifier(n_estimators=200,random_state=42,class_weight='balanced'); model.fit(Xtr,ytr); OUT.parent.mkdir(parents=True,exist_ok=True); joblib.dump({'model':model,'features':X.columns.tolist()},OUT); print('Model saved:',OUT); print('Train:',len(Xtr),'Test:',len(Xte))
