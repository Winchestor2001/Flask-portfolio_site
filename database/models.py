from peewee import *

db = SqliteDatabase(database='portfolio.db')


class BaseModel(Model):
    class Meta:
        database = db


class About(BaseModel):
    id = AutoField(primary_key=True)
    description = TextField()

    class Meta:
        db_name = 'about'


# class Project(BaseModel):
#     id = AutoField(primary_key=True)

#     class Meta:
#         db_name = 'project'