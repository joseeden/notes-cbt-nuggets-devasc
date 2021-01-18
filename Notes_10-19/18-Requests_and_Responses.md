
# 18 - REST API - Requests and Responses #
____________________________________________________________
<!-- #2021-01-13 03:58:22 -->

All HTTP Communication uses this overarching structure - **REQUESTS and RESPONSES**

This is basically what an HTTP does: You generate a request and then you geta  response ffrom the server.
You can generate requests through alot of ways, example: web browser.

**FOLLOWING A STRUCTURE** 
HTTP/1.1 Requests and responses  are plain-text formatted communications that follow a specific structure.

1. **Request / response**
<br>

2. **Start Line** 
This is actually the beginning. Indicates the type of request 
<br>

3. **Headers (key-value pairs)** 
This may be one or more headers. (optional)
<br>

4. **Blank Line**                   
Indicates that we're done with  the portion of the request/response
<br>

5. **Body**                         
Includes tha payload data (optional)

______________________________________________________________

## HTTP Request Method ##

All-caps, located right at te beginning of the start line, at the top of your HTTP request.

These are actually called **HTTP VERBS** - generally indicates what the request is trying to do.

It is a single word *TOKEN* that loosely describes teh desired action being performed.

The Request Methods include:

    GET         - most common, used to get information
    HEAD        - most common, 
    POST        - most common, updates/sends information on the server
    PUT  
    DELETE 
    CONNECT
    OPTIONS
    TRACE

______________________________________________________________

## HTTP Response Codes ##

A 3-digit numeric code that the server sends back to the client as part of the HTTP response. Included at the start line, after the protocol.

The codes are categorized based on the first digit:

    1xx     Informational
    2xx     SUccessful 
    200     OK
    3xx     Redirects, when requests hit a server and server redirects it to another URL
    4xx     Client Errors
    401     Unauthorized, user is not signed-in
    403     Forbidden, user is not allowed to some action
    404     Not Found
    5xx     Server error

______________________________________________________________

## HTTP Headers ##

Key-value pairs that are sent up to the server along with the request, and then sent back to the client. This is also optional. Types may include:

    General headers
    Request Headers
    Response Headers

Note that headers are **not meant to send actual data** to the server, they are **meant to send data about the request** itself.

You can see a complete List of HTTP Header Fields [here](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)



