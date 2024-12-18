import random
import time
import sqlite3
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker, Session

from user import User
from constants import users

from base import Base


def create_db():
    conn = sqlite3.connect('data.db')

    create_users_table = '''
        CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        family BOOLEAN NOT NULL,
        login BOOLEAN NOT NULL,
        chosen BOOLEAN NOT NULL,
        gifting VARCHAR(50) NOT NULL
    );
    '''

    conn.execute(create_users_table)
    conn.commit()
    conn.close()


def delete_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    DROP_TABLE = 'DROP TABLE IF EXISTS user;'

    c.execute(DROP_TABLE)
    conn.commit()
    conn.close()


def connect_db(logger):
    SQLITE_CONNECTED = False

    while not SQLITE_CONNECTED:
        try:
            DB_ENGINE = create_engine(f"sqlite:///data.db")
            Base.metadata.bind = DB_ENGINE
            DB_SESSION = sessionmaker(bind=DB_ENGINE)

            logger.info("Successfully connected to SQLite")
            SQLITE_CONNECTED = True
        except Exception as sqlite_error:
            logger.error(sqlite_error)
            logger.error(
                "Failed to connect to SQLite database, retrying in 5 seconds")
            time.sleep(5)
    
    return DB_SESSION


def set_default(DB_SESSION):
    session: Session = DB_SESSION()

    for user in users:
        entry = User(user["name"], user["family"], user["login"], user["chosen"], user["gifting"])
        session.add(entry)
    
    session.commit()
    session.close()


def check_user(DB_SESSION, username):
    session: Session  = DB_SESSION()

    user = session.query(User).filter(User.name == username).first()

    if user is None:
        session.close()
        return "invalid"
    
    if user.login:
        session.close()
        return "completed"
    
    user.login = True
    session.commit()
    session.close()
    return "valid"


def check_family(DB_SESSION, username):
    session: Session = DB_SESSION()

    result = session.query(User).filter(User.name == username).first()
    return result.family


def get_random_name(DB_SESSION, username):
    session: Session = DB_SESSION()

    family = check_family(DB_SESSION, username)
    options = []

    if family:
        result = session.query(User).filter(and_(User.name != username, User.chosen == False)).all()
    else:
        result = session.query(User).filter(and_(User.name != username, User.chosen == False, User.family == True)).all()

    for user in result:
        options.append(user.name)
    
    random_name = random.choice(options)

    random_user = session.query(User).filter(User.name == random_name).first()
    random_user.chosen = True

    gifter = session.query(User).filter(User.name == username).first()
    gifter.gifting = random_name
    
    session.commit()
    session.close()
    return random_name


def get_chosen(DB_SESSION, username):
    session: Session = DB_SESSION()

    user = session.query(User).filter(User.name == username).first()
    session.close()
    return user.gifting