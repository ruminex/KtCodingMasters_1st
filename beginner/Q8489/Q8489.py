N = (int)(input())

Apartment = []
total_dist = []
for a in range(0,N):
    x = [int(k) for k in input().split()]   
    Apartment.append(x)

for b in range(0,N):
    dist = 0
    for c in range(0,N):
        dist += (abs(Apartment[b][0] - Apartment[c][0]) * Apartment[c][1])
    total_dist.append(dist)
    
print(total_dist.index(min(total_dist))+1)
        