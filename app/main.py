import os
import pandas as pd
from analysis import count_flights_by_month, most_frequent_flyers, most_visited_countires_without_sg, flights_together

def main():
    # Set up path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    flight_csv = os.path.join(base_dir, "data", "flightData.csv")
    passengers_csv = os.path.join(base_dir, "data", "passengers.csv")
    
    # Load data
    flight_df = pd.read_csv(flight_csv)
    passengers_df = pd.read_csv(passengers_csv)
    
    while True:
        print("1. Question 1: Total Number of Flights Each Month")
        print("2. Question 2: Top 10 Most Frequent Flyers")
        print("3. Question 3: Longest Run Without SG")
        print("4. Question 4: Pairs Who Flew Together More Than 2 Times")
        print("5. Question 4 (With Bonus): Pairs Who Flew Together More Than 2 Times in Date Range")
        print("0. End app.")
        choice = input("Please enter your choice: ")
    
        if choice == "1":
            print("\nTotal Number of Flights Each Month\n")
            print(count_flights_by_month(flight_df).to_string(index=False))
            print("\n")
        
        elif choice == "2":
            print("\nTop 10 Most Frequent Flyers\n")
            print(most_frequent_flyers(flight_df, passengers_df).to_string(index=False))
            print("\n")
            
        elif choice == "3":
            print("\nLongest Run Without SG\n")
            print(most_visited_countires_without_sg(flight_df).to_string(index=False))
            print("\n")
            
        elif choice == "4":
            print("\nPairs Who Flew Together More Than 2 Times\n")
            print(flights_together(flight_df).to_string(index=False))
            print("\n")
            
        elif choice == "5":
            print("\nPairs Who Flew Together More Than 2 Times in Date Range\n")
            print(flights_together(flight_df).to_string(index=False))
            print("\n")
            
        elif choice == "0" or choice == "End" or choice == "end" or choice == "Stop" or choice == "stop":
            break
            
        else:
            print("\nYou have entered an invalid choice, please choose again.\n")
    
if __name__ == "__main__":
   main()