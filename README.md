# gbapi
*qeaml's wrapper for GameBanana's API*

## About
`gbapi` is a straight-to-the-point, asynchronous Python API wrapper for
[GameBanana](https://gamebanana.com)'s API. Please do note that this is my first
proper API, so go easy on me :) If you want to get in contact with me through
GB, [click here](https://gamebanana.com/members/1479808) to go to my profile, and feel free to PM me about anything.

## Requirements
* Python 3.6+
* `aiohttp`

## Usage
After you've installed the library:
```py
import asyncio
import gbapi

async def main():
	gb = gbapi.Client()
	m = await gb.get_map(12345)
	print(m.game.name)      #prints the name of the game the map is for
	print(m.author.name)    #prints the name of the submitter
	await gb.close()        #remember to always close() your client !
	
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
```