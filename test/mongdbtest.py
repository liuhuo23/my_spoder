import pymongo
import requests
# client = pymongo.MongoClient('mongodb://localhost:27017')
#
# mydb = client.list_database_names()
# print(mydb)
# mydouban = client['douban']
# print(client.list_database_names())
# print(mydouban.list_collection_names())
# mycol = mydouban['book']
# mycol.insert_one({'age':12, 'name':'hello'})
# print(mydouban.list_collection_names())
# resourt = requests.get('https://www.zibu123.com/vodshow/6-----------.html')
# print(resourt.text)
import gridfs
from bson import ObjectId
client = pymongo.MongoClient('localhost', connect=False)
db = client['demo']
def save_file_to_mongo(content):
    with open(content, 'rb') as f:
        data = f.read()
        fs = gridfs.GridFS(db, 'img')
        return fs.put(data)


print(save_file_to_mongo('img.jpg'))