# cosi107a-FinalProject

Final Project for COSI-107A: Introduction to Computer Security

Created by:

* Anya Lefkowitz
* Hannah Whitmore
* Thomas Vandalovsky

## Project Description

This project is an implementation of SQL injection in Python. The purpose of this project is to demonstrate how a poorly designed application which uses SQL as its database managment system is vulnerable to cyber attacks and can have unwanted data extraction and manipulation.

The vulnerable SQL command that is taken advantage of in this project occurs in unsafe app.py around line 50 of the code. Since the query is not parameterized an attacker is able to pass unwanted SQL commands through the html form which get executed by MySQL and grant admin access to the attacker.

To use the project and execute the code you should first run `make dependencies` which install all needed packages. Next you can run `make unsafe_run` or `make safe_run` to play with the unsafe and safe app enviornments. To clean up your MySql enviornment you can run `make unsafe_clean` or `make safe_clean` which will delete the database created for the project and all tables and entries within it.

## Project Implementation

This project is implemented in Python and uses Flask and MySQL.

The dependences you need to run the apps on your own machine can be seen in the Makefile under dependences make target.

The current necessary python packages are:

* Flask
* mysql-connector-python

The current necessary software packages are:

* MySQL

## TODO

* [x] get sql injections to work in unsafe enviornment

  * [x] automate sql operations to populate unsafe_db
  * [ ] automate sql injection testing
  * [x] create better documentation for code!!!
  * [ ] support other forms of SQL attacks such as UNIION, DROP, and INSERT

* [x] create safe enviornment with sql injections
