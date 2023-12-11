# Import the pandas library
import pandas as pd

# Read the GED dataset from a CSV file
ged = pd.read_csv("./data/GEDEvent_v23_1.csv")

# Filter the GED dataset for events from the year 2018 onwards
ged = ged[ged["year"] >= 2018]

# Display the shape and column names of the filtered GED dataset
ged.shape
ged.columns

# Rename specific countries in the GED dataset
ged.replace(
    {
        "Central African Republic": "CAR",
        "Yemen (North Yemen)": "Yemen",
        "DR Congo (Zaire)": "DRC",
        "Madagascar (Malagasy)": "Madagascar",
        "United States of America": "USA",
        "Guinea": "Equatorial Guinea",
        "Kingdom of eSwatini (Swaziland)": "Swaziland",
    },
    inplace=True,
)

# Read the SHCC dataset from a CSV file
shcc = pd.read_csv("./combined_shcc_incidents_data_no20.csv")

# Rename specific countries in the SHCC dataset
shcc.replace(
    {
        "OPT": "Israel",
        "oPt": "Israel",
        "Myanmar": "Myanmar (Burma)",
        "Myanmar ": "Myanmar (Burma)",
        "The Philippines": "Philippines",
    },
    inplace=True,
)

# Convert the 'Attack date' column to datetime format in the SHCC dataset
shcc["Attack date"] = pd.to_datetime(shcc["Attack date"])

# Extract the 'Year' and 'Week' information from the 'Attack date' in the SHCC dataset
shcc["Week"] = shcc["Attack date"].dt.isocalendar().week
shcc["Year"] = shcc["Attack date"].dt.year

# Aggregate data in the SHCC dataset based on year, week, and country
aggregated_shcc = (
    shcc.groupby(["Year", "Week", "Country"])
    .agg(
        {
            "Total number of attacks on facilities which reported damage": "sum",
            "Total health worker killed": "sum",
            "Health transportation destroyed": "sum",
            "Total health worker arrested ": "sum",
            "Health transportation damaged": "sum",
            "Health transportation stolen/highjacked": "sum",
            "Total health worker kidnapped": "sum",
            "Total health worker injured": "sum",
            "Total number of attacks on facilities which reported destruction": "sum",
        }
    )
    .reset_index()
)

# Convert date columns to datetime format in the GED dataset
ged["date_start"] = pd.to_datetime(ged["date_start"])
ged["date_end"] = pd.to_datetime(ged["date_end"])

# Calculate the average date between 'date_start' and 'date_end' in the GED dataset
ged["date_average"] = ged.apply(
    lambda row: row["date_start"] + (row["date_end"] - row["date_start"]) / 2, axis=1
)

# Extract 'Year' and 'Week' information from the average date in the GED dataset
ged["Year"] = ged["date_average"].dt.year
ged["Week"] = ged["date_average"].dt.isocalendar().week

# Create a new column with a list of dictionaries for each row in the GED dataset
ged["grouped_rows"] = ged.apply(lambda row: dict(row), axis=1)

# Group by 'country', 'Year', and 'Week' in the GED dataset and aggregate the 'grouped_rows' column
grouped_ged = ged.groupby(["country", "Year", "Week"], as_index=False)[
    "grouped_rows"
].agg(list)

# Merge the aggregated SHCC and grouped GED datasets based on 'Country', 'Year', and 'Week'
merged_df = pd.merge(
    aggregated_shcc,
    grouped_ged,
    left_on=["Country", "Year", "Week"],
    right_on=["country", "Year", "Week"],
    how="left",
)

# Drop rows with null values in the merged dataset
merged_df.dropna(inplace=True)

# Write the merged dataset to an Excel file named 'shcc_ged_merged.xlsx'
merged_df.to_excel("shcc_ged_merged.xlsx", index=False)
