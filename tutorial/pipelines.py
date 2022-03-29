# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter


class TutorialPipeline:
    def process_item(self, item, spider):
        return item


#import string
#import re

#from sys import path
#path.append('/nimble/shared/modules')

#import pymongo
#from scrapy import settings
#from scrapy.exceptions import DropItem
#from termcolor import colored
#from scrapy import log

#import bingwriter as bbw

#class MongoDBPipeline(object):

 #   def __init__(self):
  #      connection = pymongo.MongoClient('mongodb://localhost', 27017)
   #     db = connection['webscraping']
        #print(db)
    #    self.collection = db['raw']

    #def process_item(self, item, spider):
     #   print("here")
      #  valid = True
       # for data in item:
        #    if not data:
         #       valid = False
          #      raise DropItem("Missing {0}!".format(data))
        #if valid:
         #   self.collection.insert(dict(item))
            #log.msg("Question added to MongoDB database!",
                    #level=log.DEBUG, spider=spider)
        #return item