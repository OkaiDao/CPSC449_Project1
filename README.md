# CPSC449_Project1
CPSC 449 - Web Back-End Engineering Project 1

Ismael Barajas
Zack Sarvas
Jonathan Dao

The project integrates serveses with HTTP and JSON. It uses the FOAAS and purgomalum api.

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


In Server put an exception when putting the "/opertations" path to send a 404 error back to the user.
Exception for the default path
If there is a correct path the function is called from redact.py
In payload create the HTML Outline, coppied the bootstrap styling and the link to foaas.com   
