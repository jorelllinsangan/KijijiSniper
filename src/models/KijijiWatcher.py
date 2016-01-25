import requests, webbrowser, re
from sqlalchemy import Column, Integer, String, ForeignKey
from database.Base import Base
from sqlalchemy.orm import relationship
class KijijiWatcher(Base):

	__tablename__ = 'kijiji_watcher'


	base_url = "www.kijiji.ca/"

	area_codes = {
		'winnipeg': 'k0l1700192'
	}

	id = Column(Integer, primary_key = True)
	client_id = Column(Integer, ForeignKey('clients.id'))
	client = relationship("Client", back_populates="kijiji_watcher")
	product_id = Column(Integer, ForeignKey('products.id'))
	product = relationship("Product")

	
	# def form_url(self, product, price = '', location = 'winnipeg'):
	# 	#validate product, price, and location. 
	# 	#for product and location, spaces are turned into -
	# 	#price must be 0__price
	# 	product = product.replace(" ", "-")
	# 	location = location.replace(" ", "-")

	# 	if not re.match(r'0__[0-900]+', price):
	# 		price = '0__%s' % price

	# 	return "%s/b-%s/%s/%s?%s" (base_url, location, product, area_codes[location], price)

	# def get_page(self,url):

	# 	'''makes arequests get request to retrive html data from kijiji.ca'''

	# def get_ads(self,page):
	# 	'''Returns a list of ads found in page'''

	# def add_product(self,product_id):
	# 	'''Adds product to database'''

	# def product_saved(self,product_id):
	# 	'''Checks if product is stored in databas'''

	# def add_page(self, product, price = '', location = 'winnipeg'):
	# 	'''This function adds a query to the list of things to watch out for'''

	# 	url = self.form_url(product, price, location)

