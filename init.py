import os 
import json

class app_info_mode():
    def __init__(self):
        self.path = os.getcwd()
        #get the appid&seckey;if none set before,then input
        #and store in info.json,if stored in info.json,then 
        #read it 
        fd = open(self.path+"/info.json","r")
        info_dict = json.load(fd)
        info_private_appid = info_dict["private"]["appid"]
        info_private_seckey = info_dict["private"]["seckey"]
        if info_private_appid == info_private_seckey:
            self.appid = input("set the appid:")
            self.seckey = input("set the seckey:")
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
if __name__ == "__main__":
    app_info = app_info_mode()
    print(app_info.appid,app_info.seckey)
