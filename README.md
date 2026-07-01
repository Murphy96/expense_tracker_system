# Welcome!

This project creates a simple expense tracker system using Python. 

## Project Requirements 

### 1) Simulate a Database 

This section creates a global lists to simulate a connection to a database. 

### 2) Functions
 
This section contains 4 functions: 
      
- **add_expense(amount, category, description)**
     - Validates that the amount is greater than 0, raises a ValueError if the amount is invalid,
       creates a dictionary for the expense, appends it to the expenses list, returns the created expense.  

 - **calculate_total_expenses()**
      - Loops through all expenses, calculates the total amount of the expenses, returns the total.    

 - **calculate_total_by_category(category)**
     - Loops through all expenses, calculates the total only for the given category, returns the total. 

 - **show_expenses()**
     -   Clearly displays all stored expenses 

### 3) Testing Section

This section contains a testing script that: 
   -  Adds multiple expenses, includes an invalid expense, prints total expenses,
      prints total for a specific categoy, displays all stored expenses. 




 This section contains a function called **create_user_account(name,email,password)**

 - This function calls **validate_user_date()** to validate inputs. Checks if the email already exists, and if it doest, raises a Value Error. 
 If validation passes, the function creates a dictionary containing name, email, password, and a status flag set to active. It appends the dictonary to the "database" and 
 returns the created user dictionary. 

