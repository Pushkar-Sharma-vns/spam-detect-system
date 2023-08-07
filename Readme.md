

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