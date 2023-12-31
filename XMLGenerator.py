#David's latest XML generator 

#to to adding extra section of if isOpticalLink:

import os
import json
from lxml import etree
from XMLgenerator.fcBoardC import *
from XMLgenerator.Settings.MonitoringSettings import *
from XMLgenerator.Settings.HWSettings import *
from XMLgenerator.Settings.RegisterSettings import *
from XMLgenerator.Settings.FESettings import *
from XMLgenerator.Settings.GlobalSettings import *

class XMLGenerator:
    """Use to create XML File"""


    #original init method. it is outdated
    """
    def __init__(self, root_node: str):
        self.root = etree.Element(root_node)
        self.initial_dictionary = {}
    """
    
    """
    def __init__(self, boardClass):
        self.board = boardClass
        self.loadingXML(self.board)
    """
    
        
    #after loading xml, using david's method create_xmlFile to create xml in the given path
    #disable the second board by default
    def loadingXML(self,board1,board2=None,isOpticalLink=False): 
        test = board1.GetTest() #adding this method to board class(TBD)
        xml = self.buildingRoot("HwDescription")
        boardList = []
        boardList.append(board1)


        #adding this section to setting folder as a mapping?
        StatusStr = 'Status'
        if "v4-11" in Ph2_ACF_VERSION:
            StatusStr = 'enable'
        if "v4-13" in Ph2_ACF_VERSION:
            StatusStr = 'enable'
        if "v4-14" in Ph2_ACF_VERSION:
            StatusStr = 'enable'



        if board2 != None:
            boardList.append(board2)
        for i in range(len(boardList)):
            #adding beboard sumelement
            beboardElement = self.add_node(xml,"BeBoard",{"Id" : boardList[i].boardID, "boardType" : boardList[i].boardType, "eventType" :"VR"})
            #adding connection subelement
            connectionElement = self.add_node(beboardElement,"connection",{"address_table" : boardList[i].address_table, "id" : "cmsinnertracker.crate0.slot0" , "uri" : boardList[i].uri})
            #connectionElement = self.add_node(beboardElement, "OpticalGroup",boardList[i].OpticalGroupDict)
            
            
            specificBoard = boardList[i]
            for OG in specificBoard.OGList.values():
                #OGList is a dictionary where keys are OGIG and value is the corresponding OGmodule Class
                connectionElement = self.add_node(beboardElement, "OpticalGroup",{"FMCId":OG.FMCId ,"Id":OG.Id}) #it complains OG is string. it seems I am printing a name of dictionary
                #hybridElement = self.add_node(connectionElement,"Hybrid",{"Id" : module.moduleId, "Name" : module.serialNo, StatusStr:module.status})


                #loop over modules that are conneting to a same fc board
                for module in OG.moduleList:
                    hybridElement = self.add_node(connectionElement,"Hybrid",{"Id" : module.moduleId, "Name" : module.serialNo, StatusStr:module.status})
                    if isOpticalLink:
                        #FIXME: Add additional stuff for optical link here.
                        Node_OpFiles = self.add_node(connectionElement, 'lqGBT_Files',{'path':"${PWD}/"})
                        Node_lqGBT = self.add_node(connectionElement, 'lqGBT',{'Id':'0','version':'1','configfile':'CMSIT_LqGBT-v1.txt','ChipAddress':'0x70','RxDataRate':'1280','RxHSLPolarity':'0','TxDataRate':'160','TxHSLPolarity':'1'})
                        Node_lqGBTsettings = self.add_node(Node_lqGBT, 'Settings')
                    self.add_node(hybridElement, "RD53_Files" ,{"file" : module.Files})
                    #loop over chips
                    type = module.moduleType
                    chiptype = module.chipType
                    for chip in module.chipList:
                        ChipElement = self.add_node(hybridElement,chiptype, {"Id" : chip[0], "Lane" : chip[1] , "configfile" : chip[2]})
                        #adding FESetting/ one setting per chip
                        VDDA = chip[3]
                        VDDD = chip[4]
                        print("adding FEsetttings debug")
                        self.addFESetting(ChipElement,type,test,VDDA,VDDD)
                
                    #adding global setting/  one setting per module
                    self.addGOSettings(hybridElement,chiptype,test) #Q: ask matt does muduole type is RD53 or CROC

            #adding Register setting/ one setting per board
            self.addRegisterSetting(beboardElement)

        #adding HWSetting
        #specificBoard.OGList.values()
        self.addHWSetting(xml,chiptype,test)

        #adding MonitorSetting
        self.addMonitorSetting(xml,chiptype,"1","1000")

        return xml


    def loadingData(self, boardClass):
       pass
        

    def buildingRoot(self, root_node): #used in usingXMLGen.py
        spcialRoot = etree.Element(root_node)
        return spcialRoot

    def add_element(self, parent, element):
        parent.append(element)


    def add_node(self, parent, tag, attrib=None, nsmap=None, **extra):
        element = etree.SubElement(parent, tag, attrib=attrib, nsmap=nsmap, **extra)
        return element


    def display_dict(self, dictionary=None):
        if dictionary is None:
            dictionary = self.initial_dictionary
        elif not isinstance(dictionary, dict):
            raise TypeError("Input not a dictionary")
        formatted_dict = json.dumps(dictionary, indent=4)
        print(formatted_dict)
    
    
    def dict_to_xml(self, dictionary=None, root_name=None):
        if dictionary is None:
            dictionary = self.initial_dictionary
        elif not isinstance(dictionary, dict):
            raise TypeError("You must input a dictionary.")
            
        if root_name is None:
            if len(dictionary) == 0:
                raise ValueError("The dictionary is empty!")
            elif len(dictionary) != 1:
                raise ValueError("The dictionary has multiple highest-level keys.\
                                \nPlease provide a new root name.")
            else:
                root_name = next(iter(dictionary.keys()))
        elif not isinstance(root_name, str):
            raise TypeError("Root name has to be a string.")
        
        outer_dict = {root_name: dictionary}

        def build_xml_element(element, dictionary):
            if isinstance(dictionary, dict):
                for key, value in dictionary.items():
                    if key == "@attributes":
                        element.attrib.update(value)
                    elif key == "#text":
                        element.text = value  # Set text content directly
                    elif isinstance(value, list):
                        for item in value:
                            sub_element = etree.SubElement(element, key)
                            build_xml_element(sub_element, item)
                    else:
                        sub_element = etree.SubElement(element, key)
                        build_xml_element(sub_element, value)
            elif isinstance(dictionary, str):
                element.text = dictionary

        root_element = etree.Element(root_name)
        build_xml_element(root_element, outer_dict[root_name])

        return root_element


    def display_xml(self, xml_element=None):
        if xml_element is None:
            xml_element = self.root
        xml_str = etree.tostring(xml_element, pretty_print=True).decode("utf-8")
        print(xml_str)


    def create_xmlFile(self, xml_element, filename=None, filepath=None):
        if isinstance(xml_element, str):
            root_element = etree.fromstring(xml_element)
        elif isinstance(xml_element, etree._Element):
            root_element = xml_element
        else:
            raise TypeError("Input must be a string containing XML data or an etree._Element object.")

        tree = etree.ElementTree(root_element)

        if filename is None:
            filename = "output.xml"

        if filepath is None:
            full_filepath = filename
        else:
            full_filepath = os.path.join(filepath, filename)
        print("full_filepath:" + str(full_filepath))
        tree.write(full_filepath, encoding="utf-8", xml_declaration=False, pretty_print=True)
    
    
    def xml_to_dict(self, xml_data):
        if isinstance(xml_data, str):
            root_element = etree.fromstring(xml_data)
        elif isinstance(xml_data, etree._Element):
            root_element = xml_data
        else:
            raise TypeError("Input must be a string containing XML data or an etree._Element object.")

        def convert_element(element):
            result = {}

            attributes = dict(element.attrib)
            if attributes:
                result["@attributes"] = attributes

            if element.text and element.text.strip():
                result["#text"] = element.text.strip()

            for child in element:
                if child.tag is etree.Comment:  # Skip comment elements
                    continue

                sub_element = convert_element(child)
                if child.tag in result:
                    # If the tag already exists, make it a list of sub-elements
                    if isinstance(result[child.tag], list):
                        result[child.tag].append(sub_element)
                    else:
                        existing_element = result.pop(child.tag)
                        result[child.tag] = [existing_element, sub_element]
                else:
                    result[child.tag] = sub_element

            return result
        
        self.initial_dictionary = {root_element.tag: convert_element(root_element)}

        return {root_element.tag: convert_element(root_element)}

    def read_xml_file(self, filename, filepath=None):
        if filepath is None:
            full_filepath = filename
        else:
            full_filepath = os.path.join(filepath, filename)

        if not os.path.exists(full_filepath):
            raise FileNotFoundError(f"File '{full_filepath}' not found.")

        with open(full_filepath, "r", encoding="utf-8") as file:
            # Read the first line to check for an encoding declaration
            first_line = file.readline()
            
            # Check if the first line contains the word "encoding" (case-insensitive)
            if "encoding" in first_line.lower():
                # Skip the first line if it contains an XML declaration
                xml_content = file.read()
            else:
                # If no declaration is found, include the first line and read the rest
                xml_content = first_line + file.read()

        return xml_content
    
    
    ###for debugging purposes###
    def create_txt_file_from_dict(self, dictionary=None, filename=None, filepath=None):
        if dictionary is None:
            dictionary = self.initial_dictionary
        indent = 0
        def write_dict_to_file(file, data, indent):
            for key, value in data.items():
                line = f"{indent * ' '}{key}:"
                if isinstance(value, dict):
                    file.write(line + '\n')
                    write_dict_to_file(file, value, indent + 1)
                else:
                    value_lines = str(value).split('\n')
                    if len(value_lines) == 1:
                        line += f" {value}"
                        file.write(line)
                    else:
                        file.write(line + '\n')
                        for vline in value_lines:
                            file.write(f"{(indent + 1) * ' '}{vline}\n")
                        
                if key != list(data.keys())[-1]:
                    file.write('\n')
        
        if filename is None:
            filename = "output_dictionary.txt"

        if filepath is None:
            full_filepath = filename
        else:
            full_filepath = os.path.join(filepath, filename)

        with open(full_filepath, "w", encoding="utf-8") as file:
            write_dict_to_file(file, dictionary, indent)
    
    #adding Setting parameters
    

    #monitor setting
    def addMonitorSetting(self,parent,boardtype,enable,sleeptime):
        # Create the Monitoring element with attributes
        monitoring_title = etree.SubElement(parent, "MonitoringSettings")
        monitoring_elem = etree.SubElement(monitoring_title, "Monitoring", enable="1", type="RD53A")

        # Create MonitoringSleepTime element
        monitoring_sleep_time_elem = etree.SubElement(monitoring_elem, "MonitoringSleepTime")
        monitoring_sleep_time_elem.text = sleeptime
        self.innerMonitorSetting(monitoring_elem,boardtype)

    def innerMonitorSetting(self,monitoring_elem,boardtype):
        if boardtype == "RD53A":
            MonDict = MonitoringListB
        else:
            MonDict = MonitoringListB
        # Create MonitoringElement elements based on the MonitoringListA dictionary
        for register, enable in MonDict.items():
            etree.SubElement(monitoring_elem, "MonitoringElement", device="RD53", enable=enable, register=register)
    
    #HWSetting
    def addInnerHWSetting(self,parent,chiptype,test):
        
        if chiptype == "RD53A":
            HWDict = HWSettings_DictA[test]
        else:
            HWDict = HWSettings_DictB[test]

        for name, value in HWDict.items():
            setting_elem = etree.SubElement(parent, "Setting", name=name)
            setting_elem.text = str(value)
    
    def addHWSetting(self,parent,boardtype,test):
        self.setting_title = etree.SubElement(parent, "Settings")
        self.addInnerHWSetting(self.setting_title,boardtype,test)

        

    #Register Setting
    def create_subelements_Register(self,parent, path, value):
        elements = path.split('.')
        for elem in elements:
            parent = etree.SubElement(parent, "Register", name=elem)
        parent.text = str(value)

    def addRegisterSetting(self,parent):
        for path, value in RegisterSettings.items():
            self.create_subelements_Register(parent, path, value)
        
    def addFESetting(self,parent,boardType,test,VDDAtrim=None,VDDDtrim=None):
        if boardType == "RD53A":
            FEDict = FESettings_DictA[test]
        else:
            FEDict = FESettings_DictB[test]
        
        if VDDAtrim == None:
            pass
        else:
            FEDict['VOLTAGE_TRIM_ANA'] = VDDAtrim
        
        if VDDDtrim == None:
            pass
        else:
            FEDict['VOLTAGE_TRIM_DIG'] = VDDDtrim


        self.add_node(parent,"Settings",FEDict)

    def addGOSettings(self,parent,chipType,test):
        if chipType == "RD53A":
            GODict = globalSettings_DictA[test]
        else:
            GODict = globalSettings_DictB[test]
            
        #calling add_node in the xml class
        self.add_node(parent,"Global",GODict)



if __name__ == "__main__":
    xmlgen = XMLGenerator("HwDescription")
    
    
    # #import CMSIT.xml
    # cmsfile = xmlgen.read_xml_file("CMSIT_RD53ATest.xml")
    
    # #convert xml to nested dictionary
    # cmsfile_dict = xmlgen.xml_to_dict(cmsfile)
    
    # #now recreate xml file from the dictionary
    # recreatedXML = xmlgen.dict_to_xml(cmsfile_dict, 354)
    
    # #save(create) the file
    # xmlgen.create_xmlFile(recreatedXML)
    
    # ##########  uncomment below to check...  #############
    # # 1. the dictionary by creating a txt file or print()
    # # 2. print recreated xml
    # ######################################################
    
    # # #create txt file of the dictionary
    # xmlgen.create_txt_file_from_dict(cmsfile_dict)
    
    # #show the dictionary on the prompt
    # xmlgen.display_dict(cmsfile_dict)
    
    # #show recreated xml strings on the prompt
    # xmlgen.display_xml(recreatedXML)
    