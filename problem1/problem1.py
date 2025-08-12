# Problem 1
# In the problem1 module, create a function named is_leap_year that takes one argument, an integer, that represents the year.
# The function should return True if the year is a leap year and False otherwise.
# A leap year is a year that adheres to the following:
# Is divisible by 4 and not by 100
# Or if it is divisible by 100, it is also divisible by 400
# For example, 2100 is not a leap year, but 2400 is a leap year.
# Uncomment the import in test_problem1.py, uncomment the test bodies, and delete the pass keyword.
# Run the tests and if they pass, commit and push the code to GitHub.
# Verify that the tests pass under the Actions tab in GitHub.

def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 400 == 0) and (year % 100 == 0):
        return True
    else:
        return False
