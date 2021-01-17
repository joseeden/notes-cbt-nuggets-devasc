
# 21-Postman_for_API_Interaction
________________________________________________________

<!-- 2021-01-13 22:06:00 -->

## POSTMAN ##

Popular API testing tool. Download the Postman Desktop App [here](https://www.postman.com/downloads/)
Install it, then sign-in/create an account.

Select 'New' request and then create new collection if there's no existing collection. 

To test it using a request, paste this link on the GET field: https://postman-echo.com/get

Hit send afterwards. You should see the empty box for the 'Body' start to populate.

______________________________________________________________

## POSTMAN REQUESTS AND RESPONSES ##

In Postman, you can change the verb - '**GET**' - to to other options.
<br>
**PARAMS** 
Here you can fill-in Key, value, description. For example, you may have the URL: 
https://www.postman.com/downloads/

When you fill in the parameters with:

&nbsp;&nbsp;&nbsp;&nbsp;Key: Name       
&nbsp;&nbsp;&nbsp;&nbsp;Value: John

The URL is automatically updated to: https://www.postman.com/downloads/?Name=John

This can also be done in reverse. You can edit the URL in place, and the params are automatically updated.
https://www.postman.com/downloads/?Name=John&Action=Remove
<br>

**HEADERS**
Similar with params, also has key, value, description. try typing, then hit send.

&nbsp;&nbsp;&nbsp;&nbsp;Key: MyHeader   
&nbsp;&nbsp;&nbsp;&nbsp;Value: Custom Header Value

To open the Postman console: Ctrl-Alt-C
The console will show all the reqeusts that's been made. It looks like this:

> GET https://www.postman.com/downloads/
    > Network
    > Request Headers 
    > Response Headers 
    > Response Body
> GET https://www.postman.com/downloads/?Name=John&Action=Remove%20
    > Network
    > Request Headers 
    > Response Headers 
    > Response Body

<br>

**BODY** 
The default one is 'none' but there's other choices

- none 
- form-data
- x-www-form-url.encoded
- raw
- binary
- GraphQL

<br>

**RESPONSE**
This is the bottom of the Postman App. You can see here the:

- status - HTTP status code
- Time - latency
- Size
- Tabs for Body, Cookiers, Headers, Test Results

<br>

**AUTHORIZATION**

______________________________________________________________

## HTTP AUTHENTICATION WITH POSTMAN ##

In the postman app, you can see the following tabs:

- Params 
- Authorization 
- Headers 
- Body 
- Pre-request Scripts 
- Tests 
- Settings

If you open Authorization, you will see a tab 'Type' which contains methods on how to authorize.

As an example, copy this URL and paste it onto the GET field in the Postman App and hit Send.

    https://postman-echo.com/basic-auth

Under Authorization tab > Basic Auth > Enter Username and Password > Save > Send

    Username: postman
    Password: password

Under Body tab, you should see:

    {
        "authenticated": true
    }

Going back to the Postman console, open the latest GET request, then Request Headers. It should show:

    > Request Headers 
        MyHeader: Custom Header Value
        Authorization: Basic cG9zdG1hbjpwYXNzd29yZA==                   <<<< This is the password
        User-Agent: PostmanRuntime/7.26.8
        Accept: */*
        Postman-Token: 118f5807-46ab-4601-a228-6a4188e7e802
        Host: postman-echo.com
        Accept-Encoding: gzip, deflate, br
        Connection: keep-alive
        Cookie: sails.sid=s%3AhkPRL2SqqG3okPJcnx8wfaDeGoMhXDnb.J%2FUO0LMhrT4rPUS6HPzYYrSdYEobx9dRmrTmrFO3REA

You can also choose Authorization type of **'Inherit Auth from Parent'**. What this does is, the parent is the folder or the Collection the URL belongs to.

You can organize the requests into Collections and set the authentication on the Collection level.

That way, you'll only set the credentials one time, and all URLs belonging to that Collection can inherit the 
authentication.

To do this, right click on the Collection > Edit > Edit Collection > Authorization > Type 

You then select the Authentication type to be used.
You can choose 'Basic Auth' for now and use the same Username and Password from above. Hit Update.


**OVERRIDING**
Note that the individual URL can override the authentication set on the Collection level.

______________________________________________________________

## POSTMAN COLLECTIONS AND FOLDERS ##

**COLLECTIONS**
Collections contains URL, or a way to organize URLs that are similar or associated with one another. 

These could be API requests that are sharing the same endpoint. They may also be sharing the same authentication schemes.

You can have Folders inside Collections, and these can also have authorizatin schemes associated with them.

You can also run the URLs inside the Collection or Folder all at the same time. To do this, click the '**Run**' sign beside the Collection name.

This will open a new window - **'Collection Runner'**
Here you can choose how you want to run the requests.
<br>

**POSTMAN SCRIPTS **
Postman integrates an engine that allows you to execute scripts - before request is executed and after response is received. This scripts are written in Javascript.

This are called **PRE-REQUEST SCRIPTS** and **POST-REQUEST SCRIPTS**. 
The order of the execution:

    1. Scripts associated on Collection level is run first          
    2. Scripts associated with Folder/s 
    3. Scripts associated with Request/s 
    4. Request is sent
    5. Response comes back
    6. Scripts associated on Collection level is run first
    7. Scripts associated with Folder/s 
    8. Scripts associated with Request/s 

To set a pre-request script, set a URL again on the GET field. 
You can use: https://www.postman-echo.com/get

Under the **'Pre-request Script'** tab, type in: 

    console.log('This is my pre-request script')
    
Hit Save and then Send. Check on the Postman Console again.
You should see the following:

    "This is my pre-request script"
    GET https://www.postman-echo.com/get

This can also be done on the Folder-level and Collection-Level
Just right click on the Collection or Folder > Edit > pre-request Scripts
______________________________________________________________

## POSTMAN ENVIRONMENTS ##

User environement/s can be seen on the upper-right of the Postman GUI - 'No environment'

This is a way to create groups of variables. This is useful when you're switching between the test environment and production environment.

To add a new environemnt, click the Gear icon beside the 'no environment'.
This should display a window - **'Manage Environment'** > Add 
Next, fill in the fields. you can use the values below:

    Add Environment: Test 
    
    Variable: username      
    Initial Value: admin            
    Current Value: postman 
    
    Variable: password      
    Initial Value: password         
    Current Value: password 

Going back to the Postman UI, click the dropdown for the 'No environment' and choose **'Test'**.

Click the 'eye' icon beside it and you'll see the variables that we just set.

Now to use the variables on the key or values, you must put them inside double **{{}}**.

As an example, go back to the first request with GET https://www.postman-echo.com/get

Under Authorization, fill in the Username and Password fields:

    Username: {{username}}
    Password: {{password}}

By doing this, the request will use the variables that are set on the Test environment.

Notice that when you hover on the {{}}, you'll see a pop-up that shows the variable's value:

    username 
    INITIAL: admin 
    CURRENT: postman
    SCOPE: environment

Hit Send and check the Body. You'll see:
    
    "authenticated": true

Note that for this example, the values for the variables should match the Username and password specified on the Authorization scheme on the Collection /Folder-level.

