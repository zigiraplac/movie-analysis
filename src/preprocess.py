import pandas as pd

def get_collection_name(x):
    if isinstance(x, dict):
        return x.get("name")

    return "Standalone Movie"


def join_names(x, key="name"):
    if isinstance(x, list):
        values = [d[key] for d in x if isinstance(d, dict) and key in d]

        return "|".join(values)

    return None


def flatten_tmdb_fields(df):

    df["belongs_to_collection"] = df["belongs_to_collection"].apply(get_collection_name)

    df["genres"] = df["genres"].apply(join_names)

    df["spoken_languages"] = df["spoken_languages"].apply(
        lambda x: join_names(x, key="english_name")
    )

    df["production_countries"] = df["production_countries"].apply(join_names)

    df["production_companies"] = df["production_companies"].apply(join_names)

    return df


def clean_data(df):

    # remove duplicate movies

    df = df.drop_duplicates(subset=["id"])

    # convert numeric columns

    numeric_columns = [
        "budget",
        "revenue",
        "runtime",
        "vote_average",
        "vote_count",
        "popularity",
    ]

    for col in numeric_columns:

        if col in df.columns:

            df[col] = pd.to_numeric(df[col], errors="coerce")

    # zero usually means unknown

    for col in ["budget", "revenue", "runtime"]:

        df[col] = df[col].replace(0, pd.NA)

    # ratings without votes are meaningless

    df.loc[df["vote_count"] == 0, "vote_average"] = pd.NA

    # remove invalid records

    df = df.dropna(subset=["id", "title"])

    return df


def create_features(df):

    # million dollar conversion

    df["budget_musd"] = df["budget"] / 1_000_000

    df["revenue_musd"] = df["revenue"] / 1_000_000

    # profit

    df["profit_musd"] = df["revenue_musd"] - df["budget_musd"]

    # ROI

    df["roi"] = df["profit_musd"] / df["budget_musd"]

    # franchise

    df["is_franchise"] = df["belongs_to_collection"].notna()

    # release year

    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

    df["release_year"] = df["release_date"].dt.year

    return df


def preprocess_pipeline(df):

    df = flatten_tmdb_fields(df)

    df = clean_data(df)

    df = create_features(df)

    return df
