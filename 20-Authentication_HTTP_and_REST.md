
# 20 - Authentication: HTTP and REST
____________________________________________________________

<!-- 2021-01-13 06:23:53 -->

## REST AUTHENTICATION ##
Most APIs will require some sort of authentication and authorizationin order to be used. Some API actually limits your access and anonymous usage unless you create an account which you'll use 
to identify yourself everytime you use those APIs.

&nbsp;&nbsp;&nbsp;&nbsp;**AUTHENTICATION**
&nbsp;&nbsp;&nbsp;&nbsp;Prove you are who you say you are
   
&nbsp;&nbsp;&nbsp;&nbsp;**AUTHORIZATION**
&nbsp;&nbsp;&nbsp;&nbsp;Prove you are allowed to do whatever it is you're trying to do

______________________________________________________________

## Base64 Encoding vs. Encryption ##

Differentiating between data to be included/transmitted along with HTTP message versus data meant to instruct the browser about what to do to the data

**ENCODING IS NOT ENCRYPTION**
Note that these two terms are not the same.
Encoding data allows us to transmit binary data over systems that use text-based control.

Most of all, it is *REVERSIBLE BY DESIGN*.
It's basically writing information but in a different method or characters available.

**BASE64 ENCODING** 
Uses 64 characters to represent data and is considered URL-SAFE. This means it is safe to be included on the URL, and then transmitted to the world wide web.


**ENCRYPTION**
Way to obscure data. Modern HTTP uses TLS protocol to encrypt data in transit.

When TLS is applied on HTTP traffic, it is known as *HTTPS* - this is now a secured traffic.

This is *NOT REVERSIBLE* in general.
It can be reversed only if you have the PRIVATE KEY.
______________________________________________________________

## API KEY AUTHENTICATION ##

Similar in practice and execution with basic HTTP authentication. The main difference is:
- HTTP authentication relies on username and password
- API authentication relies on a a single API key - a single token stored inside an application.

API Keys are plain-text token that is generated, stored in a program, and transmitted to the server in a request header.

This is used to grant full administrative access.

______________________________________________________________

## TOKEN AUTHENTICATION ##

Popular form of authentication, allows to create stateless authentication methods. Allows lot ofocntrol as well.

One of most used is **JWTS - JAVASCRIPT WEB TOKENS.**

&nbsp;&nbsp;&nbsp;&nbsp;JWTS == {JSON} + CRYPTOGRAPHIC SIGNATURE

Basically JWTS is just a JSON data along with a cryptographic signature. This is used to support **STATELESSNESS**

In the traditional model:

1. User sign-in to a website, website remembers the SESSION ID.
2. The SESSION ID is attached to the computer or session. if session/computer restarts,
   a new session IS is generated. and thus needs to re-log-in to the website.
3. The webs server remembers the session ID and stores them in a database or a local storage.
4. Every time the user goes to the website and performs an operation, the requests are sent 
   to the server, algon with the session ID.
5. The server checks the session ID that comes with the request and check it against the IDs stored in
   the database or the local storage. If it matches, it proceeds with the request.

In the model using JWTS:

1. Server hands back the JWTS that is cryptographically signed, and the user passes that each time 
   a request is made.
2. This way, the server doesn't have to always check a database for user data.

The advantage with JWTS:

- **SPEED**
Don't have to hit the storage/DB for each user request.

- **SCALABILITY** 
Can safely distribute requests across many servers. 
Requests can be balanced to the available servers
