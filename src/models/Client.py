from sqlalchemy import Column, Integer, String
from database.Base import Base
class Client(Base):

	__tablename__ = 'clients'

	id = Column(Integer, primary_key=True)
	twitter_handle = Column(String)
	location = Column(String)
	name = Column(String)
	followers_count = Column(Integer)
	twitter_id = Column(String)
	autoincrement = 1
	sqlite_autoincrement = True
	
	def __repr__(self):
		return "<Client(twitter_handle = '%s')>" % (self.twitter_handle)

