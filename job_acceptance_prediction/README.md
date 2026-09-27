# Job Acceptance Prediction

## Structure
- data/raw and data/processed
- notebooks
- src scripts 01-08
- models
- outputs/figures and reports
- app.py

## Run
```powershell
cd D:\project\job_acceptance_prediction
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src\01_inspect_data.py
python src\02_clean_data.py
python src\03_eda.py
python src\04_feature_engineering.py
python src\05_train_model.py
python src\06_evaluate_model.py
python src\08_prediction.py
streamlit run app.py
```

For MySQL, run mysql_setup.sql first, then `python src\07_sql_upload.py`.

The included CSV is a synthetic sample dataset. Replace it with your approved real dataset for final submission.
