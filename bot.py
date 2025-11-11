import asyncio
from pocketoptionapi_async.client import AsyncPocketOptionClient
from pocketoptionapi_async.exceptions import ConnectionError

SSID = '42["auth",{"sessionToken":"40527f1167b31e5240fc7c2b174589ce","uid":"115265714","lang":"ru","currentUrl":"cabinet/demo-quick-high-low","isChart":1}]'

client = AsyncPocketOptionClient(SSID)  

async def main():
    try:
        await client.connect()               
        balance = await client.get_balance() 
        print("Баланс:", balance)
    except ConnectionError as e:
        print("Ошибка подключения:", e)

asyncio.run(main())






