from db import sqlalchemydatabaseinstancev #to get sqlalchemy database instance from db.py file

class ItemModel(sqlalchemydatabaseinstancev.Model):
    __tablenames__ = "itemstable" #tells sqlalchemy that we want to ues a table called items for this class and all of this classe's objects

    #define columns that should be a part of this items table above - Integer indicates the type values that the column accepts
    #by default, when we use postgres, it will be autoincremented, so everytime we create a new item and save into db, the id column will be prepopulated by db and be given next available number starting from 1
    identifiercolumnv = sqlalchemydatabaseinstancev.Column(sqlalchemydatabaseinstancev.Integer, primary_key=True)
    namecolumnv = sqlalchemydatabaseinstancev.String(sqlalchemydatabaseinstancev.String(100), unique=True, nullable=False) #nullable False means that you cannot create an item that does not have a name
    pricecolumnv = sqlalchemydatabaseinstancev.Column(sqlalchemydatabaseinstancev.Float(precision=4), unique=False, nullable=False)
    #storeidcolumnv is a link between items table and the stores table. The value stored in this column needs to match value of id in the stores table we will define now 
    storeidcolumnv = sqlalchemydatabaseinstancev.Column(sqlalchemydatabaseinstancev.Integer, unique=True, nullable=False)
