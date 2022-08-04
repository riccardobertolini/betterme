# BetteMe

## Table of Contents
1. [General Information](#General-Information)
2. [Prerequisites](#Prerequisites)
3. [Install](#Install)
4. [Start](#Start)
5. [Test](#Test)
6. [Usage](#Usage)
7. [Contribution](#Contribution)


## General Information 
BetterMe is an app that want to improve users life, while they develop good habits repeating healthy tasks.
The app is written in Python, using questionary to help the navigation throught the menu. It's currently supporting multi users and saving the data on a local SQL Database, in order to improve performance, usability and portability.
The app is written using Object Oriented pattern and functional programming, reusing the functions as much as possible. Also, there is real case scenario test for the Tasks main file.

The users can:
* create their own profile
* create new tasks, assigning a periodicity (day, week, month)
* record their progress daily
* analyse their progresses, in particular:
  * longest streak ever on a specific task
  * task with the longest streak ever
  * tasks completed this specific day
* updating their password

This app has been my first python project, however I've tried to focus on some particular aspects that could make it work even if some edges are still rough:
* intuitive navigation via CLI
* performance and security due local DB
* validation on fields to enable consistent data
* flexibility to expand with more functionalities
* test suite installed and creating a virtual db to simulate real time queries

## Prerequisites
Before you continue, ensure you have met the following requirements:
* You have installed the latest version of Python (3.9+).
* You are using a machine that allow the usage of SQL-lite with full permission to write on database

## Install
Run before you go the pip command in order to install dependencies with:
```
pip install -r requirements.txt
```


## Start

Once the dependencies are satisfied, unzip the folder and navigate into it using the `cd` command. Then, run on terminal, 
```
python main.py
```
and follow the instruction on screen.
BetterMe will run a quick check on the database, and if it's empty, it will create the main tables. 


## Tests
The tests are using `pytest`. This software can detect automatically where the tests are following the convention `***__test.py`. The current file tested is Tasks, so to see if there's passing please run:
Run on terminal
```
pytest .
```
and follow the instruction on screen.


## Usage
As first step, please create an user. On the current repository is provided an example DB with an user (username: mary, password: test) and some tasks already completed for demo purposes. You can erase the database in case you don't want to use the demo data and the app will take care to create the tables that are needed. 
Main menu functionalities (matching their file naming):
* Tasks
* Analytics
* Settings
* Logout and Exit
 

## Contribution
Any suggestions and pull requests are welcome.    

