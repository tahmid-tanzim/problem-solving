#!/Library/Frameworks/Python.framework/Versions/3.10/Resources/Python.app/Contents/MacOS/Python
import asyncio
import time


def timeit(func):
    if asyncio.iscoroutinefunction(func):
        async def coroutine_wrapper(*args, **kwargs):
            start_time = time.time()
            coroutine_result = await func(*args, **kwargs)
            end_time = time.time()
            total_time = end_time - start_time
            print(f'Coroutine Function {func.__name__!r} took {total_time:.4f} seconds')
            return coroutine_result
        return coroutine_wrapper
    else:
        def wrapper(*args, **kwargs):
            start_time = time.time()
            non_coroutine_result = func(*args, **kwargs)
            end_time = time.time()
            total_time = end_time - start_time
            # first item in the args, ie `args[0]` is `self`
            print(f'Function {func.__name__!r} took {total_time:.4f} seconds')
            return non_coroutine_result
        return wrapper


@timeit
def power(a, b):
    return a ** b


@timeit
async def main(x, y):
    print('Start')
    output = await asyncio.sleep(2, result=power(x, y))
    print('Result:', output)
    print('End')


if __name__ == "__main__":
    asyncio.run(main(3, 5), debug=True)




