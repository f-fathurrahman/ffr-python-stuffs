from __future__ import print_function
import requests
import sys

Nargs = len(sys.argv)
print("Nargs = ", Nargs)
if Nargs < 2:
    url_text = "http://localhost:5000/"
else:
    url_text = sys.argv[1]

print("url_text = ", url_text)
r = requests.get(url_text)

print("Status = %s" % r.status_code)
print("Reason = %s" % r.reason)

print("HTML response follows\n\n")
print(r.text)

