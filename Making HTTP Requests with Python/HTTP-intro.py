# HTTP Intro and Crash Course

# Objectives:
# - Describe what happens when you type a URL into a URL bar
# - Describe the request/response cycle
# - Explain the different categories of respose codes
# - Compare GET and POST requests


# What happens when you type a URL into a URL bar?:
# 1. DNS Lookup
# 2. Computer makes a REQUEST to a server
# 3. Server processes the REQUEST
# 4. Server issues a RESPONSE
# Steps 2-4 is the Request/Response Cycle


# DNS Lookup is like a Phonebook for the internet
# Takes domain names (google.com) and turns them into an ip address (172.217.9.142)
# The ip address what we send the REQUEST to
# E.g.:
# facebook.com -----> | DNS Server | -----> 157.240.2.35


# Requests and Responses:


# |                      | ------ 172.217.9.142 GET / ------> |        |
# |         Client       |                                    | Server |
# | (e.g. your computer) | <------------ 200 OK ------------- |        |
#                                 <!doctype html>
#                                 <html lang='en'>
#									 <!--
#									   HTML for google.com
#									   will be here!
#                                    -->
#                                  </html>

# - Client sends a request to the corresponding ip address
# - The server processes the request and then sends the page we're looking for, as long as nothing went wrong (errors e.g. Error 404: Page not found x_x)
# - To be more specific, it sends back an HTTP Response containing information (called the response body, which is HTML) as well as a status code (if everything worked, status code is 200: OK like in the diagram above)
# - The HTML that the server sent back in the response body is then rendered by the Clients computer and displayed


# HTTP Headers
# - Sent with both requests and responses
# - Provide additional information about the request or response

# Headers Examples

# Request Headers:
# - Accept ~ Acceptable content-types for response (e.g. html, json, xml)
# - Cache-Control ~ Specify caching behavior
# - User-Agent ~ Information about the software used to make the request

# Response Headers:
# - Access-Control-Allow-Origin ~ specify domains that can make requests
# - Allowed ~ HTTP verbs that are allowed in requests

# Response Status Code:
# 2xx - Success
# 3xx - Redirect
# 4xx - Client Error (your fault!)
# 5xx - Server Erroe (not your fault!)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# HTTP Verbs and APIs


# HTTP Verbs

# GET:
# - Useful for retrieving data
# - Data passed in query string
# - Should have no "side-effects" (because it's just retrieving something)
# - Can be cached
# - Can be bookmarked

# POST:
# - Useful for writing data
# - Data passed in a request body (could be a text post, image, video, etc.)
# - Can have "side-effects" (because it's changing something, either inserting or updating or deleting)
# - Not cached
# - Can't be bookmarked



# APIs

# - API = Application Programming Interface
# - A version of a website intended for computers to talk between computers or between code
# - Allows you to get data from another application without needing to understand how the application works
# - Can often send data back in different formats (JSON, XML)
# - Examples of companies with APIs: GitHub, Spotify, Google

