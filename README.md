🎬  <b> Movie Recommendation System </b>

A content-based Movie Recommendation System built using Python, Streamlit, and Machine Learning. The application recommends movies similar to a user's selected movie by analyzing movie metadata and computing similarity scores.

🚀 <b> Features </b> <br>
Content-based movie recommendations <br>
Interactive Streamlit web interface <br>
Movie poster integration using OMDb API <br>
IMDb ratings and release year display <br>
Fast similarity-based recommendation engine <br>
Clean and user-friendly UI<br> 
🛠️ <b>Tech Stack </b> <br>
Machine Learning <br>
Python <br>
Pandas <br>
NumPy <br>
Scikit-Learn <br>
NLP & Feature Engineering <br>
Porter Stemmer (NLTK) <br>
CountVectorizer <br>
Cosine Similarity <br>
Frontend : Streamlit
External APIs : OMDb API <br>
📊 <b>Project Workflow </b> <br>
- Collect movie metadata dataset.<br>
- Perform data cleaning and preprocessing. <br>
- Combine important features such as:<br>
  Genres <br>
  Keywords <br>
  Cast <br>
  Crew <br>
  Overview <br>
- Apply text preprocessing and stemming using Porter Stemmer. <br>
- Convert textual data into numerical vectors using CountVectorizer. <br>
- Compute cosine similarity between movie vectors. <br>
- Recommend the most similar movies to the selected movie. <br>
- Fetch movie posters, ratings, and release years using OMDb API. <br>
- Display recommendations through a Streamlit web application. <br>
📂 <b> Project Structure </b> <br>

movie-recommendation-system/ <br>

├── app.py <br>

├── movies.pkl <br>

├── requirements.txt <br>

├── README.md <br>

├── .gitignore <br>

└── similarity.pkl (generated locally and excluded from GitHub)

⚙️ <b> Installation </b> <br>

Clone the repository: <br>

git clone https://github.com/aditi2902/movie-recommendation-system.git <br>

cd movie-recommendation-system <br>

Create a virtual environment: <br>

python3 -m venv venv <br>

source venv/bin/activate <br>

Install dependencies: <br>

pip install -r requirements.txt <br>

▶️ <b> Run the Application </b> <br>

streamlit run app.py <br>

The application will open in your browser at: <br>

http://localhost:8501 <br>
