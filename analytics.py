# coding: utf-8
from favs import user_fav_dataset
from favs import lyric_faved_users_dataset
from math import sqrt

# Calc similarity score using jaccard exp.
def similarity_score(item_key, target1, target2):
    both_viewed = {}  # 双方に共通のアイテムを取得

    if len(user_fav_dataset[target1][item_key]) == 0:
        return 0

    if len(user_fav_dataset[target2][item_key]) == 0:
        return 0

    for item in user_fav_dataset[target1][item_key]:
        if item in user_fav_dataset[target2][item_key]:
            both_viewed[item] = 1

    if len(both_viewed) == 0:
        return 0

    # Get jaccard exp
    set_e1 = set(user_fav_dataset[target1][item_key])
    set_e2 = set(user_fav_dataset[target2][item_key])
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
        score = similarity_score("favs", target_user_idx, i)
        if score > 0 and target_user_idx != i:
            user = { "score": score, "user_id": i }
            similarUsers.append(user)
        i += 1

    similarUsers.sort(key=lambda x: x["score"], reverse=True)
    userSimilardata["similar_users"] = similarUsers[0:fetchCount]
    return userSimilardata

def getSimilarLyrics(target_fav_idx, fetchCount):
    i = 0
    lyricSimilardata = {
        "target_fav_idx": target_fav_idx,
        "target_lyric_id": lyric_faved_users_dataset[target_fav_idx]["lyric_id"],
        "similar_lyrics": []
    }
    similarLyrics = []

    while i < len(lyric_faved_users_dataset):
        score = similarity_score("faved_users", target_fav_idx, i)
        if score > 0 and target_fav_idx != i:
            lyric = { "score": score, "fav_idx": i }
            similarLyrics.append(lyric)
        i += 1

    similarLyrics.sort(key=lambda x: x["score"], reverse=True)
    lyricSimilardata["similar_lyrics"] = similarLyrics[0:fetchCount]
    return lyricSimilardata
