import os
import json

def printJsonData(filename):
  file = open(filename)
  jsonString = file.read()
  jsonString = jsonString.replace('\'', '"')
  #print(jsonString)
  jsonObject = json.loads(jsonString)
  print(jsonObject['Namespace'] , '|', jsonObject['ProcPrefix'])
  file.close()
  

dir = 'c:\\svn\\k2\\trunk\\services'

for root, dirs, files in os.walk(dir):
  for filename in files:
    if filename == "DataLayer.json":
      filename = os.path.join(root, filename)
      printJsonData(filename)

