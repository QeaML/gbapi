import asyncio
from gbapi import *

async def main():
	g = gbApi()
	m = await g.get_map(210265)
	print(m.game.name)
	await g.close()
	
l = asyncio.get_event_loop()
l.run_until_complete(main())