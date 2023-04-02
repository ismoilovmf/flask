import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, func

from exceptions import ApiException

load_dotenv()

PG_DNS = f'postgresql://{os.environ.get("PG_USER")}:' \
         f'{os.environ.get("PG_PASS")}@{os.environ.get("PG_HOST")}:' \
         f'{os.environ.get("PG_PORT")}/{os.environ.get("PG_DB")}'


engine = create_engine(PG_DNS)
Session = sessionmaker(bind=engine)

Base = declarative_base(bind=engine)


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(length=30), nullable=False)
    password = Column(String, nullable=False)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.email, self.password)


class Adv(Base):

    __tablename__ = "advertisements"

    id = Column(Integer, primary_key=True)
    title = Column(String(length=50), nullable=False, index=True, unique=True)
    description = Column(String, nullable=False)
    created = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))


Base.metadata.drop_all()
Base.metadata.create_all()


def get_user(user_id: int, session: Session):
    user = session.get(User, user_id)
    if user is None:
        raise ApiException(404, 'user not found')
    return user


def get_adv(adv_id: int, session: Session):
    adv = session.get(Adv, adv_id)
    if adv is None:
        raise ApiException(404, 'advertisement not found')
    return adv