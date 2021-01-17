
# 19 - REST_API - Parameters and Payloads #
_____________________________________________________________

<!-- 2021-01-13 05:55:13 -->

**PARAMETERS AND PAYLOADS**
HTTP uses parameters and payloads to transmit data alognside the request. This is found on the body of the HTTP Reqeust/response.

**HTTP QUERY STRINGS**
This is part of the URL, a key-value pair. This begins with '?' and is always at the end of the URL. The key-value pairs are separated by an '&'
_____________________________________________________________

## WHY USE QUERY STRINGS, INSTEAD OF HEADERS? ##

Since both are key-value pairs, what is the advantage of query strings over headers?

Recall that headers are not included in the URL, so you cannot share th headers. On the other hand, you can simply share the URL containing the query strings to anyone and they'll be redirected to the same webpage.

Also recall that the **headers are intended to send data about the request**, and not the actual data itself.

The **query string is the actual data that you want to transmit** to the server. Query strings are not also meant for huge blocks of data.

They must short, quick values.
______________________________________________________________

## HTTP BODY (PAYLOADS) ##

This is the portion of the HTTP Request/responsethat is at the very bottom. This is meant to store and transmit large chunks of data. 

**SUMMARY**
- Headers       - stores data about the request
- Query string  - sends small bits of data to the server 
- payloads      - send large chunks of data to server and vice versa