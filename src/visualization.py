import matplotlib.pyplot as plt


from pathlib import Path


def plot_budget_vs_revenue(df):

    output_path = Path("reports/figures/revenue_vs_budget.png")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 6))

    plt.scatter(df["budget_musd"], df["revenue_musd"])

    plt.xlabel("Budget (Million USD)")
    plt.ylabel("Revenue (Million USD)")
    plt.title("Revenue vs Budget")

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print(f"Saved figure: {output_path}")


def plot_roi_by_genre(df):

    output_path = Path("reports/figures/roi_by_genre.png")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    genre_df = df[["genres", "roi"]].copy()

    genre_df["genres"] = genre_df["genres"].str.split("|")

    genre_df = genre_df.explode("genres")

    plt.figure(figsize=(12, 6))

    genre_df.boxplot(column="roi", by="genres", rot=45)

    plt.title("ROI Distribution by Genre")

    plt.suptitle("")

    plt.xlabel("Genre")

    plt.ylabel("ROI")

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print(f"Saved figure: {output_path}")


def plot_rating_vs_popularity(df):
    
    output_path = Path("reports/figures/rating_vs_popularity.png")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 6))

    plt.scatter(df["vote_average"], df["popularity"])

    plt.xlabel("Rating")

    plt.ylabel("Popularity")

    plt.title("Popularity vs Rating")

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print(f"Saved figure: {output_path}")


def plot_revenue_by_year(df):

    output_path = Path("reports/figures/revenue_by_year.png")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    yearly_revenue = df.groupby("release_year")["revenue_musd"].sum()

    plt.figure(figsize=(10, 6))

    yearly_revenue.plot(marker="o")

    plt.xlabel("Year")

    plt.ylabel("Revenue (Million USD)")

    plt.title("Yearly Box Office Revenue")

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print(f"Saved figure: {output_path}")


def plot_franchise_comparison(franchise_data):

    output_path = Path("reports/figures/franchise_comparison.png")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    franchise_data[["mean_revenue", "mean_budget"]].plot(kind="bar", figsize=(8, 6))

    plt.title("Franchise vs Standalone")

    plt.ylabel("Million USD")

    plt.xticks([0, 1], ["Standalone", "Franchise"], rotation=0)

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print(f"Saved figure: {output_path}")
