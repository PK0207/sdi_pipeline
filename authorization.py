#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:03:29 2018

@author: andrew
"""

import requests

def get_authorization(username, password):
#    username = raw_input('Enter LCO username: ')
#    password = raw_input('Enter LCO password: ')
    
    try:
        tok = requests.post(
            'https://observe.lco.global/api/api-token-auth/',
            data = {
                'username': username,
                'password': password
            }
        ).json()

        token = 'Token ' + tok['token'] 
              
        return {'Authorization': token}
        
    except:
        print('\n-> Incorrect username/password')
