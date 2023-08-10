class board():
    def __init__(self,test):
        self.test = test #test for all module connected to same board should be the same?

    def adding_module(self,serialNo,Id,enable,Files,moduleType,test):
        self.serialNo = serialNo
        self.SerialId = Id
        self.enable = enable
        self.Files = Files
        self.moduleType = moduleType
        self.test = test

    def adding_chips(self,Id,Lane,Configfile):
        self.chipId = Id
        self.chipLane = Lane
        self.Configfile = Configfile

    def get_module_info(self):
        return self.serialNo, self.SerialId, self.Files, self.moduleType


    def getting_registerSetting():
        return 

    def getting_HWSetting():
        return #dict

    def getting_monitorSetting():
        return #dict
    
    def getting_globalSetting():
        return #dict

class OpticleGroup():
    def adding_FMC(FMCid,id):
        pass  

board1 = board()
board.