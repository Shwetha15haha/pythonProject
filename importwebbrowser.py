"""
This module demonstrates how to use the webbrowser module to open a web browser with a search term.

The webbrowser module provides a high-level interface to allow displaying Web-based documents to users. Under most circumstances, simply calling the open() function from this module will open the default web browser to a specific URL.
"""

import webbrowser  # Import the webbrowser module for opening web pages

# Prompt the user to enter a search term
user_term = input('Enter a search term: ')

# Open the default web browser and search for the user's term on Google
webbrowser.open('https://www.google.com/search?q=' + user_term)
