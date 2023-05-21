import asyncio
import logging

async def delay(delay_seconds: int) -> int:
    logging.info(f"sleeping {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    logging.info(f"Finished sleeping {delay_seconds} seconds")
    return delay_seconds
