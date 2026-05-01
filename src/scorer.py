# scorer.py
from src.logic import weights, field_streaming_service, field_show, field_rating, field_imdb_rating, field_rot_rating, field_other_rating, field_recomended, friend_recommendation_multiplier

#Logic for weighted average of shows that have broken out ratings
def calculate_base_rating(show, weights):
    #Initialize variables so if statement works
    imdb_rating = 0
    rt_rating = 0
    other_rating = 0
    
    if show[field_imdb_rating] is not None and show[field_imdb_rating] > 0 :
        imdb_rating = show.get(field_imdb_rating, 0) * weights["weight_imdb"]
    if show[field_rot_rating] is not None and show[field_rot_rating] > 0 :
        rt_rating = show.get(field_rot_rating, 0) * weights["weight_rottenT"]
    if show[field_other_rating] is not None and show[field_other_rating] > 0 :
        other_rating = show.get(field_other_rating, 0) * weights["weight_other"]

    return imdb_rating + rt_rating + other_rating

#Default logic to revert back to base average of dataset rating if no broken out rating by site
def get_final_score(show, weights):
    quality = show.get(field_rating, 0)
        
    #Check if broken out score exists and use weighted average or use manual base rating
    if show.get(field_imdb_rating, 0) > 0 and show.get(field_rot_rating, 0) > 0 and show.get(field_other_rating, 0):
        quality = calculate_base_rating(show, weights) * 100
    else:
        quality = show.get(field_rating, 0)
    
    #Recommendation multiplier if file has value in recommendation it will use multiplier
    is_recommended = show.get("is_recommended")
    rec_rating = quality
    if is_recommended == 1 or is_recommended == "1":
        rec_rating *= friend_recommendation_multiplier
    
    return quality, rec_rating