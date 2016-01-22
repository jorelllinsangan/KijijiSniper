from sqlalchemy import Column, Integer, String, Float
from database.Base import Base
class Product(Base):

	__tablename__ = 'products'

	id = Column(Integer, primary_key = True)
	name = Column(String)
	postal_code = Column(String)
	price = Column(Float)
	autoincrement = 1
	sqlite_autoincrement = True

	def __repr__(self):
		return "<Client(name = '%s', price = '%f', postal_code = '%s')>" % (self.name, self.price, self.postal_code)






	

	 

