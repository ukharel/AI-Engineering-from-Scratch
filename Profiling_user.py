# First Principle: Profiling via Vector Addition
user_profile = [0.0, 0.0] # [Action, Romance]

movie_1 = [1.0, 0.1] # High Action
movie_2 = [0.9, 0.2] # High Action
movie_3 = [0.1, 1.0] # High Romance (User HATED this, 1 star)

# Building the profile
user_profile = [user_profile[0] + movie_1[0], user_profile[1] + movie_1[1]]
user_profile = [user_profile[0] + movie_2[0], user_profile[1] + movie_2[1]]

# Apply a negative scalar for the hated movie
penalty = -1.0
user_profile = [
    user_profile[0] + (movie_3[0] * penalty), 
    user_profile[1] + (movie_3[1] * penalty)
]

print(f"Final User Profile Vector: {user_profile}")
# The profile stayed in Action and retreated from Romance!