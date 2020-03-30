# Item Catalog with REST API using flask and shelve

## Setup

Run the following commands to install and run

```pip install -r requirements.txt```

```python run.py```

## Usage

All responses will have the form

```json
{
    "message": "Results of REST operation",
	"data": "Mixed data type"
    
}
```

Response definitions for data field on successful operations

### List all items

**Definition**

`GET /items`

**Response**

- `200 OK` on success

```json
[
        {
            "identifier": "matrix",
            "name": "The Matrix",
            "item_type": "movie",
            "item_genre": "science_fiction"
        },
        {
            "identifier": "halo",
            "name": "Halo",
            "item_type": "game",
            "item_genre": "first_person_shooter"
        }
]
```

### Registering a new item

**Definition**

`POST /items`

**Arguments**

- `"identifier":string` a globally unique identifier for this item
- `"name":string` a friendly name for this item
- `"item_type":string` the type of the item as understood by the client
- `"item_genre":string` the genre of the item

If an item with the given identifier already exists, the existing item will be overwritten.

**Response**

- `201 Created` on success

```json
{
	"identifier": "matrix",
	"name": "The Matrix",
	"item_type": "movie",
	"item_genre": "science_fiction"
}
```

## Lookup item details

`GET /items/<identifier>`

**Response**

- `404 Not Found` if the item does not exist
- `200 OK` on success

```json
{
	"identifier": "matrix",
	"name": "The Matrix",
	"item_type": "movie",
	"item_genre": "science_fiction"
}
```

## Delete a item

**Definition**

`DELETE /items/<identifier>`

**Response**

- `404 Not Found` if the item does not exist
- `204 No Content` on success
