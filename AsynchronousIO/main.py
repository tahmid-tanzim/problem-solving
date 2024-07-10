#!/Library/Frameworks/Python.framework/Versions/3.10/Resources/Python.app/Contents/MacOS/Python
import asyncio


async def main():
    result = await asyncio.sleep(10, result='hello world')
    print(result, '- 10 sec')

if __name__ == "__main__":
    # asyncio.run(main(), debug=True)
    with asyncio.Runner() as runner:
        runner.run(main())


