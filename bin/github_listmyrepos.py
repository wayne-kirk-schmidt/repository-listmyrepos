#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exaplanation: github_listmyrepos.py. list all of your Github repositories!

Usage:
   $ python  github_listmyrepos.py [ options ]

Style:
   Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

    @name           github_listmyrepos.py
    @version        1.00
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   Apache 2.0
    @license-url    https://www.apache.org/licenses/LICENSE-2.0
"""

__version__ = 1.00
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@gmail.com)"

### import os
import sys
import datetime
import argparse
import requests
sys.dont_write_bytecode = 1

MY_CFG = 'undefined'

PARSER = argparse.ArgumentParser(description="""

github_listmyrepos.py displays info on all Github repositories you have.

""")

PARSER.add_argument("-u", metavar='<username>', required=True, dest='USERNAME', help="set username")

PARSER.add_argument("-r", metavar='<resource>', default="html_url", dest='RESOURCE', \
                    help="specify resource (default: html_url )")

ARGS = PARSER.parse_args()

RESOURCE = ARGS.RESOURCE

try:
    USERNAME = ARGS.USERNAME
except KeyError as myerror:
    print(f'Environment Variable Not Set :: {myerror.args[0]}')
    sys.exit()

REPOLIST = {}

RIGHTNOW = datetime.datetime.now()

DATESTAMP = RIGHTNOW.strftime('%Y%m%d')

TIMESTAMP = RIGHTNOW.strftime('%H%M%S')

### beginning ###

def main():
    """
    Retrieve the repository list into JSON, and extract out details
    """

    baseurl = 'https://api.github.com/users'
    tailurl = 'repos?type=all&per_page=10000'
    githubrepo = f'{baseurl}/{USERNAME}/{tailurl}'
    response = requests.get(githubrepo)
    repolist = response.json()
    for repo in repolist:
        repourl = repo[ARGS.RESOURCE]
        reponame = repourl.split('/')[-1]
        print(f'| [{reponame}]({repourl}) |')

if __name__ == '__main__':
    main()
