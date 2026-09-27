from pathlib import Path
import joblib
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
MODEL=ROOT/'models'/'job_acceptance_model.pkl'
if not MODEL.exists():
    raise FileNotFoundError(f'{MODEL} not found. Run train_model.py first.')
model=joblib.load(MODEL)
sample=pd.DataFrame([{
 'age':28,'education':'MCA','experience':4,'current_salary':40000,
 'offered_salary':52000,'job_role':'Data Analyst','location':'Chennai',
 'work_mode':'Hybrid','relocation':'Yes','career_growth':'High'
}])
pred=int(model.predict(sample)[0])
print('Predicted acceptance:', 'Yes' if pred==1 else 'No')
if hasattr(model,'predict_proba'):
    print('Acceptance probability:', f'{model.predict_proba(sample)[0][1]:.2%}')
