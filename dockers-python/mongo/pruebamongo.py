from pymongo import MongoClient

client = MongoClient("mongodb://jbermejo:miclavesecreta@127.0.0.1:27017")
db = client.admin

def mongo_test():

    try:
        db.command("serverStatus")
    except:
        return False
    else:
        return True

if __name__ == '__main__':
    print(mongo_test())
    client.close()