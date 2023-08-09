from lxml import etree
from itertools import product

PH2ACF_BASE_DIR = "GUI"

#Information for lists are to be retrieved from hardware, other places, or direct user input.
#Lists in each "block" should have the equal length and I plan to add that.


#Beboards [first beboard, second beboard, ...]
boardId = ["0", "1"]
boardType = ["RD53", "RD53"]
eventType = ["VR", "VR"]

#Connection [first beboard, second beboard, ...]
address_table = ["file://${PH2ACF_BASE_DIR}/settings/address_tables/CMSIT_address_table.xml",
                 "file://${PH2ACF_BASE_DIR}/settings/address_tables/CMSIT_address_table.xml"] #need to fix this thing with fstring(TBD)
connectionId = ["cmsinnertracker.crate0.slot0",
                "cmsinnertracker.crate0.slot0"]
connectionUri = ["chtcp-2.0://localhost:10203?target=192.168.1.80:50001",
                 "chtcp-2.0://localhost:10203?target=192.168.1.81:50001"]

#OpticalGroup [first beboard, second beboard, ...]
FMCId = ["0", "1"]
enable = ["1", "1"]

#First Board Hybrid
#These lists should all have equal length
board1_hybridId = ["0","1"]
board1_hybridName = ["zh0018", "zh0019"] #serial number
board1_enable = ["1", "1"]
#First Board RD53_Files [first hybrid, second hybrid, ...]
board1_RD53File = ["./", "b"]

#Second Board Hybrid
#hybridId, hybridName, enable lists should all have equal length
board2_hybridId = ["0", "1", "2"]
board2_hybridName = ["zh0020", "zh0021", "zh0022"]
board2_enable = ["1", "1", "1"]
#Second Board RD53_Files [first hybrid, second hybrid, ...]
board2_RD53File = ["c", "d", "e"]

#First Board Lanes
#Lists should have equal length
#"None" represents the lane that are not being used.
board1_Lane = ["0", "1", None, "3"]
board1_RD53AId = ["4", None ,None, "5"]
board1_RD53BId = [None, "4", None, None]
board1_configfile = ["CMSIT_RD53_zh0018_0_4.txt",
                     "CMSIT_RD53_zh0018_0_2.txt",
                     None,
                     "CMSIT_RD53_zh0018_0_5.txt",]

#Second Board Lanes
#Lists should have equal length
board2_Lane = ["0", "1", "2", None]
board2_RD53AId = ["1", "7", "9", None]
board2_RD53BId = [None, None, None, None]
board2_configfile = ["CMSIT_RD53_zh0018_0_4.txt",
                     "CMSIT_RD53_zh0018_0_2.txt",
                     "CMSIT_RD53_zh0018_0_7.txt",
                     "CMSIT_RD53_zh0018_0_5.txt",]




# Create XML element with attributes
def add_node(parent, tag, attrib=None, nsmap=None, **_extra):
    element = etree.SubElement(parent, tag, attrib=attrib, nsmap=nsmap, **_extra)
    return element

# Start to create xml
root1 = etree.Element("HwDescription")
beboards = []


#some instances are created but never used. They are for possible future changes or addition. 

def beboard(beboardNum):
    index = beboardNum - 1
    beboard = etree.Element("BeBoard", {"Id": boardId[index], "boardType": boardType[index], "eventType": eventType[index]})
    beboards.append(beboard)

    connection_Dict = {
                    "address_table": address_table[index],
                    "connectionId": connectionId[index],
                    "connectionUri": connectionUri[index],
                    }
    connection = add_node(beboard, "connection", connection_Dict)
    
    optical_group = add_node(beboard, "OpticalGroup", {"FMCId": FMCId[index], "enable": enable[index]})
    for i in range(len(eval(f"board{beboardNum}_hybridId"))):
        hybrid = add_node(optical_group, "Hybrid", {"Id": eval(f"board{beboardNum}_hybridId[i]"), "Name": eval(f"board{beboardNum}_hybridName[i]"), "enable": eval(f"board{beboardNum}_enable[i]")})
        rd53_files = add_node(hybrid, "RD53_Files", {"file": eval(f"board{beboardNum}_RD53File[i]")})

        for l in range(len(eval(f"board{beboardNum}_RD53AId"))):
            if eval(f"board{beboardNum}_Lane[l]") and eval(f"board{beboardNum}_RD53AId[l]") is not None:
                rd53a = add_node(hybrid, "RD53A", {"Id": eval(f"board{beboardNum}_RD53AId[l]"), "Lane": eval(f"board{beboardNum}_Lane[l]"), "configfile": eval(f"board{beboardNum}_configfile[l]")})
                settings = add_node(rd53a, "Settings", {"key": "value"})

            elif eval(f"board{beboardNum}_Lane[l]") and eval(f"board{beboardNum}_RD53BId[l]") is not None:
                rd53b = add_node(hybrid, "RD53B", {"Id": eval(f"board{beboardNum}_RD53BId[l]"), "Lane": eval(f"board{beboardNum}_Lane[l]"), "configfile": eval(f"board{beboardNum}_configfile[l]")})
                settings = add_node(rd53b, "Settings", {"key": "value"})



beboard(1)
beboard(2) #only if there is a second FC7
#could be used even when there are more than 2 fc7.

for each_beboard in beboards:
    root1.append(each_beboard)

tree = etree.ElementTree(root1)
tree.write("output.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")