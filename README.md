![Multiple screens image](assets/readme-images/multiple-screens.png)

# Sushi Yamato

Sushi Yamato is a Sushi restaurant, which accepts bookings, and booking handling. Editing and viewing the menu.

# Features

## Menu

- Here customers can view the menu without authentication.

- The lists is sorted with the diffrent meals and beverages available.

- Can see the price. 

- Can see the description of the diffrent meals/beverages.

- The menu adopts to diffrent screen sizes.

   ![Menu image](assets/readme-images/score-count.png)

- Menu for employees
    
    - An employee can sign in and wiew the separate view with the menu only available to employees.

    - The employee is able to add, edit or delete menu items

      ![Employee menu image](assets/readme-images/score-count.png)

## Booking

- On the booking page the customers is able to book a table. 

- If there are no tables available the user is notified directly when choosing time, date or tablesize and the submit button is disabled.

- If there are no tables available and the customer has turned of javascript the booking won't go through and a message will appear.

- When the booking is saved the customer gets a notification with a booking number.

- The customer can with the booking number edit the booking or entirely delete it.

- Booking for employees

    - An employee can sign in and view the separate view with bookings only available to employees. Here the employee can view all the bookings that has been saved.

    - The employee is able to add, edit or delete booking

## Accounts

- It is possible to create accounts for everyone.

- If the administrator hasn't added the user account to a specific group or added the right permissions, the user won't be able to see the employee features.

# Testing

- I have tested the application on mobile and also in diffrent browsers to make sure everything is displayed correctly and that every button works as expected.

- All the automated tests description is located [here](/README-TESTS.md).


## Solved Bugs

When deploying the application to heroku there were multiple bugs that arose.

- First the application didn't deploy, this was due to a compatability error with the backports.zoneinfo package.
This was fixed by adding “backports.zoneinfo==0.2.1;python_version<"3.9" in the requirements.txt instead of “backports.zoneinfo==0.2.1"

- The hero image didn't display, this was due to i didn't know that heroku don't host normal images. 
I could fix this by either installing a package that is called whitenoise or host the image on cloudinary.
I chose cloudinary as i had already made a connection to cloudinary with everything else, but the image was hardcoded into the source tag in the CSS.

- The booking page didn't work when deployed at first. The error message was "Access forbidden 400", this was due to that the JS was comming from cloudinary and that wasn't allowed. This was fixed by adding the small amount of JS directly in to the html file.

## Remaining Bugs

- There are no known bugs remaining.

# Validator Testing



# Deployment



# Credits

