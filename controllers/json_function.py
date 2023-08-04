import os 
import json

def writeJson(directory_path, file_path, data):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        
    with open(file_path, "w") as file:
        json.dump(data, file)
        
    print("Les données ont bien été enregistrées")
    
def loadJson(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data
