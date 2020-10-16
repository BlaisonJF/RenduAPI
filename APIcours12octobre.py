# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:40:44 2020

@author: jfbla
"""

import requests #dépend code java

produit = '{"code":5,"designation":"SFP_module","prix":200}'
produit_url = "http://localhost:8989/produit"+code
ajouterunproduit = "http://localhost:8989/ajouterunproduit"+produit

r = requests.get('http://localhost:8989/produit/')
	#récupère les infos sur les produits à l'adresse indiquée ci-dessus
print(r)
	#j'affiche les produits dans la console
