import json
import pymongo
import pprint

client = pymongo.MongoClient('localhost', 27017)

db = client.igti

collection = db.video_game_sales

def readJson():
    filename = 'videogame_sales_mongo.json'

    with open(filename, 'r', encoding='utf8') as f:
        return json.load(f)


data = readJson()

collection.insert_many(data)

#Pergunta 7 - Resposta: Grand Theft Auto: San Andreas
for documents in collection.find({"Platform": "PS2"}).sort("Global_Sales", -1).limit(1):
  print("Pergunta 7")
  pprint.pprint(documents['Name'])

#Pergunta 8 - Resposta: 3
for documents in collection.find({}).sort("EU_Sales", -1).limit(2):
  print("Pergunta 8")
  pprint.pprint(documents['Rank'])

#Pergunta 9 - Resposta: Sora no Otoshimono: DokiDoki Summer Vacation
for documents in collection.find({"Year": 2010}).sort("Global_Sales", 1).limit(1):
  print("Pergunta 9")
  pprint.pprint(documents['Name'])

#Pergunta 10 - Resposta: Wii
for documents in collection.find({"Year": 2008}).sort("Global_Sales", -1).limit(1):
  print("Pergunta 10")
  pprint.pprint(documents['Platform'])

#Pergunta 11 - Resposta: Call of Duty: Black Ops 3
print("Pergunta 11")
pprint.pprint(collection.find_one({"Platform": "PS4"})['Name'])

#Pergunta 12 - Resposta: 1265
print("Pergunta 12")
pprint.pprint(collection.count_documents({"Platform": "X360"}))

#Pergunta 13 - Resposta: 3DS
for documents in collection.find({"Year": 2015}).sort("JP_Sales", -1).limit(1):
  print("Pergunta 13")
  pprint.pprint(documents['Platform'])

#Pergunta 14 - Resposta: 1607
for documents in collection.find({"Platform": "XOne","Name": "The Witcher 3: Wild Hunt"}):
  print("Pergunta 14")
  pprint.pprint(documents['Rank'])

#Pergunta 15 - Resposta: 851
print("Pergunta 15")
pprint.pprint(collection.count_documents({"Global_Sales":{"$gte":2}}))