# Django_Live_Video
This project is built for streaming live video through django and UDP Socket. With the help of MongDB,
we can save the new image from camera into server. Then django in server retrives the last frame and render it to the web page.

we write a shell script for quickly start. Please note that you should modify the start.sh before everything start. Plz change the dir of virtual Env if you use conda, otherwise, comment it.
Then, when running start.sh, plz indicate the ipv4 of the server. For example, in terminator:

> ./start.sh 192.168.0.25

Then the django and udp server will be started. The port of this django is 0.0.0.0:7001. plz ensure that it doest conflict with other port you use.

> Go to 0.0.0.0:7001/monitor/ to watch the live video.

If you want to watch it inside other web page, plz use

> "\<img src="http://serverIP:7001/monitor/ " width="300" height="250" \>"

in template html in another django.
