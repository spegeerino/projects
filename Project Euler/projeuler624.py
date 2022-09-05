# P(n) = 1/2 * sum_{k=1}^\infty f_(kn-1) / 2^(kn-1)
# find the recurrence relation:
# f_{nk-1}
# f_{2n} / f_n = f_n + f_{n-2}
# f_{2n} = f_n^2 + f_nf_{n-2}
# A = [f_{k+1}    f_k  ]
#     [  f_k    f_{k-1}]
# A^2 = [f_{2k+1}    f_2k  ]
#       [  f_2k    f_{2k-1}]
# f_2k = f_{k+1}f_k + f_kf_{k-1} = f_k(f_{k+1} + f_{k-1})
# f_2k+1 = f_{k+1}(f_{k+2} + f_k) - f_k(f_{k+1} + f_{k-1}) = f_{k+1}f_{k+2} - f_kf_{k-1}
# f_2k+1 = f_{k+1}(f_{k+1} + f_{k-1}) + [f_{k+1}f_{k-2} - f_kf_{k-1}] (* f_1)
# claim: [f_{k+1}f_{k-2} - f_kf_{k-1}] = (-1)^(k+1)
# proof by induction: base case of k = 1
# f_2(f_(-1)) - f_1f_0 = 1 - 0 = 1 = (-1)^2 true 
# inductive step
# [f_{k+1}f_{k-2} - f_kf_{k-1}] = (-1)^(k+1)
# [f_{k+2}f_{k-1} - f_kf_{k+1}] = [f_{k+1}f_{k-1} + f_kf_{k-1} - f_{k-1}f_{k+1} - f_{k-2}f_{k+1}] = -[f_{k+1}f_{k-2} - f_kf_{k-1}] = (-1)^(k+2)
# done, cool 
# so we get f_n = (f_{k+1} + f_{k-1})f_{n-k} + (-1)^{k+1}f_{n-2k}
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# now we have to create gen_func based on this, and eval at (1/2)^k 
# F_k(x) = p_k(x) / q_k(x), q_k(x) = 1 - (f_{k+1} + f_{k-1})x - (-1)^{k+1}x^2, ex. q_3(x) = 1 - 4x - x^2
# F_k(x) = sum_{i=1}^\infty f_{ik-1}x^i = (f_{k-1})x + (f_{2k-1})x^2 + sum_{i=3}^\infty f_{ik-1}x^i
# F_k(x) = f_{k-1}x + f_{2k-1}x^2 + (-1)^{k+1}x^2F(x) + (f_{k+1} + f_{k-1})x[F(x) - f_{k-1}x]
# F_k(x)q_k(x) = f_{k-1}x + [f_{2k-1} - f_{k+1}f_{k-1} - f_{k-1}^2]x^2 = p_k(x)
# F_2(1/4) = p_2(1/4) / q_2(1/4) = (1/4 - 1/16) / (1 - 3/4 + 1/16) = 3/5 YEEEEEEEEEEEEEEEEEEEEEEEEEES
# F_3
# now that we have this all we have to do is to find p(x) and q(x) * 2^{2k} to find the numer and denom
# then just modular inverse and we're done
import functions as f
mod = 1000000009
num = 10 ** 18
fn = f.fast_fib(num, mod)
f2n = f.fast_fib(num*2, mod)
numer = pow(2, num, mod) * (fn[0] - fn[1]) + ((f2n[0] - f2n[1]) - (fn[0] * (fn[0]-fn[1])) - (fn[0]-fn[1])**2)
denom = pow(2, 2*num, mod) - (2 * fn[0] - fn[1]) * pow(2,num,mod) + pow(-1, num, mod)
numer %= mod
denom %= mod
d = f.gcd2(numer,denom)
numer //= d
denom //= d
inv_denom = f.mod_inverse(denom, mod)
inv_denom *= numer
inv_denom %= mod 
print(f"{inv_denom * denom % mod} = {numer}")
print(inv_denom)

