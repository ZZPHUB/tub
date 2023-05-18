import os 
import json
import requests

class app_info_mode():
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__))
        self.mode = "translate"
        self.print_format = "t_mode"
        self.version = "v2.0"
        self.fromlang = 'en'
        self.tolang = 'zh'
        #get the appid&seckey;if none set before,then input
        #and store in info.json,if stored in info.json,then 
        #read it
    def translate_init(self): 
        fd = open(self.path+"/info.json","r")
        info_dict = json.load(fd)
        info_private_appid = info_dict["private"]["appid"]
        info_private_seckey = info_dict["private"]["seckey"]
        if info_private_appid == info_private_seckey:
            self.appid = input("[translate mode]set the appid:")
            self.seckey = input("[translate mode]set the seckey:")
            fd.close()

            info_dict["private"]["appid"]=self.appid
            info_dict["private"]["seckey"]=self.seckey

            #make the str that will write into the info.json
            #file a easy format to read
            info_str = str()
            for i in json.dumps(info_dict):
                info_str = info_str + i
                if i == ',':
                    info_str = info_str+'\n'

            #wirte the str into the info.json
            fd = open(self.path+"/info.json","w")
            fd.write(info_str)
            fd.close()
        else:
            self.appid = info_private_appid
            self.seckey = info_private_seckey
            fd.close()

    def robot_token_update(self):
        api_id = input("[robot mode]set api_id:")
        seckey = input("[robot mode]set seckey:")
        url = "https://aip.baidubce.com/oauth/2.0/token"
        req_url = url+f"?grant_type=client_credentials&client_id={api_id}&client_secret={seckey}"
        payload = ""
        headers = {'Content-Type': 'application/json','Accept': 'application/json'}
        response = requests.request("POST", req_url, headers=headers, data=payload)
        response = json.loads(response.text)

        if response["access_token"]:
           self.token = response["access_token"]
           fd = open(self.path+"/info.json",'r')
           info_dict = json.load(fd)
           fd.close()
           info_dict["token"]=response["access_token"]
           info_dict = json.dumps(info_dict)
           info_str = str()
           
           for i in info_dict:
               info_str = info_str+i
               if i == ',':
                   info_str=info_str+'\n'
             
           fd = open(self.path+"/info.json",'w')
           fd.write(info_str)
           fd.close()
    def token_get(self):
        fd = open(self.path+"/info.json",'r')
        info_dict = json.load(fd)
        #print(info_dict["token"])
        if info_dict["token"]=="none":
            #print(info_dict["token"])
            self.robot_token_update()
        else:
            #print('111')
            self.token = info_dict["token"]   

if __name__ == "__main__":
    app_info = app_info_mode()
    print(app_info.appid,app_info.seckey)
