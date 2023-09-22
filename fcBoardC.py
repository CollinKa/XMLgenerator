from XMLgenerator.Settings.HWSettings import *
from XMLgenerator.Settings.RegisterSettings import *
from XMLgenerator.Settings.MonitoringSettings import *
from XMLgenerator.Settings.FESettings import *
from XMLgenerator.Settings.GlobalSettings import *
from XMLgenerator.Settings.settings import * #get the ModuleLaneMap dict for chip id,lane number

#note
"""
need to change the following
RD53 A/B chip type 
TFpx module type
"""


class Module():
    def __init__(self,serialNo,moduleId,chipInfo,status="1"):
        self.serialNo = serialNo
        self.moduleId = moduleId #input for “FMC port:” in GUI
        self.status = status # control by a click mark in gui start window.
        self.Files = "./" # following the xml file we have now
        self.moduleType = None #I need to add a method get module type automatically. #module type is RD53a?? or tfpx
        self.chipType = None
        self.test = None
        self.chipInfo = chipInfo
        self.chipList = []
        #self.txtFileLocatoin = "/home/RD53A/workspace/collin/Ph2_ACF_GUI_DICT_Submodule/Ph2_ACF_GUI/Ph2_ACF/settings"
        #self.VDDA = None
        #self.VDDD = None
        self.setModuleType()
        self.SetChipType()
        self.adding_chips()
        


    # I dont think adding_chips manually is useful, because the chip is a module is fixed
    #def adding_chips(self,Id,Lane,Configfile):
    def adding_chips(self):
        IdLaneDict=ModuleLaneMap[self.moduleType]
        numberOfChips = len(IdLaneDict)
        #for ChipID in range(numberOfChips): #wrong script
        print("self.chipInfo:" + str(self.chipInfo))
        for chip in self.chipInfo:    
            #chip ID start from 0, so it is ok to use for chipInfor
            #one of significant error that I can think of is manaully define module type doesn't match automaticaly setup chip Type 
            #chipInfo=self.chipInfo #it complains chipInfo is none
            #chip=chipInfo[ChipID]
            if not chip.getStatus():
                continue
            VDDA=chip.getVDDA()
            VDDD=chip.getVDDD()
            ChipId = chip.getID()
            Lane = chip.getLane()
            #ConfigfileName = os.environ.get(
            #        "PH2ACF_BASE_DIR"
            #    )+ f"/settings/RD53Files/CMSIT_RD53_{self.serialNo}_{self.moduleId}_{ChipId}.txt"   #follow the guide in GenerateXMLConfig() in guituil.py
            #self.chipList.append([ChipId,Lane,ConfigfileName,VDDA,VDDD])
            ConfigfileName = f"CMSIT_RD53_{self.serialNo}_{self.moduleId}_{ChipId}.txt"   #follow the guide in GenerateXMLConfig() in guituil.py
            self.chipList.append([ChipId,Lane,ConfigfileName,VDDA,VDDD])
            
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
            self.chipType = "RD53B"
        else:
            self.chipType = "RD53A"

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
        
class OGModule():
    def __init__(self,OGID,FMCID):
        self.Id=OGID
        self.FMCId=FMCID
        self.isOpticalLink = False
        #self.HyBridList = []
        self.moduleList = []
        self.test = None

    def SetOpticalGrp(self, Id, FMCId, isOptLink=False):
        self.Id=Id
        self.FMCId=FMCId
        self.isOpticalLink = isOptLink

    def adding_module(self,NewModule,chipInfo):
        NewModule.test =self.test
        NewModule.chipInfo = chipInfo
        self.moduleList.append(NewModule)

    #def AddHyBrid(self, HybridModule):
    #    self.HyBridList.append(HybridModule)

class board():
    def __init__(self,boardID,testName):
        #self.moduleList = []
        self.OGList = {}
        #self.OpticalGroupDict = {'Id':"0",'FMCId':"0"}
        self.boardID = boardID
        self.boardType = "RD53"
        self.eventType = "VR"
        self.test = testName
        self.ip_address = '0.0.0.0'
        self.id = "cmsinnertracker.crate0.slot0" 
        self.uri = "chtcp-2.0://localhost:10203?target={0}:50001".format(self.ip_address)
        self.address_table = "file://${PH2ACF_BASE_DIR}/settings/address_tables/CMSIT_address_table.xml"

    def addOG(self,OGID="0",FMCID="0"):
        OG0=OGModule(OGID,FMCID)
        OG0.test = self.test
        #dict = {OGID:OG0}
        self.OGList[OGID] = OG0

    def GetTest(self): 
        return self.test

    def add_connection(self,address_table,connectionID,uri):
        self.address_table = address_table
        self.connectionID = connectionID
        self.uri = uri

    """
    def adding_module(self,NewModule,chipInfo):
        NewModule.test =self.test
        NewModule.chipInfo = chipInfo
        self.moduleList.append(NewModule)
    """
    
    #useless code
    #def get_module(self,index):
    #    return self.moduleList[index]


    #useless code
    #to get proper setting, we need to know Ph2_ACF version, module type(RD53)
    #def getting_registerSetting():
    #    return RegisterSettings
    

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
    
    
    


