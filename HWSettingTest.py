from lxml import etree
from Settings.HWSettings import *


"""
# Define the dictionary of settings
settings = {
    "nEvents": "10000000.0",
    "nEvtsBurst": "10000.0",
    "VDDDTrimTarget": "1.3",
    # ... (other settings)
    "DataOutputDir": ""
}
"""

#test
boardType ="RD53A"
test = "PixelAlive"

if boardType == "RD53A":
    HWDict = HWSettings_DictA[test]
else:
    HWDict = HWSettings_DictB[test]


# Create the root element
root = etree.Element("T")

#HWDict = HWSettingsB_PixelAlive

# Iterate through the dictionary and create XML elements
for name, value in HWDict.items():
    setting_elem = etree.SubElement(root, "Setting", name=name)
    setting_elem.text = str(value)

# Create an XML tree from the root element
tree = etree.ElementTree(root)

# Serialize the XML tree to a string
xml_string = etree.tostring(tree, pretty_print=True, encoding="utf-8")

print(xml_string.decode("utf-8"))
