
import redis

import gevent

from gevent import Timeout
from gevent.pool import Pool

import time


r = redis.Redis(host='localhost', port=6379, db=1)

class TimeoutException(Exception):
    pass

def start(name):
    """start time"""
    t =  time.time()
    r.set("%s.start" % (name), t)    
    

def heartbeat(name):
    """heartbeat to redis"""
    t =  time.time()
    r.set(name, t) 
    print ( "%s:%s" % (name, t) )

def f1():
    
    """function and heartbeat"""
    
    ex = TimeoutException("timeout ex")
    
    timeout = Timeout(5, ex)
    timeout.start()
    try:
        """
        exception will be raised here, after *seconds* 
        passed since start() call
        """
        gevent.sleep(11)
        #print "f1 heart beat"
        heartbeat("f1")

    except TimeoutException as ex:
        print ex
    finally:
        timeout.cancel()


def main():

    """spawn"""

     
     
    v = r.get('f1')   

    print(v)
    
    pool = Pool(20)
    
    start('f1')

    while True:
        
        #print( time.time() )
        
        pool.spawn(f1)
        #print pool.wait_available()
        print ( pool.free_count() )
        
        #
        gevent.sleep(2)    
        
        

if __name__ == "__main__":
    
    main()