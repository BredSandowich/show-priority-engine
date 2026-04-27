# main.py
import os
from src.loader import load_shows

base_dir = os.path.dirname(__file__) #This file's directory
csv_path = os.path.join(base_dir, "data", "shows.csv") #CSV file


#Make sure rating is truly a "float"
def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def main():
    data = load_shows(csv_path)
    print(f"Loaded {len(data)} shows from your list!")
    
    print("--- Welcome to the Show watch priority engine ---")
    
    #if data:
    #    print(data[0])
        
    for show in data:
        print(show)
        print(type(show))
        break


if __name__ == "__main__":
    main()