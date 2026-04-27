# loader.py
import csv

#Load CSV file
def load_shows(filename):
    shows = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = ["network", "show", "rating"]
        reader.fieldnames = headers
        
        for row in reader:
            network = row.get("network","Unknown network")
            show = row.get("show","Unknown title")
            raw_rating = row.get("rating","")
            
            try:
                if raw_rating.strip() == "":
                    rating = 0.0
                else:
                    rating = float(raw_rating)
            except ValueError:
                print(f"Warning: Could not convert a '{raw_rating}' for {show}")
                rating = 0.0
            
            show = {
                "streaming_service": network,
                "show": show,
                "rating": raw_rating
            }
            shows.append(row)
    return shows
