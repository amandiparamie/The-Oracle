# 🎬 The Oracle: AI Cinematic Forecaster

The Oracle is a full stack Web Application that utilizes a Random Forest Classifier to predict the commercial success of a movie based on historical IMDb data. The project features a high end, minimalist interface and a self healing data pipeline.

## 🚀 Technical Stack

* **Frontend:** React.js, Vite, CSS3 (Luxury Glassmorphism aesthetic)
* **Backend:** Python (Flask), Flask-CORS
* **Machine Learning:** Scikit-learn (Random Forest), Pandas, NumPy
* **Deployment:** Netlify (Frontend) & Render/Railway (Backend)

---

## 🧠 Machine Learning Logic

The AI model analyzes three core features from the provided IMDB dataset:
1.  **User Engagement:** Historical vote counts and popularity metrics.
2.  **Runtime:** The duration of the film in minutes.
3.  **Critical Reception:** Expected IMDb ratings.

### Success Criteria
The model defines a **"SUCCESS"** through a strict dual-threshold logic:
* The movie must achieve a **Rating ≥ 7.5**.
* The movie must fall within the **Top 40% of popularity** (calculated via dataset quantiles).

---

## ✨ Key Features

* **Self-Healing Pipeline:** The backend automatically detects column name variations in the CSV (e.g., mapping "Revenue" to "Gross") and uses smart fallbacks if data is missing.
* **Luxury UI:** A cinematic dark-themed interface with gold accents, responsive glassmorphic cards, and smooth CSS animations.
* **Decoupled Architecture:** Frontend and Backend are hosted independently, allowing for efficient scaling of the ML model.
