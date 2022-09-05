# (k-m)^2 + ... + k^2 = (n+1)^2 + ... + (n+m)^2 for some n >= k
# (k)(k+1)(2k+1) - (k-m)(k-m-1)(2k-2m-1) = (n+m)(n+m+1)(2n+2m+1) - n(n+1)(2n+1)
# 6k^2m + 6k^2 - 6km^2 - 6km = 6m^2n + 6mn^2 + 6mn
# (m+1)(6k^2) - (m+1)(6km) = 6mn(m+n+1)
# (m+1)(k^2-km) = mn(m+n+1)
# k(m+1)(k-m) = mn(m+n+1)
# [m]n^2 + [m(m+1)]n - [k(m+1)(k-m)]1 = 0
# n = -[m(m+1)] + sqrt([m(m+1)]^2 + 4m[k(m+1)(k-m)]) / 2m
# need sqrt([m(m+1)]^2 + 4m[k(m+1)(k-m)]) as m(2x + ((m+1) % 2)) for some nonneg integer x
# therefore k(m+1)(k-m) is a multiple of m, which requires k to be a multiple of m
# let k = lm
# then we obtain sqrt([m(m+1)]^2 + 4m(lm(m+1)(l-1)m)) = m*sqrt([m+1]^2 + 4lm(l-1)(m+1)) which is guaranteed to be same parity as m+1 if integer
# therefore we need only that [m+1]^2 + 4lm(l-1)(m+1) is square
# specifically it will equal (2n + m+1)^2