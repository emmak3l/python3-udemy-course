# Defining Classes and Objects

# What is OOP?
# - Object Oriented Programming
# - it's a method of programming that attempts to model some process or thing in the world, a class or object(instance)
# - class ~ a blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict)
# - instance ~ objects that are constructed from a class blueprint that contain their class's methods and properties

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

# Abstraction and Encapsulation

# Why OOP?
# With OOP, the goal is to encapsulate code into logical, hierachical groupings using classes
# so you can reason about your code at a higher level

# Example:
# Say we want to model a game of poker in our program
# We could have the following entities:
# - Game
# - Player
# - Card
# - Deck
# - Hand
# - Chip
# - Bet

# Card Deck possible implementation (pseudocode)
# - _cards {private list attribute}
# - _max_cards {private int attribute}
# - shuffle {public method}
# - deal_card {public method}
# - deal_hand {public method}
# - count {public method}

# python doesn't actually have true private and public variables, attributes or methods
# the way we make something private is by leading with an underscore for the name, like _cards
# makes it clear to other developers that it's only meant to be used inside the class not outside
# there is nothing stopping someone from accessing it anyways, this is just a naming convention

# Encapsulation
# - the grouping of public and private attributes and methods into a programmatic class, making abstraction possible

# Example
# - designing the deck class, he makes cards a private attribute (a list)
# - he decided that the length of the cards should be accessed via a public method called count() -- i.e. Deck.count()

# Abstraction
# -exposing only the "relevant" data in a class interface, hiding private attributes and methods (aka the "inner workings") form users
