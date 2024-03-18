from . import db


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. Chose to chnange table name despite having been told it was unnecessary.
    __tablename__ = "properties" 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    bedNum = db.Column(db.Integer)
    bathNum = db.Column(db.Integer)
    location= db.Column(db.String(100))
    price = db.Column(db.String(15))
    type= db.Column(db.String(40))
    description = db.Column(db.String(400))
    photo = db.Column(db.String(100))

    def __init__(self,title,bedNum, bathNum, location, price, type, description, photo):
        self.title = title
        self.bedNum = bedNum
        self.bathNum = bathNum
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo
    
        

    # def is_authenticated(self):
    #     return True

    # def is_active(self):
    #     return True

    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     try:
    #         return unicode(self.id)  # python 2 support
    #     except NameError:
    #         return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)