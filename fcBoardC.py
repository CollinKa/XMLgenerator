from Settings.HWSettings import *
from Settings.RegisterSettings import *
from Settings.MonitoringSettings import *
from Settings.FESettings import *
from Settings.GlobalSettings import *
from Settings.settings import * #get the ModuleLaneMap dict for chip id,lane number

#note
"""
need to change the following
RD53 A/B chip type 
TFpx module type
"""


class Module():
    def __init__(self,serialNo,moduleId,status="1"):
        self.serialNo = serialNo
        self.moduleId = moduleId #input for “FMC port:” in GUI
        self.status = status # control by a click mark in gui start window.
        self.Files = "./" # following the xml file we have now
        self.moduleType = None #I need to add a method get module type automatically. #module type is RD53a?? or tfpx
        self.chipType = None
        self.test = None
        self.chipList = []
        self.txtFileLocatoin = "/home/RD53A/workspace/collin/Ph2_ACF_GUI_DICT_Submodule/Ph2_ACF_GUI/Ph2_ACF/settings"
        self.VDDA = None
        self.VDDD = None
        self.setModuleType()
        self.SetChipType()
        self.adding_chips()


    # I dont think adding_chips manually is useful, because the chip is a module is fixed
    #def adding_chips(self,Id,Lane,Configfile):
    def adding_chips(self,VDDA,VDDD):
        IdLaneDict=ModuleLaneMap[self.moduleType]
        numberOfChips = len(IdLaneDict)
        for ChipID in range(numberOfChips):
            ChipIdStr = str(ChipID)
            Lane = IdLaneDict[ChipIdStr]
            ConfigfileName = os.environ.get(
                    "PH2ACF_BASE_DIR"
                )+ f"/settings/RD53Files/CMSIT_RD53_{self.serialNo}_{self.moduleId}_{ChipID}.txt"   #follow the guide in GenerateXMLConfig() in guituil.py
            self.chipList.append([ChipIdStr,Lane,ConfigfileName,VDDA,VDDD])
            
            #create the txt file for each chip(leave it blank now)
            #I dont understand what does IN file used for SetupRD53ConfigfromFile()
            # disable cp command beofre using it in GUI 
            #try:
            #    os.system("cp {0}/CMSIT_{1} {2}").format(self.txtFileLocatoin,self.chipType,ConfigfileName)
            #except OSError:
            #    print("Can not copy the XML files {0} to {1}").format(self.txtFileLocatoin,ConfigfileName)

    def setModuleType(self):
        if 'ZH' in self.serialNo:
            self.moduleType = "TFPX Quad"
        if 'SCC' in self.serialNo:
            self.moduleType = "SingleSCC"
        if 'RH' in self.serialNo:
            self.moduleType = "CROC 1x2"
        # there should be more
    
    def getModuleType(self):
        return self.moduleType

    def SetChipType(self):
        if 'CROC' in self.moduleType:
            self.chipType = "RD53A"
        else:
            self.chipType = "RD53B"

    def getChipType(self):
        return self.chipType
        
    
    def get_Chip_info(self):
        return self.chipList
    
    def getting_globalSetting(self):
        if self.moduleType == "RD53A":
            GO_Dict = globalSettings_DictA[self.test]
        else:
            GO_Dict = globalSettings_DictB[self.test]
        return GO_Dict
            
    def setTest(self,testName):
        self.test = testName
        


class board():
    def __init__(self,boardID,testName):
        self.moduleList = []
        self.OpticalGroupDict = {'Id':"0",'FMCId':"0"}
        self.boardID = boardID
        self.boardType = "RD53"
        self.eventType = "VR"
        self.test = testName
        self.ip_address = '0.0.0.0'
        self.id = "cmsinnertracker.crate0.slot0" 
        self.uri = "chtcp-2.0://localhost:10203?target={0}:50001".format(self.ip_address)
        self.address_table = "file://${PH2ACF_BASE_DIR}/settings/address_tables/CMSIT_address_table.xml"

    def GetTest(self): 
        return self.test

    def add_connection(self,address_table,connectionID,uri):
        self.address_table = address_table
        self.connectionID = connectionID
        self.uri = uri


    def adding_module(self,NewModule):
        NewModule.test =self.test
        self.moduleList.append(NewModule)

    def get_module(self,index):
        return self.moduleList[index]

    #to get proper setting, we need to know Ph2_ACF version, module type(RD53)
    def getting_registerSetting():
        return RegisterSettings
    

if __name__ == "__main__":
    #loading the data board1
    #first board

    #outdated code need to be removed
    """
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
    """
    
    
    


