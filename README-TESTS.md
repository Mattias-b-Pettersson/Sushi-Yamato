# Tests

For the testing i have done the manual testing with clickin all the buttons, filled in the forms, entered wrong data to make sure it wasn't accepted and it didn't break the site.
But there is also alot of automatic tests that can be run.

# Automatic tests

Automatic tests is in total 40 python tests and 6 jest/javascript tests:

## Python

To run the python tests you must comment out the "DATABASES" variable in settings and set the database used for testing to the following in settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

When that to is do is run the command "python3 manage.py test" in the console. If it is necessary to test a individuall app in the project, type the command and add the appname after, like this "python3 manage.py menu"

### Menu tests:

- Test urls
    - Test menu url.
    - Test delete menu item url.
    - Test edit menu item url.
    - Test add menu item url.
- Test views
    - Test menu view.
    - Test delete menu item with no access.
    - Test delete menu item with access.
    - Test add menu item, both GET and POST.
    - Test edit menu item with and without permission.
- Test forms
    - Test to make sure all fields is requierd.
    - Test fields are explicit in form metaclass and in the right order.

### Booking tests

- Test urls
    - Test booking url.
    - Test booking search url.
    - Test edit booking url.
    - Test delete booking url.
    - Test show all bookings url.
    - Test check booking API url.
- Test views
    - Test booking view, both GET and POST.
    - Test edit booking, both GET and POST.
    - Test delete delete booking.
    - Test check bookings API.
- Test forms
    - Test to make sure all fields is requierd exept phonenumber field.
    - Test fields are explicit in form metaclass and in the right order.

### Menu and contact views

- - Test urls
    - Test home url.
    - Test contact search url.
- Test views
    - Test home view.
    - Test contact view.
- Test forms
    - No forms were tested in this app as there are none used.

## Javascript / Jest

To run the tests you need to have npm installed.

To test the javascript you need to install jest. The command used to install jest i used is “npm install --save-dev jest@26.6.3”. After this, write “npm init” now it will ask for values, click on enter till "test command" is displayed, write “jest” as test command. Then keep pressing enter till the yes or no question arise, write yes. Then in the console write “npm test” and the tests will run. 

### Disable submit button tests

- Check if all the classes has been added to the P tag
- Check if the text has been added to the P tag
- Check if "disabled" has been added to the P tag

### Enable submit button test

- Check if all the classes has been added to the P tag
- Check if the text has been added to the P tag
- Check if "disabled" has been added to the P tag