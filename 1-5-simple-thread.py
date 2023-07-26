import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor

#ใช้ async await, asyncio, และ ThreadPoolExecutor เพื่อทำงานแบบแบ่งเป็น thred concurrent
#ไม่บังคับให้รอเวลาในการทำงาน และคำนวณเวลาที่ใช้ในการ run ทั้งหมด
def sleep():
    print(f'Time: {time.time() - start:.2f}')  
    time.sleep(1) 


async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')  
        sleep()  
        total += number  
    #นำตัวเลขแต่ละตัวมาบวกกับค่า total ฟังก์ชัน sleep จะถูกเรียกเพื่อ delay 1 sec ก่อนที่จะคำนวณตัวเลขถัดไป
    print(f'Task {name}: Sum = {total}\n')  
start = time.time()  

#สร้าง event loop 
loop = asyncio.get_event_loop()

#สร้างงานให้กับ event loop โดยใช้ loop.create_task
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]

#run event loop โดยใช้ loop.run_until_complete
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2} sec')


# Task A: Computing 0+1
# Time: 0.01
# Task A: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.02
# Task B: Computing 1+2
# Time: 3.02
# Task B: Computing 3+3
# Time: 4.03
# Task B: Sum = 6

# Time: 5.0 sec