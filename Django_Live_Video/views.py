
import pymongo
from django.http import StreamingHttpResponse
from django.shortcuts import render


mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
print(mongo_client.server_info())  # 判断是否连接成功
mongo_db = mongo_client['CAM_db']

mongo_collection = mongo_db['CAM_collection']

def getmonitor(request):
    return StreamingHttpResponse(gen(),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def gen():
    while True:
        try:
            last_frame = [i for i in mongo_collection.find({'machine_id': 'CAM'}).sort('_id', -1).limit(1)][0]['data']
            last_id = [i for i in mongo_collection.find({'machine_id': 'CAM'}).sort('_id', -1).limit(1)][0]["_id"]
            try:
                myquery = {
                    "machine_id": "CAM",
                    "_id": {'$lt': last_id}
                }
                x = mongo_collection.delete_many(myquery)
            except:
                pass
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + last_frame + b'\r\n\r\n')
        except:
            continue





