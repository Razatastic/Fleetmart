import json
import bcrypt


def getDBCredentials(path):
    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)
    return f"{data['driver']}://{data['user']}:{data['password']}@{data['host']}:{data['port']}/{data['db']}"

def getAppKey(path):
    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)
    return data['app_key']