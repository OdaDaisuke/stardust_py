# coding: utf-8
import analytics
from favs import user_fav_dataset
from favs import lyric_faved_users_dataset

def getUserBasedFilteringData():
    i = 0
    users = []

    while i < len(user_fav_dataset):
        rankingRange = 3
        similar_users = analytics.getSimilarUsers(i, rankingRange)
        i += 1

        if len(similar_users["similar_users"]) <= 0:
            continue

        users.append(similar_users)
    return users

def getLyricBasedFilteringData():
    i = 0
    users = []

    while i < len(lyric_faved_users_dataset):
        rankingRange = 3
        similar_lyrics = analytics.getSimilarLyrics(i, rankingRange)
        i += 1

        if len(similar_lyrics["similar_lyrics"]) <= 0:
            continue

        users.append(similar_lyrics)
    return users

for v in getUserBasedFilteringData():
    print v
