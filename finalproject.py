from flask import Flask, render_template, request, redirect, jsonify, url_for
# adding asc for names below
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem 

app = Flask(__name__)

engine = create_engine('sqlite:///kidsevents.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all catalog venues
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Categories).order_by(asc(Categories.name))
    # should show all catagories
    return render_template('catalog.html', categories=categories)
    #return "this page will show all my venues"

# create a new category venue
# wking: http://localhost:5000/catalog/new/
@app.route('/catalog/new/', methods=['GET', 'POST'])
def newCategory():
	if request.method == 'POST':
		newCategory = Categories(name=request.form['name'])
		session.add(newCategory)
		flash('New Category %s Succesfully Created' % newCategory.name)
		session.commit()
		return redirect(url_for('showCatalog'))
	else:	
            return render_template('newCategory.html')
    #return "this pg is for making new category"

#edit a catalog venue
#wking: http://localhost:5000/catalog/1/edit
@app.route('/catalog/<int:categories_id>/edit/')
def editCategory(categories_id):
    editedCatalog = session.query(Categories).filter_by(id=categories_id).one()
    if request.method == 'POST':
    	if request.form['name']:
    		editedCatalog.name = request.form['name']
    		#flash('Catalog Venue Succesfully Edited %s' editedCatalog.name)
    		return redirect(url_for('showCatalog'))
    else:		
        return render_template('editCategory.html', categories=editedCatalog)
    #return "pg to edit venue"


# Delete a catalog venue
#http://localhost:5000/catalog/1/delete/
@app.route('/catalog/<int:categories_id>/delete/')
def deleteCategory(categories_id):
    categoryToDelete = session.query(Categories).filter_by(id=categories_id).one()
    if request.method == 'POST':
    	session.delete(categoryToDelete)
    	flash('%s Succesfully Deleted' % categoryToDelete.name)
    	session.commit()
    	return redirect(url_for('showCatalog', categories_id=categories_id))
    else:
        return render_template('deleteCategory.html', categories=categoryToDelete)
    #return 'this pg will be for deleting categories %s' % categories_id     

# Show a catalog venue's item menu
#http://localhost:5000/catalog/1/menu/
#Works if use above link, but can't get to work when click on!
@app.route('/catalog/<int:categories_id>/')
@app.route('/catalog/<int:categories_id>/menu/')
def showCategoryItem(categories_id):
    #allcategories = session.query(Categories).all()
    categories = session.query(Categories).filter_by(id=categories_id).one()
    items = session.query(CategoryItem).filter_by(categories_id=categories_id).all()
    return render_template('menu.html', categories=categories, items=items)
    #return 'this pg is the menu for the venues'

#create a new venue's menu item
#http://localhost:5000/catalog/2/menu/new/
@app.route('/catalog/<int:categories_id>/menu/new/')
def newCategoryItem(categories_id):
    categories = session.query(Categories).filter_by(id=categories_id).one()
    return render_template('newCategoryItem.html', categories_id=categories_id)
    #return 'updated new venues menu item' 


#updated task 2 create route for edit venue menu items
# to check: http://localhost:5000/catalog/1/menu/2/edit/
@app.route('/catalog/<int:categories_id>/menu/<int:item_id>/edit/')
def editCategoryItem(categories_id, item_id):
    editedItem = session.query(CategoryItem).filter_by(id=item_id).one()
   # return render_template('editCategoryItem.html', categories_id=categories_id, 
    #    item_id=item_id, item=editedItem )
    return "page to edit a menu item. task 2 complete!"


#task 3: Delete venue menu item
#http://localhost:5000/catalog/1/menu/2/delete/
@app.route('/catalog/<int:categories_id>/menu/<int:item_id>/delete/')
def deleteCategoryItem(categories_id, item_id):
    itemToDelete = session.query(CategoryItem).filter_by(id=item_id).one()
    #return render_template('deleteCategoryItem.html', item=itemToDelete)
    return "page to delete a menu item. Task 3 complete %s" %item_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
