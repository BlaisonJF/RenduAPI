# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:40:44 2020

@author: jfbla
"""

import requests

r = requests.get('http://localhost:8989/produit/')
	#récupère les infos (produits) à l'adresse indiquée ci-dessus
print(r)
	#j'affiche les produits dans la console