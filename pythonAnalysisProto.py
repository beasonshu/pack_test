import sys
import importlib

sys.path.append(sys.path[0] + '/scripts')

from google.protobuf.json_format import MessageToJson, Parse


def dynamic_import(module):
    return importlib.import_module(module)


def deserializationMsg(pyFileName, msgName, body):
    # print ("testPytonDeserializationPrint")
    # print ("body: ")
    # print (body)
    module = dynamic_import(pyFileName)
    msgClass = getattr(module, msgName)
    msg = msgClass()
    msg.ParseFromString(body)
    jsonStr = MessageToJson(msg)
    # print ("jsonStr: ")
    # print (jsonStr)
    return jsonStr


def serializeMsg(pyFileName, msgName, msgJsonStr):
    # print ("testPytonSerializeMsgPrint")
    # print ("msgJsonStr: ")
    # print (msgJsonStr)
    module = dynamic_import(pyFileName)
    msgClass = getattr(module, msgName)
    msg = msgClass()
    Parse(msgJsonStr, msg)
    bytes = msg.SerializeToString()
    # print ("bytes: ")
    # print (bytes)
    return bytes;
