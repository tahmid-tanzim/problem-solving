import asyncio
import yappi


async def slow_task():
    await asyncio.sleep(2000)
    print("Slow task completed")


async def fast_task():
    await asyncio.sleep(1000)
    print("Fast task completed")


async def main():
    yappi.start()  # Start profiling
    await asyncio.gather(slow_task(), fast_task())
    yappi.stop()  # Stop profiling

    # Print out the profiling results
    yappi.get_func_stats().print_all()

if __name__ == "__main__":
    asyncio.run(main())