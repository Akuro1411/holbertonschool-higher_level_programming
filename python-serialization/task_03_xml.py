#!/usr/bin/env python3
"""
elementtree was imported
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serializes given data to xml and writes to file
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    xml_tree = ET.ElementTree(root)
    xml_tree.write(filename)


def deserialize_from_xml(filename):
    """
    deserializes given file to data
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
