# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
from pythonAnalysisProto import deserializationMsg
import binascii
if __name__ == '__main__':
    result = deserializationMsg('login_pb2','cl_login_req',binascii.a2b_hex('0a0a3237303834383832333430a0062a0241311a1b383734373934323237303834383832333431363434383233323134'))
    print("cl_login_req --->  \n" + result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/



