import atexit
import re
import threading
import time
import urllib2

REGEX = re.compile('#([\d.]+) in Books ')
aws_url = 'http://www.amazon.com/dp'

iSBNs = {'D132269937':'Core Python Programing'}

def get_ranking(isbn):
