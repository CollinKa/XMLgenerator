import os
import json
from lxml import etree

#I haven't put comments yet

class XMLGenerator:
    """Use to create XML File"""

    def __init__(self, root_node: str):
        self.root = etree.Element(root_node)
        self.initial_dictionary = {}
        

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
    