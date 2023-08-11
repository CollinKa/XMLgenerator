#check warning
#do fakesetup.sh first
#ask optical group, same test for all chip on a same module?

from XMLGenerator2 import *


#load data for board & module class copy from fcBoardc.py
#loading the data board1
    #first board
module1 = Module("RH0001","1","1","files?","RD53A","IVCurve")
module1.adding_chips("Id","Lane","Configfile")
module2 = Module("RH0002","0","0","files?","RD53A","IVCurve")
module2.adding_chips("Id1","Lane1","Configfile")
board1 = board("0","RD53","VR") #in the order of board id, boardType, EventType
board1.adding_module(module1)
board1.adding_module(module2)
board1.add_connection("connectionID1","id1","uri1")
print(board1.address_table)



#second board
module3 = Module("RH0003","0","0","files?","RD53A","IVCurve")
module3.adding_chips("Id1","Lane1","Configfile")
board2 = board("1","RD53","VR") #in the order of board id, boardType, EventType
board2.adding_module(module3)
board2.add_connection("connectionID2","id2","uri2")




#list of fcboard 
boardList = [board1,board2]



#-----------------------------
#create the tree
Xtree = XMLGenerator("HWDescrption") #bug1: probably need to fix the init method, so it can work with usingXMLgen

top=Xtree.buildingRoot("HWDescrption") 


#catch a bug talk to david.


#create tree with mutiple boards
for i in range(len(boardList)):
    #adding beboard sumelement
    beboardElement = Xtree.add_node(top,"BeBoard",{"Id" : boardList[i].boardID, "boardType" : boardList[i].boardType, "eventType" :boardList[i].boardType})
    #adding connection subelement
    
    connectionElement = Xtree.add_node(beboardElement,"connection",{"address_table" : boardList[i].address_table, "id" : boardList[i].boardID, "uri" : boardList[i].uri})
    
    #optical group?related to FMC
    #Warning!! so far I assume hybrid is the sub element of connection, I should fix it into Optical group later
    
    #loop over modules that are conneting to a same fc board
    for module in boardList[i].moduleList:
        #print(i)
        #bug2: it seem connectionElement has some issue, check Ryan's code
        hybridElement = Xtree.add_node(connectionElement,"Hybrid",{"Id" : module.SerialId, "Name" : module.serialNo})
        Xtree.add_node(hybridElement, "RD53_Files" ,{"file" : module.Files})
        #loop over chips
        type = module.moduleType
        for chip in module.chipList:
            ChipElement = Xtree.add_node(hybridElement,type, {"Id" : chip[0], "Lane" : chip[1] , "configfile" : chip[2]})


Xtree.display_xml_custom(top)

