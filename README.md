# Movie Analysis Workflow

## Overview

This project is a modular movie analytics pipeline built using the **TMDB (The Movie Database) API**.

The workflow downloads movie information from the TMDB API, cleans and transforms the data, performs analytical queries, and generates visualizations that provide insights into movie performance.

---

## Objectives

* Fetch movie data from the TMDB API.
* Clean and preprocess raw movie metadata.
* Engineer useful analytical features.
* Analyze financial and rating-related trends.
* Visualize insights through charts.
* Demonstrate a modular software architecture instead of a single Jupyter notebook.


## Workflow

```
Movie IDs
     │
     ▼
fetch_data.py
     │
     ▼
Raw Data
(data/raw/)
     │
     ▼
preprocess.py
     │
     ▼
Processed Data
(data/processed/)
     │
     ▼
analysis.py
     │
     ▼
visualization.py
     │
     ▼
Figures & Insights
(reports/figures/)
```

---

## Module Responsibilities

### `fetch_data.py`

Responsible for communicating with the TMDB API.

Features:

* Downloads movie details.
* Downloads cast and crew information.
* Extracts director information.
* Combines all information into a pandas DataFrame.

---

### `preprocess.py`

Responsible for preparing the raw dataset for analysis.

Main tasks include:

* Flatten nested TMDB JSON fields.
* Convert lists and dictionaries into readable values.
* Handle missing values.
* Remove duplicate records.
* Convert data types.
* Create analytical features such as:

  * Profit
  * ROI
  * Release Year
  * Franchise Indicator

---

### `analysis.py`

Contains reusable analytical functions.

Examples include:

* Ranking movies by different metrics.
* Franchise vs standalone comparison.
* Franchise statistics.
* Director statistics.
* Searching movies by actor.

Each function returns DataFrames instead of printing results, making them reusable and easy to test.

---

### `visualization.py`

Generates charts for analytical insights.

Current visualizations include:

* Budget vs Revenue
* ROI by Genre
* Rating vs Popularity
* Revenue by Release Year
* Franchise vs Standalone Comparison

Charts are saved inside:

```
reports/figures/
```

---

### `utils.py`

Provides helper functions used across the project.

Examples:

* Save DataFrames to CSV.
* Load DataFrames.
* Handle file paths.

---

### `main.py`

Acts as the application entry point.

Responsibilities:

1. Fetch movie data.
2. Save raw dataset.
3. Preprocess the dataset.
4. Save processed dataset.
5. Execute analyses.
6. Generate visualizations.

---

## Data Pipeline

### Raw Dataset

The raw dataset contains the original information returned by the TMDB API.

Location:

```
data/raw/movies_raw.csv
```

---

### Processed Dataset

The processed dataset contains cleaned and transformed data ready for analysis.

Location:

```
data/processed/movies_processed.csv
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd movie-analysis-workflow
```

Create a virtual environment (recommended):

```bash
python -m venv .venv
```

Activate the environment.

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a TMDB API key from:

https://www.themoviedb.org/

Then update `src/config.py`:

```python
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.themoviedb.org/3"
```

---

## Running the Project

From the project root:

```bash
python -m src.main
```

The workflow will:

* Download movie data.
* Save the raw dataset.
* Preprocess the data.
* Save the processed dataset.
* Perform analyses.
* Generate visualizations.

---

## Example Analyses

The project can answer questions such as:

* Which movies generated the highest revenue?
* Which movies achieved the highest ROI?
* Do franchise movies outperform standalone movies?
* Which directors generate the highest total revenue?
* Which genres have the best return on investment?
* Which movies feature a specific actor?

---

## Technologies Used

* Python 3
* pandas
* matplotlib
* requests
* TMDB API

---

## Software Engineering Principles

This project follows several software engineering best practices:

* Separation of concerns.
* Modular architecture.
* Reusable functions.
* Clear project structure.
* Data pipeline design.
* Configuration management.
* Single responsibility principle.

---

## Future Improvements

Potential enhancements include:

* Unit tests with `pytest`.
* Logging instead of print statements.
* Interactive dashboards (Plotly or Streamlit).
* Export analytical reports.
* Command-line arguments for selecting analyses.
* Additional statistical analyses.
* More comprehensive movie datasets.

---

