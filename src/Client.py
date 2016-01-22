from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from Base import Base
class Client(Base):

	__tablename__ = 'clients'

	id = Column(Integer, primary_key=True)
	twitter_handle = Column(String)
	autoincrement = 1
	sqlite_autoincrement = True
	def __repr__(self):
		return "<Client(id = %d, twitter_handle = '%s')>" % (self.id,self.twitter_handle)

	def get_base(self):
		return Base.get_base()
		
print Client.__table__