import time

import redis
from flask import Flask
import pymongo
import main

path = "\\data\\"   #r"./code/data"
# os.chdir(path)
current_dir = os.getcwd()
print("current_dir",current_dir)
files = os.listdir(current_dir+path)

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    final_list = main.resources(files)
    return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/query_data')
def query_data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    emis_db = myclient["emis_database"]
    mycol = emis_db["resources"]
    for y in mycol.find():
        print(y) 
        return y