from pocketoptionapi_async.client import Client
import asyncio

ssid = '42["auth",{"sessionToken":"40527f1167b31e5240fc7c2b174589ce","uid":"115265714","lang":"ru","currentUrl":"cabinet/demo-quick-high-low","isChart":1}]	'

client = Client(ssid=ssid, demo=True)

async def main():
    await client.connect()
    balance = await client.get_balance()
    print("Баланс:", balance)

asyncio.run(main())

