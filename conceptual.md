### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
  Python is a scripting language that requires an installed intepreter to run, as such, the version that it's interpreted as depends on the version installed on the computer. Javascript runs within the browser. Javascript has limitations based around maintaining browser security, the version of Javascript that's run is based on the version that's supported by the browser client. Because Javascript is isolated to it's browser environment though, it's limited in it's capacity to work with other computer resources. Because of these differences, Python functions more easily as a server hosting language, while Javascript works well as a client rendering and request making language.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
  given a dictionary **_dict_** with keys **_a_** and **_b_** I would write code to attempt to access a missing key (like **_c_**) with the built in dict function **_dict.get()_**. **_dict.get('c',"empty")_** would return the string **_"empty"_** instead of generating a **_KeyError_**

- What is a unit test?  
  A unit test is a test that applies to a module block of code, typically a function to verify that it meets a set of requirements. Unit testing is strongest when programming is oriented more towards functional code, with functions strictly accepting inputs and returning outputs without modifying state/environmental conditions. Unit testing is most useful when attempting to isolate problems in programming because the testing paradigm specifies which exact functions failed. End to end testing is the style of testing on the opposite side of the testing spectrum and is intended to verify that the modules of code produce the results expected when working together in a real life scenario.

- What is an integration test?  
  An integration test exists between a unit test and an end to end test. It will test isolated chains of unit code links to ensure that the correct effects are being made without affecting other unintended systems and services. This can verify that groups of functions and modules work together as intended since sometimes individual modules of code can produce the correct outputs but their orientation to eachother produces unexpected results or does not cover all of the edge cases defined in the requirements.

- What is the role of web application framework, like Flask?  
  A web application framework is intended to serve hosted content over IP protocols like http. These frameworks include class objects and functions that expose the data within requests, and can help a developer assemble response objects in a variety of different formats. Finally, these frameworks usually include modules of code intended to progress testing practices for the development of the web application as well.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?  
  A path variable is typically used to identify a specific resource, or subject, whereas a query parameter is used to modify, filter, or sort the data that's provided by the online resource. So if a specific backend resource exists to satisfy a request, then a route URL should likely be used. If the route will accept some handling data that should describe how the route is served, then a query parameter should be used to take in the.

- How do you collect data from a URL placeholder parameter using Flask?
  URL placeholder parameters are defined with open and closure carrats (**_<_** and **_>_**) in the route argument definition for the app wrapper function. The placeholders are then available as arguments in the method definition.

- How do you collect data from the query string using Flask?  
  Query parameters are exposed by the request object in the Flask application model. They are accessible as an immutable dictionary within the **_request.args_** class variable. The query string parameter can then be retrieved using a **_.get()_** function call or square bracket and key parameter (as a string). 

- How do you collect data from the body of the request using Flask?  
  Data about the request, including all information stored in the body of the request is handled with the flask **_Request_** object. Generally the **_Request.get\_data()_** method is used to read data from the request body as a bytestream. The **_Request.get\_json()_** method returns the data parsed into a JSON format for easier interpretation.

- What is a cookie and what kinds of things are they commonly used for?  
  A HTTP typically is stateless, it does not have a persistent mechanism to remember information about a request, the browser client can work around this with the client cookies. A cookie is a small allotment of data that can be sent along with a request to tell the server more details about the client request. Because they are sent along with the request, they are limited to 4kb in storage size. Cookies can tell a server simple things, like if a user has seen an cleared a special banner before, or if a specific user preference was established previously. Cookies are not secure, and can usually be viewed and modified in browser dev tools. This makes them poor choices to store private unencrypted data within.

- What is the session object in Flask?  
  Flask provides a way for the digitally signed and encoded piece of data to be saved with a browser session. The session object requires that a secret key be defined in the app so that the session object can be encrypted. The session is stored in the cookies of the client, but since it's hashed with the secret key, clients using the browser should be unable to modify it. Within the server application the session object operates as a dictionary, with string key-value pairs. This object can then be parsed and read by the app to deliver user specific content. 

- What does Flask's `jsonify()` do?  
  The flask method jsonify accepts a dict or string and parses it into a json data structure. This is useful for sending data back to the browser client.
