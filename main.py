# main.py
import os
from src.loader import load_shows
from src.scorer import get_final_score
from src.logic import weights, field_streaming_service, field_show, field_rating, field_imdb_rating, field_rot_rating, field_other_rating, field_recomended

base_dir = os.path.dirname(__file__) #This file's directory
csv_path = os.path.join(base_dir, "data", "shows.csv") #CSV file

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
    
    if not filtered_data:
        print(f"Dang outta luck, couldn't find any shows on '{target_streaming_prompt}'.")
        return 
    
    #Calculate score
    for show in filtered_data:
        quality, rec_rating = get_final_score(show, weights)
        show["quality"] = quality
        show["rec_rating"] = rec_rating
        
    #Sort and display result
    filtered_data.sort(key=lambda x: show["rec_rating"], reverse=True)
    
    print(f'The top 4 recommendations for you are: ')
    for show in filtered_data[:4]:
        recommended_tag = "recommended!" if show.get("is_recommended") == 1 else ""
        print(f'\n{show["show"]} {recommended_tag} (Rating: {show["quality"]:.2f} Score: {show["rec_rating"]:.2f})')

if __name__ == "__main__":
    main()