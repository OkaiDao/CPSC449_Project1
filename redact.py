# import sys
import http.client
import json
import urllib.parse

url = "foaas.com"
url2 = "www.purgomalum.com"
purgomalumPath = "/service/json?text="

# if len(sys.argv) == 1 or len(sys.argv) > 2:
#     sys.exit(f"Usage: {sys.argv[0]} URL")


def get_censored_json(path):
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
    json_string = json.dumps(dictionary, indent=4)
    print(json_string)
    return dictionary


# print(get_censored_json(sys.argv[1]))

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
# https://www.reddit.com/r/learnprogramming/comments/kxy3fm/my_first_api_with_python_trying_to_use_foaas/
