#!/usr/bin/python
"""CS 489 Big Data Infrastructure (Winter 2016): Self-check script

This file can be open to students

Usage: 
    run this file on 'bigdata2016w' repository with github-username
    ex) check_assignment0_public_altiscale.py [github-username]
"""

import sys
import os
from subprocess import call
import re

def convertusername(u):
  return re.sub(r'^(\d+.*)',r'a\1',u)

def check_a0(u):
    """Run assignment0 in linux environment"""
    call(["mvn","clean","package"])

    call([ "hadoop","jar","target/bigdata2016w-0.1.0-SNAPSHOT.jar",
           "ca.uwaterloo.cs.bigdata2016w."+u+".assignment0.PrefixCount",
           "-input", "/shared/cs489/data/enwiki-20151201-pages-articles-0.1sample.txt", 
           "-output", "cs489-2016w-"+u+"-a0-wiki" ])
    print("Question 4.")
    call("hadoop fs -cat cs489-2016w-"+u+"-a0-wiki/part-r-00000 | sort -k 2 -n -r | head -3",shell=True)
    print("Question 5.")
    call("hadoop fs -cat cs489-2016w-"+u+"-a0-wiki/part-r-00000 | grep li",shell=True)
    

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    u = convertusername(sys.argv[1])
    check_a0(u)
  except Exception as e:
    print(e)
