class chatDB():
    def __init__(self):
        self.db = {}
        self.id = 0

    def insertmsg(self,msg):
        self.id = self.id + 1 
        self.db[self.id] = msg 

    def getmsg(self,msgid):
        if len(self.db) == 0:
            return 'No message yet!'
        elif msgid == 0:
            return '\n'.join(self.db.values())
                
        elif msgid != 0:
            tmp = self.db[msgid]
            return tmp
        else:
            return '\n'
        
