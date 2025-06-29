import pandas as pd

"""
Function to count total number of flights for each month
Step 1: Create a copy of the flights dataframe to avoid accidental changes to the original data
Step 2: Convert the 'date' column from string to datetime type using the format 'dd/mm/yyyy'
Step 3: Extract the month as a new column 'Month' from the 'date' column
Step 4: Group by 'Month' and count the number of unique 'flight_id' for each month.
Returns a dataframe with columns: Month, Number of Flights
"""
def count_flights_by_month(flight_df):
    df = flight_df.copy()
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    df['Month'] = df['date'].dt.month
    result = df.groupby('Month')['flight_id'].nunique().reset_index(name='Number of Flights')
    return result

"""
Function to get the top 10 most frequent flyers.
Step 1: Count flights for each passenger by grouping by 'passenger_id'.
Step 2: Merge with passengers DataFrame to get names.
Step 3: Sort by 'Number of Flights' (descending), then by 'Passenger ID' (ascending).
Step 4: Select the top 10 rows.
Returns: DataFrame with columns ['Passenger ID', 'Number of Flights', 'First Name', 'Last Name'].
"""
def most_frequent_flyers(flight_df, passengers_df):
    flight_counts = (flight_df.groupby('passenger_id').size().reset_index(name='Number of Flights'))
    merged = pd.merge(flight_counts, passengers_df, on='passenger_id')
    merged_sorted = merged.sort_values(['Number of Flights', 'passenger_id'], ascending=[False, True])
    result =  merged_sorted.head(10)[['passenger_id', 'Number of Flights', 'first_name', 'last_name']]
    result.columns = ['Passenger ID', 'Number of Flights', 'First Name', 'Last Name']
    return result

def most_visited_countires_without_sg(flight_df):
    return

def flights_together(flight_df, flights_tgt=2, from_date=None, to_date=None):
    return