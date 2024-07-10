#!/Library/Frameworks/Python.framework/Versions/3.10/Resources/Python.app/Contents/MacOS/Python
import asyncio
import time


def timeit(func):
    if asyncio.iscoroutinefunction(func):
        async def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = await func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f'Function {func.__name__!r} took {total_time:.4f} seconds')
            return result
    else:
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f'Function {func.__name__!r} took {total_time:.4f} seconds')
            return result
    return wrapper


@timeit
def power(a, b):
    return a ** b

@timeit
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

@timeit
async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main(), debug=True)




