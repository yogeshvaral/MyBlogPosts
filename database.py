from pymongo import MongoClient
class Database(object):
    URI = "mongodb://localhost:27017"
    DATABASE = None
    
    def initialise():
        client = MongoClient(Database.URI)
        Database.DATABASE = client['Fullstack']

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert_one(data)
    
    @staticmethod
    def find_one(collection,query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find(collection,query):
        return Database.DATABASE[collection].find(query)