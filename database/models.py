from peewee import *

db = SqliteDatabase(database='portfolio.db')


class BaseModel(Model):
    class Meta:
        database = db


class About(BaseModel):
    id = AutoField(primary_key=True)
    fullname = CharField(max_length=200)
    profession = CharField(max_length=100)
    dv_file = TextField()
    description = TextField()

    class Meta:
        db_name = 'about'


# class Project(BaseModel):
#     id = AutoField(primary_key=True)

#     class Meta:
#         db_name = 'project'