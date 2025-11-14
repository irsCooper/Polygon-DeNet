import asyncio
import json
import aiohttp
from web3 import AsyncWeb3
# from src.core.config import settings

class PolygonClient:
    def __init__(self):
        # self.w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(settings.RPC_URL))
        self.w3: AsyncWeb3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider("https://rpc-amoy.polygon.technology"))
        self.session: aiohttp.ClientSession | None = None

    async def init(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()

    async def close(self):
        if self.session:
            await self.session.close()

    async def call_polygonscan(self, params: dict):
        params["apikey"] = "AVB4C6QA3Z6QWD9QVI3HENJUGNHYKBEK5R"

        async with self.session.get("https://api.etherscan.io/v2/api", params=params) as r:
            data = await r.json()
            return data


client = PolygonClient()

async def main():
    await client.init()

    params = {
        "module": "stats",
        "action": "tokensupply",
        "contractaddress": "0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0",
        "chainId": 137
    }

    result = await client.call_polygonscan(params)
    print(result)

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())