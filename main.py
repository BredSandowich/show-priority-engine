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
    #Remove faulty load of first row in CSV if loaded with wrong UTF
    if data and data[0]["show"] == "show":
        data.pop(0)
        
    print(f"Loaded {len(data)} shows from your list!")
    print("--- Welcome to the Show watch priority engine ---")
    
    #User input
    target_streaming_prompt = input("Enter streaming service to filter or press 'Enter' for all:").strip()
    
    if target_streaming_prompt:
        filtered_data = [show for show in data if show["network"].lower() == target_streaming_prompt.lower()]
    else:
        filtered_data = data
    
    print(filtered_data[0])

if __name__ == "__main__":
    main()