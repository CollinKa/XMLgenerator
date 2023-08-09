from lxml import etree
from itertools import product

PH2ACF_BASE_DIR = "GUI"

#Beboards [First Beboard, second Beboard, ...]
boardId = ["0", "1"]
boardType = ["RD53", "RD53"]
eventType = ["VR", "VR"]

#Connection [First Beboard, second Beboard, ...]
address_table = ["file://${PH2ACF_BASE_DIR}/settings/address_tables/CMSIT_address_table.xml",
                 "file://${PH2ACF_BASE_DIR}/settings/address_tables/CMSIT_address_table.xml"] #need to fix this thing with fstring(TBD)
connectionId = ["cmsinnertracker.crate0.slot0",
                "cmsinnertracker.crate0.slot0"]
connectionUri = ["chtcp-2.0://localhost:10203?target=192.168.1.80:50001",
                 "chtcp-2.0://localhost:10203?target=192.168.1.81:50001"]

#OpticalGroup
FMCId = ["0"]
enable = ["1"]

#Hybrid
hybridId = ["0"]
hybridName = ["zh0018"] #serial number
enable = ["1"]

#RD53_Files
RD53File = ["./"]

#First Board Lanes
board1_Lane = ["0", "1", None, "3"]
board1_RD53AId = ["4", None ,None, "5"]
board1_RD53BId = [None, "4", None, None]
board1_configfile = ["CMSIT_RD53_zh0018_0_4.txt",
                     "CMSIT_RD53_zh0018_0_2.txt",
                     None,
                     "CMSIT_RD53_zh0018_0_5.txt",]

#Second Board Lanes
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


def beboard(beboardNum):
    index = beboardNum - 1
    beboardOne = etree.Element("BeBoard", {"Id": boardId[index], "boardType": boardType[index], "eventType": eventType[index]})
    beboards.append(beboardOne)

    connection_Dict = {
                    "address_table": address_table[index],
                    "connectionId": connectionId[index],
                    "connectionUri": connectionUri[index],
                    }
    root1a1 = add_node(beboardOne, "connection", connection_Dict)
    for i in range(len(FMCId)):
        optical_group = add_node(beboardOne, "OpticalGroup", {"FMCId": FMCId[i], "enable": enable[i]})
        
        for j in range(len(hybridId)):
            hybrid = add_node(optical_group, "Hybrid", {"Id": hybridId[j], "Name": hybridName[j], "enable": enable[j]})

            for k in range(len(RD53File)):
                rd53_files = add_node(hybrid, "RD53_Files", {"file": RD53File[k]})

            for l in range(len(eval(f"board{beboardNum}_RD53AId"))):
                if eval(f"board{beboardNum}_Lane[l]") and eval(f"board{beboardNum}_RD53AId[l]") is not None:
                    rd53a = add_node(hybrid, "RD53A", {"Id": eval(f"board{beboardNum}_RD53AId[l]"), "Lane": eval(f"board{beboardNum}_Lane[l]"), "configfile": eval(f"board{beboardNum}_configfile[l]")})
                    settings = add_node(rd53a, "Settings", {"key": "value"})

                elif eval(f"board{beboardNum}_Lane[l]") and eval(f"board{beboardNum}_RD53BId[l]") is not None:
                    rd53b = add_node(hybrid, "RD53B", {"Id": eval(f"board{beboardNum}_RD53BId[l]"), "Lane": eval(f"board{beboardNum}_Lane[l]"), "configfile": eval(f"board{beboardNum}_configfile[l]")})
                    settings = add_node(rd53b, "Settings", {"key": "value"})

beboard(1)
beboard(2)

for each_beboard in beboards:
    root1.append(each_beboard)

tree = etree.ElementTree(root1)
tree.write("output.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")