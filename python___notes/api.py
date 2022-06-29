##import requests
##response=requests.get("https://www.google.com/")
##print(response)

##
##import requests
##response=requests.get("http://api.open-notify.org/astros.json")
##print(response)


##import requests
##response=requests.get("http://api.open-notify.org/astros.json")
##print(response.json())
##
##import json
##a=response.json()
##data=json.dumps(a,sort_keys=True,indent=4)
##print(data)


##import requests
##parameters={
##    'lat':42,
##    'lon':32
##    }
##response=requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)
##
##print(response.json())
##
##a=response.json()
##import json
##data=json.dumps(a,sort_keys=True,indent=4)
##print(data)
##
##nxt=a["response"]
##print(nxt)
##li=[]
##for x in nxt:
##    c=x["risetime"]
##    li.append(c)
##print("li is:",li)
##
##from datetime import datetime
##new=[]
##for x in li:
##    d=datetime.fromtimestamp(x)
##    new.append(d)
##print("new is:",new)
##
##result=[]
##for x in new:
##    fmt="%d/%m/%y%H-%M-%S"
##    x=datetime.strftime(x,fmt)
##    result.append(x)
##print(result)



































