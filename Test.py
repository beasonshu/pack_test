import re

if __name__ == '__main__':
    temp = 'eLOGIN_CL_LOGIN_REQ = SET_MSG_ID(eMSG_TYPE_LOGIN, 12), // 登录请求'
    print(temp[(temp.find('_')+1):])
