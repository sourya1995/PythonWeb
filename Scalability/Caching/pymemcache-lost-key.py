from pymemcache.client import base

def do_some_query():
    return 42

client = base.Client(('localhost', 11211))
result = client.get('some_key')
if result is None:
    result = do_some_query()
    client.set('some_key', result)
print(result)