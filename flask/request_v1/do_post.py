from __future__ import print_function
import requests

# json or Python dict
json_data = {
    "language" : "Python",
    "framework" : "Flask",
    "website" : "efefer.com",
    "version_info" : {
        "python" : "3.6.6",
        "flask" : "1.0.2",
    },
    "examples" : ["query", "form", "json"],
    "boolean_test" : True,
}

r = requests.post("http://127.0.0.1:5000/json-example", json=json_data)

print("Status = %s" % r.status_code)
print("Reason = %s" % r.reason)

print("HTML response follows\n\n")
print(r.text)

