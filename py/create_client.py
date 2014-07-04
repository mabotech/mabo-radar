


a = None

b = 2

print a or b

prefix = 'h'

def get_key(key):
    
    return ":".join([prefix, key])
    
if __name__ == "__main__":
    print get_key("abc")