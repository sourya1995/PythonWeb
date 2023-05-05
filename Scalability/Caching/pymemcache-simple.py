from pymemcache.client import base

client = base.Client(('localhost', 11211))
client.set('some_key', 'some_value')
result = client.get('some_key')
print(result)