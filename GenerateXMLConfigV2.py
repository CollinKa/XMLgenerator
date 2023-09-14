
#the goal of this file is for creating a draft of GenerateXMLConfig with XMLGenerator

from fcBoardC import *
from XMLGenerator import *

def GenerateXMLConfig(firmwareList, testName, outputDir, **arg):
    outputFile = outputDir + "/CMSIT_" + testName + ".xml"
    fileNanme = "/CMSIT_" + testName + ".xml"
    filePath = outputDir
    #AllModules = firmwareList.getAllModules().values() # orginal code for doing the OG setup, but i ingore this section

    #ignore the section of setting up OGModule

    #in the old code boardID is always zero, we might need to change it later when using multiple boards
    #create the code for doing the summer first 
    boardID = "0"
    boardObject = board(boardID,testName)


    for module in firmwareList.getAllModules().values():
        moduleID = module.getModuleID()
        serialNumber = module.getModuleName()
        #status = "1" by default in Module class
        ModuleObject = Module(serialNumber,moduleID)
        boardObject.adding_module(ModuleObject)

    XMLGen = XMLGenerator()
    XMLFile=XMLGen.loadingXML(boardObject)
    #XMLGen.display_xml(XMLFile) #display xml in terminal
    #XMLGen.create_xmlFile(XMLFile,filePath,fileNanme)


    return outputFile

