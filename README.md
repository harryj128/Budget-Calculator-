# Budget-Calcuator

### DevOps Core Fundamental Project - Author Harry Johnson

#### Objective
To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

To meet all the goals/objectives I will need to
* Create a Kanban board to provide clear project mangement
* Have a relational database in which there are a minimum of 2 tables with a relationship between them
* Clear Documents to go along with the programming hosted here on the readme page
* A Functional CRUD (Create, Read, Update, Delete) application coded in python as set out in my epic on my board
* Well designed tests that cover my programming as much as possible
* A frontend website build with python and html
* Code which uses a version control system 

#### Project Overview
I want to create an app that is a Budget Calculator.I want to have lots of users which are able to create multiple
budgets which in turn will have multiple items attached to it. Users will be able to input and view their username email and annual salary, User will also be able to create and view budgets which will have relationships with both users and task, budgets will also have a name and a max spending amount. Items will be part of budgets and will have names, descriptions, amounts and you will also be able to see how much of the max budget they are. 

All tables (Users, Budgets and items) should have full CRUD functionailty

#### Planning and Design
The Workflow and tools are as Following

*Kanban Board: Jira
*Database: GCP SQL Server or SQLite database hosted on VM.
*Programming language: Python
*Unit Testing with Python (Pytest)
*Integration Testing with Python (Selenium)
*Front-end: Flask (HTML and CSS)
*Version Control: Git/ GitHub
*CI Server: Jenkins
*Cloud server: GCP Compute Engine

##### ERD
This is the ERD i produced for the database tables. It was really helpful when it came to actually making the
python tables. This was becuase the three tables had a complex set of relationships and becuase they were pre planned out they were easier to think about. 
![ERD](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/Budget_calac.drawio.png)
the actual tables that are in my devloped product are very similar to the ERD. The only changes that I made were to 
do with the size of some of the fields. Emails did not have to be as big as 50 chars and item descriptions were to
small so I increased that to 30. 

##### Jira

##### Risk Assessment
Below is my risk assessment i thought it was quite comprehensive however halfway through development I encountered a problem which i have not encountered
before. Where my VS code would stop working so I added that to the risk assessment as it was obsitcal I might have to overcome in future projects.
![risk_assessment]()

#### Development

#### Testing
Unit testing was developed so I wouldn't have to manually test the routes and moddeling each time I made changes. This was further automated by the jenkins server. When I would make a git push from my code VM it would automaticly run both the unit and intergration testing in the background so I didn't have to do it, It would then show me if the tests were successful and generate a coverage report.

In the end I had 12 unit tests. They covered each of the CRUD functions of each table. My final product passes all the tests but 

#### Further analysis

#### Licensing

#### Contributors

#### Acknowledgements
https://www.w3schools.com/css/css_navbar_horizontal.asp
#### Versioning

