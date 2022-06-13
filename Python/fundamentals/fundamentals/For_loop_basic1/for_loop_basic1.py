#integers 0-150
for i in range(151):
    print(i)

#multiples of 5
for i in range(0, 1001, 5):
    print(i)

#Counting the Dojo Way
for i in range(1,101):
    if i %10==0:
        print("Coding Dojo")
    
    elif i % 5==0:
        print("coding")

#That sucker's huge
total=0
for i in range(1, 500001, 2):
    total = i + total
print(total)

#Countdown by 4
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
lowNum=5
highNum=100
mult=5
for lowNum in range(lowNum,highNum):
    if lowNum % mult == 0:
        print(lowNum)
