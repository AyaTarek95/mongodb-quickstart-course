import mongoengine

def global_init():
    """call this function to talk to mongodb"""
    mongoengine.register_connection(alias='core', name='snake_bnb')
