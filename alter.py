import re, os


def alter(file, old_str, new_str):
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(old_str, new_str, line))
    os.remove(file)
    os.rename("%s.bak" % file, file)


def compute(temp, aint):
    file = open('/Users/shuxinghu/Desktop/test/' + temp, 'r')
    content = file.read()
    firstpos = content.rfind("{")
    # position of closing square bracket
    lastpos = content.rfind("}")
    # printing the text between two square brackets
    content = content[firstpos + 1:lastpos]
    result = ""
    for item in content.split("\n"):
        # print(item)
        newitem = re.sub('(\d+)', lambda item: str(int(item.group(1)) + aint), item)
        if not newitem.__contains__("SET_MSG_ID"):
            continue
        newitem = newitem[(newitem.find('_',0)+1):]
        newitem = newitem.replace("SET_MSG_ID(eMSG_TYPE_BATTLE,", "")
        newitem = newitem.replace("SET_MSG_ID(eMSG_TYPE_CENTER,", "")
        newitem = newitem.replace("SET_MSG_ID(eMSG_TYPE_CLIENT,", "")
        newitem = newitem.replace("SET_MSG_ID(eMSG_TYPE_FRIEND,", "")
        newitem = newitem.replace("SET_MSG_ID(eMSG_TYPE_GATE,", "")
        newitem = newitem.replace("SET_MSG_ID(eMSG_TYPE_GAME,", "")
        newitem = newitem.replace("SET_MSG_ID(emsg_type_game,", "")
        newitem = newitem.replace("SET_MSG_ID(eMSG_TYPE_LOGIN,", "").replace("),", ";")
        result += newitem.lower() + "\n"

    return result







if __name__ == '__main__':
    # alter("/Users/shuxinghu/Desktop/test/client_msg.h", "(eMSG_TYPE_CLIENT), (\d+)", "$1" + compute("$2"))
    # compute('battle_msg.h', 28672)
    # compute('center_msg.h', 20480)
    # compute('client_msg.h', 4096)
    # compute('friend_msg.h', 24576)
    # compute('game_msg.h', 16384)
    # compute('gate_msg.h', 12288)
    # compute('login_msg.h', 8192)
    file_handle=open('/Users/shuxinghu/Desktop/test/test.txt',mode='w')
    file_handle.writelines(compute('login_msg.h', 8192))
    file_handle.writelines(compute('gate_msg.h', 12288))
    file_handle.writelines(compute('game_msg.h', 16384))
    file_handle.writelines(compute('friend_msg.h', 24576))
    file_handle.writelines(compute('client_msg.h', 4096))
    file_handle.writelines(compute('center_msg.h', 20480))
    file_handle.writelines(compute('battle_msg.h', 28672))
    file_handle.close()
