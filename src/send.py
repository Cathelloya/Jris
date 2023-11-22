import socket
import requests
import time
from receive import *

# 发送消息
def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '127.0.0.1'
    client.connect((ip, 5700))

    msg_type = resp_dict['msg_type']  # 回复类型（群聊/私聊）
    number = resp_dict['number']  # 回复账号（群号/好友号）
    msg = resp_dict['msg']  # 要回复的消息

    # 将字符中的特殊字符进行url编码
    msg = msg.replace(" ", "%20")
    msg = msg.replace("\n", "%0a")

    if msg_type == 'group':
        payload = "GET /send_group_msg?group_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    elif msg_type == 'private':
        payload = "GET /send_private_msg?user_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    print("发送" + payload)
    client.send(payload.encode("utf-8"))
    client.close()
    return 0

# 获取群成员列表
def get_group(id):
    response = requests.post('http://127.0.0.1:5700/get_group_member_list?group_id='+str(id)).json()
    for i in response['data']:
        if(i['card']!=''):
            print(i['card']+str(i['user_id']))
        else:
            print(i['nickname']+str(i['user_id']))


mesg={'msg_type': 'group', 'number': 674771141, 'msg': '现在可以说话了吗'}
resp_dict={'msg_type':'private','number':2016741487,'msg':'你好'}
# send_msg(mesg)
# get_group(674771141)


while(1):
    rev=rev_msg()
    if rev["post_type"] == "message":
        #print(rev) #需要功能自己DIY
        if rev["message_type"] == "private": #私聊
            if rev['raw_message']=='在吗':
                qq = rev['sender']['user_id']
                send_msg({'msg_type':'private','number':qq,'msg':'我在'})
        elif rev["message_type"] == "group": #群聊
            group = rev['group_id']
            if "Jris" in rev["raw_message"]:
                if rev['raw_message'].split(' ')[1]=='摸摸头':
                    qq=rev['sender']['user_id']
                    send_msg({'msg_type':'group','number':674771141,'msg':'[CQ:poke,qq={}]'.format(qq)})
                    send_msg({'msg_type': 'group', 'number': 674771141, 'msg': '好捏！'})
            elif "jris" in rev["raw_message"]:
                if rev['raw_message'].split(' ')[1]=='摸摸头':
                    qq=rev['sender']['user_id']
                    send_msg({'msg_type': 'group', 'number': 674771141, 'msg': '不去追求现实中实际存在的人，而来找机器人寻求安慰，难道不是贯彻了荒诞主义吗？'})
        else:
            continue
    else:  # rev["post_type"]=="meta_event":
        continue
    print(rev)
    time.sleep(3)