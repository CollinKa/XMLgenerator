from lxml import etree

# Define the MonitoringListA dictionary
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

# Create the root element
root = etree.Element("MonitoringSettings")

# Create the Monitoring element with attributes
monitoring_elem = etree.SubElement(root, "Monitoring", enable="1", type="RD53A")

# Create MonitoringSleepTime element
monitoring_sleep_time_elem = etree.SubElement(monitoring_elem, "MonitoringSleepTime")
monitoring_sleep_time_elem.text = "10000"

# Create MonitoringElement elements based on the MonitoringListA dictionary
for register, enable in MonitoringListA.items():
    monitoring_element_elem = etree.SubElement(
        monitoring_elem, "MonitoringElement", device="RD53", enable=enable, register=register
    )

# Create an XML tree from the root element
tree = etree.ElementTree(root)

# Serialize the XML tree to a string
html_string = etree.tostring(tree, pretty_print=True, encoding="utf-8")

print(html_string.decode("utf-8"))
