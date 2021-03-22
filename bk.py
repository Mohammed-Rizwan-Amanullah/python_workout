def skewness(x):
    res = 0
    m = x.mean ()
    s = x.std()
    for i in x:
        res += (i-m) * (i-m) * (i-m)
        res /= (len(x) * s * s * s)
        return res

print "Skewness of the male population = ", skewness(ml2_age)
print "Skewness of the female population is = ", skewness(fm2_age)
