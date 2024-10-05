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
    for i in dictionary:
        element = ET.SubElement(root, i)
        element.text = dictionary[i]
    data = ET.ElementTree(root)
    data.write(filename)

def deserialize_from_xml(filename):
    """
    deserializes given file to data
    """
    tree = ET.parse(filename)
    dictionary = dict()
    root = tree.getroot()
    for i in root:
        dictionary[i.tag] = i.text
    return dictionary
