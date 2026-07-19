def rank_movies(df, by, ascending=False, n=10, min_budget=None, min_votes=None):
    """
    Return top/bottom movies based on a selected metric.
    """

    data = df.copy()

    # Filter by minimum budget if required
    if min_budget is not None:
        data = data[data["budget_musd"] >= min_budget]

    # Filter by minimum votes if required
    if min_votes is not None:
        data = data[data["vote_count"] >= min_votes]

    # Sort movies
    result = data.sort_values(by=by, ascending=ascending).head(n)

    return result[["title", by]]


def movie_rankings(df):
    return {
        "highest_revenue": rank_movies(df, "revenue_musd"),
        "highest_budget": rank_movies(df, "budget_musd"),
        "highest_profit": rank_movies(df, "profit_musd"),
        "highest_rated": rank_movies(df, "vote_average", min_votes=10),
    }


def franchise_comparison(df):

    comparison = df.groupby("is_franchise").agg(
        mean_revenue=("revenue_musd", "mean"),
        median_roi=("roi", "median"),
        mean_budget=("budget_musd", "mean"),
        mean_popularity=("popularity", "mean"),
        mean_rating=("vote_average", "mean"),
    )

    return comparison


def franchise_statistics(df):

    franchise_df = df[df["is_franchise"]]

    statistics = (
        franchise_df.groupby("belongs_to_collection")
        .agg(
            num_movies=("id", "count"),
            total_budget=("budget_musd", "sum"),
            mean_budget=("budget_musd", "mean"),
            total_revenue=("revenue_musd", "sum"),
            mean_revenue=("revenue_musd", "mean"),
            mean_rating=("vote_average", "mean"),
        )
        .sort_values("total_revenue", ascending=False)
    )

    return statistics


def director_statistics(df):

    statistics = (
        df.groupby("director")
        .agg(
            num_movies=("id", "count"),
            total_revenue=("revenue_musd", "sum"),
            mean_rating=("vote_average", "mean"),
        )
        .sort_values("total_revenue", ascending=False)
    )

    return statistics


def find_movies_by_actor(df, actor_name):

    result = df[
        df["cast"].apply(
            lambda cast_list: any(actor["name"] == actor_name for actor in cast_list)
        )
    ]

    return result[["title", "genres", "vote_average"]]
