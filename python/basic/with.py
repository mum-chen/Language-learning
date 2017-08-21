

class WithWhat(object):
    def __init__(self, *args, **kw):
        print("======= start =======")
        print "init:", args, kw

    def __enter__(self):
        print "enter"
        return self

    def __exit__(self, *args):
        print "exit", args
        print("======= end =========")


    def what(self):
        print "what"

with WithWhat(1, 3, "aa", timeout=10) as what:
    what.what()

class WithWhatWhat(WithWhat):
    def what(self):
        super(WithWhatWhat, self).what()
        super(WithWhatWhat, self).what()

with WithWhatWhat() as what:
    what.what()

class WithoutWhat(WithWhat):
    def __enter__(self):
        instance = super(WithoutWhat, self).__enter__()
        def what():
            print("without what")

        instance.what = what
        return instance

with WithoutWhat() as what:
    what.what()

print("--------------------------------------------")
def setting_inner_with(b):
    res = "empty"
    with WithoutWhat() as what:
        if b:
            res = "b is true"
        else:
            res = "b is false"

    return res

print("setting_inner_with", setting_inner_with(True))

def return_inner_with(b):
    with WithWhat() as what:
        if b:
            return True

    return False

print("return_inner_with", return_inner_with(True))
print("return_inner_with", return_inner_with(False))
