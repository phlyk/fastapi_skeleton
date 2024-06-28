# FastAPI skeleton with in-memory DB
In the [reference_endpoints file](app/reference_endpoints.py) you will find 2 GET endpoints and 1 POST endpoint for an Item entity.

Each endpoint shows a few key things you'll need for the challenge:
- `GET "/"` shows the top-level routing and dictionary response
- `GET "/items/{item_id}` shows parameter extraction from a path and an optional HTTP query_string
- `POST "items"` shows how to passing a model as HTTP Request Body to create a new entity and "saving it to the DB" (adding it to the list). 
  - It also shows use of the `IDGenerator` class to create auto-incrementing PKs for a desired model.
