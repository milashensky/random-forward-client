#!/usr/bin/env python
import asyncio
from client import RandomMessageClient
import settings


async def main():
    async with RandomMessageClient() as client:
        message = await client.get_random_message(settings.FROM_CHANNEL)
        await client.forward_message(
            message,
            settings.TO_CHANNEL,
        )


if __name__ == '__main__':
    asyncio.run(main())
