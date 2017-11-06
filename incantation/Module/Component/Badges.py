#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:53:43 2017

@author: misakawa
"""

from ..abst import abstract_object,indent_setter, Seq, default_attr, attrset_sugar

class badge:
    """
    badge(name, new=False, href='', color='')
    """
    def __new__(self, name, href = '#!', new:{True,False,None} = None,  num = "", color = ''):
        
        class_ = 'new badge' if new else 'badge'
        
        if color: class_ += color
        res = f'{name}<span class="{class_}">{num}</span>'

        if href:
            res = f'<a href="{href}">{res}</a>'
        
        return res

class collections(indent_setter, abstract_object):
    """
    See http://materializecss.com/badges.html
    user help : >> help (collections.init)
        Guide:
            >> cs = collections([badge(new = False,href = '#!', num = 1, name = 'Alan'),
                                 badge(new = True, href = '#!', num = 4, name = 'Alan'),
                                 badge(href = '#!', name = 'Alan'),
                                 badge(new = False,href = '#!', num = 14,name = 'Alan')
                                ],
                                )
            >> cs
              <div class="collection">
                  <a href="#!" class="collection-item"><span class="badge">1</span>Alan</a>
                  <a href="#!" class="collection-item"><span class="new badge">4</span>Alan</a>
                  <a href="#!" class="collection-item">Alan</a>
                  <a href="#!" class="collection-item"><span class="badge">14</span>Alan</a>
              </div>
    """
    @default_attr(attr = 'class', value = "collection")
    def init(self, content : (list,[badge]), **attributes):
        body   = \
"""
{{indent}}<div {{attributes_dict}}>
{{indent+Indent_unit}}{% for badge in content%}
{{indent+Indent_unit*2}}<div class="collection-item">{{badge}}</div>
{{indent+Indent_unit}}{% endfor %}
{{indent}}</div>
"""      
        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body
        
    
class dropdown(indent_setter, abstract_object):
    """
    See http://materializecss.com/badges.html
    user help : >> help (dropdown.init)
         Guide:
             dd = dropdown([badge(new = False,href = '#!', num = 1, name = 'Alan'),
                            badge(new = True, href = '#!', num = 4, name = 'Alan'),
                            badge(href = '#!', name = 'Alan'),
                            badge(new = False,href = '#!', num = 14,name = 'Alan')
                            ],
                            name = 'a dropdown list', id = 'someid'
                            )
             
    """
    def init(self, content:(list,[badge]), **attributes:dict(material_icons = 'arrow_drop_down')):
        body = \
"""
{{indent}}<ul id="{{id}}" class="dropdown-content">
{{indent+Indent_unit}}{% for badge in content%}
{{indent+Indent_unit*2}}<li>{{badge}}</li>
{{indent+Indent_unit}}{% endfor %}
{{indent}}</ul>
{{indent}}<a {{attributes_dict}} data-activates="{{id}}">{{name}}<i class="material-icons right">{{material_icons}}</i></a>
           
"""
        sugar = attrset_sugar(self.conf, attributes)
        sugar('name', 'Dropdown[name = ???]')
        sugar('id', 'ID[unknown]')
        sugar('material_icons', 'arrow_drop_down')
        
        @default_attr(attr = 'class', value = 'btn dropdown-button')
        @default_attr(attr = 'href' , value = '#!')
        def  _init_(content:(list,[dict]), **attributes):
            self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
            self.body = body
        _init_(content, **attributes)
        

class collapsible(indent_setter, abstract_object):
    """
    See http://materializecss.com/badges.html
    user help : >> help (collapsible.init)
        Guide:
            collap = collapsible([(icon('filter_drama'),badge(href = '#!', name = "First") , "<p>Lorem ipsum dolor sit amet.</p>"),
                                  (icon('place'),       badge(href = '#!', name = "Second"), "place")
                                 ])
    """
    @default_attr(attr = 'class', value = "collapsible")
    @default_attr(attr = 'data-collapsible', value = 'accordion')
    def init(self, content, **attributes):
        sugar = attrset_sugar(self.conf, attributes)
        sugar('active', False)
        body = \
"""
{{indent}}<ul {{attributes_dict}}>
{{indent+Indent_unit}}{% for item in content %}
{{indent+Indent_unit}}<li>
{{indent+Indent_unit}}<div class="collapsible-header {%if active%}active{%- endif -%}">
{{indent+Indent_unit}}{{item[0]}}
{{indent+Indent_unit}}{{item[1]}}
{{indent+Indent_unit}}</div>
{{indent+Indent_unit}}<div class="collapsible-body">
{{indent+Indent_unit*2}}<ul>
{{indent+Indent_unit*2}}<li>
{{indent+Indent_unit*3}}{{item[2]}}
{{indent+Indent_unit*2}}</li>
{{indent+Indent_unit*2}}</ul>
{{indent+Indent_unit}}</div>
{{indent+Indent_unit}}</li>
{{indent+Indent_unit}}{% endfor %}
{{indent}}</ul>
"""
        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body
        
    
    
        