from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('connectionstring',
                       echo=True, encoding='utf-8', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

engine2 = create_engine('connectionstring2',
                        echo=True, encoding='utf-8', convert_unicode=True)
db_session2 = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False, bind=engine2))

Base = declarative_base()
Base.query = db_session.query_property()
Base.query2 = db_session2.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    #import models
    #Base.metadata.create_all(bind=engine) #모델로 정의된 테이블을 생성하고싶다면
    pass

'''
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
'''