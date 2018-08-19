#!/usr/bin/env python3
# encoding: UTF-8

import psycopg2

DBNAME = "news"

# Define Constants
metric1_query = """SELECT articles.title, count(*) as views "
                "FROM articles inner JOIN log ON log.path "
                "LIKE concat('/article/', articles.slug) "
                "WHERE log.status LIKE '%200%' GROUP by "
                "articles.title, log.path ORDER by views DESC limit 3"""

metric2_query = """SELECT authors.name, count(*) as views "
                "FROM articles JOIN authors ON articles.author = authors.id "
                "JOIN log ON articles.slug = substring(log.path, 10)"
                "WHERE log.status LIKE '200 OK' GROUP BY authors.name "
                "ORDER BY views DESC;"""

metric3_query = """WITH num_requests AS (SELECT time::date AS day, count(*)"
                "FROM log GROUP BY time::date ORDER BY time::date),"
                "num_errors AS ("
                "SELECT time::date AS day, count(*) FROM log "
                "WHERE status != '200 OK'"
                "GROUP BY time::date ORDER BY time::date), error_rate AS ("
                "SELECT num_requests.day, num_errors.count::float / "
                "num_requests.count::float * 100"
                "AS error_pc FROM num_requests, num_errors "
                "WHERE num_requests.day = num_errors.day"
                ") SELECT * FROM error_rate WHERE error_pc > 1;"""

# Define functions


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except Exception as e:
        print ("Unable to connect to the database")
        print ("Error: " + str(e))
        print (traceback.format_exc())


def popular_article():
    db, c = connect()
    c.execute(metric1_query)
    result = c.fetchall()
    db.close()
    print("\nTOP THREE ARTICLES BY PAGE VIEWS:")
    for i in range(0, len(result), 1):
        print ("(" + str(i + 1) + ") \"" + result[i][0] +
               "\" - " + str(result[i][1]) + " views")


def popular_authors():
    db, c = connect()
    c.execute(metric2_query)
    result = c.fetchall()
    db.close()
    print("\nTOP AUTHORS BY VIEWS:")
    for i in range(0, len(result), 1):
        print ("(" + str(i + 1) + ") \"" + result[i][0] +
               "\" - " + str(result[i][1]) + " views")


def log_status():
    db, c = connect()
    c.execute(metric3_query)
    results = c.fetchall()
    db.close()
    print("\nDAYS WITH MORE THAN 1% ERRORS:")
    for result in results:
        print('{date:%B %d, %Y} - {error_rate:.1f}% errors'
              .format(date=result[0], error_rate=result[1]))


if __name__ == "__main__":
    popular_article()
    popular_authors()
    log_status()
