from .umbrellaclient import UmbrellaClient

c = UmbrellaClient(
    '3f4b22b094ce484682fe6869844947a0',
    'f13907f2e071445a9c91693b5325fa91'
)

r = c.destination_lists.add_destination_list_destination('16564849', destination='example.com')

print(r)