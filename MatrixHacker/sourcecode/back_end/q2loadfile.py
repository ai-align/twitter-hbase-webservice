#!/usr/bin/python
#coding = utf-8

import boto
import urllib2
import json
from boto.s3.connection import S3Connection
import urllib, MySQLdb
import sys

def usage():
    print "Usage: python26 mysql.py or ./mysql.py"
    sys.exit(1)

if len(sys.argv) != 1:
    usage()


def main():

    # Connect to the database and create the tables
    connSQL = MySQLdb.connect (host = "localhost",
                       user = "root",
                       passwd = "82267185", init_command = "set names utf8")
    connSQL.autocommit(False)
    cursor = connSQL.cursor ()
    cursor.execute("set names utf8")
 #   cursor.execute ("DROP DATABASE IF EXISTS twitter")
 #   cursor.execute ("CREATE DATABASE twitter")
    cursor.execute ("USE twitter")
    cursor.execute ("""
        CREATE TABLE tweetsq2
        (
          
          create_at      VARCHAR(35),
          tidtext       text
    	  
    
        ) ENGINE=InnoDB CHARACTER SET=utf8;
   """)
    
    conn =   S3Connection('AKIAIUUSLBP7GFHBNSDA','PDCZYJMlo6C4JnyWTMybv2XhDLbZhdtHsIjoTU20')
    mybucket = conn.get_bucket('tweetq2')
    set = mybucket.list()
    for i in set:
            s=i.name
            s = "http://s3.amazonaws.com/tweetq2/" + s
            response = urllib2.urlopen(s)
            tweets = response.read().split('\n')
            print s
            
            for tweetJasons in tweets:
                    if tweetJasons == "":
                            continue
                    
                    create_at = tweetJasons.split('\t')[0]
 		    
                    tid_textList = sorted(tweetJasons.split('\t')[1:])
                    tid_text = '\t'.join(tid_textList)
		    #tweet = json.loads(tweetJason)
                    #userid = tweet['userid']
	#            print userid
                    #tid = tweet['tid']
	#	    print count 
                    #content = tweet['text']
                    #content = "content"
	#	    print content
		    #create_at = tweet['timestamp']
                    #if tweets['o_userid'] == false:
                    #    o_userid = -1
                    #else:
                   # o_userid = tweet['o_userid']
 #                   print userid + ' '+ tid+ ' '+ content +' ' + create_at + '\n'   

#                   cursor.execute ("""INSERT INTO tweetsq2   (create_at, tid_text) VALUES  (%s, %s)""", (create_at, tid_text))
    #Commit the changes.
                    connSQL.commit()
	#	    print "my heart is in the work"  
    cursor.close()
    connSQL.close()
       
if __name__=="__main__":
    main()
