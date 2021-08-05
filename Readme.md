# PyWars

> A public topic consumer for Chat Wars ... **with steroids**


## 🚀 Motivations

- 🤖 Build a bot? 
- 👥 Help comunity? 
- 🚀 Personal training?


## ☄ Quick start

```python
from PyWars import *

app = Client()

@app.agent(Deal)
async def deals(stream:Stream[Deal]):
    async for deal in stream:
        print(deal)

app.run()
```
## 📚 Overview

### Dummy client creation

```python
from PyWars import Client
app = Client()
```
>This will create a client with a autogenerate id for chat wars **v2** api

----------


### Specifiying client version

```python
from PyWars import Client
app = Client(version=Client.Version.CW3)
```
>This will create a client for chat wars **v3** api

----------

### Adding agents

```python
from PyWars import *
app = Client()

@app.agent(Deal)
async def deals(stream:Stream[Deal]):
    async for deal in stream:
        print(deal)

app.run()
```
The **Client.agent** method recieve an allowed record. The allowed records are:

- **Deal** for *cw\*-deals* topic
- **Duel** for *cw\*-duels* topic
- **Offer** for *cw\*-offers* topic
- **SexDigest** for *cw\*-sex_digest* topic
- **YellowPage** for *cw\*-yellow_pages* topic
- **AuctionDigest** for *cw\*-au_digest* topic

----------

### Adding timers

```python
from PyWars import *
app = Client()
procesed_deals = 0

@app.agent(Deal)
async def deals(stream:Stream[Deal]):
    async for deal in stream:
        procesed_deals += 1

@app.timer(60)
async def print_procesed():
    print(procesed_deals)
    procesed_deals = 0

app.run()
```
A timer is a courutine that is trigger every *n* seconds in this examples we use *60 seconds*.

----------

### Using executions loops

```python
from PyWars import *
import asyncio

app = Client(loop=asyncio.get_event_loop())

@app.agent(Deal)
async def deals(stream:Stream[Deal]):
    async for deal in stream:
        print(deal)
try:
    app.start()
finally:
    app.stop()
```

The magics start and stop methods are thinking to run and stop client with his exxecution loop smootly

----------

### Bulking

```python
from PyWars import *nicely

app = Client()

@app.agent(Deal)
async def deals(stream:Stream[Deal]):
    async for bulk in stream.take(100, 10):
        print(bulk)

app.run()
```
A bulk is just the use of **Stream.take** method from **faust**. It will try take bulks of 100 objetcs, in case that it can´t return the 100 objects its gona wait for 10 seconds and return any amount gathered in that time.

----------

For extended documentation see for the docs page.