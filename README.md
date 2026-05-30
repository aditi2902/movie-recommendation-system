🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python, Streamlit, and Machine Learning. The application recommends movies similar to a user's selected movie by analyzing movie metadata and computing similarity scores.

🚀 Features
Content-based movie recommendations
Interactive Streamlit web interface
Movie poster integration using OMDb API
IMDb ratings and release year display
Fast similarity-based recommendation engine
Clean and user-friendly UI
🛠️ Tech Stack
Machine Learning
Python
Pandas
NumPy
Scikit-Learn
NLP & Feature Engineering
Porter Stemmer (NLTK)
CountVectorizer
Cosine Similarity
Frontend
Streamlit
External APIs
OMDb API
📊 Project Workflow
Collect movie metadata dataset.
Perform data cleaning and preprocessing.
Combine important features such as:
Genres
Keywords
Cast
Crew
Overview
Apply text preprocessing and stemming using Porter Stemmer.
Convert textual data into numerical vectors using CountVectorizer.
Compute cosine similarity between movie vectors.
Recommend the most similar movies to the selected movie.
Fetch movie posters, ratings, and release years using OMDb API.
Display recommendations through a Streamlit web application.
📂 Project Structure

movie-recommendation-system/

├── app.py

├── movies.pkl

├── requirements.txt

├── README.md

├── .gitignore

└── similarity.pkl (generated locally and excluded from GitHub)

⚙️ Installation

Clone the repository:

git clone https://github.com/aditi2902/movie-recommendation-system.git

cd movie-recommendation-system

Create a virtual environment:

python3 -m venv venv

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

▶️ Run the Application

streamlit run app.py

The application will open in your browser at:

http://localhost:8501