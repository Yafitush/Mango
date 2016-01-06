__author__ = 'nick'
#!python
# -*- coding: utf-8 -*-


import requests
import argparse



class Connect():
    """
    Abstact class / Make a connection object to haystack server using requests module
    A class must be made for different type of server. See NiagaraAXConnection(HaystackConnection)
    """
    def __init__(self, url, username, password):
        """
        Set local variables
        Open a session object that will be used for connection, with keep-alive feature
            baseURL : http://XX.XX.XX.XX/ - Server URL
            USERNAME : used for login
            PASSWORD : used for login
            COOKIE : for persistent login
            isConnected : flag to be used for connection related task (don't try if not connected...)
            s : requests.Session() object
            _filteredList : List of histories created by getFilteredHistories
            timezone : timezone from site description
        """
        self.baseURL = url
        self.USERNAME = username
        self.PASSWORD = password
        self.COOKIE = ''
        self.isConnected = False
        self.s = requests.Session()
        self.authenticate()

    def authenticate(self):

        myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'password': self.PASSWORD}
        try:
            r = self.s.get('http://' + self.baseURL + ':8080' + '/rest/v1/login/' + self.USERNAME, headers=myHeader)
        except requests.packages.urllib3.exceptions.ProtocolError:
            print "Server is unavailable, Connection Not set"
        else:
            if r.status_code == 200 or r.status_code == 201:
                self.isConnected = True
                print "Connected to mango " + self.baseURL
                setCookie = r.headers['Set-Cookie']
                self.parseMyCookie(setCookie)
            else:
                print "Could Not connect"

    def parseMyCookie(self, reqCookie):
        temp_cookie = reqCookie.split(',')
        my_cookie = {(temp_cookie[0].split(';')[0]).split('=')[0].strip(): (temp_cookie[0].split(';')[0]).split('=')[1],
                     (temp_cookie[1].split(';')[0]).split('=')[0].strip(): (temp_cookie[1].split(';')[0]).split('=')[1]}
        self.COOKIE = my_cookie

