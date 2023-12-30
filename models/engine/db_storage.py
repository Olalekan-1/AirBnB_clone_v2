#!/usr/bin/python3

""" creates the database management system
"""

import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
from models.base_model import Base


db_user = os.environ.get("HBNB_MYSQL_USER")
db_password = os.environ.get("HBNB_MYSQL_PWD")
db_host = os.environ.get("HBNB_MYSQL_HOST")
db_name = os.environ.get("HBNB_MYSQL_DB")
# env = os.environ.get("HBNB_ENV")
test_env = os.getenv("HBNB_ENV") == 'test'
port = 3306


# classes_to_query = dict(User=User, State=State, City=City,
# Amenity=Amenity, Place=Place, Review=Review)

class DBStorage:
    """ The data base class to handle the management
    of the dabase operations
    """

    __engine = None
    __session = None

    def __init__(self):

        """ An instance of db Storage created
        """

        self.__engine = self.create_engine()

    def create_engine(self):
        """
            creates the engine for the database
        """

        engine = create_engine(
                "mysql+mysqldb://{}:{}@{}:{}/{}".format(
                    db_user, db_password, db_host, port, db_name,
                    pool_pre_ping=True))
        if test_env:
            db = engine.cursor()
            session = scoped_session(
                    sessionmaker(bind=engine)
                    )()
            metadata = MetaData(bind=engine)
            metadata.reflect()
            for table_name in metadata.tables.keys():
                session.execute(
                        'DROP TABLE IF EXISTS {} CASCADE;'.format(table_name))
            session.commit()
            session.close()

        return engine

    def all(self, cls=None):
        """
        Query on the current database session all objects
        depending on the class name.

        Args:
            cls: Class type to filter the query (default is None).

        Returns:
            A dictionary where key is '<class-name>.<object-id>'
            and value is the object.
        """
        # If cls is None, query all types of objects
        result_dict = {}

        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                result_dict[key] = elem
        else:
            classes_to_query = [State, City, User, Place, Review, Amenity]
            for clase in classes_to_query:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    result_dict[key] = elem
        return result_dict

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        reset configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
