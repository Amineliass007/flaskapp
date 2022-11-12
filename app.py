'''import requests
import json'''
from flask import Flask
from flask import jsonify
app = Flask(__name__)
@app.route("/")
def hello():
    return ("Hello world")
app.set("port",3000)
if __name__ == '__main__':
app.run()
'''
def getApiResponse(url):
    auth="x-key"
    value="2056efd4b2a3c1b2a25ee38794c9b118"
    my_headers = {auth: value}
    response = requests.get(url, headers=my_headers)
    return(response.json())
@app.route("/")
def getAgsiProviders():    
    url="https://agsi.gie.eu/api/about?listing=true"
    
    data=getApiResponse(url)
    st={}
    Li=[]
    for country in data["SSO"].keys():
        d={}
        l=[]
        d["country"]=country
        for i in data["SSO"][country]:
            s={}
            s["zone"]=i["data"]["code"]
            s["countryCode"]=i["data"]["country"]["code"]
            s["countryName"]=i["data"]["country"]["name"]
            s["companyName"]=i["name"]
            s["companyEic"]=i["eic"]
            s["companyType"]=i["data"]["type"]
            for j in i["facilities"]:
                s["facilityName"]=j["name"]
                s["facilityEic"]=j["eic"]
                s["facilityCountryName"]=j["country"]["name"]
                s["facilityType"]=j["type"]
            
            l.append(s)
        d["data"]=l
        Li.append(d)
    st["body"]=Li
    return(jsonify(st))
app.run(host='0.0.0.0', port=5000)


@app.route("/agsi/facilities")
def getAgsiFacilities():    
    data=getAgsiProviders().json
    Li=[]
    for country in data["body"]:
        d={}
        for facility in country["data"]:
            urlFacility="https://agsi.gie.eu/api?country="+str(facility["countryCode"])+"&company="+str(facility["companyEic"])+"&facility="+str(facility["facilityEic"])
            data=getApiResponse(urlFacility)
            for facilityData in data["data"]:
                d["gas_day"]=data["gas_day"]
                d["name"]=facilityData["name"]
                d["gasDayStart"]=facilityData["gasDayStart"]
                d["gasInStorage"]=facilityData["gasInStorage"]
                Li.append(d)
    return (jsonify(Li))'''
#git
