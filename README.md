# 🎬 The Oracle: AI Cinematic Forecaster

The Oracle is an intelligent web application designed to forecast whether a movie will be a hit by analyzing industry data like audience ratings and runtimes. It functions through a smart "Random Forest" brain that learns from vast cinematic datasets to make its predictions. To provide a premium user experience, the tool features a sleek, gold accented interface built with modern web frameworks that ensure the site is fast and responsive.

---

## 🚀 Technical Stack

* **Frontend:** React.js, Vite, CSS3 (Luxury Glassmorphism aesthetic)
* **Backend:** Python (Flask), Flask-CORS
* **Machine Learning:** Scikit-learn (Random Forest), Pandas, NumPy

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

* **Self Healing Pipeline:** The backend automatically detects column name variations in the CSV and uses smart fallbacks if data is missing.
* **Luxury UI:** A cinematic dark themed interface with gold accents, responsive glassmorphic cards and smooth CSS animations.
* **Decoupled Architecture:** Frontend and Backend are hosted independently, allowing for efficient scaling of the ML model.

---

## 📸 Interface Preview

<p align="center">
  <img width="100%" alt="The Oracle Home Screen" src="https://github.com/user-attachments/assets/d638d918-2d75-4aee-919d-b025a7f93b03" />
</p>

<p align="center">
  <img width="100%" alt="The Oracle Prediction Result" src="https://github.com/user-attachments/assets/dd00ce42-c09a-41c3-a7bf-349855bf6e64" />
</p>
