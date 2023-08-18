from XMLGenerator import XMLGenerator
from EditDictionary import EditDictionary
import data as d

class pixelDictConstruct:
    def __init__(self):
        self.gen = XMLGenerator()
        self.edit = EditDictionary()
        self.counter:int = 0
        
    def _getColumn(self, index, *lists):
        lengths = [len(lst) for lst in lists]
        
        if all(length == lengths[0] for length in lengths):
            columnlist = [lst[index] for lst in lists]
            return columnlist
        else:
            raise ValueError('Input lists have different lengths')

    def createRoot(self, tag_name):
        base = self.edit.createRoot(tag_name)
        return base

    def createbranch(self, tag_name, attribList, dataList):
        root = self.edit.createRoot(tag_name)
        attrib_claim = self.edit.createRoot('attributesClaimer')
        branch = self.edit.createDict(attribList, dataList)
        self.edit.addDict(attrib_claim, branch, ['attributesClaimer'])
        self.edit.addDict(root, attrib_claim)
        return root
    
    def createregister(self, registerList, registervaluelist):
        root0 = self.edit.createRoot("Register")
        attrib_claim0 = self.edit.createRoot('attributesClaimer')
        Reg0 = self.edit.createDict(['name'], [registerList[0]])
        self.edit.addDict(attrib_claim0,Reg0)
        self.edit.addDict(root0,attrib_claim0) 
        
        root1 = self.edit.createRoot("Register")
        attrib_claim1 = self.edit.createRoot('attributesClaimer')
        Reg1 = self.edit.createDict(['name'], [registerList[1]])
        self.edit.addDict(attrib_claim1,Reg1)
        self.edit.addDict(root1,attrib_claim1)
        
        root2 = self.edit.createRoot("Register")
        attrib_claim2 = self.edit.createRoot('attributesClaimer')
        Reg2 = self.edit.createDict(['name'], [registerList[2]])
        self.edit.addDict(attrib_claim2,Reg2)
        self.edit.addDict(root2,attrib_claim2)
        
        root3 = self.edit.createRoot("Register")
        attrib_claim3 = self.edit.createRoot('attributesClaimer')
        Reg3 = self.edit.createDict(['name'], [registerList[3]])
        self.edit.addDict(attrib_claim3,Reg3)
        value = self.edit.createDict(['textClaimer'], registervaluelist)
        self.edit.addDict(attrib_claim3,value)
        self.edit.addDict(root3,attrib_claim3)
        
        self.edit.addDict(root2, root3)
        self.edit.addDict(root1, root2)
        self.edit.addDict(root0, root1) 
        
        return root0       
    
    def beboardinfo(self, index):
        info = self._getColumn(index, d.boardId, d.boardType, d.eventType)
        return info
    
    def connectioninfo(self, index):
        info = self._getColumn(index, d.address_table, d.connectionId, d.connectionUri)
        return info
    
    def opticalgroupinfo(self, index):
        info = self._getColumn(index, d.OpticalGroup_Id, d.FMCId)
        return info
    
    def hybridinfo(self, boardnumber, index):
        attr_name_prefix = f'board{boardnumber}_'
        hybrid_id_attr = f'{attr_name_prefix}hybridId'
        hybrid_name_attr = f'{attr_name_prefix}hybridName'
        enable_attr = f'{attr_name_prefix}enable'

        hybrid_id = getattr(d, hybrid_id_attr)
        hybrid_name = getattr(d, hybrid_name_attr)
        enable = getattr(d, enable_attr)

        info = self._getColumn(index, hybrid_id, hybrid_name, enable)
        return info
    
    def RD53filesinfo(self, boardnumber, index):
        listname = f'board{boardnumber}_RD53File'
        rd53_file = getattr(d, listname)
        info = self._getColumn(index, rd53_file)
        return info
        
    def RD53info(self, boardnumber, hybridnumber, letter, index):
        attr_name_prefix = f'board{boardnumber}_hybrid{hybridnumber}_'
        lane_attr = f'{attr_name_prefix}Lane'
        rd53_id_attr = f'{attr_name_prefix}RD53{letter}Id'
        config_file_attr = f'{attr_name_prefix}configfile'

        lane = getattr(d, lane_attr)
        rd53_id = getattr(d, rd53_id_attr)
        config_file = getattr(d, config_file_attr)

        info = self._getColumn(index, lane, rd53_id, config_file)
        return info
    
    def RD53settingsinfo(self, boardnumber, hybridnumber, letter, index):
        settingsName = f'board{boardnumber}_hybrid{hybridnumber}_RD53{letter}_Settings'
        settings = getattr(d, settingsName)
        info = settings[index]
        return info
    
    def registervalue(self, boardnumber, registernumber):
        registerName = f'board{boardnumber}_register{registernumber}_value'
        value = getattr(d, registerName)
        return value
    
    def addDict(self, base_dictionary: dict, dict_to_add: dict, path=None):
        self.edit.addDict(base_dictionary, dict_to_add, path)
    
        
if __name__ == '__main__':
    con = pixelDictConstruct()
    ed = EditDictionary()
    gen = XMLGenerator()
        
    root = con.createRoot('HwDescription')
    beboard0 = con.createbranch('Beboard', d.Beboard_attrib, con.beboardinfo(0))
    connection0 = con.createbranch('connection', d.connection_attrib, con.connectioninfo(0))
    optical0 = con.createbranch('OpticalGroup', d.OpticalGroup_attrib, con.opticalgroupinfo(0))
    hybrid0 = con.createbranch('Hybrid', d.Hybrid_attrib, con.hybridinfo(0,0))
    RD53files = con.createbranch('RD53_Files', d.RD53_Files_attrib, con.RD53filesinfo(0,0))
    
    RD53Alanes = 4
    RD53A = [] 
    RD53A_set = []

    for i in range(RD53Alanes):
        instance = con.createbranch('RD53A', d.RD53A_attrib, con.RD53info(0, 0, "A", i))
        RD53A.append(instance)
        # instance2 = con.createbranch('Settings', d.RD53A_Settings_attrib, con.RD53settingsinfo(0,0,"A",i))
        # RD53A_set.append(instance2)

    # registernum = 10
    # register_list = []

    # for i in range(registernum):
    #     register = con.createregister(getattr(d, f"board0_Register{i}"), con.registervalue(0, i))
    #     register_list.append(register)


    # for i in range(RD53Alanes):
    #     con.addDict(RD53A[i], RD53A_set[i])

    con.addDict(hybrid0, RD53files)
    
    for i in range(RD53Alanes):
        con.addDict(hybrid0, RD53A[i])

    con.addDict(optical0, hybrid0)
    con.addDict(beboard0, connection0)
    con.addDict(beboard0, optical0)

    # for i in range(registernum):
    #     con.addDict(beboard0,register_list[i])
        
    con.addDict(root, beboard0)
    
    #ed.visualizeDict(root)
    testxml = gen.dict_to_xml(root)
    gen.display_xml(testxml)

    # root = con.createRoot('HwDescription')
    # beboard0 = con.createbranch('Beboard', d.Beboard_attrib, con.beboardinfo(0))
    # connection0 = con.createbranch('connection', d.connection_attrib, con.connectioninfo(0))
    # optical0 = con.createbranch('OpticalGroup', d.OpticalGroup_attrib, con.opticalgroupinfo(0))
    # hybrid0 = con.createbranch('Hybrid', d.Hybrid_attrib, con.hybridinfo(0,0))
    # RD53files = con.createbranch('RD53_Files', d.RD53_Files_attrib, con.RD53filesinfo(0,0))
    # RD53A0 = con.createbranch('RD53A', d.RD53A_attrib, con.RD53info(0,0,"A",0))
    # RD53A1 = con.createbranch('RD53A', d.RD53A_attrib, con.RD53info(0,0,"A",1))
    # RD53A2 = con.createbranch('RD53A', d.RD53A_attrib, con.RD53info(0,0,"A",2))
    # RD53A3 = con.createbranch('RD53A', d.RD53A_attrib, con.RD53info(0,0,"A",3))
    # RD53A0settings = con.createbranch('Settings', d.RD53A_Settings_attrib, con.RD53settingsinfo(0,0,"A",0))
    # RD53A1settings = con.createbranch('Settings', d.RD53A_Settings_attrib, con.RD53settingsinfo(0,0,"A",1))
    # RD53A2settings = con.createbranch('Settings', d.RD53A_Settings_attrib, con.RD53settingsinfo(0,0,"A",2))
    # RD53A3settings = con.createbranch('Settings', d.RD53A_Settings_attrib, con.RD53settingsinfo(0,0,"A",3))

    # register0 = con.createregister(d.board0_Register0, con.registervalue(0,0))
    # register1 = con.createregister(d.board0_Register1, con.registervalue(0,1))
    # register2 = con.createregister(d.board0_Register2, con.registervalue(0,2))
    # register3 = con.createregister(d.board0_Register3, con.registervalue(0,3))
    # register4 = con.createregister(d.board0_Register4, con.registervalue(0,4))
    # register5 = con.createregister(d.board0_Register5, con.registervalue(0,5))
    # register6 = con.createregister(d.board0_Register6, con.registervalue(0,6))
    # register7 = con.createregister(d.board0_Register7, con.registervalue(0,7))
    # register8 = con.createregister(d.board0_Register8, con.registervalue(0,8))
    # register9 = con.createregister(d.board0_Register9, con.registervalue(0,9))


    # con.addDict(RD53A0, RD53A0settings)
    # con.addDict(RD53A1, RD53A1settings)
    # con.addDict(RD53A2, RD53A2settings)
    # con.addDict(RD53A3, RD53A3settings)
    
    # con.addDict(hybrid0, RD53files)
    # con.addDict(hybrid0, RD53A0)
    # con.addDict(hybrid0, RD53A1)
    # con.addDict(hybrid0, RD53A2)
    # con.addDict(hybrid0, RD53A3)
    
    # con.addDict(optical0, hybrid0)

    # con.addDict(beboard0, connection0)
    # con.addDict(beboard0, optical0)
    
    # con.addDict(beboard0,register0)
    # con.addDict(beboard0,register1)
    # con.addDict(beboard0,register2)
    # con.addDict(beboard0,register3)
    # con.addDict(beboard0,register4)
    # con.addDict(beboard0,register5)
    # con.addDict(beboard0,register6)
    # con.addDict(beboard0,register7)
    # con.addDict(beboard0,register8)
    # con.addDict(beboard0,register9)
        
    # con.addDict(root, beboard0)

    
    # ed.visualizeDict(root)

    

    
