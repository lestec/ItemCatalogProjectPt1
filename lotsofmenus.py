from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Categories, CategoryItem 

engine = create_engine('sqlite:///kidsevents.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
#user1 = User(name="test dummy",email='tdummy@gmail.com')
#session.add(user1)
#session.commit()


# Create Location of Events #not sure if ADD user_id=1 ????
category1 = Categories(name="Library")
session.add(category1)
session.commit()

# Create Activites at above location
categoryItem1 = CategoryItem(
    name="Storytime",
    description='Storytimes for varies ages.',
    categories=category1
    #user = user_id=1
    )
session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(
    name="Playtime",
    description='An hour playtime for ages 3-6.',
    categories=category1
    #user = user_id=1
	)
session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(
    name="STEM Programs",
    description='Programs focused on Math, Science, Engineering, and Math',
    categories=category1
    #user = user_id=1    
    )
session.add(categoryItem3)
session.commit()

category2 = Categories(name="Recreation Center")
session.add(category2)
session.commit()

categoryItem1 = CategoryItem(
    name="Events",
    description='Events for kids.',
    categories=category2
    #user user_id=1
	)
session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(
    name="Classes",
    description='Classes for kids',
    categories=category2
    #user user_id=1
	)
session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(
    name="Camps",
    description='Day camps for school breaks',
    categories=category2
    #user user_id=1
	)
session.add(categoryItem3)
session.commit()


category3 = Categories(name="Children's Amusement Centers")
session.add(category3)
session.commit()

categoryItem1 = CategoryItem(
    name="Kangamoo",
    description='Indoor playland and events.',
    categories=category3
    #user user_id=1
	)
session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(
    name="Lost World Myth and Magic",
    description='Indoor playland and arcade.',
    categories=category3
    #user user_id=1
	)
session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(
    name="Bouncy World Indoor Bounce Playland",
    description='Indoor bouncy playland',
    categories=category3
    #user user_id=1
	)
session.add(categoryItem3)
session.commit()


print "added Location and Events!"