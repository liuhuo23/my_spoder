import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

mydb = client.list_database_names()
print(mydb)
mydouban = client['douban']
print(client.list_database_names())
print(mydouban.list_collection_names())
mycol = mydouban['book']
mycol.insert_one({'age':12, 'name':'hello'})
print(mydouban.list_collection_names())
