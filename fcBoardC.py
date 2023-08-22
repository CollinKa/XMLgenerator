from Settings.HWSettings import *
from Settings.RegisterSettings import *
from Settings.MonitoringSettings import *
from Settings.FESettings import *
from Settings.GlobalSettings import *

class Module():
    def __init__(self,serialNo,SerialId,enable,Files,moduleType,test):
        self.serialNo = serialNo
        self.SerialId = SerialId
        self.enable = enable
        self.Files = Files
        self.moduleType = moduleType
        self.test = test
        self.chipList = []
    
    def adding_chips(self,Id,Lane,Configfile):
        self.chipList.append([Id,Lane,Configfile])
    
    def get_Chip_info(self):
        return self.chipList
    
    def getting_globalSetting(self):
        if self.moduleType == "RD53A":
            GO_Dict = globalSettings_DictA[self.test]
        else:
            GO_Dict = globalSettings_DictB[self.test]
        return GO_Dict
            

        


class board():
    def __init__(self,boardID,boardType,eventType):
        self.moduleList = []
        self.OpticalGroupDict = {'Id':"0",'FMCId':"0"}
        self.boardID = boardID
        self.boardType = boardType
        self.eventType = eventType
        

    def add_connection(self,address_table,connectionID,uri):
        self.address_table = address_table
        self.connectionID = connectionID
        self.uri = uri


    def adding_module(self,NewModule):
        self.moduleList.append(NewModule)

    def get_module(self,index):
        return self.moduleList[index]

    #to get proper setting, we need to know Ph2_ACF version, module type(RD53)
    def getting_registerSetting():
        return RegisterSettings
    

if __name__ == "__main__":
    #loading the data board1
    #first board
    module1 = Module("RH0001","1","1","files?","RD53A","IVCurve")
    module1.adding_chips("Id","Lane","Configfile")
    module2 = Module("RH0002","0","0","files?","RD53A","IVCurve")
    module2.adding_chips("Id1","Lane1","Configfile")
    board1 = board("0","RD53","VR") #in the order of board id, boardType, EventType
    board1.adding_module(module1)

    #second board
    module3 = Module("RH0003","0","0","files?","RD53A","IVCurve")
    module3.adding_chips("Id1","Lane1","Configfile")

    board2 = board("1","RD53","VR") #in the order of board id, boardType, EventType
    board2.adding_module(module3)

    #retrieving data
    module2_retrieve = board2.get_module(0)
    print(module2_retrieve.serialNo)
    
    


