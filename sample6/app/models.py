import mongoengine as me

me.connect("sample6")


class Car(me.Document):
    model = me.StringField()
    engine = me.StringField()


class User(me.Document):
    login = me.StringField(unique=True, required=True)
    password = me.StringField(required=True, min_length=6)
    interests = me.ListField(me.StringField())
    car = me.ReferenceField(Car)


if __name__ == "__main__":
    car = Car(model='Audi', engine='3T').save()
    User(login='qwerty123', password='passwd1212121', interests=['Sport', 'Books'], car=car).save()
