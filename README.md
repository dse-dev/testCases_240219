# testCases_240219

## Test Cases for Sogeti Interview Test

All test were created on an Windows 10 OS, PyCharm IDE, Postman Web Browser Platform
Other operating systems or IDEs have not been tested

### Requirements

Python
Python IDE
Selenium

Postman Web

### Python

Install Python

open command line with admin rights

> cd C:\
> python


Microsoft Store will now open Python 3.12 download page
Click Get on the  Python 3.12 page
Python 3.12 will be installed

After installation you can run following in CMD to see installed files

> pip list


### Python IDE

#### Installation of PyCharm

Download community version of PyCharm ```(https://www.jetbrains.com/pycharm/download/)```
After downloading run the installer exe.

#### Open and run tests 1..3

Open PyCharm and open "testCases_240219\testCases\UI Tests\testCases" from the git repository (link)

If not included in the repository it may be required to install Selenium into the environment.
Therefore navigate to the terminal and enter:

> pip install selenium


(pic)

Open testCase1.py from the navigation bar, right-click into IDE, select run 'testCase1'
A browser will open up and follow the instructions from the test script.
Results from the test will appear in the PyCharm console
(pic)

Repeat same procedure with test cases 2 and 3


### Postman Web Browser Platform

No need to install anything
Create a free account on ```https://www.postman.com/```
After creating an account and signing in open the Postman Web Platform on https://go.postman.co/homenull


### Import Postman API Tests

Postman Test Cases have been exported in a JSON file (link)
This can be imported by using the file (Sogeti API Test.postman_collection.json)