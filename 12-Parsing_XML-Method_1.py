
#******************************************************************************************************************#

# 12-Parsing_XML-Method_1

#******************************************************************************************************************#

# 2021-01-07 14:17:37

# This is the 1st of the 3 codes used in "11-Parsing_XML_with_Python"

# PARSE XML WITH PYTHON 

# Here we'll be using  python module 'xml' built-in library
# We'll use the sample below. Note that this code can also be seen in a separate file, "12-Parsing_XML-Method_1"..
# We will import and use "Sample.xml" fiel which is in the same directory as the .py code below.

# EDEN: I was having errors when trying to run this code - the errors seem to root in this line: xml = ET.parse(stream)
# The error I'm getting is: xml.etree.ElementTree.ParseError: not well-formed (invalid token)
# Atfer some editing and testing, adn readin online, I was convinced that the code below is correct and the
# issue might be in the xml file it is trying to open.
#
# EDEN: After some editing on the XML file, I found out tha the comments were causing the xml to be read as invalid.
# Although I have followed the articles online on how to put annotationsin an xml file,
# I decided to remove all the unnecessary comments - and voila - the code was able to read the xml file!

#------------------------------------------------START OF CODE----------------------------------------------------#

# Importing the ElementTree function and assigning it with ET as alias
import xml.etree.ElementTree as ET 

# Get the xml file data.
stream = open('Sample.xml', 'r')

# Parse the data into an ElementTree object
xml = ET.parse(stream)

# Get the 'root' Element object from the ElementTree
root = xml.getroot()

# Iterate through each child of the 'root' Element'
# This will basically go through all the subelements ('Person') under the root ('People').
for e in root:

    # Print the stringified version of the element
    print(ET.tostring(e))

    # Print the id attribute of the Element object
    print(e.get("Id"))
    print("")

#-------------------------------------------------END OF CODE----------------------------------------------------#
