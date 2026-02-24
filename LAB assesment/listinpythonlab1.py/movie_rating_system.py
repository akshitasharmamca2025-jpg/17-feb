# List of movie ratings (some may be invalid)
ratings = [5, 4, 3, 6, 2, 5, -1, 4, 1, 5]

# Step 1: Remove invalid ratings (valid ratings are between 1 and 5)
valid_ratings = []
for r in ratings:
    if 1 <= r <= 5:
        valid_ratings.append(r)

# Step 2: Find average rating
if len(valid_ratings) > 0:
    average_rating = sum(valid_ratings) / len(valid_ratings)
else:
    average_rating = 0

# Step 3: Count number of 5-star ratings
five_star_count = 0
for r in valid_ratings:
    if r == 5:
        five_star_count += 1

# Step 4: Sort ratings in ascending order
valid_ratings.sort()

# Display results
print("Valid Ratings:", valid_ratings)
print("Average Rating:", round(average_rating, 2))
print("Number of 5-Star Ratings:", five_star_count)