import asyncio

async def idly():
    print("one idly is being made")
    await asyncio.sleep(1)
    print("one idly is ready")
    
async def dosa():
    print("one dosa is being made")
    await asyncio.sleep(4)
    print("one dosa is ready")
    
async def main():
    # await asyncio.gather(idly(), dosa())#gather is used to run multiple coroutines concurrently
    task1 = asyncio.create_task(idly())
    task2 = asyncio.create_task(dosa())
    
    await task1
    await task2
    
    
asyncio.run(main())
    
