import os
import json
from lxml import etree
from fcBoardC import *

class XMLGenerator():
    """Use to create XML File"""

    def __init__(self, root_node: str):
        self.root = etree.Element(root_node)
    
    def buildingRoot(self, root_node): #used in usingXMLGen.py
        spcialRoot = etree.Element(root_node)
        return spcialRoot

    """Editting XML Trees"""
    def create_element(self, tag, attrib=None, nsmap=None, **_extra):
        return etree.Element(tag, attrib=attrib, nsmap=nsmap, **_extra)

    def add_element(self, parent, element):
        parent.append(element)

    def add_node(self, parent, tag, attrib=None, nsmap=None, **_extra):
        element = etree.SubElement(parent, tag, attrib=attrib, nsmap=nsmap, **_extra)
        return element

    """Dictionary Related Functions"""
    def display_dict(self, dictionary):
        formatted_dict = json.dumps(dictionary, indent=4)
        print(formatted_dict)
        
    def update_dict(self, dictionary, source_list, index, *keys):
        if not isinstance(index, int):
            raise TypeError("Index should be an integer")
        
        if index >= len(source_list) or index < 0:
            raise ValueError("Invalid index provided from source_list")
        
        if len(keys) == 1:
            new_value = source_list[index]
            existing_value = dictionary.get(keys[0])  # Get the existing value, if it exists
            if new_value is not None and existing_value is not None and type(new_value) != type(existing_value):
                raise TypeError(f"Value type {type(new_value)} does not match the existing value type {type(existing_value)}")
            dictionary[keys[0]] = new_value
            return
        
        key = keys[0]
        if key in dictionary:
            self.update_dict(dictionary[key], source_list, index, *keys[1:])
        else:
            raise KeyError(f"Key '{key}' not found in dictionary")
    
    def dict_to_xml(self, root_element, dictionary):
        if root_element is None:
            root_keys = list(dictionary.keys())
            if len(root_keys) > 1:
                raise ValueError("Multiple highest-level keys found in the dictionary. Provide a root element name.")
            root_key = root_keys[0]
            self.root = self.add_node(self.root, root_key)
            root_element = self.root

        for key, value in dictionary.items():
            if isinstance(value, dict):
                sub_element = self.add_node(root_element, key)
                self._dict_to_xml(sub_element, value)
            else:
                sub_element = self.add_node(root_element, key)
                sub_element.text = str(value)

    """Creating XML file"""
    def display_xml(self):
        print(etree.tostring(self.root, pretty_print=True).decode())

    def create_xml(self, filename, filepath=None):
        tree = etree.ElementTree(self.root)
        if filepath is None:
            tree.write(filename, encoding="utf-8", xml_declaration=True, pretty_print=True)
        else:
            full_filepath = os.path.join(filepath, filename)
            tree.write(full_filepath, encoding="utf-8", xml_declaration=True, pretty_print=True)


if __name__ == "__main__":
    xmlgen = XMLGenerator("root")
    
    #example list that will contain data to which the dictionary value will change.
    source_list = ["14", "babababababa"]
    
    #example dictionary
    optical_group = {
        "OpticalGroup": {
            "attrib": {"attr1": "value1", "attr2": "value2"},
            "sub_elements": {
                "SubElement1": {
                    "attrib": {"sub_attr": "sub_value"},
                    "sub_elements": {
                        "SubSubElement1": {
                            "attrib": {"sub_sub_attr": "sub_sub_value1"},
                            "text": "SubSubElement1 text content"
                        },
                        "SubSubElement2": {
                            "attrib": {"sub_sub_attr": "sub_sub_value2"},
                            "text": "SubSubElement2 text content"
                        }
                    }
                },
                "SubElement2": {
                    "attrib": {"sub_attr": "sub_value"},
                    "sub_elements": {
                        "SubSubElement3": {
                            "attrib": {"sub_sub_attr": "sub_sub_value3"},
                            "text": "SubSubElement3 text content"
                        },
                        "SubSubElement4": {
                            "attrib": {"sub_sub_attr": "sub_sub_value4"},
                            "text": "SubSubElement4 text content"
                        }
                    }
                }
            }
        },
        
        #Commented out to test the "dict_to_xml(None, dictionary)" you can un-comment it for other testing.
        #
        # "AnotherOpticalGroup": {
        #     "attrib": {"attr3": "value3"},
        #     "sub_elements": {
        #         "SubElement3": {
        #             "attrib": {"sub_attr": "sub_value"},
        #             "sub_elements": {
        #                 "SubSubElement5": {
        #                     "attrib": {"sub_sub_attr": "sub_sub_value5"},
        #                     "text": "SubSubElement5 text content"
        #                 },
        #                 "SubSubElement6": {
        #                     "attrib": {"sub_sub_attr": "sub_sub_value6"},
        #                     "text": "SubSubElement6 text content"
        #                 }
        #             }
        #         }
        #     }
        # }
    }
    
    xmlgen.update_dict(optical_group, source_list, 0, "OpticalGroup", "sub_elements", "SubElement1", "sub_elements", "SubSubElement2", "attrib", "sub_sub_attr")
    xmlgen.display_dict(optical_group)
    xmlgen.dict_to_xml(None, optical_group) 
    #None is used when there's only one highest key of the dictionary to use that key as the root.
    #Otherwise, dict_to_xml("decide_root_Name", dictionary)
    
    xmlgen.create_xml('output.xml')


'''
Dictionary 

optical_group
| - OpticalGroup
|   |- attrib: {"attr1": "value1", "attr2": "value2"}
|   |- sub_elements
|      |- SubElement1
|      |  |- attrib: {"sub_attr": "sub_value"}
|      |  |- sub_elements
|      |     |- SubSubElement1
|      |     |  |- attrib: {"sub_sub_attr": "sub_sub_value1"}
|      |     |  |- text: "SubSubElement1 text content"
|      |     |- SubSubElement2
|      |        |- attrib: {"sub_sub_attr": "sub_sub_value2"}
|      |        |- text: "SubSubElement2 text content"
|      |- SubElement2
|         |- attrib: {"sub_attr": "sub_value"}
|         |- sub_elements
|            |- SubSubElement3
|            |  |- attrib: {"sub_sub_attr": "sub_sub_value3"}
|            |  |- text: "SubSubElement3 text content"
|            |- SubSubElement4
|               |- attrib: {"sub_sub_attr": "sub_sub_value4"}
|               |- text: "SubSubElement4 text content"
| - AnotherOpticalGroup
|   |- attrib: {"attr3": "value3"}
|   |- sub_elements
|      |- SubElement3
|         |- attrib: {"sub_attr": "sub_value"}
|         |- sub_elements
|            |- SubSubElement5
|               |- attrib: {"sub_sub_attr": "sub_sub_value5"}
|               |- text: "SubSubElement5 text content"
|            |- SubSubElement6
|               |- attrib: {"sub_sub_attr": "sub_sub_value6"}
|               |- text: "SubSubElement6 text content"

The second key, AnotherOpticalGroup was commented out to test the "xmlgen.dict_to_xml(None, optical_group)"
'''