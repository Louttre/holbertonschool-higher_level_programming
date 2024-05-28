#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
     with open(filename, 'w') as file:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
          tree = ET.ElementTree(root)
          tree.write(file)
