# CPSC449_Project1
CPSC 449 - Web Back-End Engineering Project 1

Ismael Barajas
Zack Sarvas
Jonathan Dao

The project integrates services with HTTP and JSON, that uses FOAAS and purgomalum api. 
The user enter a path, and if there is a correct path called from redact.py, a payload  is created and makes an HTML outline showing a message to the user copying the bootstrap styling from foaas.com and the link to website.   

How To Run
using redact URL connect to the HTTP server using redact.py/'message_param'/'subtitle_param'
first paramater, message_param, will generate a message from FOAAS ussing their API and the second parameter, subtitle_param, writes the string as a subtitle.

redact.py 
	contains functions that make API calls to FOAAS and purgomalum
	
make_request(url, path)
	takes url and path of a request to create a connection to the http server and loads a JSON object and returns the object

get_censored_json(path)
	Checks if the path is valid with the first character of the string being '/'
	If the path is '/operations' return the json data by calling make_request 
	otherwise if the path is valid use the make_request function to collect the data with the valid path
	It then parses the message and is used to make a api call to the purgomalum with the parsed message and path and calls the 
		make_request to pull the data from the updated path.
	It returns the data as a dictionary with message, and subtitle.

cmd_censored_json(path)
	prints the data of the json data from the path using get_censored_json to the console

main()
	if length of sys.argv is not 2 it exits, if it does print data to console.

server.py
	subclass of http.server.BaseHTTPRequestHandler with an implementation of the do_GET() function that retrives a path from an incoming request to make an API call to FOAAS and PurgoMalum. Any of the other paths and filters from foaas produces a message with the exception of the path '/operations' and a '/' path.

class ExampleHTTPRequestHandler(http.server.BaseHTTPRequestHandler)
	checks if path is '/operations', if it is send 404 error
	checks if path is '/favicon.ico', if it is send 404 error
	checks if path is '/', if it is send response 200 and show a blank
	otherwise send 200 response and show content using get_censored_json from redact.py

with socketserver.TCPServer(("", PORT), ExampleHTTPRequestHandler) as httpd:
	Connects to the http server
