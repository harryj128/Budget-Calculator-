# Budget-Calculator

### DevOps Core Fundamental Project - Author Harry Johnson

#### Objective
To create a CRUD application with the utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

To meet all the goals/objectives I will need to
* Create a Kanban board to provide clear project management
* Have a relational database in which there are a minimum of 2 tables with a relationship between them
* Clear Documents to go along with the programming hosted here on the readme page
* A Functional CRUD (Create, Read, Update, Delete) application coded in python as set out in my epic on my board
* Well-designed tests that cover my programming as much as possible
* A frontend website build with python and HTML
* Code which uses a version control system 

#### Project Overview
I want to create an app that is a Budget Calculator. I want to have lots of users who can create multiple
budgets which in turn will have multiple items attached to them. Users will be able to input and view their username email and annual salary, User will also be able to create and view budgets which will have relationships with both users and items, budgets will also have a name and a max spending amount. Items will be part of budgets and will have names, descriptions, and amounts and you will also be able to see how much of the max budget they are. 

All tables (Users, Budgets and items) should have full CRUD functionality

#### Planning and Design
The Workflow and tools are as follows

*Kanban Board: Jira
*Database: GCP SQL Server or SQLite database hosted on VM.
*Programming language: Python
*Unit Testing with Python (Pytest)
*Integration Testing with Python (Selenium)
*Front-end: Flask (HTML and CSS)
*Version Control: Git/ GitHub
*CI Server: Jenkins
*Cloud server: GCP Compute Engine

I also made a design for how a user might navigate through the site and how it would connect with the database. The helped a lot when making templates and my routes. 

![Site layout](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/Site_Layout.png)

##### ERD
This is the ERD I produced for the database tables. It was really helpful when it came to making the
python tables. This was because the three tables had a complex set of relationships and because they were pre-planned out they were easier to think about.

![ERD](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/Budget_calac.drawio.png)

The actual tables that are in my developed product are very similar to the ERD. The only changes that I made were to 
do with the size of some of the fields. Emails did not have to be as big as 50 chars and item descriptions were too
small so I increased that to 30. 

##### Jira
I found Jira has project management tool very helpful. It was my first time using such a tool but it helped me keep on track and organise my thoughts. I think this would be even better in a team environment, however. Unfortunately after my project sprint, I realised that I had not assigned points to each of the tasks. This meant that my burndown reports did not generate correctly. This is disappointing because I would have liked to see my workflow. Underneath is a cumulative flow diagram. This was quite an interesting report. In the future, I will keep track more accurately of my tasks.

![Cumulative flow diagram](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/Cumulative%20flow%20diagram.png)

##### Risk Assessment
Below is my risk assessment I thought it was quite comprehensive however halfway through development I encountered a problem which I have not encountered
before. Where my VS code would stop working so I added that to the risk assessment as it was an obstacle I might have to overcome in future projects.

![risk_assessment](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/riskassess.png)

I also had another problem where when I started using a SQL server I accidentally uploaded the username and password to git hub. The passwords were promptly changed and the risk assessment was updated. 

#### Development
##### Front End
There is a navbar for ease of use when using the application and because I put links for all of the CRUD functions underneath all the printed records there is no need for any user to mess around with the URL.
These are the forms for inputting a new entry into the tables or updating them. If you are updating a user it is pre-filled for ease of use.

![forms](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/bc-adding-item.png)
![forms](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/bc-users-adding.png)
![forms](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/bd_budgets_adding.png)

And this is what you can see when you are just viewing the different tables. You can either see all the User/Budgets/Items or specific ones according to which entities they are linked.

![views](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/bc-budgets-view.png)
![views](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/bc-users-add.png)
![views](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/bs-item-view.png)

##### Back End
The file structure was really important to this project. I made it much easier to navigate than in previous projects. I also made sure to comment as I went when I noticed problems which helped with working to a tight deadline.

![file sruct](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/file-struc.png)

Also in the background is the deletion process because you don't need to see anything it just automatically deletes the Entity from the database as well as any dependencies.

![user-delete](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/delete%20users.png)

#### Testing
Unit testing was developed so I wouldn't have to manually test the routes and modelling each time I made changes. This was further automated by the Jenkins server. When I would make a git push from my code VM it would automatically run both the unit and integration testing in the background so I didn't have to do it, It would then show me if the tests were successful and generate a coverage report.

![Coverage report](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/cov-report.png)

In the end, I had 12 unit tests. They covered each of the CRUD functions of each table. My final product passes all the tests but only has a 92% coverage. Think if I had more time I would write more integration tests as there are only 3. While I have tested the product manually thoroughly as well I think it would be better to have 100% automated tests. 

#### Automation
Jenkins as the CI server handles most of the automation and GitHub handles the rest. When I push code to git hub there is a webhook that sends the repo to the Jenkins server. From there it builds an artifact but not before running the unit and integration tests. 

![Jenkins](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/jenkins-proof.png)
![Jenkins](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/tests%20passing%20in%20jenkins.png)

#### Further analysis
In the future as I stated previously I would like the application to have some more integration tests. I would also expand the app by having buttons to filter tasks and order them in a certain way. I think the front end would need a lot of work for more public deployment. For future projects I think I will try to limit my scope a bit more, I spent too much time working on the 3 different types of tables and did not need the user's table. 

#### Acknowledgements
A big thank-you to Adam Gray and Victoria Sacre for their knowledge and help on this project.
I also used a simple navbar as linked below from w3schools. 
https://www.w3schools.com/css/css_navbar_horizontal.asp

#### Versioning
I mostly worked off a dev branch while programming only merging back when needed. Below are my branches and my commits for this project. When I ran into the problems as described in my risk assessment with VS-code not connecting with the VM very well I started making much more frequent commits and pushes.
![git](https://github.com/harryj128/Budget-Calculator-/blob/main/readme_images/Screenshot%202022-08-05%20085439.png) 

After I merged back in main I did some work on my README becuase that did not impact the code, I also tested some ideas on a dev branch but that didn't pan out. 
