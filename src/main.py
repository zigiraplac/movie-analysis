from data.movies_id import movie_ids

from src.fetch_data import fetch_movies
from src.preprocess import preprocess_pipeline

from src.analysis import (
    movie_rankings,
    franchise_comparison,
    franchise_statistics,
    director_statistics,
)

from src.visualization import (
    plot_budget_vs_revenue,
    plot_roi_by_genre,
    plot_rating_vs_popularity,
    plot_revenue_by_year,
    plot_franchise_comparison,
)


from src.utils import save_dataframe

from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH


def main():

    print("Starting movie analysis workflow...")

    # -----------------------------
    # 1. Fetch data
    # -----------------------------

    print("Fetching movies from TMDB...")

    raw_df = fetch_movies(movie_ids)

    print(f"Fetched {len(raw_df)} movies")

    save_dataframe(raw_df, RAW_DATA_PATH)

    # -----------------------------
    # 2. Preprocess data
    # -----------------------------

    print("Cleaning and preprocessing...")

    df = preprocess_pipeline(raw_df)

    save_dataframe(df, PROCESSED_DATA_PATH)

    print(f"Processed dataframe contains {len(df)} movies")

    # -----------------------------
    # 3. Analysis
    # -----------------------------

    print("Running analysis...")

    rankings = movie_rankings(df)

    print("\nHighest Revenue Movies")
    print(rankings["highest_revenue"])

    franchise_compare = franchise_comparison(df)

    print("\nFranchise Comparison")
    print(franchise_compare)

    franchise_stats = franchise_statistics(df)

    director_stats = director_statistics(df)

    # -----------------------------
    # 4. Visualization
    # -----------------------------

    print("Creating visualizations...")

    plot_budget_vs_revenue(df)

    plot_roi_by_genre(df)

    plot_rating_vs_popularity(df)

    plot_revenue_by_year(df)

    plot_franchise_comparison(franchise_compare)

    print("Workflow completed successfully!")


if __name__ == "__main__":
    main()
