from sqlalchemy import Column, Integer, String, DateTime, Float, Date, UniqueConstraint, PrimaryKeyConstraint

from app.database import Base

from app import db as tdb

from app.utils import isfloat



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

#cfs2
class c_code(Base):
    __tablename__ = 'c_code'
    __table_args__ = (
        UniqueConstraint('cd', 'cd_val', name='code_UNIQUE'),
        PrimaryKeyConstraint('cd', 'cd_val')
    )

    cd = Column(String(10))
    cd_val = Column(String(10))
    cd_name = Column(String(45))
    append_1 = Column(String(100))
    append_2 = Column(String(100))
    append_3 = Column(String(100))
    UseYN = Column(String(1))
    CreateDate = Column(DateTime)
    LastDate = Column(DateTime)

    def __init__(self, cd=None, cd_val=None, cd_name=None, append_1=None, append_2=None, append_3=None, UseYN=None):
        self.cd = cd
        self.cd_val = cd_val
        self.cd_name = cd_name
        self.append_1 = append_1
        self.append_2 = append_2
        self.append_3 = append_3
        self.UseYN = UseYN

    def __repr__(self):
        return "<c_code('%s', '%s', '%s', '%s'>" % (self.cd, self.cd_val, self.cd_name, self.UseYN)


class Loan(tdb.Document):
    from datetime import datetime
    loanId = tdb.StringField(required=False)
    userNo = tdb.IntField(required=False)
    cellPhone = tdb.StringField(required=False)
    password = tdb.StringField(required=False)
    type = tdb.StringField(required=False)
    address1 = tdb.StringField(required=False)
    address2 = tdb.StringField(required=False)
    zipCode = tdb.StringField(required=False)
    numberHouseholds = tdb.StringField(required=False)
    schedule = tdb.StringField(required=False)
    progressRate = tdb.IntField(required=False)
    supplyArea = tdb.FloatField(required=False)
    owner = tdb.StringField(required=False)
    guest = tdb.StringField(required=False)
    sellType = tdb.StringField(required=False)
    sellAmount = tdb.FloatField(required=False)
    bank = tdb.StringField(required=False)
    bankingAmount = tdb.FloatField(required=False)
    bankingStatus = tdb.StringField(required=False)
    job = tdb.StringField(required=False)
    proofIncome = tdb.FloatField(required=False)
    unProofIncome = tdb.FloatField(required=False)
    totalIncome = tdb.FloatField(required=False)
    exclusiveArea = tdb.FloatField(required=False)
    expectedSlaes = tdb.FloatField(required=False)
    businessExpenses = tdb.FloatField(required=False)
    profixsBusiness = tdb.FloatField(required=False)
    ownAmount = tdb.FloatField(required=False)
    loanAmount = tdb.FloatField(required=False)
    channel = tdb.StringField(required=False)
    comment = tdb.StringField(required=False)

    createDate = tdb.DateTimeField(default=datetime.now())
    updateDate = tdb.DateTimeField(default=datetime.now())

    def __repr__(self):
        return "<Loan('%s', '%s'>" % (self.userNo, self.cellPhone)

    def __init__(self, *args, **kwargs):
        import uuid
        super(Loan, self).__init__(*args, **kwargs)
        self.loanId = str(uuid.uuid4()).replace('-', '')
        if kwargs.get('userNo') is None:
            self.cellPhone = kwargs['cellPhone']
            self.password = kwargs['password']
        else:
            self.userNo = kwargs['userNo']


    def __getitem__(self, key):
        return getattr(self, key)

    def fromdict(self, v):
        for key, value in v.items():
            if value.isdigit() is True:
                setattr(self, key, int(value))
            elif isfloat(value=value) is True:
                setattr(self, key, float(value))
            else:
                setattr(self, key, value)
        return self