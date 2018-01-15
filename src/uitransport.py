# v.0.2

import struct
import json

#bridge

class BridgeException(Exception):
    def __init__(self, message='unknown message'):
        self.Message = message


class Vulnerability:
    ExistingValue = ''
    RecommendedValue = ''
    Type = ''
    Function = ''
    SourceFile = ''
    NumberLine = 0
    RawLine = ''
    Place = ''
    Exploit = ''

class Message:
    #Type Constants
    UNKNOWN = 0
    START = 1
    STOP = 2
    ABORT = 3
    VULNERDETECTED = 4
    COREERROR = 5

    PREP_START = 10
    PROGRESS = 11
    PREP_STOP = 13

    POTENTIAL_VULN = 14
    COMMON_VULN = 21
    FILES_PRIORITY = 23
    INCREMENTAL_DEPENDENCY = 24

    #variables
    Type = UNKNOWN
    ObjectValue = None

    def __init__(self, type, objVal):
        self.Type = type
        self.ObjectValue = objVal


class Bridge:
    __pipe = None

    def __init__(self, _pipeName=r'pipe_0'):
        self.pipeName = '\\\\.\\pipe\\' + _pipeName
        self.encoding = "utf8"

        #open pipe to wrinting
        try:
            self.__pipe = open(self.pipeName, 'r+b', 0)
            pass
        except IOError as err:
            #close on error create pipe
            appException = BridgeException("Error on create pipe: " + _pipeName + ". " + err.strerror)
            raise appException

    def __sendMessage(self, message):
        if not isinstance(message, Message):
            raise BridgeException('try to send to transport non-message object')

        if message.ObjectValue is not None:
            objval = message.ObjectValue
            mtype = message.Type
            if (self.json_version == '3.0') and hasattr(objval, 'getCommonVulnerability') and mtype in [Message.VULNERDETECTED, Message.POTENTIAL_VULN]:
                objval = objval.getCommonVulnerability()
                mtype = Message.COMMON_VULN

            jsonstr = json.dumps(objval, default=lambda o: o.__dict__)
            sendresult = struct.pack('I', mtype) + struct.pack('I', len(jsonstr)) + jsonstr.encode()
        else:
            sendresult = struct.pack('I', message.Type) + struct.pack('I', 0)
        try:
            self.__pipe.write(sendresult)
        except (IOError, AttributeError):
            raise BridgeException("Can\'t send data: broken pipe")

    def SendVulnerability(self, vulnerability):
        message = Message(Message.VULNERDETECTED, vulnerability)
        self.__sendMessage(message)

    def SendError(self, error):
        message = Message(Message.COREERROR, error)
        self.__sendMessage(message)

    def SendProgress(self, progress):
        message = Message(Message.PROGRESS, progress)
        self.__sendMessage(message)

    def SendMessage(self, message):
        self.__sendMessage(message)

    def SendPriorities(self, message):
        message = Message(Message.FILES_PRIORITY, message)
        self.__sendMessage(message)

    def OnStart(self):
        message = Message(Message.START, None)
        self.__sendMessage(message)

    def OnStop(self):
        message = Message(Message.STOP, None)
        self.__sendMessage(message)

    def PrepStart(self):
        message = Message(Message.PREP_START, None)
        self.__sendMessage(message)

    def PrepStop(self):
        message = Message(Message.PREP_STOP, None)
        self.__sendMessage(message)

    def OnError(self, message):
        message = Message(Message.STOP, message)
        self.__sendMessage(message)