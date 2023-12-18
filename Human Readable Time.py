def make_readable(seconds):
    s = 0
    m = 0
    h = 0

    for i in range(seconds):
        s += 1
        if s >= 60:
           m += 1
           s = 0
        if m >= 60:
           h += 1
           m = 0
    
    return str("{0:0=2d}".format(h)) + ":" + str("{0:0=2d}".format(m)) + ":" + str("{0:0=2d}".format(s))