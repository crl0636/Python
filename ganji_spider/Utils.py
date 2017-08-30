import logging
import urllib2
import Common
import random
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_data(url):
    logging.info('Start to pick up from page:{0}'.format(url))

    try:
        req = urllib2.Request(url, headers=Common.hds[random.randint(0, len(Common.hds)-1)])
        source_code = urllib2.urlopen(req,timeout=30).read()
        text = unicode(source_code)
        soup = BeautifulSoup(text, 'html5lib')
    except urllib2.HTTPError as http_error:
        logging.error('Error: {0}'.format(http_error.message))
        raise urllib2.HTTPError('http exception')
    except urllib2.URLError as url_error:
        logging.error('Error: {0}'.format(url_error))
        raise urllib2.URLError('URL is wrong:{0}'.format(url))
    except Exception as exception:
        logging.error('Error: {0}'.format(exception))
        raise Exception('Error: {0}'.format(exception))
    return soup

