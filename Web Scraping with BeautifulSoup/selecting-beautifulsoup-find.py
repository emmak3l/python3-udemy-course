# Selecting with BeautifulSoup: find()

# - To extract data from HTML we install Beautiful Soup with pip
# - Beautiful Soup lets us navigate through HTML with Python
# - Beautiful Soup does NOT download HTML! For this, we need the requests module!

from bs4 import BeautifulSoup

# Mocked HTML in a variable to use for our example
# We're going to pretend we got this back from making a request
html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>First HTML Page</title>
</head>
<body>
	<div id="first">
		<h3 data-example="yes">hi</h3>
		<p>more text.</p>
	</div>
	<ol>
		<li class="special">This list item is special.</li>
		<li class="special">This list item is also special.</li>
		<li>This list item is not special.</li>
	</ol>
	<div>bye</div>
</body>
</html>
"""

# Parsing and Navigating HTML
# - BeautifulSoup(html_string, "html.parser") - parse HTML
#		- BeautifulSoup can also parse xml like this: BeautifulSoup(xml_string, "xml.parser")
# - Once parsed, There are several ways to navigate:
#		- By Tag Name (<p>,<div>,<h1>,<a>, ect.)
#		- Using find (returns one matching tag)
#		- Using find_all (returns a list of matching tags)

soup = BeautifulSoup(html, "html.parser")
print(type(soup)) # <class 'bs4.BeautifulSoup'>
# ^ now our HTML isn't a string, it's an instance of BeautifulSoup


# Selecting Using Tags

print(soup.body)
# ^
# <body>
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>
# <ol>
# <li class="special">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>
# <div>bye</div>
# </body>

print(soup.body.div)
# ^ (we only get the first div, even though there are two)
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>

d = soup.find("div")
print(d)
# ^ (we only get the first div, even though there are two)
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>

print(type(d)) # <class 'bs4.element.Tag'>
# Even though the output looks like a string it isn't, because it was parsed

print(soup.find_all("div"))
# ^ now we get both divs in a list
# [<div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>, <div>bye</div>]

print(soup.find_all("li"))
# ^ all lis in a list
# [<li class="special">This list item is special.</li>,
# <li class="special">This list item is also special.</li>,
# <li>This list item is not special.</li>]


# Selecting Using Attributes (id, class)

print(soup.find(id="first"))
# ^ finding the id named 'first'
# <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>

print(soup.find_all(class_="special"))
# ^ finding all elements with the class 'special'
# (when searching for class you have to put an underscore after so python doesn't get confused)
# [<li class="special">This list item is special.</li>,
# <li class="special">This list item is also special.</li>]

print(soup.find_all(attrs={"data-example": "yes"}))
# <h3 data-example="yes">hi</h3>


