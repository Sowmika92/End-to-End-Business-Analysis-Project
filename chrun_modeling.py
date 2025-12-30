# Simple reusable churn scoring pipeline (skeleton)
import pandas as pd
import joblib
from sklearn.ensemble import GradientBoostingClassifier

def train(features_path, model_output_path):
    df = pd.read_parquet(features_path)
    X = df.drop(columns=['user_id','churn_30'])
    y = df['churn_30']
    model = GradientBoostingClassifier(n_estimators=200, max_depth=5, random_state=42)
    model.fit(X, y)
    joblib.dump(model, model_output_path)

def score(model_path, scoring_df_path, out_path):
    model = joblib.load(model_path)
    df = pd.read_parquet(scoring_df_path)
    X = df.drop(columns=['user_id'])
    df['churn_score'] = model.predict_proba(X)[:,1]
    df.to_parquet(out_path, index=False)

if __name__ == '__main__':
    # Example entrypoint
    train('features/train_snapshot.parquet', 'models/churn_model.pkl')
    score('models/churn_model.pkl', 'features/score_snapshot.parquet', 'scores/today_scores.parquet')
