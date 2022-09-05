# Consider the alphabet A made out of the letters of the word "project": A={c,e,j,o,p,r,t}.
# Let T(n) be the number of strings of length n consisting of letters from A that do not have a substring that is one of the 5040 permutations of "project".

# T(7)=7^7-7!=818503.
# Find T(10^12). Give the last 9 digits of your answer.

# state-based recurrence relation: then do powers of matrices - the inelegant sol 
# requires lots of states and might not even work 