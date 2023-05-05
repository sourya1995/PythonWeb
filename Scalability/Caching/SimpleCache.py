cache = {}
cache['key'] = 'value'
cache = {}

def compute_length_or_read_in_cache(s):
    try:
        return cache[s]
    except KeyError:
        cache[s] = len(s)
        return cache[s]
    
print("Foobar: ", compute_length_or_read_in_cache("foobar"))
print('Cache: ', cache)