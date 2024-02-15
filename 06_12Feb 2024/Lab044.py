# Break

# for i in range(1,10)
# i=5 -->break from loop -kick out from loop

for i in range(1, 11):
    if i == 5:
        break
    print(i)
print("Outside the loop")
# o/p: 1, 2, 3, 4, outside the loop


for i in range(1, 11):
    print(i)
    if i == 5:
        break
print("Outside the loop")

# o/p: 1,2,3,4,5,outside the loop
