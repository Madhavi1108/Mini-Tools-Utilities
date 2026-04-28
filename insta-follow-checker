import json

# Load followers
with open("file_name", "r", encoding="utf-8") as f:
    followers_data = json.load(f)

followers = []

for i in followers_data:
    name = i["string_list_data"][0]["value"]
    followers.append(name)

# Load following
with open("following.json", "r", encoding="utf-8") as f:
    following_data = json.load(f)

following = []

for i in following_data["relationships_following"]:
    name = i["string_list_data"][0]["value"]
    following.append(name)

# People you follow but they don't follow back
not_following_back = []

for name in following:
    if name not in followers:
        not_following_back.append(name)

# People who follow you but you don't follow back
you_dont_follow_back = []

for name in followers:
    if name not in following:
        you_dont_follow_back.append(name)

print("\n--- Not Following You Back ---")
for i in not_following_back:
    print(i)

print("\n--- You Don't Follow Back ---")
for i in you_dont_follow_back:
    print(i)
