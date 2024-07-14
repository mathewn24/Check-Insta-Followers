import json

with open("followers_1.json") as followers_f:
    followersdata = json.load(followers_f)

with open("following.json") as following_f:
    followingdata = json.load(following_f)["relationships_following"]

not_following_back = []

followers = [f["string_list_data"][0]["value"] for f in followersdata]
following = [f["string_list_data"][0]["value"] for f in followingdata]

for f in following:
    if f not in followers:
        not_following_back.append(f)