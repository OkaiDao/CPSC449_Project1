import sys
import http.client
import json
import urllib.parse
import os.path

url = "foaas.com"
url2 = "www.purgomalum.com"
purgomalumPath = "/service/json?text="

def get_censored_json(path):
    if path[0] != "/":
        sys.exit(f"{path} is an invalid URL path, e.g. /{path}")
    headers = {"Accept": "application/json"}
    connection = http.client.HTTPSConnection(url)
    connection.request('GET', path, "", headers)
    response = connection.getresponse()
    data = json.loads(response.read())
    connection.close()
    parsedMessage = urllib.parse.quote(data["message"])
    updatedPurgoPath = purgomalumPath + parsedMessage
    connection = http.client.HTTPConnection(url2)
    connection.request('GET', updatedPurgoPath)
    response = connection.getresponse()
    data2 = json.loads(response.read())
    connection.close()
    dictionary = {"message": data2["result"], "subtitle": data["subtitle"]}
    # json_string = json.dumps(dictionary, indent=4)
    # print(json_string)
    return dictionary

def cmd_censored_json(path):
    if path == "/operations":
        sys.exit(f"{path} is an invalid URL path")
    censoredJson = get_censored_json(path)
    json_string = json.dumps(censoredJson, indent=4)
    print(json_string)

if sys.argv[0] == os.path.basename(__file__) and ( len(sys.argv) == 1 or len(sys.argv) > 2):
    sys.exit(f"Usage: {sys.argv[0]} URL")
elif len(sys.argv) == 2:
    cmd_censored_json(sys.argv[1])
    sys.exit()

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
# https://www.reddit.com/r/learnprogramming/comments/kxy3fm/my_first_api_with_python_trying_to_use_foaas/
