import matplotlib.pyplot as plt


def plot_budget_vs_revenue(df):

    plt.figure(figsize=(8, 6))

    plt.scatter(df["budget_musd"], df["revenue_musd"])

    plt.xlabel("Budget (Million USD)")

    plt.ylabel("Revenue (Million USD)")

    plt.title("Revenue vs Budget")

    plt.show()


def plot_roi_by_genre(df):

    genre_df = df[["genres", "roi"]].copy()

    genre_df["genres"] = genre_df["genres"].str.split("|")

    genre_df = genre_df.explode("genres")

    plt.figure(figsize=(12, 6))

    genre_df.boxplot(column="roi", by="genres", rot=45)

    plt.title("ROI Distribution by Genre")

    plt.suptitle("")

    plt.xlabel("Genre")

    plt.ylabel("ROI")

    plt.show()


def plot_rating_vs_popularity(df):

    plt.figure(figsize=(8, 6))

    plt.scatter(df["vote_average"], df["popularity"])

    plt.xlabel("Rating")

    plt.ylabel("Popularity")

    plt.title("Popularity vs Rating")

    plt.show()


def plot_revenue_by_year(df):

    yearly_revenue = df.groupby("release_year")["revenue_musd"].sum()

    plt.figure(figsize=(10, 6))

    yearly_revenue.plot(marker="o")

    plt.xlabel("Year")

    plt.ylabel("Revenue (Million USD)")

    plt.title("Yearly Box Office Revenue")

    plt.show()


def plot_franchise_comparison(franchise_data):

    franchise_data[["mean_revenue", "mean_budget"]].plot(kind="bar", figsize=(8, 6))

    plt.title("Franchise vs Standalone")

    plt.ylabel("Million USD")

    plt.xticks([0, 1], ["Standalone", "Franchise"], rotation=0)

    plt.show()
