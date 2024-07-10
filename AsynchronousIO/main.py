#!/usr/bin/python3
import asyncio


async def main():
    result = await asyncio.sleep(10, result='hello world')
    print(result, ' - 10 sec')

if __name__ == "__main__":
    asyncio.run(main())


