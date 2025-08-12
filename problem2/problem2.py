# Problem 2
# In the problem2 module, create a function named date_format that takes one argument, a string, that is in the format MM/DD/YYYY.
# The function should the date formatted as YYYY-MM-DD.
# Uncomment the import in test_problem1.py, uncomment the test bodies, and delete the pass keyword.
# Run the tests and if they pass, commit and push the code to GitHub.
# Verify that the tests pass under the Actions tab in GitHub.

def date_format(d):
    year = d[6:]
    day = d[3:5]
    month = d[0:2]
    return f"{year}-{month}-{day}"
