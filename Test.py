import re

if __name__ == '__main__':
    # temp = 'eLOGIN_CL_LOGIN_REQ = SET_MSG_ID(eMSG_TYPE_LOGIN, 12), // 登录请求'
    # temp = temp[(temp.find('_') + 1):]
    # print(temp)


    f = open("/Users/shuxinghu/Desktop/test123/test.txt")
    line = f.readline()
    while line:
        print(line[(line.find('_') + 1):])
        line = f.readline()
    f.close()
