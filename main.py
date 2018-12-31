# coding: utf-8
from user_fav_dataset import user_fav_dataset
from math import sqrt

# Calc similarity score using jaccard exp.
def similarity_score(person1, person2):
    both_viewed = {}  # 双方に共通のアイテムを取得

    if len(user_fav_dataset[person1]["favs"]) == 0:
        return 0

    if len(user_fav_dataset[person2]["favs"]) == 0:
        return 0

    for item in user_fav_dataset[person1]["favs"]:
        if item in user_fav_dataset[person2]["favs"]:
            both_viewed[item] = 1

    if len(both_viewed) == 0:
        return 0

    # Get jaccard exp
    favs_1 = user_fav_dataset[person1]["favs"]
    favs_2 = user_fav_dataset[person2]["favs"]
    set_e1 = set(favs_1)
    set_e2 = set(favs_2)
    return round(float(len(set_e1 & set_e2)) / float(len(set_e1 | set_e2)), 3)

def getSimilarUsers(target_user_idx, fetchCount):
    i = 0
    userSimilardata = {
        "target_user_idx": target_user_idx,
        "target_user_twitter_id": user_fav_dataset[target_user_idx]["twitter_id"],
        "target_user_screen_name": user_fav_dataset[target_user_idx]["screen_name"],
        "similar_users": []
    }
    similarUsers = []

    while i < len(user_fav_dataset):
        score = similarity_score(target_user_idx, i)
        if score > 0 and target_user_idx != i:
            user = { "score": score, "user_id": i }
            similarUsers.append(user)
        i += 1

    similarUsers.sort(key=lambda x: x["score"], reverse=True)
    userSimilardata["similar_users"] = similarUsers[0:fetchCount]
    return userSimilardata

# 663, 643, 619, 616, 659
i = 0

similar_users = []
while i < len(user_fav_dataset):
    similar_users = getSimilarUsers(i, 3)
    if len(similar_users["similar_users"]) <= 0:
        i += 1
        continue

    similar_users.append(similar_users)
    i += 1

for v in similar_users:
    print(v)