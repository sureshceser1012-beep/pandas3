import pandas as pd


def load_sales(path: str) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        parse_dates=["date"]
    )
    df = df.set_index("date")
    return df


def total_revenue(df: pd.DataFrame) -> pd.Series:
    revenue = df["units_sold"] * df["unit_price"]

    return revenue.groupby(df["store_id"]).sum()


def category_pivot(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()

    data["month"] = data.index.to_period("M")

    pivot = pd.pivot_table(
        data,
        index="category",
        columns="month",
        values="units_sold",
        aggfunc="sum",
        fill_value=0
    )

    return pivot.sort_index(axis=1)


# Load sales data
sales = load_sales("sales.csv")

# Total revenue per store
revenue = total_revenue(sales)

# Category-wise monthly units sold
pivot = category_pivot(sales)

print("Sales Data:")
print(sales)

print("\nTotal Revenue:")
print(revenue)

print("\nCategory Pivot:")
print(pivot)