def clamp(x, a, b):
    """ Forces `x` to be between `a` and `b` """
    assert a <= b
    if x < a:
        return a
    if x > b:
        return b
    return x


def interpolate_01(a, b, per):
    """ Returns the point that is `per` between `a` and `b` """
    if a > b:
        (a, b) = (b, a)
    per = clamp(per, 0, 1)
    return a + (b - a) * per


def interpolate_pm1(a, b, p):
    if a > b:
        (a, b) = (b, a)
    p = clamp(p, -1, +1)
    return a + (b - a) * (.5 + p/2)
