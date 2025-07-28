from pymongo import MongoClient




db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)