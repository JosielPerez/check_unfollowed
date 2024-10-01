import json

# Function to check if a user is following another user
with open('connections/followers_and_following/followers_1.json', 'r') as file:
    data_followers = json.load(file)

with open('connections/followers_and_following/following.json', 'r') as file:
    data_following = json.load(file)


followers = []
following = []

for item in data_followers:
    if "string_list_data" in item and item["string_list_data"]:
        # Loop through each entry in 'string_list_data'
        for string_item in item["string_list_data"]:
            followers.append(string_item["value"])


for item in data_following["relationships_following"]:
    if "string_list_data" in item and item["string_list_data"]:
        # Loop through each entry in 'string_list_data'
        for string_item in item["string_list_data"]:
            following.append(string_item["value"])

# Check if users in following are following you
unfollow = []
for user in following:
    if user not in followers:
        unfollow.append(user)

# Prints the users that are not following you
print(f" People who don't follow you back {unfollow}")