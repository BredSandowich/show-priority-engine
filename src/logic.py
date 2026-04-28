# logic.py

#Field names (Constants)
field_network = "network"
field_show = "show"
field_rating = "rating"
field_imdb = "imdb_rating"
field_rot = "rot_rating"
field_other_rating = "other_rating"
field_recomended = "recommended" #binary 1 = yes, null = no


#Scoring weights from internet (adjust as needed)
weight_imdb = 0.5
weight_rottenT = 0.3
weight_other = 0.2

#Multipliers (adjust as needed)
friend_recommendation_multiplier = 2
mood_multiplier = 0.7