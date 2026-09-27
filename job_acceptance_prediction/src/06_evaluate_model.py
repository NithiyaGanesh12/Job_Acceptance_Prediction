from pathlib import Path
import pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data/processed/features.csv'; MODEL=ROOT/'models/job_acceptance_model.pkl'; REPORT=ROOT/'outputs/reports/model_evaluation.txt'
df=pd.read_csv(DATA); X=df.drop(columns='acceptance'); y=df.acceptance.astype(int); _,Xt,_,yt=train_test_split(X,y,test_size=.2,random_state=42,stratify=y); bundle=joblib.load(MODEL); pred=bundle['model'].predict(Xt); text=f'Accuracy: {accuracy_score(yt,pred):.4f}\n\nConfusion Matrix:\n{confusion_matrix(yt,pred)}\n\n{classification_report(yt,pred,target_names=["Rejected","Accepted"])}'; print(text); REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text(text,encoding='utf-8')
