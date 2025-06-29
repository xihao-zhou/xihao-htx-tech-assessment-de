import pandas as pd

"""
Function to count total number of flights for each month
Step 1: Create a copy of the flights dataframe to avoid accidental changes to the original data
Step 2: Convert the 'date' column from string to datetime type using the format 'dd/mm/yyyy'
Step 3: Extract the month as a new column 'Month' from the 'date' column
Step 4: Group by 'Month' and count the number of rows (flights) for each month
Returns a dataframe with columns: Month, Number of Flights
"""
def count_flights_by_month(flight_df):
    df = flight_df.copy()
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    df['Month'] = df['date'].dt.month
    flights_per_month = df.groupby('Month').size().reset_index(name='Number of Flights')
    
    return flights_per_month

def most_frequent_flyers(flight_df, passengers_df):
    return

def most_visited_countires_without_sg(flight_df):
    return

def flights_together(flight_df, flights_tgt=2, from_date=None, to_date=None):
    return