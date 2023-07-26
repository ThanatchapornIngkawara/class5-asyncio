# 1-1-simple-sync.py
import time 

def sleep():
    print(f'Time: {time.time() - start:.2f}')  
    time.sleep(1) 

# ผลรวมของตัวเลขในรายการ numbers ที่ถูกคำนวณแล้ว
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')  
        sleep()  
        total += number  
    #นำตัวเลขแต่ละตัวมาบวกกับค่า total ฟังก์ชัน sleep จะถูกเรียกเพื่อ delay 1 sec ก่อนที่จะคำนวณตัวเลขถัดไป
    print(f'Task {name}: Sum = {total}\n')  
start = time.time()  

# คำนวณผลรวมของตัวเลขที่อยู่ในรายการ numbers 
tasks = [
    sum("A", [1, 2]),  
    sum("B", [1, 2, 3]),  
]

end = time.time()  

print(f'Time: {end-start:.2f} sec') 

# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.02
# Task B: Computing 1+2
# Time: 3.03
# Task B: Computing 3+3
# Time: 4.04
# Task B: Sum = 6

# Time: 5.05 sec
