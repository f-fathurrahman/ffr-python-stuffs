from xml.dom import minidom

mydoc = minidom.parse("quran-uthmani.xml")

items = mydoc.getElementsByTagName("sura")

# one specific item attribute
print("Item #2 attribute:")
print(items[1].attributes["name"].value)
