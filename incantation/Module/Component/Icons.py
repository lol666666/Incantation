#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 17:20:58 2017

@author: misakawa
"""

def icon(name, loc = ''):
    return f'<i class="material-icons {loc}" >{name}</i>'

mode_edit = icon('mode_edit')
icon_url = 'http://materializecss.com/icons.html'