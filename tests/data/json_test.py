import json
from json.encoder import JSONEncoder

version_json = """
{
 "date": "2020-10-29T07:57:53+0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "539478470b53bd3e96473b411e1322bb158fd444",
 "version": "0.12.1"
}    
"""
result = json.loads(version_json)
print(type(result))
for index, val in enumerate(result):
    print("%s---%s" % (index, val))

print(result["version"])

print(JSONEncoder.encode(result))

