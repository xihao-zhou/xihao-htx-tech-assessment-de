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
            result = count_flights_by_month(flight_df)
            print("\nTotal Number of Flights Each Month\n")
            print(result.to_string(index=False))
            print("\n")
        
        elif choice == "2":
            result = most_frequent_flyers(flight_df, passengers_df)
            print("\nTop 10 Most Frequent Flyers\n")
            print(result.to_string(index=False))
            print("\n")
            
        elif choice == "3":
            result = most_visited_countires_without_sg(flight_df)
            print("\nLongest Run Without SG\n")
            print(result.to_string(index=False))
            print("\n")
            
        elif choice == "4":
            result = flights_together(flight_df)
            print("\nPairs Who Flew Together More Than 2 Times\n")
            print(result.to_string(index=False))
            print("\n")
            
        elif choice == "5":
            try:
                n = input("Enter the minimum number of flights together (>=0): ")
                fd = input("Enter the from date (dd/mm/yyyy): ")
                td = input("Enter the TO date (dd/mm/yyyy): ")
                
                n = int(n)
                result = flights_together(flight_df, at_least_n_times=n, from_date=fd, to_date=td)
                print(f"\nPairs Who Flew Together More Than {n} Time(s) from {fd} to {td}\n")
                print(result.to_string(index=False))
            except Exception as e:
                print(f"\n{e}")
            print("\n")
            
        elif choice == "0" or choice == "End" or choice == "end" or choice == "Stop" or choice == "stop":
            break
            
        else:
            print("\nYou have entered an invalid choice, please choose again.\n")
    
if __name__ == "__main__":
   main()