#!/usr/bin/env python3
"""
    Usage: python3 sqlalchemy_metadata.py -d/--dir directory_name
"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from optparse import OptionParser

def createAndWalkMetadataDB(directory = "."):
    # Part 1: Create engine
    engine = create_engine("sqlite:///:memory:")

    # Part 2: Define Table and Mapped class
    Base = declarative_base()

    class FileSystem(Base):
        __tablename__ = 'Filesystem'  # The table name

        id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
        path = Column(String(500)) 
        file = Column(String(255))  # Optional column

        def __repr__(self):
            return "[Filesystem('%s','%s','%s)]" % (self.id, self.path, self.file)
        
    # Part 3: 
    Base.metadata.create_all(engine)

    # Part 5: Create a session
    Session = sessionmaker(bind=engine, autoflush=True)
    session = Session()

    # Part 6: Crawl and populate the DB with results
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            fullpath = os.path.join(directory, dirpath, filename)
            session.add(FileSystem(path = fullpath, file = filename))
    
    # Part 7: Commit the transaction
    session.commit()

    # Part 8: Query
    for record in session.query(FileSystem).all():
        print(record)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="directory", help="Walk FILE path", metavar="FILE")
    (options, args) = parser.parse_args()
    if not options.directory:
        print(__doc__)
        exit(1)
    if not (os.path.exists(options.directory) and os.path.isdir(options.directory)):
        print(__doc__)
        exit(1)
    createAndWalkMetadataDB(options.directory)