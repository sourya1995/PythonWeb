from pymemcache.client import base
from pymemcache import fallback

def do_some_query():
    return 42

old_cache = base.Client(('localhost', 11211), ignore_exc=True)
new_cache = base.Client(('localhost', 11212))

client = fallback.FallbackClient((new_cache, old_cache))

result = client.get('some_key')
if result is None:
    result = do_some_query()
    client.set('some_key', result)
print(result)
