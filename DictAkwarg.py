import xml.etree.ElementTree as ET

def create_xml_element(tag, **kwargs):
    element = ET.Element(tag)
    for key, value in kwargs.items():
        element.set(key, str(value))
    return element

attributes = {
    'a': 'Real',
    'b': 'Python',
    'c': 'Is',
    'd': 'Great',
    'e': '!'
}

#custom_element = create_xml_element('custom', **attributes)
custom_element = create_xml_element('custom', a='Real', b='Python', c='Is', d='Great', e='!')

ET.dump(custom_element)
