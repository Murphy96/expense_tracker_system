#*********************************************
# Simple Expense Tracker System 
#*********************************************

# Part 1: Database Simulation 

expenses = []

#**********************************************
#Part 2: Functions 
#**********************************************


#Expense Function 
#---------------------------------
def add_expense(amount: float, category: str, description: str) -> dict:
    '''
    Validates a user entered expense, creates a dictionary for the expense, appends it to the expenses list
    Arguments: 
        amount(float): User entered amount
        category(str): User entered expense category
        description(str): User entered description of expense
    
    Returns: 
        Created expense (dict)
    
    Raises: 
        ValueError if expense amount is invalid (less than or equal to 0)
    '''
    if amount <= 0:
       raise ValueError('Amount must be greater than 0')

    expense = {
        'amount': amount, 
        'category': category, 
        'description': description 
    }

    expenses.append(expense)
    return expense

#Total Expense Calculation Function 
#-----------------------------------

def calculate_total_expenses():
    '''
    Loops through all expenses, calculates the total amount    
    Returns: 
       float: Total of expenses
    '''
    total = 0
    for expense in expenses: 
        total += expense['amount']

    return total 

#Total Expense by Category Calculation Function
#----------------------------------------------

def calculate_total_by_category(category: str) -> float:
    '''
    Loops through expenses, calculates total for given category 
    
    Arguments: 
        category (str): The category to filter by. 
    
    Returns: 
        float: total amount for that category. 
       
    '''
    total = 0
    for expense in expenses: 
        if expense['category'].lower() == category.lower():
            total += expense['amount']

    return total 

#Print All Expenses
#------------------

def show_expenses() -> None: 
    '''
    Displays all stored expenses 

    Returns: None
    '''
    if not expenses: 
        print('No expenses recorded')
        return 
    
    print('\nAll Expenses:')
    for index, expense in enumerate(expenses, start=1):
        print(
            f'{index}, {expense['category']} - '
            f'{expense['description']}: ${expense['amount']}'
        )
    
 # Test Script
#-------------

def test_script()-> None: 
    '''
    Executes test scenarios 
    '''

    try: 
        add_expense(150, 'Food', 'Groceries')
        add_expense(20, 'Transport', 'Uber')
        add_expense(50, 'Food', 'Takeout')
        add_expense(0, 'Personal Care', 'Tolietries')

    except ValueError as error: 
        print('Error:', error)
    
    print(calculate_total_expenses())
    print(calculate_total_by_category('Food'))

    show_expenses()


if __name__=='__main__':
    test_script() 
