# testCases_240219

## Test Cases for Sogeti Interview Test

- All test were created on an Windows 10 OS, PyCharm IDE, Postman Web Browser Platform
- Other operating systems or IDEs have not been tested

### Requirements

- Python
- Python IDE
- Selenium
- Postman Web Platform

## Python

### Install Python

- open command line with admin rights
- type in:

> cd C:\
> python


Microsoft Store will now open Python 3.12 download page
Click Get on the  Python 3.12 page
Python 3.12 will be installed

After installation you can optionally run following in CMD to see installed files

> pip list


## Python IDE

### Installation of PyCharm

- Download community version of PyCharm
    - ```(https://www.jetbrains.com/pycharm/download/)```
- Run the installer exe after download to install PyCharm

![PyCharm Download Page](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/pycharm/00_install_pycharm.JPG "PyCharm Download Page")


### Open UI test directory

- Open PyCharm
- open "testCases_240219\testCases\UI Tests\testCases" from the git repository (link)

If not included in the repository it may be required to install Selenium into the environment.

Therefore navigate to the terminal and enter:

> pip install selenium

![PyCharm Selenium Install](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/pycharm/00_install_selenium.JPG "PyCharm Selenium Install")


### Open and run tests 1..3

- Open testCase1.py from the navigation bar
- right-click into IDE
- select run 'testCase1'

![PyCharm Selenium Test 1](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/pycharm/01_test1_run.JPG "PyCharm Selenium Test 1")

A browser will open up and follow the instructions from the test script

and results from the test will appear in the PyCharm console

![PyCharm Selenium Test Result](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/pycharm/02_test1_result.JPG "PyCharm Selenium Test Result")

Repeat same procedure with test cases 2 and 3


## Postman Web Browser Platform

- Create a free account on
    - https://www.postman.com/
- Sign in after creating account
- Open Postman Web Platform on
    - https://go.postman.co/homenull

### Import Postman API Tests

Postman Test Cases have been exported in a JSON file (link)
This can be imported by using the provided file from the repository

- Open your Workspace

![Postman Workspace](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/01_nav_myworkspace.JPG "Postman Workspace")

- Click 'Import' on left navigation bar
- Choose (Sogeti API Test.postman_collection.json)
- Click OK

![Postman Import](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/02_nav_import.JPG "Postman Import")

![Postman Drop File](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/03_import_dropfile.JPG "Postman Drop File")

You will now have the directory "Sogeti API Test" with testCase4 and 5 in your Workspace

![Tests in workspace](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/04_workspace_test4%2B5.JPG "Tests in workspace")


### Run Test Case 4

To run testCase4 proceed as follows:

- click "testCase4" and move to the "Tests" register to see the testing scripts
- click "Send" to run the test
- results will be shown below under "Test Results"

![Postman Test Case 4](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/05_testCase4.JPG "Postman Test Case 4")

![Postman Test Case 4 Result](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/06_testCase4_result.JPG "Postman Test Case 4 Result")


### Run Test Case 5

As this case is data driven, "Body" and the "Run Collection" have to be configured

- click the testCase5 register and navigate to "Body" to see the added variables

![Postman Testcase 5 Body](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/09_testCase5_body.JPG "Postman Testcase 5 Body")

- move to "Tests" to see the test script

![Postman Testcase 5](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/07_testCase5.JPG "Postman Testcase 5")

- right-click onto the 3-dots button on "Sogeti API Test"
- click Run Collection
- only tick the checkbox of testCase5
- import configuration file by selecting from repository
    - [Select "testCase5post.json"](file:https://github.com/dse-dev/testCases_240219/blob/main/testCases/API%20Tests/testCase5post.json)

![Postman Testcase 5 Run Collection](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/08_testCase5_runCollection.JPG "Postman Testcase 5 Run Collection")

![Postman Testcase 5 Select File](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/10_testCase5_selectFile.JPG "Postman Testcase 5 Select File")

- click "Run Sogeti API Test"

Now all data from the uploaded JSON file will be posted

Results from the performed tests will appear automatically

![Postman Testcase 5 Results](https://github.com/dse-dev/testCases_240219/blob/main/docs/img/postman/11_testCase5_PostResults.JPG "Postman Testcase 5 Results")


