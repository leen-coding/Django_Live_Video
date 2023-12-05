# Django_Live_Video

This project is built for streaming live video through django and UDP Socket. With the help of MongDB,
we can save the new image from camera into server. Then django in server retrives the last frame and render it to the web page.

## Environment Building
Open your terminal:
```
# create conda env
conda create -n Django_env python==3.9 

# activate created env
conda activate Django_env

# install Django
conda install -c anaconda django

# install pymongo so that we can use python controll mongodb
pip install pymongo
```

Install MongoDB

## Reference:  https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#std-label-install-mdb-community-ubuntu

```
sudo apt-get install gnupg curl

curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

#If ubuntu 22.04
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

#elif ubuntu 20.04
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

sudo apt-get update

sudo apt-get install -y mongodb-org

#start MongoDB
sudo systemctl start mongod

```

## Server
we write a shell script for quickly start. Please note that you should modify the start.sh before everything start. Plz change the dir of virtual Env when you use conda, otherwise, comment it. By default, the created conda env should be at ' ~/anaconda3/bin/activate Django_env'. If you install Anaconda under user's home, then you do not need to modify *start.sh*.

Then, when running start.sh, plz indicate the ipv4 of the server. For example, in terminator:

> ./start.sh 192.168.0.25(your server IP) 

Then the django and udp server will be started. The port of this django is 7001. plz ensure that it doest conflict with other port you use.

## Cam client
At the cam side, modify the host ip, which means, you need to change the line 4 in the script *host = "192.168.0.25"* in to host = yourserverIP. Then you can run it by python directly.

## Speed Test Client

For you quick test the delay of the streaming, we also worte a script for your quick test. 
Firstly, you still need to modify the host(server) IP in the script *speedtest.py* (line 8)

Then open this link for a exact time. https://clock.zone/

then run it using python. The screen will turn semi-transparent and then, you should click your mouse, the position of frist click indicates the top left point of the part of the screen you want to cut. and the second means the bottom right point. The zone you select should include the *exact time *in the page you just opened.

Then this part of your screen will be send to the server. you can measure the delay of the streaming by calculating the time difference between the pulling(viewing by the next step) and exact time (on your opened https://clock.zone/).

## View your Streaming:

> Go to yourserverIP:7001/monitor/ to watch the live video.
> If you want to watch it inside other web page, plz use

> \<img src="http://yourserverIP:7001/monitor/ " width="300" height="250" \>

in template html in another django.
