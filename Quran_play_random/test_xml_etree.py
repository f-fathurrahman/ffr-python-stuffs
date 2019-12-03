import xml.etree.ElementTree as ET

tree = ET.parse("quran-uthmani.xml")
root = tree.getroot()

print( root[0][0].attrib["text"] )
