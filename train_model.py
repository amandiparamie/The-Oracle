def train_movie_model():
    try:
        csv_path = os.path.join("dataset", "IMDB_Movies_Data.csv")
        df = pd.read_csv(csv_path)
        
        #Print columns to terminal to help us debug
        print("--- DEBUG: YOUR DATASET COLUMNS ---")
        print(df.columns.tolist())
        print("-----------------------------------")

        #Force lowercase and remove spaces
        df.columns = df.columns.str.strip().str.lower()
        
        #Check for the essential columns
        required = ['budget', 'runtime', 'score']
        available = df.columns.tolist()
        
        money_col = None
        for col in ['gross', 'revenue', 'box_office']:
            if col in available:
                money_col = col
                break
        
        if not money_col or 'budget' not in available:
            print(f"CRITICAL ERROR: Could not find Budget or Gross/Revenue columns.")
            return None

        #Clean and Train
        df = df[(df[money_col] > 0) & (df['budget'] > 0)].dropna(subset=['score', 'runtime'])
        df["success_label"] = (df[money_col] > df['budget'] * 2).astype(int)
        
        X = df[['budget', 'runtime', 'score']]
        y = df["success_label"]
        
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X, y)
        print("SUCCESS: AI Model is Live!")
        return clf
    except Exception as e:
        print(f"Detailed Training Error: {e}")
        return None