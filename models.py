from sqlalchemy import Column, Integer, String, DateTime, Float, Text, Date
from database import Base, db_session2


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    description = Column(String(120), unique=False)

    def __init__(self, name=None, email=None, description=None):
        self.name = name
        self.email = email
        self.description = description

    def __repr__(self):
        return '<User %r>' % (self.name)


class TbTest(Base):
    __tablename__ = 'tbTable'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    string = Column(String(250))

    def __init__(self, datetime, string):
        self.datetime = datetime
        self.string = string

    def __repr__(self):
        return "<TbTest('%d', '%s', '%s'>" % (self.id, str(self.datetime), self.string)


class api_key(Base):
    __tablename__ = 'api_key'
    seq = Column(Integer, primary_key=True)
    auth_key = Column(String(64), unique=True)
    type = Column(Integer, nullable=False)
    ip = Column(Integer, nullable=False)
    user_info = Column(String(255))
    create_dt = Column(DateTime)

    def ip4(self):
        import ipaddress
        return str(ipaddress.IPv4Address(self.ip))

    def __init__(self, seq=None, auth_key=None, type=0, ip=0, user_info=None):
        self.seq = seq
        self.auth_key = auth_key
        self.type = type
        self.ip = ip
        self.user_info = user_info

    def __repr__(self):
        return "<api_key('%s', '%s', '%s'>" % (str(self.seq), self.auth_key, self.user_info)


#cfs2
class t_fund_items(Base):
    __tablename__ = 't_fund_items'

    fundsID = Column(String(10), unique=True, primary_key=True)
    applicationID = Column(Integer)
    type = Column(String(1))
    title = Column(String(45))
    rateOfReturn = Column(Float)
    loanPeriod = Column(Integer)
    targetAmount = Column(Integer)
    unitAmount = Column(Integer)
    startDate = Column(DateTime)
    finishDate = Column(DateTime)
    status = Column(String(1))
    contractNo = Column(String(8))
    loanStartDate = Column(Date)
    loanFinishDate = Column(Date)
    expectedLoanFinishDate = Column(Date)
    isCeiling = Column(String(1))
    ceilingRate = Column(Integer)
    isAutoInvest = Column(String(1))
    autoInvestRate = Column(Integer)
    ltv = Column(Integer)
    mainBanner = Column(String(100))
    mainBannerOrder = Column(String(1))
    createDate = Column(DateTime)
    lastDate = Column(DateTime)

    def __repr__(self):
        return "<t_fund_items('%s', '%s', '%s'>" % (self.fundsID, self.title, str(self.targetAmount))
