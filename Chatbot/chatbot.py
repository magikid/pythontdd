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