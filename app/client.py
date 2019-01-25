import aiohttp
import asyncio


async def fetch(sess, url):
    async with sess.get(url) as resp:
            return await resp.text(), resp.cookies


async def main():
    url = "http://localhost:8081"
    async with aiohttp.ClientSession() as sess:
        for i in range(0, 10):
            print(await fetch(sess, url))


if __name__ == '__main__':
    asyncio.run(main())
