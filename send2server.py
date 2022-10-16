from sqlite3 import paramstyle
from urllib import request
import pymongo
from pymongo import MongoClient

import info_mongodb
import gather

import requests

# Implementar sistema de login
# import login

# interface_uri = info_mongodb.creds  

data = gather.data_gather()

emotion = gather.data_gather()

client = MongoClient(info_mongodb.creds)


def send():
    db = client.umirror
    collection = db.emotions
    post_id = collection.insert_one(data).inserted_id

    params = {"id": post_id,
              "Avg": gather.data_gather()["Avg"]
              }

    print(f"[+]Post ID: {post_id}")


    # info = requests.post(interface_uri,params)
    # print(f"[+]Dados enviados para a interface: {info}\n")    # print(f"[+]ID unico: {}")


