

### we have a shop item website and we can view items form this endpoint

![Screenshot_213](https://github.com/kiro6/writeups/assets/57776872/bca2fb60-9e9f-4c5a-9c83-6585edebc3a3)


### if found the function for retriving the data and it's vuln to sql injection

- **models.py**
```python
from application.database import query_db

class shop(object):

    @staticmethod
    def select_by_id(product_id):
        return query_db(f"SELECT data FROM products WHERE id='{product_id}'", one=True)
```

### i found that the app store the data as serialzed objects in the database

```python
class Item:
	def __init__(self, name, description, price, image):
		self.name = name
		self.description = description
		self.image = image
		self.price = price

def migrate_db():
    items = [
        Item('Pickle Shirt', 'Get our new pickle shirt!', '23', '/static/images/pickle_shirt.jpg'),
        Item('Pickle Shirt 2', 'Get our (second) new pickle shirt!', '27', '/static/images/pickle_shirt2.jpg'),
        Item('Dill Pickle Jar', 'Literally just a pickle', '1337', '/static/images/pickle.jpg'),
        Item('Branston Pickle', 'Does this even fit on our store?!?!', '7.30', '/static/images/branston_pickle.jpg')
    ]
    
    with open('schema.sql', mode='r') as f:
        shop = map(lambda x: base64.b64encode(pickle.dumps(x)).decode(), items)
        get_db().cursor().executescript(f.read().format(*list(shop)))
```

### and here we have the desrilzation function

- **app.py**
```python

@app.template_filter('pickle')
def pickle_loads(s):
	return pickle.loads(base64.b64decode(s))

```

- **item.html**
```html
   {% set item = product | pickle %}
                    <div class="col-md-6"><img class="card-img-top mb-5 mb-md-0" src="{{ item.image }}" alt="..." /></div>
                    <div class="col-md-6">
                        <h1 class="display-5 fw-bolder">{{ item.name }}</h1>
                        <div class="fs-5 mb-5">
                            <span>£{{ item.price }}</span>
                        </div>
                        <p class="lead">{{ item.description }}</p>
```

## steps
1) sql injection
2) insecure desrilzation
3) get the flag
4) i have wrote automation script for the challenge
