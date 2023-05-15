# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from pythonAnalysisProto import deserializationMsg, serializeMsg
import binascii

if __name__ == '__main__':
    # result = deserializationMsg('login_pb2','cl_login_req',binascii.a2b_hex('0a0a3237303834383832333430a0062a0241311a1b383734373934323237303834383832333431363434383233323134'))
    result = deserializationMsg('task_pb2', 'submit_task_req', binascii.a2b_hex(
        '0a03cbb8020000'))
    print("submit_task_req des--->  \n" + result)

    # result = serializeMsg('avatar_part_pb2', 'wear_avatar_part_req', result).hex()
    # print("wear_avatar_part_req serializeMsg--->  \n" + str(result))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
