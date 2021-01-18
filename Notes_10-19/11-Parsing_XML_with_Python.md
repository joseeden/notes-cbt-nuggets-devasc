
# 11 - Parsing XML with Python #
____________________________________________________________

<!-- 2021-01-07 14:05:05 -->

**SERIALIZATION**
Creating the data from the program of your choice and pass that out to a plain-text data format.


**DESERIALIZATION**
Reading the data in from a plain-text data format

_____________________________________________________________

## PARSE XML WITH PYTHON ##

There are three method we can use in parsing xml with python/

**For METHOD 1**, we'll be using  python module 'xml' built-in library
We'll use the sample below. Note that this code can also be seen in a separate file, "12-Parsing_XML-Method_1"
This method is good for working on small xml files that are not necessarily going to run in the production system.

**For METHOD 2,** we'll be using an expanded version of ElementTree, called 'lxml'
This is generally preferred when working with xml files - aimed for production systems.

**For METHOD 3,** we'll use another external library, called 'xmltodict'
This works a little different with the first two methods as it reads the xml file into 
an ordered dictionary inside of Python.
