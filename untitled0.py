# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 11:43:36 2022

@author: francois
"""

import requests
resultat=requests.post(url='http://127.0.0.1:5000/predict',data={'SK_ID_CURR':185758}).json()
print(resultat)
