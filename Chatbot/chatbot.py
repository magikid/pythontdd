'''

These are the websites that I've been referencing:
http://blog.initprogram.com/2010/10/14/a-quick-basic-primer-on-the-irc-protocol/
http://colinhorne.blogspot.com/2005/01/irc-protocol.html
http://docs.python.org/release/2.6/

'''

class chatbot():
    pass    

class socketReader():
    def __init__(self):
        pass
        
    def messageType(self, socketData):
        strSocketData = str(socketData)
        return strSocketData.split(' ',2)[1]
    
    def messageData(self, socketData):
        strSocketData = str(socketData)
        return strSocketData.split(':',2)[2]
        
    def sender(self, socketData):
        strSocketData = str(socketData)
        return strSocketData.split('!',1)[0].strip(':')