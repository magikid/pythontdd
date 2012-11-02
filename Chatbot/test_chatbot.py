import unittest
from chatbot import *

class ChatbotTests(unittest.TestCase):
        
    def testSocketReaderInit(self):
        sr = socketReader()
        self.assertTrue(isinstance(sr,socketReader))

    def testMessageType(self):
        sr = socketReader()
        socketData = bytearray(":irc.freenode.net PING :message\r\n")
        messageTypePing = sr.messageType(socketData)
        socketData2 = bytearray(":irc.freenode.net ERROR :Something went horribly wrong")
        messageTypeError = sr.messageType(socketData2)
        self.assertTrue(messageTypePing == "PING" and messageTypeError == "ERROR")
    
    def testMessageData(self):
        sr = socketReader()
        socketData = bytearray(":irc.freenode.net ERROR :Something went horribly wrong")
        messageInfo = sr.messageData(socketData)
        self.assertTrue(messageInfo == "Something went horribly wrong")
        
    def testPriMsg(self):
        sr = socketReader()
        socketData = bytearray(":ubottu!ubbotu@localhost PRIVMSG magikid :Hi")
        messageInfo = sr.messageData(socketData)
        self.assertTrue(messageInfo == "Hi")
        
    def testPriMsgType(self):
        sr = socketReader()
        socketData = bytearray(":ubottu!ubbotu@localhost PRIVMSG magikid :Hi")
        messageType = sr.messageType(socketData)
        self.assertTrue(messageType == "PRIVMSG")
        
    def testSender(self):
        sr = socketReader()
        socketData = bytearray(":ubottu!ubbotu@localhost PRIVMSG magikid :Hi")
        messageSender = sr.sender(socketData)
        self.assertTrue(messageSender == "ubottu")
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()