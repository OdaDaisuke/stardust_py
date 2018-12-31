# coding: utf-8
import pandas as pd
import csv

def readCSV(fileSrc):
    file = open(fileSrc, "r")
    return csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

files = {
    "favs": readCSV("./data/favs.csv"),
    "lyrics": readCSV("./data/lyrics.csv"),
    "users": readCSV("./data/users.csv")
}

user_fav_dataset = []

next(files["users"])
next(files["favs"])

favs = list(files["favs"])
users = list(files["users"])

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

for v in user_fav_dataset:
    print(v)