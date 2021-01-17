
#******************************************************************************************************************#

# 13-Parsing_XML-Method_2

#******************************************************************************************************************#

# 2021-01-08 01:36:31

# This is the 2nd of the 3 codes used in "11-Parsing_XML_with_Python"

# Note that unlike xml, lxml is not a built-in library.
# You must install lxml first by running either of the commands below
#       pip install lxml
#       python -m pip install lxml

#------------------------------------------------START OF CODE----------------------------------------------------#

# The rest of the code is almost the same as with Method 1
from lxml import etree as ET

# Get the xml file data.
stream = open('Sample.xml', 'r')

# Parse the data into an ElementTree object
xml = ET.parse(stream)

# Get the 'root' Element object from the ElementTree
root = xml.getroot()

# Iterate through eachc hild of the 'root' Element'
# This will basically go through all the subelements ('Person') under the root ('People').
for e in root:

    # Print the stringified version of the element
    print(ET.tostring(e))

    # Print the id attribute of the Element object
    print(e.get("Id"))
    print("")

#-------------------------------------------------END OF CODE----------------------------------------------------#
