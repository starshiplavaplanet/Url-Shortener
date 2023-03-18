# Url-Shortener

*************************************************************************************************************************************************

This code creates a simple URL shortening web application using Flask and SQLite.

The user enters a URL in the form on the home page, which is then stored in a SQLite database along with a randomly generated short code. 
When the user submits the form, the application generates a shortened URL by concatenating the base URL of the application with the short code, 
and displays the shortened URL to the user.

The user can then use the shortened URL to access the original URL. When a user accesses a shortened URL, 
the application looks up the corresponding original URL in the database and redirects the user to that URL.

This allows users to easily share and access long URLs using shorter, more convenient links.

************************************************************************************************************************************************

Created by 'me' as part of learning Python
