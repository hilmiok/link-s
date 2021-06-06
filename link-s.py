#!/usr/bin/env/python3
#Developer ...
###########################################
#Bu program localhostta ngrok servisi     #
#ile http portu açarak link kısaltmatadır.#
###########################################



import sys
import os


if os.name =="posix":
	pass
else: 
	print("This program  run the linux system:( ")
	print("exiting")
	sys.exit()

print("Welcome link-S url shoter service.\n")



url = str(input("url> "))
port = int(input("port> "))

dosya = open("index.html" , "w")

dosya.write(f"""
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Link-S</title>
		<meta http-equiv="refresh" content="0;url={url}">
	</head>
</html>
""")

dosya.close()
print("Starting Php server and Ngrok service...\n")

os.system(f"php -S 127.0.0.1:{port}  & ./ngrok-i686 http {port}")
	
	

