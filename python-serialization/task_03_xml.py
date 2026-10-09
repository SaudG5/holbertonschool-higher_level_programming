#!/usr/bin/env python3
"""Module that serializes and deserializes with XML files"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML and save it to a file."""
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)    
        
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """Load an XML file and return its data as a dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        return dictionary
    except Exception:
        return None
