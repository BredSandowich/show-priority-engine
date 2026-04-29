# scorer.py
import logic

#Logic for weighted average of shows that have broken out ratings
def calculate_base_rating(show, weights):
    #Initialize variables so if statement works
    imdb_rating = 0
    rt_rating = 0
    other_rating = 0
    
    if show[field_imdb] is not None and show[field_imdb] > 0 :
        imdb_rating = show.get(field_imdb, 0) * weight_imdb
    if show[field_rot] is not None and show[field_rot] > 0 :
        rt_rating = show.get(field_rot, 0) * weight_rottenT
    if show[field_other_rating] is not None and show[field_other_rating] > 0 :
        other_rating = show.get(field_other_rating, 0) * other_rating
        
    return imdb_rating + rt_rating + other_rating

#Default logic to revert back to base average of dataset rating if no broken out rating by site
def get_final_score(show, weights):
    #Check if broken out score exists and use weighted average or use manual base rating
    if show.get(field_imdb, 0) > 0 :
        base_rating = calculate_base_rating(show, weights)
    else:
        base_rating = show.get(field_rating,0)
    
    #Recommendation multiplier if file has value in recommendation it will use multiplier
    is_recommended = show.get("is_recommended")
    if is_recommended == 1 or is_recommended == "1":
        base_rating *= 1.5
    
    return base_rating