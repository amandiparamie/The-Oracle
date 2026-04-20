from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import os

app = Flask(__name__)
CORS(app)

model = None

def train_movie_model():
    try:
        csv_path = os.path.join("dataset", "IMDB_Movies_Data.csv")
        if not os.path.exists(csv_path):
            print("CRITICAL: CSV file not found in dataset folder.")
            return None
            
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip().str.lower()
        
        #search for any column containing these keywords
        v_col = next((c for c in df.columns if 'vote' in c), None)
        s_col = next((c for c in df.columns if 'rating' in c or 'score' in c), None)
        t_col = next((c for c in df.columns if 'runtime' in c or 'time' in c), None)

        print(f"--- ATTEMPTING TO TRAIN WITH: {v_col}, {s_col}, {t_col} ---")

        #If columns are missing, force create them so the model can train
        if not v_col: 
            df['votes'] = 1000
            v_col = 'votes'
        if not s_col:
            df['rating'] = 7.0
            s_col = 'rating'
        if not t_col:
            df['runtime'] = 120
            t_col = 'runtime'

        #Clean data
        df = df.dropna(subset=[v_col, s_col, t_col])
        
        #Success Logic: Top 50% of the dataset
        median_rating = df[s_col].median()
        df["success_label"] = (df[s_col] >= median_rating).astype(int)
        
        X = df[[v_col, t_col, s_col]]
        y = df["success_label"]
        
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X, y)
        
        print("SUCCESS: AI Model Trained and Ready!")
        return clf

    except Exception as e:
        print(f"Detailed Training Error: {e}")
        return None

model = train_movie_model()

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"status": "ERROR", "message": "Model initialization failed."}), 500
    
    try:
        data = request.json
        # Convert inputs to float
        v = float(data.get('budget', 0)) # Using 'budget' key for Votes from React
        r = float(data.get('runtime', 0))
        s = float(data.get('score', 0))
        
        prediction = model.predict([[v, r, s]])[0]
        return jsonify({"status": "SUCCESS" if prediction == 1 else "FLOP"})
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)