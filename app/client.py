import argparse

import aiohttp
import asyncio


async def fetch(sess: aiohttp.ClientSession, url: str, headers: dict):
    async with sess.get(url, headers=headers) as resp:
        return await resp.text()


async def perform_requests(n: int, url: str, headers: dict):
    async with aiohttp.ClientSession() as sess:
        res = await asyncio.gather(*[fetch(sess, url, headers) for _ in range(0, n)])
        for item in res:
            print(item)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--port', type=int, default=8080, dest='port', help="port for http requests")
    parser.add_argument(
        '-n', '--number', type=int, default=5, dest='number', help="number of requests")
    parser.add_argument(
        '-s', '--session-id', dest='sess_id', help="session id")
    return parser.parse_args()


def main():
    args = parse_args()
    url = "http://localhost:{}".format(args.port)
    headers = {'X-SESSION-ID': args.sess_id}
    asyncio.run(perform_requests(args.number, url, headers))


if __name__ == '__main__':
    main()
