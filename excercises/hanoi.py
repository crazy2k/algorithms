# Move disk ``n`` and smaller from peg ``pfrom`` to peg ``pto`` using
# ``pvia`` as spare peg
def move(n, pfrom, pvia, pto):
    if n == 1:
        print "Move %d from %s to %s" % (n, pfrom, pto)
    else:
        move(n - 1, pfrom, pto, pvia)
        print "Move %d from %s to %s" % (n, pfrom, pto)
        move(n - 1, pvia, pfrom, pto)

move(5, "A", "B", "C")
