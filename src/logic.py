# logic.py

#Field names (Constants)
field_streaming_service = "network"
field_show = "show"
field_rating = "rating"
field_imdb_rating = "imdb_raw"
field_rot_rating = "rt_raw"
field_other_rating = "other_raw"
field_recomended = "is_recommended" #binary 1 = yes, null = no

#Scoring weights from internet (adjust as needed)
weights = {
    "weight_imdb" : 0.5,
    "weight_rottenT" : 0.2,
    "weight_other" : 0.3
}

#Multipliers (adjust as needed)
friend_recommendation_multiplier = 1.5
mood_multiplier = 0.7