import functions as f
largest = 0
for k in f.pf(600851475143):
    if k > largest:
        largest = k 
print(largest)