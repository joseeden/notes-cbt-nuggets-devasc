
# 7-XML_JSON_YAML
_____________________________________________________

## PLAIN-TEXT DATA FOPMATS ##

<!-- 2021-01-07 00:40:36 -->

Why use Plain-text data formats?

- Human-readable
- COmputer-readable

Plain-text data formats combines these two. Both humans and the computer should be able to read and figure out how to use the data. Sample of plain-text data formats commonly used today:

- XML
- YAML 
- JSON

**Main benefits:**

1.  **Structured for computers**
Follows certain rules so the computer can interpret the data
<br>

2.  **Annotated for humans**      
Humans should be able to understand it as well
<br>

3.  **Open and extensible**       
No licensing associated, specs are public domain
<br>

4.  **Self-describing**           
Similar with being annotated for humans 
<br>

5.   **Platform-agnostic**         
Every computer system can support plain-text.

___________________________________________________

## XML - EXTENSIBLE MARKUP LANGUAGE ##

Main Features:

- Describes data usign tags. 
- Looks similar with HTML.
- Also the data format for *SOAP* - this is a web-based API protocol that relies on XML to transfer data.

Downside:  
- Too verbose - lot of data, meaning lots of BW to use when transferring data.
___________________________________________________

## JSON - JAVASCRIPT OBJECT NOTATION ##

Main Features:

- Just like how you write objects in a javascript code.
- Popular, widely-supported. 
- Also lightweight - less BW in transferring less characters.  
- Also native to javascript.
- Whitespace and middle lines don't mean anything
- More ideal in compressing data.

___________________________________________________

## YAML - YAML AIN'T MARKUP LANGUAGE ##

Main Features:

- Lighter-weight than JSON
- Highly-legible
- Fairly compact and succint - less characters as well in terms of no brackets
- Whitespace and middle lines ARE important.
Ideal for configuration

________________________________________________________

## XML SYNTAX ##

A well-formed XML file includes

1. Prolog
2. Root tag 
3. Every tga s opened and closed
4. Attributes have values inside double quotes/single quotes

Sample XML:

```xml
# Prolog - recommended
<?xml version="1.0" encoding="UTF-8"?>                      

# This is the ROOT TAG - Mandatory
<People>                                                    
    <Person Id="1">
        <FirstName>John</FirstName>
        <LastName>Smith</LastName>
        <Email>john.smith@yahoo.com</Email>
    </Person>

    # Tags can have attribute, like 'Id'   
    <Person Id="2">                                         
        <FirstName>Jane</FirstName>
        <LastName>Doe</LastName>
        <Email>jane.doe@yahoo.com</Email>
    </Person>

    # Tags can be nested
    <Person Id="3">                                         
        <FirstName>Jeff</FirstName>
        <LastName>Park</LastName>
        <Email>jeff.park@yahoo.com</Email>
    </Person>

</People>
```
_______________________________________________________

## XML ELEMENTS, TAGS, AND ATTRIBUTES ##


**XML ELEMENTS**

'Bones' of the XML file. An element is defined by an opening tag and a closing tag.
As an example:

```xml
    <FirstName>Jeff</FirstName>
    <LastName>Park</LastName>                           
    <Email>jeff.park@yahoo.com</Email>
```

It can include sub-tags as well.

```xml
# This is an element 
    <FirstName>Jeff</FirstName>                         
```

Also, for nested tags, always closed the inner tags first.

```xml
<tag1> <tag2> <tag3> ............ </tag3> </tag2> </tag1>
```

You can also have empty ELEMENTS. The example below is opening and closing itself.

```xml
<EmptyElement/>                                         
```

It can also contain Attributes:

```xml
<EmptyElement id="123" />                                         
```
<br>

**XML ATTRIBUTES**

Included inside the actual tag. Its format is 

```xml
<tag1 attr="any value">.......... </tag1>
```

You can also use escape characters

```xml
<tag1 attr="can have &quot; or &apos; ">.......... </tag1>
```

Where:

    &quot;      - same as a double quote 
    &apos;      - same as a single quote

___________________________________________________________

## XML DOM - DOCUMENT OBJECT MODEL ##

*EDEN: The video was concise, although I may need to check other resources online about XML DOM. Also installed XML Tools (Josh Johnson) extension in VSCode.*

**XML DOM**

Basically, when the xml file becomes large and hard to read, you can check out the tree view in vscode and see the elements in a tree-structure, which makes it easier to understand the file.
___________________________________________________________

## JSON SYNTAX ##

Basically a javascript code - since javascript is a programming language interpreted by all modern web browser, JSON has been a widely adapted data serialization method.

The very pattern of JSON syntax is the key-value pair.

&nbsp;&nbsp;&nbsp;&nbsp;**"key": "value"**        
&nbsp;&nbsp;&nbsp;&nbsp;This is a key-value pair.

&nbsp;&nbsp;&nbsp;&nbsp;**{ javascript object }**   
&nbsp;&nbsp;&nbsp;&nbsp;Javascript objects are enclosed with {}.

&nbsp;&nbsp;&nbsp;&nbsp;**[ Array ]**              
&nbsp;&nbsp;&nbsp;&nbsp;Arrays are enclosed with [].

Note also that JS objects within an array are numbered 0,1,2...
Another thing:  Whitespace and new lines are not important.

All keys should be enclosed by double quotes.
Not all values are enclosed by double quotes.

Sample JSON:

```json
[                                                                 {                                           
        "Id": "1",
        "FirstName": "John",                    
        "LastName": "Smith",                    
        "Email": "john.smith@yahoo.com",
    },                                                   
    {                                                                           
        "Id": "2",                                                                  
        "FirstName": "Jane",
        "LastName": "Doe",
        "Email": "jane.doe@yahoo.com",
    },
    {                                           
        "Id": "3",
        "FirstName": "Jeff",                    
        "LastName": "Park",                     
        "Email": "jeff.park@yahoo.com",
    },                                          
]                                                             
```              
________________________________________________________

## JSON STRINGS, NUMBERS, AND BOOLEANS ##

*EDEN: Found out that JSON doesnt really support comments.*

Here, we differentiate numbers, strings, and BOOLEANS

&nbsp;&nbsp;&nbsp;&nbsp;**"strings"**           
&nbsp;&nbsp;&nbsp;&nbsp;Always have to be enclosed in quotes 

&nbsp;&nbsp;&nbsp;&nbsp;**123**                 
&nbsp;&nbsp;&nbsp;&nbsp;Numbers are not enclsoed in quotes

&nbsp;&nbsp;&nbsp;&nbsp;**true or false**       
&nbsp;&nbsp;&nbsp;&nbsp;All lower-case. 'True' and 'False' not valid.


Using the same example above:

```json
{"People":
    [                                            
        {                                           
            "Id": 1,
            "FirstName": "John",                    
            "LastName": "Smith",                    
            "Email": "john.smith@yahoo.com",
            "Active": true
        },                                          
        {                                           
            "Id": 2,                                                                  
            "FirstName": "Jane",
            "LastName": "Doe",
            "Email": "jane.doe@yahoo.com",
            "Active": false
        },
        {                                           
            "Id": 3,
            "FirstName": "Jeff",                    
            "LastName": "Park",                     
            "Email": "jeff.park@yahoo.com",
            "Active": true        
        },                                          
        
    ]  
}
```
___________________________________________________________

## JSON OBJECTS AND ARRAYS ##

Here we're differentiating an object from array.

&nbsp;&nbsp;&nbsp;&nbsp;**{ object }**        enclosed with {}
&nbsp;&nbsp;&nbsp;&nbsp;**[ array ]**         enclosed with []

In an object:

- key-value pairs are separated by comma
- must always have a key and a value, separated by a colon.

In an array:

- objects must be separated by comma
- elements dont need a key, the key is actually a numeric index built-in
- objects are numbered 0,1,2... with 0 being the index of the first object.

There can also be nesting done.

Sample of object nested within an object:

```json
{                                           
    "Id": 3,
    "Name": { "First": "John", "Last": "Smith"}                  
    "Email": "jeff.park@yahoo.com",
    "Active": true        
},          
```

Sample of array nested within an object:

```json
{                                           
    "Id": 3,
    "Name": ["John", "Smith"]
    "Active": true        
},          
```
___________________________________________________________

## YAML SYNTAX ##

**YAML - YAML Ain't Markup Language**

- Main goal is to be human-readable.
- Also Relies new lines and indentations 
- YAML can also differentiate integers from floating points.
- It also uses booleans 

- **'---'** indicates the start of the YAML file  
- Note that there's also the '...' at the bottom of the YAML file - this is optional
- **'...'** indicates the end of the YAML file

You can also put 2 YAML documents into single one, by using the **'---'** and **'...'** just like the example below.

Sample yaml:

```yaml
---
people:
- id: 1
  Code: 2.5  
  FirstName: John
  LastName: Smith
  Email: john.smith@yahoo.com
  Active: true
- id: 2
  Code: 4.6 
  FirstName: Jane 
  LastName: Doe 
  Email: jane.doe@yahoo.com
  Active: false 
- id: 3
  Code: 56.5
  FirstName: Jeff 
  LastName: Park 
  Email: jeff.park@yahoo.com
  Active: true
...
--- # this is the start of a new document in YAML
item1: item1value
item2: item2value


Note that the number of indentations are arbitrary, as the attributes of an object are aligned
The example below is still considered valid, although not a good practice

people:
- id: 1
  Code: 2.5  
  FirstName: John
  LastName: Smith
  Email: john.smith@yahoo.com
  Active: true
-   id: 2
    Code: 4.6 
    FirstName: Jane 
    LastName: Doe 
    Email: jane.doe@yahoo.com
    Active: false 
-  id: 3
   Code: 56.5
   FirstName: Jeff 
   LastName: Park 
   Email: jeff.park@yahoo.com
   Active: true
```

The '-' identifies a collection or a group - this is basically the same as object. YAML calls them **MAPPING**.

```yaml
- id: 1
  Code: 2.5  
  FirstName: John
  LastName: Smith
  Email: john.smith@yahoo.com
  Active: true
```
_________________________________________________________

## YAML STRINGS, NUMBERS, FLOAT, AND BOOLEANS ##

Using the sample below:

```yaml
---
Anumber: 123
AFloat: 12.3
Astring: Hello World!
AQuotedString: "Hello WOrld!\n" 
AMultilineString: This is valid as long as the lines 
                  are on same indentation
ABoolean: true
```

Here we have **IMPLICIT DATATYPES**

&nbsp;&nbsp;&nbsp;&nbsp;***123***                 
&nbsp;&nbsp;&nbsp;&nbsp;As long as numeric and not enclosed in "", it is treated as an integer

&nbsp;&nbsp;&nbsp;&nbsp;***12.3***                
&nbsp;&nbsp;&nbsp;&nbsp;If the number has a decimal point, then it is treated as a float

&nbsp;&nbsp;&nbsp;&nbsp;***Hello World!***        
&nbsp;&nbsp;&nbsp;&nbsp;Valid string, but cannot contain escape charactes such as new line (\n)

&nbsp;&nbsp;&nbsp;&nbsp;**"Hello World\n"**    
&nbsp;&nbsp;&nbsp;&nbsp;Valid string. YAML can read escape characters inside quotes

