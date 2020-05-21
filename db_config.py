import pymongo
import db_config

myclient = pymongo.MongoClient("mongodb+srv://gering1:GreenCheckeredShirt!@firstcluster-otzmt.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = myclient['firstdb']

#db.test.insert_one({"FirstName": "FooBar", "Lastname": "BarFoo"})
for s in db.test.find():
    print(s)
