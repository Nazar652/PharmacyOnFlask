from peewee import *

db = SqliteDatabase('db.sqlite')


class Drug(Model):
    title = CharField()
    description = TextField()
    price = IntegerField()
    photo = CharField()

    @classmethod
    def get_drug(cls, ident: int):
        try:
            return cls.get(id=ident)
        except DoesNotExist:
            return None

    class Meta:
        database = db
