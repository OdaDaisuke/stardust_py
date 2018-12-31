# coding: utf-8
import pandas as pd
import csv

user_fav_dataset = []
lyric_faved_users_dataset = []

def readCSV(fileSrc):
    file = open(fileSrc, "r")
    return csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

favs = readCSV("./data/favs.csv")
users = readCSV("./data/users.csv")
next(users)
next(favs)

favs = list(favs)
users = list(users)

for row in users:
    twitter_id = row[5]
    screen_name = row[12]
    user_favs = {
        "twitter_id": twitter_id,
        "screen_name": screen_name,
        "favs": [],
    }

    for row_fav in favs:
        if row_fav[4] == twitter_id:
            user_favs["favs"].append(row_fav[5])

    user_fav_dataset.append(user_favs)

scannedList = []
for row in favs:
    scanned = False
    lyric_id = row[5]
    fav_id = row[0]
    fav_data = {
        "lyric_id": lyric_id,
        "fav_id": fav_id,
        "faved_users": [],
    }

    for v in scannedList:
        if v == lyric_id:
            scanned = True

    if scanned == False:

        for row_fav in favs:
            if fav_id == row_fav[0]:
                break

            if lyric_id == row_fav[5]:
                fav_data["faved_users"].append(row_fav[4])

        scannedList.append(lyric_id)

        lyric_faved_users_dataset.append(fav_data)


# for v in lyric_faved_users_dataset:
    # print v