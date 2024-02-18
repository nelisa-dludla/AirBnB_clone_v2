#!/usr/bin/python3
""" This modules handles Database Storage """
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    ''' database engine '''
    __engine = None
    __session = None

    def __init__(self):
        ''' Create engine '''
        from models.base_model import Base

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ''' query on the current database session '''
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        from models.amenity import Amenity

        classes = {
            "City": City,
            "State": State,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }
        dic = {}
        lista = []

        if cls:
            if type(cls) is str:
                cls = eval(cls)
            lista = self.__session.query(cls)
            for obj in lista:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                dic[key] = obj
            return dic
        else:
            for name, value in classes.items():
                lista = self.__session.query(value)
                for obj in lista:
                    key = '{}.{}'.format(name, obj.id)
                    dic[key] = obj
            return dic

    def new(self, obj):
        '''add the object to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delet from the current database session obj if not None'''
        self.__session.delete(obj)

    def reload(self):
        ''' create all tables in the database '''
        from models.base_model import Base
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Because SQLAlchemy doesn't reload his `Session`
        when it's time to insert new data, we force it to!
        """
        self.__session.close()
