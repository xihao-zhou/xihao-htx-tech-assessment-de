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

"""
Function to compute, for each passenger, the longest run of consecutive flights without being in SG.
Step 1: Create a copy of the flights dataframe to avoid accidental changes to the original data
Step 2: For each passenger, sort flights by date.
Step 3: Genrate a list of countires the passenger has been to starting with the "from" column of the first flight data and "to" column of all flights
Step 3: Iterate through list of countires, incrementing a counter when not SG.
Step 4: Reset the counter when SG is encountered; track the max run.
Returns: DataFrame with columns ['Passenger ID', 'Longest Run'].
"""
def most_visited_countires_without_sg(flight_df):
    
    df = flight_df.copy()
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    
    result = []
    for pid, group in df.sort_values('date').groupby('passenger_id'):
        dest_seq = group['to'].tolist()
        dest_seq.insert(0, group['from'].iloc[0])
        max_run, current_run = 0, 0
        for dest in dest_seq:
            if dest.lower() != 'sg':
                current_run += 1
            else:
                max_run = max(max_run, current_run)
                current_run = 0
        max_run = max(max_run, current_run)
        result.append({'Passenger ID': pid, 'Longest Run': max_run})
    return pd.DataFrame(result)

def flights_together(flight_df, flights_tgt=2, from_date=None, to_date=None):
    return