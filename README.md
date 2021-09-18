# CPSC449_Project1
CPSC 449 - Web Back-End Engineering Project 1

Ismael Barajas
Zack Sarvas
Jonathan Dao

The project integrates serveses with HTTP and JSON. It uses the FOAAS and purgomalum api. 
The user puts in a path, and if the correct path is called from redact.py it creates a payload to create an HTML outline showing a message to the user copying the bootstrap styling and the link to foaas.com   

How To Run
using redact URL connect to the HTTP server using redact.py/'message_param'/'subtitle_param'
first paramater, message_param, will generate a message from FOAAS ussing their API and the second parameter, subtitle_param, writes the string as a subtitle.

redact.py 

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

class ExampleHTTPRequestHandler(http.server.BaseHTTPRequestHandler)
	checks if path is '/operations', if it is send 404 error
	checks if path is '/favicon.ico', if it is send 404 error
	checks if path is '/', if it is send response 200 and show a blank
	otherwise send 200 response and show content using get_censored_json from redact.py

with socketserver.TCPServer(("", PORT), ExampleHTTPRequestHandler) as httpd:
	Connects to the http server
