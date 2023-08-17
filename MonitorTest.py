from lxml import etree
from Settings.MonitoringSettings import *

# Define the MonitoringListA dictionary
#choose RD53A/B


"""
MonitoringListA = {
    'VIN_ana_ShuLDO': "0",
    'VOUT_ana_ShuLDO': "0",
    'VIN_dig_ShuLDO': "0",
    'VOUT_dig_ShuLDO': "0",
    'ADCbandgap': "0",
    'Iref': "0",
    'TEMPSENS_1': "0",
    'TEMPSENS_4': "1",
}
"""

# Create the root element
root = etree.Element("HWDes")
def addMonitorSetting(parent,boardtype,enable,sleeptime):
    # Create the Monitoring element with attributes
    monitoring_title = etree.SubElement(parent, "MonitoringSettings")
    monitoring_elem = etree.SubElement(monitoring_title, "Monitoring", enable="1", type="RD53A")

    # Create MonitoringSleepTime element
    monitoring_sleep_time_elem = etree.SubElement(monitoring_elem, "MonitoringSleepTime")
    monitoring_sleep_time_elem.text = sleeptime

    if boardtype == "RD53A":
        MonDict = MonitoringListB
    else:
        MonDict = MonitoringListB
    # Create MonitoringElement elements based on the MonitoringListA dictionary
    for register, enable in MonDict.items():
        monitoring_element_elem = etree.SubElement(
            monitoring_elem, "MonitoringElement", device="RD53", enable=enable, register=register
        )

addMonitorSetting(root,"RD53A","1","1000")
# Create an XML tree from the root element
tree = etree.ElementTree(root)

# Serialize the XML tree to a string
html_string = etree.tostring(tree, pretty_print=True, encoding="utf-8")

print(html_string.decode("utf-8"))
