from models import Dog

def create_table(base):
     __tablename__ = 'dogs'

     id = Column(Integer(), primary_key=True)
     name = Column(String())
     breed = Column(String())
    
def save(session, dog):
    pass

def get_all(session):
    dogs = session.query(Dog).all()

def find_by_name(session, name):
    dog_by_name = [dog for dog in session.query(Dog.name)]

def find_by_id(session, id):
     query = session.query(Dog).filter(Dog.id.like(1))

def find_by_name_and_breed(session, name, breed):
    pass

def update_breed(session, dog, breed):
    for dog in session.query(Dog):
        dog.breed += "bulldog"