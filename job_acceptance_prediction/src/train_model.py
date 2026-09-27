from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'data'/'processed'/'cleaned_data.csv'
MODEL_DIR = ROOT/'models'; MODEL_DIR.mkdir(exist_ok=True)
MODEL_FILE = MODEL_DIR/'job_acceptance_model.pkl'
if not DATA.exists():
    raise FileNotFoundError(f'{DATA} not found. Run 02_clean_data.py first.')
df = pd.read_csv(DATA)
X = df.drop(columns=['acceptance','candidate_id'], errors='ignore')
y = df['acceptance'].replace({'Yes':1,'No':0,'yes':1,'no':0}).astype(int)
num_cols = X.select_dtypes(include='number').columns.tolist()
cat_cols = X.select_dtypes(exclude='number').columns.tolist()
pre = ColumnTransformer([
 ('num', Pipeline([('imputer',SimpleImputer(strategy='median')),('scale',StandardScaler())]), num_cols),
 ('cat', Pipeline([('imputer',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore'))]), cat_cols)
])
models = {
 'Logistic Regression': LogisticRegression(max_iter=2000),
 'Random Forest': RandomForestClassifier(n_estimators=200, random_state=42)
}
# stratify is used when both classes have enough examples
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42,stratify=y)
best_name=None; best_acc=-1; best_pipe=None
for name, model in models.items():
    pipe=Pipeline([('preprocessor',pre),('model',model)])
    pipe.fit(X_train,y_train)
    pred=pipe.predict(X_test)
    acc=accuracy_score(y_test,pred)
    print(f'\n{name} accuracy: {acc:.2%}')
    print(classification_report(y_test,pred,zero_division=0))
    print('Confusion matrix:\n',confusion_matrix(y_test,pred))
    if acc > best_acc:
        best_acc=acc; best_name=name; best_pipe=pipe
joblib.dump(best_pipe, MODEL_FILE)
print(f'\nSaved model: {MODEL_FILE}')
print(f'Selected model by test accuracy: {best_name} ({best_acc:.2%})')
