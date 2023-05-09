# cosi107a-FinalProject

Final Project for COSI-107A: Introduction to Computer Security

Created by:

* Anya Lefkowitz
* Hannah Whitmore
* Thomas Vandalovsky

## Project Description

This project is an implementation of SQL injection in Python. The purpose of this project is to demonstrate how a poorly designed application which uses SQL as its database management system is vulnerable to cyber attacks and can have unwanted data extraction and manipulation.

The vulnerable SQL command that is taken advantage of in this project occurs in unsafe app.py around line 50 of the code. Since the query is not parameterized an attacker is able to pass unwanted SQL commands through the html form which get executed by MySQL and grant admin access to the attacker.

To use the project and execute the code you should first run `make dependencies` which install all needed packages. Next you can run `make unsafe_run` or `make safe_run` to play with the unsafe and safe app environments. To clean up your MySql environment you can run `make unsafe_clean` or `make safe_clean` which will delete the database created for the project and all tables and entries within it.

To commit the SQL injection which grants the hacker admin access to the database pass `' OR 'a'='a';--` into the name form box and anything you would like into the email form box. This command will cause the SQL statement which is made to check if the user entered is an admin always return true granting unwanted access. By doing so the hacker will be able to see all users personal data that was meant to only be visible to admin users completing the attack. This is prevent with proper query parameterization in the safe version of the app.

## Project Implementation

This project is implemented in Python and uses Flask and MySQL.

The dependencies you need to run the apps on your own machine can be seen in the Makefile under dependencies make target.

The current necessary python packages are:

* Flask
* mysql-connector-python

The current necessary software packages are:

* MySQL

## TODO

* [x] get sql injections to work in unsafe environment

  * [x] automate sql operations to populate unsafe_db
  * [ ] automate sql injection testing
  * [x] create better documentation for code!!!
  * [ ] support other forms of SQL attacks such as UNION, DROP, and INSERT

* [x] create safe environment with sql injections
