"""
this file is rewrited based on XMLUtil.py

"""

#to-do don't hard code the stuff. think about what is need when you get a chip
from lxml import etree
from Settings.FESettings import *

def SetBeBoard(self, Id, boardType, eventType = "VR"):
    self.Id = str(Id)
    self.boardType = boardType
    self.eventType = eventType
PH2ACF_BASE_DIR = "GUI" #I make it up
# hard coding section
Id = str(0)
boardType = "RD53"
eventType = "VR"
address_table = "file://${PH2ACF_BASE_DIR}/settings/address_tables/CMSIT_address_table.xml" #need to fix this thing with fstring(TBD)
FMCId = "0"
enable = "1"

Id = "0"
Name = "zh0018" #serial number
enable = "1"



#start to create xml
root = etree.Element("HwDescription")
#root.append(etree.Element("BeBoard") )
sub_element1 = etree.SubElement(root, "BeBoard")

board_dict = {
    "Id": Id,
    "boardType": boardType,
    "eventType": eventType
}

sub_element1.attrib.update(board_dict)
sub_element2 = etree.SubElement(sub_element1, "connection")
connection_Dict ={
    "address_table" : address_table
}
sub_element2.attrib.update(connection_Dict)

sub_element3 = etree.SubElement(sub_element1, "OpticalGroup")
OpticalGroup_Dict = {
    "FMCId" : FMCId,
    "enable" : enable
}

sub_element3.attrib.update(OpticalGroup_Dict)

sub_element4 = etree.SubElement(sub_element3, "Hybrid")
Hybrid_Dict = {
    "Id" : Id,
    "Name" : Name,
    "enable" : enable
}
sub_element4.attrib.update(Hybrid_Dict)


sub_element5 = etree.SubElement(sub_element4, "RD53A")
sub_element6 = etree.SubElement(sub_element5, "setting")
sub_element6.attrib.update(FESettings)





print(etree.tostring(root, pretty_print=True,encoding='unicode'))