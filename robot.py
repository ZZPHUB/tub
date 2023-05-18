import requests
import json
import init

def robot_ask(query=str):
    robot_info  = init.app_info_mode()
    robot_info.token_get()
    token = robot_info.token
    url = 'https://aip.baidubce.com/rpc/2.0/unit/service/v3/chat?access_token='+token
    post_data = "{\"version\":\"3.0\",\"service_id\":\"S91121\",\"session_id\":\"\",\"log_id\":\"7758521\",\"request\":{\"terminal_id\":\"88888\",\"query\":\""+query+"\"}}"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=post_data.encode("utf-8"), headers=headers)
    if response:
        return (response.json()["result"]["context"]["SYS_PRESUMED_HIST"])

if __name__ == "__main__":
    print(robot_ask("日本国土面积"))
