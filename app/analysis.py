import pandas as pd
from itertools import combinations
from datetime import datetime

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

"""
Function to find all pairs of passengers who have shared more than a given number of flights.
Step 1: Validate user inputs:
        - at_least_n_times must be an integer >= 0.
        - from_date and to_date, if provided, must be valid dates in 'dd/mm/yyyy' format and from_date <= to_date.
Step 2: Create a copy of the flights dataframe to avoid accidental changes to the original data
Step 3: If date range is specified, filter flights within that period.
Step 4: For each flight, get the list of passengers and count all unique pairs.
Step 5: Aggregate counts for each pair across all flights.
Step 6: Return pairs where count > at_least_n_times (default 2).
Returns: DataFrame with columns ['Passenger 1 ID', 'Passenger 2 ID', 'Number of flights together'].
If date range provided, also includes ['From', 'To'].
"""
def flights_together(flight_df, at_least_n_times=2, from_date=None, to_date=None):
    if  type(at_least_n_times) != int or at_least_n_times < 0:
        raise ValueError("You have entered an invalid number. 'at_least_n_times' must be an integer >= 0.")
    
    date_format = "%d/%m/%Y"
    parsed_from_date, parsed_to_date = None, None
    if from_date or to_date:
        try:
            if from_date:
                parsed_from_date = datetime.strptime(from_date, date_format)
            if to_date:
                parsed_to_date = datetime.strptime(to_date, date_format)
            if parsed_from_date and parsed_to_date and parsed_from_date > parsed_to_date:
                raise ValueError("You have entered an invalid date. 'from_date' must be earlier than or equal to 'to_date'.")
        except ValueError:
            raise ValueError("You have entered an invalid date. Both 'from_date' and 'to_date' must be in 'dd/mm/yyyy' format (e.g. 31/01/2025).")
    
    df = flight_df.copy()
    
    if parsed_from_date and parsed_to_date:
        df['date'] = pd.to_datetime(df['date'], format=date_format)
        df = df[(df['date'] >= parsed_from_date) & (df['date'] <= parsed_to_date)]
    
    flights = df.groupby('flight_id')['passenger_id'].apply(list)
    pair_counts = {}
    
    for passenger_list in flights:
        for p1, p2 in combinations(sorted(passenger_list), 2):
            pair = (p1, p2)
            pair_counts[pair] = pair_counts.get(pair, 0) + 1
    
    result = []
    
    for (p1, p2), count in pair_counts.items():
        if count > at_least_n_times:
            entry = {
                'Passenger 1 ID': p1,
                'Passenger 2 ID': p2,
                'Number of flights together': count
            }
            if from_date and to_date:
                entry['From'] = from_date
                entry['To'] = to_date
            result.append(entry)
    
    return pd.DataFrame(result)