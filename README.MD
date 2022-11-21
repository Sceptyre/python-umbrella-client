# Install
`pip install git+https://github.com/Sceptyre/python-umbrella-client.git@main`  

Bleeding Edge:  
`pip install git+https://github.com/Sceptyre/python-umbrella-client.git@devel`

# Usage
```py
from umbrellaclient import UmbrellaClient

c = UmbrellaClient(
    '<API_KEY>',
    '<API_SECRET>'
)
```

```py
# Get all destination lists
c.get_destination_lists()

# Get specific destination list
c.get_destination_list('1234')

# Get list's destinations
c.get_destination_list_destinations('1234')

# Add destination to list
c.add_destination_list_destination('1234', 'example.com')
```