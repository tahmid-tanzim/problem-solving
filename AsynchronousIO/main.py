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


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    background_task = [
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    ]
    # Schedule three calls *concurrently*:
    # L = await asyncio.gather(
    #     factorial("A", 2),
    #     factorial("B", 3),
    #     factorial("C", 4),
    # )
    L = await asyncio.gather(
        *background_task
    )
    print(L)


if __name__ == "__main__":
    asyncio.run(main(), debug=True)




