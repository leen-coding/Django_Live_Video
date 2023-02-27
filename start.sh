#!/bin/bash

thisIp=${1:-1}
source ~/anaconda3/bin/activate Django_env

python3 manage.py runserver 0.0.0.0:7001 &

pid1=$!


if [ $thisIp != 1 ]; then
	python udp_server.py $thisIp &
	pid2=$!
	echo "udpMongo_server start!"

else

	echo "udpMongo disabled!!"
fi

trap "kill $pid1 $pid2" SIGINT

wait




