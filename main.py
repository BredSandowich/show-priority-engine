# main.py
import csv
import os

base_dir = os.path.dirname(__file__) #This file's directory
csv_path = os.path.join(base_dir, "data", "shows.csv")



def load_shows(filename):
    shows = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_rating = row.get("rating","")
            try:
                if raw_rating.strip() == "":
                    rating = 0.0
                else:
                    rating = float(raw_rating)
            except ValueError:
                print(f"Warning: Could not convert a '{raw_rating}'")
                rating = 0.0
            
            show = {
                "streaming_service": row.get("\ufeffnetwork"),
                "show": row.get("show"),
                "rating": raw_rating
            }
            shows.append(row)
    return shows


def main():
    data = load_shows(csv_path)
    print(f"Loaded {len(data)} shows from your list!")
    
    print("--- Welcome to the Show watch priority engine ---")
    
    if data:
        print(data[0])
    

if __name__ == "__main__":
    main()