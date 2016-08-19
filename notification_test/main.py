import pyext

def main():
    try:
        pyext.create_simple_notification("hello")
        print "hello world"
    except Exception, e:
        print "Something went wrong", e
