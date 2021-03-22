import requests
import json
from time import sleep
import Predict

def PostResolveJson(ResServer,Resolve):

    for req in Resolve:
        y=json.dumps(req)
        headers = {'Content-Type': 'application/json;charset=UTF-8','Accept': 'application/json text/plain, */*',}
        print(y)
        requests.post(ResServer,headers=headers, data=y)




def GetRequestJson(ReqServer):
    r=requests.get(ReqServer)
    sleep(0.5)
    ReqJson=r.content
    Urllist=ParseRequestJson(ReqJson,ReqServer)
    return Urllist

def DeleteRequest(Server,ID):
    req=Server+"/"+str(ID)
    r=requests.delete(req)

def ParseRequestJson(ResJson,ReqServer):
    #UrlDict={}
    GetUrlList=[]
    LoadedJson=json.loads(ResJson)
    for req in LoadedJson:
        #url=req["url"]
        #UrlDict={"id":req["id"],"url":req["url"],"image":req["image"],"isBlocked":req["isBlocked"]}
        GetUrlList.append({"id":req["id"],"url":req["url"],"tabId":req["tabId"]})
    return GetUrlList

def GetResolveJson(ReqUrllist,ReqServer):
    PostUrlList=[]
    for req in ReqUrllist:
        category=Predict.PredictContent(req["url"])
        #category="Adult2"
        print("Url:"+req["url"]+"Category:"+category)
        if(category=="Adult"):
            PostUrlList.append({"url":req["url"],"tabId":req["tabId"],"isBlocked":True,"isControlled":False})
        else:
            PostUrlList.append({"url":req["url"],"tabId":req["tabId"],"isBlocked":False,"isControlled":False})
        DeleteRequest(ReqServer,req["id"])
    return PostUrlList


def ListenJsonServer():
    ReqServer="http://localhost:3004/request"
    ResServer="http://localhost:3005/resolve"
    while 1:
        Request=GetRequestJson(ReqServer)
        Resolve=GetResolveJson(Request,ReqServer)
        PostResolveJson(ResServer,Resolve)
    #PostResolveJson(Resolve)

ListenJsonServer()
