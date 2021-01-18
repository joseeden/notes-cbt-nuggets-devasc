
#******************************************************************************************************************#

# 14-Parsing_XML-Method_3

#******************************************************************************************************************#

# 2021-01-08 01:36:31

# This is the 3rd of the 3 codes used in "11-Parsing_XML_with_Python"

# You must install xmltodict first by running either of the commands below
#       pip install xmltodict
#       python -m pip install xmltodict

#------------------------------------------------START OF CODE----------------------------------------------------#

import xmltodict

# Get the xml file data
stream = open('Sample.xml', 'r')

# Parse the xml file into an ordered dictionary.
xml = xmltodict.parse(stream.read())

# Iterate over the item in 'People':
for e in xml["People"]:
    print(e)
    print("")

# Iterate over the item inside each subelement "Person" under the root "People"
for e in xml["People"]["Person"]:
    print(e)

#-------------------------------------------------END OF CODE----------------------------------------------------#

