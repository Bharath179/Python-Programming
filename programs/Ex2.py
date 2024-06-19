import re
s=input("Enter the string to match...")
m=re.match(s,"abcdefg")
if m!=None:
    print("Match is available at the beginning of the string...")
    #print("Start Index:",m.start(), "and End Index:",m.end())
    print('start Index:{} and End Index:{}'.format(m.start(),m.end()))
else:
    print("Match is not available at the beginning of the String")


"""import re,urllib
import urllib.request
sites="google rediff".split()
print(sites)
for s in sites:
 print("Searching...",s)
 u=urllib.request.urlopen("http://"+s+".com")
 text=u.read()
 title=re.findall("<title>.*</title>",str(text),re.I)
 print(title[0])"""




