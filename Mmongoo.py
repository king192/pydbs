# -*- coding:utf-8 -*-
import pymongo

class Mongoo:
    MongoClient = ''
    db = ''
    table = ''
    def __init__(self, db):
        self.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.MongoClient[db]
        self.table = self.db["sites"]
    def __close__(self):
        self.db.close()
    def getApp(self):
    	return self.table

#m = Mongoo()
