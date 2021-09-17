import sys
import http.client
import json
import urllib.parse

url = "foaas.com"
url2 = "www.purgomalum.com"
purgomalumPath = "/service/json?text="


def make_request(url, path):
    headers = {"Accept": "application/json"}
    connection = http.client.HTTPSConnection(url)
    connection.request('GET', path, "", headers)
    response = connection.getresponse()
    data = json.loads(response.read())
    connection.close()
    return data


def get_censored_json(path):
    if path[0] != "/":
        sys.exit(f"{path} is an invalid /PATH, e.g. /{path}")
    elif path == "/operations":
        return make_request(url, path)
    data = make_request(url, path)
    parsedMessage = urllib.parse.quote(data["message"])
    updatedPurgoPath = purgomalumPath + parsedMessage
    data2 = make_request(url2, updatedPurgoPath)
    dictionary = {"message": data2["result"], "subtitle": data["subtitle"]}
    return dictionary


def cmd_censored_json(path):
    censoredJson = get_censored_json(path)
    json_string = json.dumps(censoredJson, indent=4)
    print(json_string)


def main():
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        sys.exit(f"Usage: {sys.argv[0]} /PATH")
    elif len(sys.argv) == 2:
        cmd_censored_json(sys.argv[1])


if __name__ == "__main__":
    main()
