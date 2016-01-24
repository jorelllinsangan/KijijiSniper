from sqlalchemy import Column, Integer, String, ForeignKey
from database.Base import Base
from sqlalchemy.orm import relationship
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

	kijiji_watcher = relationship("KijijiWatcher", uselist =False, back_populates="client")

	def __repr__(self):
		return "<Client(twitter_handle = '%s')>" % (self.twitter_handle)


	def get_watcher():
		return self.watcher
