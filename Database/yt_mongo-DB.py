from pymongo import MongoClient

client = MongoClient("mongodb+srv://youtubepy:8uB70x3OkHNijrrh@cluster0.6utrmw5.mongodb.net/ytmanager")



db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)