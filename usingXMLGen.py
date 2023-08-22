#do fakesetup.sh first

from XMLGenerator import *


#load data for board & module class copy from fcBoardc.py
#loading the data board1
    #first board
module1 = Module("RH0001","1","1","files?","RD53A","IVCurve")
module1.adding_chips("Id1","Lane1","Configfile1")
module2 = Module("RH0002","0","0","files?","RD53A","IVCurve")
module2.adding_chips("Id2","Lane2","Configfile2")
board1 = board("0","RD53","VR") #in the order of board id, boardType, EventType
board1.adding_module(module1)
board1.adding_module(module2)
board1.add_connection("connectionID1","id1","uri1")
print(board1.address_table)



#second board
module3 = Module("RH0003","0","0","files?","RD53A","IVCurve")
module3.adding_chips("Id3","Lane3","Configfile3")
module3.adding_chips("Id4","Lane4","Configfile4")
board2 = board("1","RD53","VR") #in the order of board id, boardType, EventType
board2.adding_module(module3)
board2.add_connection("connectionID2","id2","uri2")

#extra parameter for Moniter setting
enable = "1"
sleeptime = "1000"


#list of fcboard 
boardList = [board1,board2]
test = "PixelAlive" # note: currently, modules attached to same FC7 can only do one test due to the xml tree struture.



#-----------------------------
#create the tree
Xtree = XMLGenerator("HWDescrption") 
top=Xtree.buildingRoot("HWDescrption") 


#create tree with mutiple boards
for i in range(len(boardList)):
    #adding beboard sumelement
    beboardElement = Xtree.add_node(top,"BeBoard",{"Id" : boardList[i].boardID, "boardType" : boardList[i].boardType, "eventType" :boardList[i].boardType})
    #adding connection subelement
    connectionElement = Xtree.add_node(beboardElement,"connection",{"address_table" : boardList[i].address_table, "id" : boardList[i].boardID, "uri" : boardList[i].uri})
    connectionElement = Xtree.add_node(beboardElement, "OpticalGroup",boardList[i].OpticalGroupDict)
    
    #loop over modules that are conneting to a same fc board
    for module in boardList[i].moduleList:
        hybridElement = Xtree.add_node(connectionElement,"Hybrid",{"Id" : module.SerialId, "Name" : module.serialNo})
        Xtree.add_node(hybridElement, "RD53_Files" ,{"file" : module.Files})
        #loop over chips
        type = module.moduleType
        for chip in module.chipList:
            ChipElement = Xtree.add_node(hybridElement,type, {"Id" : chip[0], "Lane" : chip[1] , "configfile" : chip[2]})
            #adding FESetting/ one setting per chip
            Xtree.addFESetting(ChipElement,type,test)
    
        #adding global setting/  one setting per module
        Xtree.addGOSettings(hybridElement,type,test) #Q: ask matt does muduole type is RD53 or CROC

    #adding Register setting/ one setting per board
    Xtree.addRegisterSetting(beboardElement)

#adding HWSetting
Xtree.addHWSetting(top,boardList[0].boardType,test)

#adding MonitorSetting
Xtree.addMonitorSetting(top,boardList[0].boardType,"1","1000")


#display the tree
Xtree.display_xml(top)

