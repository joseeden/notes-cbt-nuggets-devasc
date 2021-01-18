
# 24 - Data Models and Yang #
_____________________________________________________________

<!-- 2021-01-14 03:48:07 -->

## DATA MODEL / DATA SCHEMA ##

Pre-agreed upon structure of data nefore it is transmitted to parties.

**HOW YANG WORKS**
in 2002, IETF discussed the shortcomings of SNMP. It was great for monitoring for a while. 

In 2003, the NETCONF working group is formed. The structure of data going between network devices and parties consuming the data will not matter because there is some form fo protocol that can transmit XML data between devices.

In addition to NETCONF, they also created **YANG - YET ANOTHER NEXT GENERATION**. It is also sometimes called *YANG or YANG MODEL or YANG DATA MODELLING LANGUAGE*
Note that a set of data only becomes a model when you set something specific.

As an example, this is a data model:

    Module:  Interfaces
        Leaf: Name

Without anything specific, this becomes a data modeling language:

    Module:
        Leaf:


**LAYERS OF YANG DATA MODEL:**

1.  **MODULES**
    This is the key topic.
    <br>

2.  **CONTAINERS:**
    These are the subtopics, this can also split up functionality.
    There can be a container which handles configuration changes, 
    and another container which handles stats and monitoring.
    <br>

3.  **LEAF**


For a real example, you can it [here](http://www.netconfcentral.org/modules/ietf-interfaces)

______________________________________________________________

## YANG TOOLS ##

1.  Yang Catalog    -   https://yangcatalog.org/

2. Yang Explorer    -   https://github.com/CiscoDevNet/yang-explorer

_____________________________________________________________
