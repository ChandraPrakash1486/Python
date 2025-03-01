import asyncio
#defining coroutines
async def Teacher():
    name = input("Enter the name of the teacher: ")#2
    await asyncio.sleep(1)#3
    age = int(input("Enter the age of the Teacher"))
    
    
    
async def Student():
    name = input("Enter the name of the Student: ")#5
    await asyncio.sleep(1)#6
    age = int(input("Enter the age of the Student"))
    
    
async def main():
   task1 = asyncio.create_task(Teacher())
   task2 = asyncio.create_task(Student())
   
   #second await
   await task1
   await task2

   
# Run the main function
asyncio.run(main())

