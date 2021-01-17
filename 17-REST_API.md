
# 17 - REST API #
_____________________________________________________________

<!--  2021-01-10 23:49:07 -->

In the traditional model, URL would look something like this:

    https://www.website.com/folder1/folder2/list-est.html

where we are actually traversing the subfolders in the web server to access the specific file.

In the modern day, we have:

    https://www.website.com/folder1/folder2?actions=list&zone=est 

where we are passing specific data that we want to access, and this hits an API.
The web server will then return some data, instead of some html page.

Here we're not browsing the folders, subfolders, and files.
Instead, we're invoking a command, and we're using a REST API.
Instead of returning a full html page, it'll return a plain text data, normally in JSON format.

________________________________________________________

## API ##

A way for a computer program to communicate directly with another program. This is how softwares talk to each other.
<br>

**RESTful API**

An API that is commonly used online over the HTTPS protocol, where the payload is a JSON data usually. It follows a specific set of constraints, listed below:

- uniform interface
- client-server
- stateless
- layered
- cacheable
- code on demand (optional)


**REST Client**

As a sample, we can use a VSCode extension - REST Client by HUachao Mao.

1.  Install the VSCode extension - REST Client
2.  Open a new file and save it as 'sample-api-text.txt'
3.  Paste in a sample request. You cna use this:    https://swapi.co/api/people/1/
4.  Hit ctrl-alt-r. This will open another tab, named 'Response' which shows the full response from the web server.

<font size="2">*EDEN: I ran into an error when doing an ctl-alt-r. I seem to get the error:The connection was rejected. Either the requested service isn’t running on the requested server/port, the proxy settings in vscode are misconfigured, or a firewall is blocking requests. Details: RequestError: connectm CONNREFUSED 72.52.178.23:443.*</font>

<font size="2">*EDEN: 2021-01-13 03:10:09, So I think it's been 3 days, and I still havent resolved the issue below. I've checked numerous links online and tried alot but to no avail. Decided to push through with the course.*</font>

<font size="2">*EDEN: 2021-01-14, Discovered that the REST Client was working all this time. The problem was I was using an link that's invalid already - swapi.co. Found online that it's now swapi.dev.*</font>
______________________________________________________________

## RESTFUL API CONSTRAINTS ##

These are the rules that RESTful APIs have to follow, but the most important are the top 3

- **uniform interface**
- **client-server**
- **stateless**
- layered
- cacheable
- code on demand (optional)
<br>

**UNIFORM INTERFACE**
APIs must follow a consistent and decoupled interface for API calls. Ideally only one URI for any given 'resource'.

Another thing that needs to be consistent is the protocol used. If you're using HTTPS for one API, you must be using HTTP for the others as well.


**CLIENT-SERVER**
There must be both a client and a server in the implementation architecture. All communication happens between the API interfaces.


**STATELESNESS** 
Every API call must contain everything needed to perform the requested operation. Every API call must be independent and self-contained. The server cannot remember the client from one request to another.

This is violated most of the time.

_____________________________________________________________

## REST vs. SOAP ##

Both are approaches to bulding an API.

**REST**
*Representational State Transfer*
- Guidelines for the structure and organization of an API.
- More high-level and elss-granular than a protocol.
- It is **NOT A PROTOCOL**
- Can use JSON, XML, YAML, Markdown, CSV, Plaintext.

REST doesn't specify the rules for what text format to use. It is typically used in public APIs scenarios where APIs may not need a lot of computing resources.

**SOAP**
*Simple Object Access Protocol *
- It is a PROTOCOL - includes specifications at various layers.
- More comprehensive on rules and control you can put into place, but has MORE OVERHEAD.
- Only use XML.

SOAP is mostly used in enterprise environment, where security is the utmost importance.

__________________________________________________

**RESTful APIs** can use query string.
This means you can pass aprameters onto the URL itself.
As an example:

    https://sampleapi.com/players/list?team=14&active=true

Where the query string starts from the '?'

    ?team=14&active=true

You can also send the data through the request body, as part of payload of the 
HTTP request, usually in JSON

```json
{
    "team": "14",
    "active": "true"
}
```

On the other hand, **SOAP** requires a verbose XML document tp transmit exactly what it's doing. The document is called the **SOAP ENVELOPE**

The **SOAP Envelope** contains:

    - Header
        - Header Block
    - Body
        - Message Block

______________________________________________________________

## REST TOOLS ##

Tools which we can use to geenrate http requests which can use give us visibility into the 
details behind those requests - for troubleshooting.

- Web Browser - Open developer tools > Network > Name 
- VS Code REST Client
- Postman - widely-used GUI which you can use to build and view requests