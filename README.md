# EasyDabble

EasyDabble is a basic landing page created using python, django, and bootstrap css.
This was a previous project which was refactored to make it more modular by creating each app so it can easily operate by its own.

The project contains a contact app that will send and receive emails using gmail, and django emailing support. You will get a SMTPAuthenticationError
the reason being Google blocks access from unknown location to resolve this issue go to https://accounts.google.com/DisplayUnlockCaptcha and follow the instructions.

The other apps include a newsletter app that collects emails in which you can use to build a newsletter campaign, and a sitemaps app which is intended to be used
for pages  that usually go into the footer such as privarcy, terms of use etc.

The project also comes with a project level templates and static folder, however the views for the index page is being render within the sitemaps app.

To get the project running create a secret.py file within the easydabble project folder, and add your secret key and email configuration info into that file.
