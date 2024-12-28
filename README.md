# IMDB Movies Analysis Dashboard

This repository contains an interactive dashboard and exploratory data analysis (EDA) for IMDB movies dataset with a focus on movies in Indonesia. The project leverages Python libraries such as Streamlit for the dashboard, and Pandas, Matplotlib, Seaborn, and Scikit-learn for data analysis and machine learning tasks.

## Repository Structure

```
- dashboard
  - dashboard.py       # Streamlit script for the interactive dashboard
  - movies_cleaned.csv # Preprocessed dataset used for the dashboard
  - imdb_logo.png      # Logo used in the dashboard

- data
  - movies.csv         # Raw dataset containing movie information

- IMDB_EDA.ipynb       # Jupyter notebook for exploratory data analysis
- requirements.txt     # List of dependencies for the project
- README.md            # Documentation for the repository
```

## Features

### Dashboard
The interactive dashboard includes:
- Visualizations for movie ratings, genres, and runtime categories.
- Insights into the distribution of votes and ratings.
- 
### Data
- The `movies.csv` file contains raw data with information such as titles, genres, runtime, and ratings.
- The `moviescsv` file is the cleaned and preprocessed version used for dashboard visualizations.


## How to Run the Dashboard

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the dashboard:
   ```bash
   streamlit run dashboard/dashboard.py
   ```

4. Open the provided local URL in your web browser to interact with the dashboard.

## Dataset
The dataset contains information about movies, including:
- Title
- Release year
- Runtime (in minutes)
- Genres
- Average rating
- Number of votes
- Names of directors and writers

## Visualization Examples
- Distribution of movie genres and runtime categories.
- Relationship between ratings and number of votes.

## Dependencies
The required Python libraries are listed in the `requirements.txt` file. To install all dependencies, run:
```bash
pip install -r requirements.txt
```

## Live Demo

Explore the live version of the IMDB Movies Dashboard here: [Streamlit Dashboard](https://imdb-data-analysis-evjcnprnx3zhctepnyg3gq.streamlit.app/)


## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
For questions or contributions, feel free to open an issue or submit a pull request.

