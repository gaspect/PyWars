# # PyWars

# We start from a strigth forward idea: use a client and a  set of types for do some stream processing over stream of those types.

# The client
from .client import Client

# The types
from .types import (
    Deal,
    Offer,
    Duelist,
    Duel,
    Item,
    SexDigest,
    OfferItem,
    Specialization,
    Shop,
    YellowPage,
    AuctionDeal,
    AuctionDigest,
)

# The stream
from faust import Stream

# I am not a hardcore player of chat war (CW) but i am a curious person
# and I was building some bots that help to play chat wars until i meet gecko and lycaon.
# But afther some research in my developing fever I found that the CW API has only an old client in GO
# but nothing that consume from actual kafka streams in a strigth forward manner.

# This is a client for **public api**  based on Chat Wars API docs and some usefull examples from sixcross repo.

"""
This implementation not behold any rpc call to private API but in the futere
I want do that and in other future merge both to have a complete functional overpowered API
"""
