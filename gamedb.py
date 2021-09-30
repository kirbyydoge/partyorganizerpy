import pymongo
import os
from pymongo import MongoClient
from game import Game
# please declare these tokens in a python file
from secrets import MONGODB_TOKEN

MAX_GAMES_BASIC = 25
MAX_GAMES_PREMIUM = 50

def connect():
    client = MongoClient(MONGODB_TOKEN)
    db = client["party_organizer"]
    collection = db["server_game_infos"]
    return collection

def push_game(collection, server_id, game, force=False):
    key = {"server_id":server_id}
    result = collection.find(key)
    cur_size = result.count()
    if cur_size < MAX_GAMES_BASIC or force:
        key = {"server_id":server_id, "game":game.name}
        post = {"server_id":server_id, "game":game.name, "emote": game.emote, "role": game.role}
        collection.update(key, post, upsert=True)
        return cur_size+1, True
    else:
        return cur_size, False

def remove_game(collection, server_id, game):
    key = {"server_id":server_id, "game":game.name, "emote": game.emote, "role":game.role}
    result = collection.delete_many(key)
    return result.deleted_count

def pull_game(collection, server_id, game_name):
    game_name = game_name.lower()
    key = {"server_id":server_id, "game":game_name}
    result = collection.find_one(key)
    if result is not None:
        game_name = result["game"]
        emote = result["emote"]
        role = result["role"]
        game = Game(game_name, emote, role)
        return game
    else:
        return None

def pull_all(collection, server_id):
    key = {"server_id":server_id}
    result = collection.find(key)
    games = []
    if result is not None:
        for entry in result:
            game_name = entry["game"]
            emote = entry["emote"]
            role = entry["role"]
            game = Game(game_name, emote, role)
            games.append(game)
        games.sort()
        return games
    else:
        return None
