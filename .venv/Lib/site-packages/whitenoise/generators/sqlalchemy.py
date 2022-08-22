import random
from whitenoise.generators import BaseGenerator

class SelectGenerator(BaseGenerator):
    '''
    Creates a value by selecting from another SQLAlchemy table
    Depends on SQLAlchemy, and receiving a session object from the Fixture runner
    the SQLAlchemy fixture runner handles this for us
    Receives the name of another class to lookup. If the
    query returns more than one option, either random or the 1st is selected
    (default is random)
    '''
    def __init__(self, model, random=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = None
        self.model = model
        self.random = random

    def generate(self):
        if(self.session is None):
            raise ValueError('You must set the session property before using this generator')
        _query = self.session.query(self.model).all()
        if self.random:
            return random.SystemRandom().choice(_query)
        else:
            return _query[0]
