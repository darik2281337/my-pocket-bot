import asyncio
from pocketoptionapi_async.client import client  

SSID = '42["auth",{"sessionToken":"40527f1167b31e5240fc7c2b174589ce","uid":"115265714","lang":"ru","currentUrl":"cabinet/demo-quick-high-low","isChart":1}]'

c = client(SSID, demo=True) 

async def main():
   
    await c.connect()
   
    balance = await c.get_balance()
    print("Баланс:", balance)


asyncio.run(main())


