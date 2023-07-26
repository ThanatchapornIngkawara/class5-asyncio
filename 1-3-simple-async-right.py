import asyncio
import time

#ใช้ await asyncio
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')  
        await sleep()  
        total += number  
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
print(f'Time: {end-start:.2f} sec')


# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.02
# Task B: Sum = 6

# Time: 3.03 sec