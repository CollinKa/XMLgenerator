from lxml import etree
from Settings.RegisterSettings import *
"""
RegisterSettings = {
    "user.ctrl_regs.fast_cmd_reg_2.trigger_source": 2,
    "user.ctrl_regs.fast_cmd_reg_2.HitOr_enable_l12": 0,
    "user.ctrl_regs.ext_tlu_reg1.dio5_ch1_thr": 128,
    "user.ctrl_regs.ext_tlu_reg1.dio5_ch2_thr": 128,
    "user.ctrl_regs.ext_tlu_reg2.dio5_ch3_thr": 128,
    "user.ctrl_regs.ext_tlu_reg2.dio5_ch4_thr": 128,
    "user.ctrl_regs.ext_tlu_reg2.dio5_ch5_thr": 128,
    "user.ctrl_regs.ext_tlu_reg2.tlu_delay": 0,
    "user.ctrl_regs.ext_tlu_reg2.ext_clk_en": 0,
    "user.ctrl_regs.fast_cmd_reg_3.triggers_to_accept": 10
}
"""
# Define the dictionary of register settings


# Function to create and add subelements recursively
def create_subelements_Register(parent, path, value):
    elements = path.split('.')
    for elem in elements:
        parent = etree.SubElement(parent, "Register", name=elem)
    parent.text = str(value)

# Create the root element
root = etree.Element("HWDescption")

# Iterate through the dictionary and create XML subelements
for path, value in RegisterSettings.items():
    create_subelements_Register(root, path, value)

# Create an XML tree from the root element
tree = etree.ElementTree(root)

# Serialize the XML tree to a string
xml_string = etree.tostring(tree, pretty_print=True, encoding="utf-8")

print(xml_string.decode("utf-8"))
