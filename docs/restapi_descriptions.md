# REST API Descriptions

- &lt;item info> schema:  
{ "name": ..., "price": ..., "website": ... (amazon, etsy, etc), "link": &lt;url>, "rating": ..., "img_link": ... } 

### GET /search
Gets details of items from e-commerce websites specified by the query parameters.
 - query params: 
    - name=&lt;search product string>
    - numProducts=&lt;number of products to get>
    - sortBy=<'Relevance' or 'Price'>
    - displayOrder=<'asc' for ascending or 'desc' for descending>
    - currency=&lt;currency format>
 - expected response: 
   - list of items in _"item info"_ schema (described above)

### POST /login
Logs users into their profile 
 - request body: 
   - { "username": ..., "password": ... }
 - expected response: 
   - { "valid": _boolean_ (for whether or not this is a valid user)}

### POST /signup
Creates a new user profile
 - request body: 
   - { "username": ..., "password": ... }
 - expected response: 
   - { "valid": _boolean_ (for whether or not a user with this username exists) }

### DELETE /deleteuser
Deletes a user profile
 - request body: 
   - { "username": ..., "password": ... }
 - expected response: 
   - { "valid": _boolean_ (for whether or not a user with this username exists) }

### GET /wishlist
Gets the user's wishlist
 - request body: 
   - { "user": &lt;username> }
 - expected response: 
   - list of items on wishlist in &lt;item info> schema

### POST /wishlistAdd
Adds an item to the user's wishlist
 - request body: 
   - { "user": <username>, "item": &lt;item info> }
 - expected response:
   - status code 200 OK

### DELETE /wishlistRemove
Removes an item from the user's wishlist
 - request body: { "user": <username>, "item": &lt;item info> }
 - expected response:
   - status code 200 OK
   
### DELETE /wishlistclear
Clears the user's wishlist
 - request body: { "user": <username> }
 - expected response:
   - status code 200 OK
