import socket
import pymongo
import logging
import datetime
import sys
print(f'params：{str(sys.argv)}')
thisIp = str(sys.argv[1])
logging.basicConfig(filename="tcp_server.log", level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
machine_id_to_socket = {}
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
print(mongo_client.server_info())  # 判断是否连接成功
mongo_db = mongo_client['CAM_db']

mongo_collection = mongo_db['CAM_collection']
try:
    mongo_collection.delete_many({"machine_id": "CAM"})
except:
    print("empty db")

Udp_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Udp_Socket.bind((thisIp, 5005))
while (True):
    Recv_Data = Udp_Socket.recvfrom(1024000)
    Recv_Data = Recv_Data[0]
    Sender_Addr = Recv_Data[1]
    info = {
        'machine_id': 'CAM',
        'data': Recv_Data,
        'date': datetime.datetime.now()
    }
    mongo_collection.insert_one(info)


