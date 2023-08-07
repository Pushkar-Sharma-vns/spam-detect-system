Registration and Profile: 
  ● A user has to register with at least name and phone number, along with a password, before using. He can optionally add an email address. 
  ● Only one user can register on the app with a particular phone number. 
  ● A user needs to be logged in to do anything; there is no public access to anything. ● You can assume that the user’s phone contacts will be automatically imported into the       app’s database - you don’t need to implement importing the contacts. 

Spam: 
  ● A user should be able to mark a number as spam so that other users can identify spammers via the global database. Note that the number may or may not belong to any               registered user or contact - it could be a random number. 
  
Search: 
  ● A user can search for a person by name in the global database. Search results display the name, phone number and spam likelihood for each result matching that name               completely or partially. Results should first show people whose names start with the search query, and then people whose names contain but don’t start with the search query.
  ● A user can search for a person by phone number in the global database. If there is a registered user with that phone number, show only that result. Otherwise, show all           results matching that phone number completely - note that there can be multiple names for a particular phone number in the global database, since contact books of multiple       registered users may have different names for the same phone number. 
  ● Clicking a search result displays all the details for that person along with the spam likelihood. But the person’s email is only displayed if the person is a registered user     and the user who is searching is in the person’s contact list.

# Instructions for Code setup in local
Firstly unzip the directory folder.
And install django, django restframework, django_filters it should be enough.
Then run migrations first: 'python manage.py migrate'

Then run the data population scripts which is present in contacts/scripts folder "python contacts/scripts/contactlist_data_population.py", 
if not able to run then copy the script and open shell and run it there, as shown below.
python manage.py shell
%cpaste
#Copy paste the script for data population

You can create superuser with, python manage.py createsuperuser and then from admin can also populate and check data.

Now you can run the server with python manage.py runserver
