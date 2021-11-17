from sqlalchemy.orm import Session
from sqlalchemy import create_engine


def commit_in_function(objects):
    engine = create_engine('sqlite:///invoice.db')
    with Session(engine) as session:
        for model_object in objects:
            session.add(model_object)
        session.commit()


