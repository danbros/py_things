#!/usr/bin/env python3

# @author: danbros

"""
Find all links in a url
"""

import re

import urllib.request


def mod_page(x_url):
    """Open a page with a modified user-agent

    Args:
      x_url: A url in 'string' format with http://
    """

    #create a list
    mod_headers = {}
    #mod_headers[user-agent] now is OS X Safari 9.1 
    mod_headers['User-Agent'] = "Mozilla / 5.0 (Maacintosh; Intel Mac OS X 10_10_5) AppleWebKit / 601.7.7 (KHTML, como o Gecko) Versão / 9.1.2 Safari / 601.7.7"
    #assign a request of a url('x_url') with the header user-agent modified('mod_headers') to 'req'
    mod_req = urllib.request.Request(x_url, headers = mod_headers)
    #assign the response of 'mod_req' to the variable 'page'
    page = urllib.request.urlopen(mod_req)
    
    return page

x_url = input('\nEnter a url (example: "https://www.google.com"): ')
#x_url = "https://www.google.com"
#assign page with function mod_page
page = mod_page(x_url)
#assign source with source of page converted binary to str
source = str(page.read())
#re to find links in source
links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', source)

print(*links, sep='\n')

#Create a file with links
#obj_file = open('url_list.txt', 'w')
#for link in links:
#    obj_file.write(link + '\n')
#obj_file.close()


#Source:
#https://www.pythonforbeginners.com/code-snippets-source-code/regular-expression-re-findall/
#https://pythonprogramming.net/urllib-tutorial-python-3/

#Problems:
#regular expression for string:
#https://docs.python.org/3/howto/regex.html#regex-howto
#https://stackoverflow.com/questions/839994/extracting-a-url-in-python

#print list:
#https://stackoverflow.com/questions/22556449/print-a-list-of-space-separated-elements-in-python-3

#string file vs binary file:
#https://stackoverflow.com/questions/5618988/regular-expression-parsing-a-binary-file

#binary to string:
#https://stackoverflow.com/questions/606191/convert-bytes-to-a-string