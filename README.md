# Udacity Full-Stack Nanodegree

## Project 1 - Log Analysis

## Project Purpose
Build an informative tool that prints out a summary report from logs. This reporting tool is a Python program using the psycopg2 module to connect to a database.

## Questions
1. What are the most popular three articles of all time?
  Which articles have been accessed the most?
  Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors?
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

# Steps to Install and Run

  - Download and install VM using `Virtual Box` from [here](https://www.virtualbox.org/wiki/Downloads).
  - Download and install `Vagrant` from [here](https://www.vagrantup.com/downloads.html).
  - To configure the VM, run the command `vagrant up` in the working folder.
  - Download the [news data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and save it on working VM folder.
  - Running `psql -d news -f newsdata.sql` command will connect to your installed database server and execute the SQL commands in the downloaded file.
  - Run `log_metrics.py` on terminal to generate the database report.

# Expected Output:

TOP THREE ARTICLES BY PAGE VIEWS:

    (1) "Candidate is jerk, alleges rival" - 338647 views
    (2) "Bears love berries, alleges bear" - 253801 views
    (3) "Bad things gone, say good people" - 170098 views
    
TOP THREE AUTHORS BY VIEWS:

    (1) "Ursula La Multa" - 507594 views
    (2) "Rudolf von Treppenwitz" - 423457 views
    (3) "Anonymous Contributor" - 170098 views
    (4) "Markoff Chaney" - 84557 views
    
DAYS WITH MORE THAN 1% ERRORS:

    July 17, 2016 - 2.3% errors