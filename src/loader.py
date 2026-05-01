# loader.py
import csv
from src.logic import weights, field_streaming_service, field_show, field_rating, field_imdb_rating, field_rot_rating, field_other_rating, field_recomended


#Load CSV file
def load_shows(filename):
    shows = []
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        #headers = ["network", "show", "rating","imdb_raw", "rot_raw", "other_raw", "is_recommended"]
        #reader.fieldnames = headers
        
        for row in reader:
            #Make sure rating is truly a "float" for multiplicationin rating
            def safe_float(value):
                try:
                    return float(value) if value else 0.0
                except (TypeError, ValueError):
                    return 0.0
                
            network = row.get("network","Unknown network")
            show = row.get("show","Unknown title")
            raw_rating = row.get("rating","")
            imdb_rating = row.get("imdb_raw","")
            rt_rating = row.get("rt_raw","")
            other_rating = row.get("other_raw","")
            recommended = row.get("is_recommended","")
            
            try:
                if raw_rating.strip() == "":
                    rating = 0.0
                else:
                    rating = float(raw_rating)
            except ValueError:
                print(f"Warning: Could not convert a '{raw_rating}' for {show}")
                rating = 0.0
            
            cleaned_show = {
                field_streaming_service: network,
                field_show: show,
                field_rating: safe_float(raw_rating),
                field_imdb_rating: safe_float(imdb_rating),
                field_rot_rating: safe_float(rt_rating),
                field_other_rating: safe_float(other_rating),
                field_recomended: recommended
            }
            shows.append(cleaned_show)
        
    return shows
