import discord
import sys
from discord import message
import gamedb as gdb
import time
from discord.utils import get
from discord.ext import commands
from game import Game
from utils import User
# please declare these tokens in a python file
from secrets import DISCORD_TOKEN_MAIN, DISCORD_TOKEN_TEST

#thumbnail
thumbnails = ["https://media.tenor.com/images/93e6661ebc2648cc8aa46add5447a4ca/tenor.gif"]

#whitelisted authors
developer_id = [165686666198122496, #doge
                198932790840918028] #gaius

whitelisted_server_ids = [504335438518157312, #anlasilabilir
                          761109150188044288] #bot developtment channel
                          
po_channels = [767041059518939139, #anlasilabilir
                            1232131]           
           

#test variable
test = False

main_server_id = whitelisted_server_ids[1] if test else whitelisted_server_ids[0]
main_channel_id = po_channels[1] if test else po_channels[0]

#token
po = DISCORD_TOKEN_MAIN
rb = DISCORD_TOKEN_TEST
if test:
    TOKEN = rb
    cur_prefix = "!rb "
else:
    TOKEN = po
    cur_prefix = "!po "

#bot object
client = commands.Bot(command_prefix=cur_prefix)
client.remove_command("help")

#db connection
collection = gdb.connect()

#collection of headcounts that are up
headcounts = {}

#timing definitions
PLAY_UPTIME = 1800
LONG_UPTIME = 60
MED_UPTIME = 30
SHORT_UPTIME = 15

#toggle no_flood
stop_flood = False

@client.event
async def on_message(message:discord.message.Message):
    print(message.channel.id)
    global stop_flood
    channel = get(message.guild.channels, name="party-organize", type=discord.ChannelType.text)
    if stop_flood and message.channel == channel and message.author.id != client.user.id \
            and message.author.id not in developer_id:
        await message.delete()
    if stop_flood:
        args = message.content.split(" ")
        if "play" in args or "toggleflood" in args:
            await client.process_commands(message)
    else:
        await client.process_commands(message)

@client.event
async def on_ready():
    print("Ready to roll.")

@client.command()
async def toggleflood(ctx:commands.Context):
    global stop_flood
    if ctx.message.author.id in developer_id:
        stop_flood = not stop_flood
        if stop_flood:
            await ctx.send(content="Keep crying. You can still use commands.")
        else:
            await ctx.send(content="Peasants may speak now.")
    else:
        await ctx.send(content="You need developer rights to toggle this feature.")
    await ctx.message.delete()
        
    
@client.command()
async def goodbot(ctx:commands.Context):
    embed = discord.Embed(
        title = "Thank you {} for the good chemicals!".format(ctx.message.author.display_name),
        color = discord.Colour.red()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/219037484531580929/761513648953753620/REACT.jpg")
    #await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def arrivederci(ctx:commands.Context):
    embed = discord.Embed(
        title = "\u200b",
        color = discord.Colour.red()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/219037484531580929/764310156875006002/maxresdefault.jpg")
    #await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def kekw(ctx:commands.Context):
    embed = discord.Embed(
        title = "\u200b",
        color = discord.Colour.red()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/504681362251579411/767043842121400360/tenor_1.gif")
    #await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def realshit(ctx:commands.Context):
    embed = discord.Embed(
        title = "\u200b",
        color = discord.Colour.red()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/504681362251579411/767044330829250570/r-e-a-l-shit-58f39ca9700e9.jpeg")
    #await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def ohmygod(ctx:commands.Context):
    embed = discord.Embed(
        title = "\u200b",
        color = discord.Colour.red()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/165829330130305024/767502707862798376/tenor.gif")
    #await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def gokce(ctx:commands.Context):
    if ctx.message.guild.id in whitelisted_server_ids:
        embed = discord.Embed(
            title = "Noice",
            color = discord.Colour.red()
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/504681362251579411/767499258987020308/ezgif.com-gif-maker.gif")
        #await ctx.message.delete()
        await ctx.send(embed=embed)
    else:
        print("LOG!!! server:{} tried to use gokce.".format(ctx.message.guild.id))

@client.command()
async def gokalp(ctx:commands.Context):
    if ctx.message.guild.id in whitelisted_server_ids:
        embed = discord.Embed(
            title = "\u200b",
            color = discord.Colour.red()
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/504681362251579411/767504383167823912/gokalp_appear.gif")
        #await ctx.message.delete()
        await ctx.send(embed=embed)
    else:
        print("LOG!!! server:{} tried to use gokalpappear.".format(ctx.message.guild.id))

@client.command()
async def gokalp2(ctx:commands.Context):
    if ctx.message.guild.id in whitelisted_server_ids:
        embed = discord.Embed(
            title = "\u200b",
            color = discord.Colour.red()
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/504681362251579411/767504356685512764/gokalp_disappear.gif")
        #await ctx.message.delete()
        await ctx.send(embed=embed)
    else:
        print("LOG!!! server:{} tried to use gokalpdisappear.".format(ctx.message.guild.id))

@client.command()
async def oguz(ctx:commands.Context):
    if ctx.message.guild.id in whitelisted_server_ids:
        embed = discord.Embed(
            title = "brb let me kill myself real quick",
            color = discord.Colour.red()
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/504681362251579411/767505642092232704/oguz.gif")
        #await ctx.message.delete()
        await ctx.send(embed=embed)
    else:
        print("LOG!!! server:{} tried to use oguz.".format(ctx.message.guild.id))


@client.command()
async def help(ctx:commands.Context, *arg): # no comment needed as its mostly string's and embeds, grow a pair and figure out yourself
    if len(arg) == 0:
        embed = discord.Embed(
            title = "Available Commands",
            color = discord.Colour.red()
        )
        message = "list\nplay\naddgame\ndeletegame\naddrole\ndeleterole\nabort\ngoodbot\narrivederci"
        embed.add_field(name="Use <!po help <command>> to display usage", value=message, inline=True)
        await ctx.send(embed=embed)
    elif len(arg) > 1:
        embed = discord.Embed(
            title = "Unsupported Format!",
            color = discord.Colour.red()
        )
        message = "<!po help <command>> or <!po help>"
        embed.add_field(name="Usage:", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "list":
        embed = discord.Embed(
            title = "<!po list>",
            color = discord.Colour.red()
        )
        message = "List of games that are added to this server."
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "play":
        embed = discord.Embed(
            title = "<!po play game1, game2, game3...>",
            color = discord.Colour.red()
        )
        message = ("Starts a headcount of players for specified games.\n"
                    "Use <!po play any> to add all games to headcount.\n"
                    "You may optionally add for:<minutes> before or after listing your games to specify an uptime for your message.\n"
                    "Or use in:<minutes> to notify users the time you'll start playing.")
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "addgame":
        embed = discord.Embed(
            title = "<!po addgame gamename, :server_emote:, @server_role>",
            color = discord.Colour.red()
        )
        message = "Adds a game to server\"s game list.\n:server_emote: and @server_role must be server custom emotes and roles.\n\nRequires administration permissions!"
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "deletegame":
        embed = discord.Embed(
            title = "<!po addgame gamename, :server_emote:, @server_role>",
            color = discord.Colour.red()
        )
        message = "Deletes specified game from server\"s game list.\n\nRequires administration permissions!"
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "deleterole":
        embed = discord.Embed(
            title = "<!po deleterole gamename>",
            color = discord.Colour.red()
        )
        message = "Removes selected game\"s role from user."
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "addrole":
        embed = discord.Embed(
            title = "<!po addrole gamename>",
            color = discord.Colour.red()
        )
        message = "Adds selected game\"s role to user."
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "listme":
        embed = discord.Embed(
            title = "<!po listme>",
            color = discord.Colour.red()
        )
        message = "Lists games that the user plays."
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "goodbot":
        embed = discord.Embed(
            title = "<!po goodbot>",
            color = discord.Colour.red()
        )
        message = "Makes your hard working bot happy."
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "abort":
        embed = discord.Embed(
            title = "<!po abort>",
            color = discord.Colour.red()
        )
        message = "Cancels user's last play check."
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    elif arg[0] == "arrivederci":
        embed = discord.Embed(
            title = "<!po arrivederci>",
            color = discord.Colour.red()
        )
        message = "To learn what this actually is, please watch JOJO."
        embed.add_field(name="\u200b", value=message, inline=True)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "Could not find command {}".format(arg[0]),
            color = discord.Colour.red()
        )
        message = "Check <!po help> for the list of commands."
        embed.add_field(name="Please enter a valid command.", value=message, inline=True)
        await ctx.send(embed=embed)
    #await ctx.message.delete()

async def helper(ctx:commands.Context):
    uptime = 1800
    username = ctx.message.author.display_name
    pfp = ctx.message.author.avatar_url
    server_id = ctx.message.guild.id
    cur_emotes = []
    cur_roles = ""
    play_title = "{}, select the games you want to play then ✅.".format(username)
    embed = discord.Embed(
        title = play_title,
        color = discord.Colour.red()
    )
    embed.set_thumbnail(url=pfp)
    games = gdb.pull_all(collection, server_id)
    if games is not None:
        all_emotes = []
        all_roles = []
        for game in games:
            game_emote = get(ctx.guild.emojis, id=game.emote)
            game_role = get(ctx.guild.roles, id=game.role)
            all_emotes.append(game_emote)
            all_roles.append(game_role)
        entries = zip(all_roles, all_emotes)
        for game_role, game_emote in entries:
            cur_emotes.append(game_emote)
            cur_roles += game_role.mention + " "
            embed.add_field(name=game_emote, value=game_role.mention, inline=True)
    if len(cur_roles) > 0:  # if there is at least 1 game being played
        author_id = ctx.message.author.id
        if author_id in headcounts and (time.time() - headcounts[author_id]["time"]) < headcounts[author_id]["uptime"]:
            try:    # user's last headcount should be going on, if message exists delete it
                await headcounts[author_id]["msg"].delete()
            except: # someone deleted the message before bot did
                print("no message")
        embed.set_footer(text="React to icons of the games that you want to play!\nThis message will stay for {} minutes.".format(int(uptime/60)))
        msg = await ctx.send(content=cur_roles, embed=embed, delete_after=uptime)
        for emote in cur_emotes:    # add reacts to message
            await msg.add_reaction(emote)
        await msg.add_reaction("✅")
        headcounts[author_id] = {"msg":msg, "time":time.time(), "uptime":uptime}    # store user data for further control
        print("server:{} author:{} plays for:{}".format(server_id, author_id, uptime))  # log data, only available to developers
        
        def check(reaction, user):
            return user.id == ctx.message.author.id and reaction.message.id == msg.id and str(reaction.emoji) == "✅"

        await client.wait_for('reaction_add', check=check)

@client.command()
async def play(ctx:commands.Context, *, arg=None):
    print(arg)
    if arg is None:
        await helper(ctx)
        return
    start = arg.find("for:")    # check for play time args
    if(start != -1):    # 60 <= playtime <= 7200
        end = arg.find(" ", start)
        if end == -1:
            end = len(arg)
        uptime = int(float(arg[start+4:end])*60)
        if uptime <= 0:
            uptime = 1
        if uptime > 7200:
            uptime = 7200
        arg = arg[:start] + arg[end:]
        print(arg)
    else:   # default playtime
        uptime = PLAY_UPTIME
    start = arg.find("in:")    # check for start time args
    if(start != -1):    # starttime <= 60
        end = arg.find(" ", start)
        if end == -1:
            end = len(arg)
        starttime = int(float(arg[start+3:end])*60)
        if starttime < 0:
            starttime = 0
        if starttime > 3600:
            starttime = 3600
        arg = arg[:start] + arg[end:]
        print(arg)
    else:   # default playtime
        starttime = 0
    uptime += starttime
    args = sorted(set(arg.lower().replace(" ", "").split(","))) # games are taken as a comma seperated list, spaces are meaningless
    addAll = False
    username = ctx.message.author.display_name  # fetch user data for embed
    pfp = ctx.message.author.avatar_url
    if starttime == 0:
        play_title = "{} wants to play:".format(username)
    else:
        play_title = "{} wants to play in {} minutes:".format(username, int(starttime/60))
    embed = discord.Embed(
        title = play_title,
        color = discord.Colour.red()
    )
    embed.set_thumbnail(url=pfp)
    server_id = ctx.message.guild.id
    cur_roles = ""  # list variables to hold games that are being played
    cur_emotes = []
    for check in args:  # look if user wants to play all games
        if check == "any" or check == "anything":
            addAll = True
    if addAll:  # adds all available games to playlist
        games = gdb.pull_all(collection, server_id)
        if games is not None:
            all_emotes = []
            all_roles = []
            for game in games:
                game_emote = get(ctx.guild.emojis, id=game.emote)
                game_role = get(ctx.guild.roles, id=game.role)
                all_emotes.append(game_emote)
                all_roles.append(game_role)
            entries = zip(all_roles, all_emotes)
            for game_role, game_emote in entries:
                cur_emotes.append(game_emote)
                cur_roles += game_role.mention + " "
                embed.add_field(name=game_emote, value=game_role.mention, inline=True)   
    else:   # parse args and add those games if they exist
        for game_name in args:
            game = gdb.pull_game(collection, server_id, game_name)
            if game is not None:
                game_emote = get(ctx.guild.emojis, id=game.emote)
                game_role = get(ctx.guild.roles, id=game.role)
                cur_emotes.append(game_emote)
                cur_roles += game_role.mention + " "
                embed.add_field(name=game_emote, value=game_role.mention, inline=True)
    #await ctx.message.delete()  # delete user message, as fetching more data is not necessary
    if len(cur_roles) > 0:  # if there is at least 1 game being played
        author_id = ctx.message.author.id
        if author_id in headcounts and (time.time() - headcounts[author_id]["time"]) < headcounts[author_id]["uptime"]:
            try:    # user's last headcount should be up, if message exists delete it
                await headcounts[author_id]["msg"].delete()
            except: # someone deleted the message before bot did
                print("no message")
        embed.set_footer(text="React to icons of the games that you want to play!\nThis message will stay for {} minutes.".format(int(uptime/60)))
        msg = await ctx.send(content=cur_roles, embed=embed, delete_after=uptime)
        for emote in cur_emotes:    # add reacts to message
            await msg.add_reaction(emote)
        headcounts[author_id] = {"msg":msg, "time":time.time(), "uptime":uptime}    # store user data for further control
        print("server:{} author:{} plays for:{}".format(server_id, author_id, uptime))  # log data, only available to developers
    else:   # no games are being played
        embed = discord.Embed(
            title = "No matching games found!",
            color = discord.Color.red()
        )
        embed.add_field(name="\u200b", value="Use command:\n<!po list> to view available games.\nUse command:\n<!po addgame gamename, :server_emoji:, @server_role> to add games.")
        await ctx.send(embed=embed)

@client.command()
async def addrole(ctx:commands.Context, *arg):
    if len(arg) != 1:   # add 1 role at a time, might support multiple roles later but too lazy idk
        embed = discord.Embed(
            title = "Unsupported Format!",
            color = discord.Colour.red()
        )
        message = "<!po addrole game_name>"
        embed.add_field(name="Usage:", value=message, inline=True)
    else:   # correct format
        server_id = ctx.message.guild.id
        game = gdb.pull_game(collection, server_id, arg[0]) # queries database to see if game exists
        if game is not None:    # user wants a valid game's role
            member = ctx.message.author
            role = get(member.guild.roles, id=game.role)    # find role from server roles list
            embed = discord.Embed(
                title = "{} now plays {}!".format(ctx.message.author.display_name, game.name),
                color = discord.Colour.red()
            )
            game_emote = get(ctx.message.guild.emojis, id=game.emote)
            embed.add_field(name=game_emote, value=role.mention, inline=True)
            embed.set_thumbnail(url=member.avatar_url)
            await member.add_roles(role)    # role granted
        else:
            embed = discord.Embed(
                title = "Could not find game {}".format(ctx.message.author.display_name, arg[0]),
                color = discord.Colour.red()
            )
            message = "Use <!po list> to view available games."
            embed.add_field(name="\u200b", value=message, inline=True)
    #await ctx.message.delete()  # delete user message
    await ctx.send(embed=embed)  # notify people that a retard is playing another loser's game

@client.command()
async def deleterole(ctx:commands.Context, *arg):
    if len(arg) != 1:   # see if user has iq > 10
        embed = discord.Embed(
            title = "Unsupported Format!",
            color = discord.Colour.red()
        )
        message = "<!po deleterole game_name>"
        embed.add_field(name="Usage:", value=message, inline=True)
    else:   # user is at least a monkey, also read addrole's comments, literally same shit happening
        server_id = ctx.message.guild.id
        game = gdb.pull_game(collection, server_id, arg[0])
        if game is not None:
            member = ctx.message.author
            role = get(member.guild.roles, id=game.role)
            embed = discord.Embed(
                title = "{} no longer plays {}!".format(ctx.message.author.display_name, game.name),
                color = discord.Colour.red()
            )
            game_emote = get(ctx.message.guild.emojis, id=game.emote)
            embed.add_field(name=game_emote, value=role.mention, inline=True)
            embed.set_thumbnail(url=member.avatar_url)
            await member.remove_roles(role)
        else:
            embed = discord.Embed(
                title = "Could not find game {}".format(ctx.message.author.display_name, arg[0]),
                color = discord.Colour.red()
            )
            message = "Use <!po list> to view available games."
            embed.add_field(name="\u200b", value=message, inline=True)
    #await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def addgame(ctx:commands.Context, *, arg):
    args = arg.replace(" ", "").split(",")  # parse args
    if len(args) != 3:  # format of 3 ci
        embed = discord.Embed(
            title = "Unsupported format!",
            color = discord.Color.red()
        )
        embed.add_field(name="Command Usage:", value="!po addgame gamename, :server_emoji:, @server_role")
        await ctx.send(embed=embed)
        return
    user = User(ctx)
    if user.user_id in developer_id:
        force = True
    else:
        force = False
    game_name = args[0]
    game_emoteid = int(args[1][args[1].rindex(":")+1:len(args[1])-1])
    game_roleid = int(args[2][3:len(args[2])-1])
    game_emote = get(ctx.guild.emojis, id=game_emoteid)
    game_role = get(ctx.guild.roles, id=game_roleid)
    game = Game(game_name, game_emote.id, game_role.id)
    count, result = gdb.push_game(collection, user.server_id, game, force)
    if result:
        embed = discord.Embed(
            title = "{} added a game.".format(user.username),
            color = discord.Colour.red()
        )
        embed.add_field(name="Name", value=game_name, inline=True)
        embed.add_field(name="Emote", value=game_emote, inline=True)
        embed.add_field(name="Role", value=game_role.mention, inline=True)
    else:
        embed = discord.Embed(
            title = "{} couldn\"t add a game.".format(user.username),
            color = discord.Colour.red()
        )
        embed.add_field(name="\u200b", value="You already have {} games.".format(count), inline=True)
        print("server:{} already had {} games.".format(user.server_id, count))
    embed.set_thumbnail(url=user.picture)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def deletegame(ctx:commands.Context, *, arg):
    args = arg.replace(" ", "").split(",")
    server_id = ctx.message.guild.id
    username = ctx.message.author.display_name
    pfp = ctx.message.author.avatar_url
    if len(args) != 3:
        embed = discord.Embed(
            title = "Unsupported format!",
            color = discord.Color.red()
        )
        embed.add_field(name="Command Usage:", value="!po deletegame gamename, :server_emoji:, @server_role")
        await ctx.send(embed=embed)
        return
    game_name = args[0]
    game_emoteid = int(args[1][args[1].rindex(":")+1:len(args[1])-1])
    game_roleid = int(args[2][3:len(args[2])-1])
    game_emote = get(ctx.guild.emojis, id=game_emoteid)
    game_role = get(ctx.guild.roles, id=game_roleid)
    game = Game(game_name, game_emote.id, game_role.id)
    count = gdb.remove_game(collection, server_id, game)
    if count > 0:
        embed = discord.Embed(
            title = "{} removed a game.".format(username),
            color = discord.Color.red()
        )
        embed.add_field(name="Name", value=game_name, inline=True)
        embed.add_field(name="Emote", value=game_emote, inline=True)
        embed.add_field(name="Role", value=game_role.mention, inline=True)
        embed.set_thumbnail(url=pfp)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "{} failed to remove a game.".format(username),
            color = discord.Color.red()
        )
        embed.add_field(name="\u200b", value="No matching entries found in database.\nUse command <!po list> to make sure game you tried to remove is added to this server.", inline=True)
        embed.set_thumbnail(url=pfp)
        await ctx.send(embed=embed)

@client.command()
async def list(ctx:commands.Context):
    user = User(ctx)
    games = gdb.pull_all(collection, user.server_id)
    embed = discord.Embed(
        title = "{} requested a list of games available:".format(user.username),
        color = discord.Colour.red()
    )
    embed.set_thumbnail(url=user.picture)
    aliasesText = ""
    emotesText = ""
    rolesText = ""
    for game in games:
        game_name = game.name
        game_emote = get(ctx.guild.emojis, id=game.emote)
        game_role = get(ctx.guild.roles, id=game.role)
        aliasesText += "{}\n".format(game_name)
        emotesText += "{}\n".format(game_emote)
        rolesText += "{}\n".format(game_role.mention)
    embed.add_field(name="Alias", value=aliasesText, inline=True)
    embed.add_field(name="Emote", value=emotesText, inline=True)
    embed.add_field(name="Role", value=rolesText, inline=True)
    #await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def listme(ctx:commands.Context):
    user = User(ctx)
    games = gdb.pull_all(collection, user.server_id)
    aliasesText = ""
    emotesText = ""
    rolesText = ""
    for game in games:
        game_name = game.name
        game_emote = get(ctx.guild.emojis, id=game.emote)
        game_role = get(ctx.guild.roles, id=game.role)
        if game_role in user.roles:
            aliasesText += "{}\n".format(game_name)
            emotesText += "{}\n".format(game_emote)
            rolesText += "{}\n".format(game_role.mention)
    if len(rolesText) > 0:
        embed = discord.Embed(
            title = "{} requested a list of the games they play:".format(user.username),
            color = discord.Colour.red()
        )
        embed.add_field(name="Alias", value=aliasesText, inline=True)
        embed.add_field(name="Emote", value=emotesText, inline=True)
        embed.add_field(name="Role", value=rolesText, inline=True)
    else:
        embed = discord.Embed(
            title = "{}, you don\"t play any games!".format(user.username),
            color = discord.Colour.red()
        )
        message = "Use <!po list> to view games.\nUse <!po help> to get further help."
        embed.add_field(name="You can add games to your playlist with:\n<!po addrole gamename>", value=message, inline=True)
    embed.set_thumbnail(url=user.picture)
    #await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def abort(ctx:commands.Context):
    user = User(ctx)
    embed = discord.Embed(
        title = f"{user.username} is HUGE shithead and decided to abort their play request. " + \
                "Buckle up next time pussy, I'll let this one slide.",
        color = discord.Colour.red()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/165829330130305024/842761008484319232/download.jpg")
    if user.user_id in headcounts:
        try:
            await headcounts[user.user_id]["msg"].delete()
            await ctx.send(embed=embed)
        except:
            print("no message")
    
@goodbot.error
@help.error
@addgame.error
@deletegame.error
@addrole.error
@deleterole.error
@play.error
@list.error
@listme.error
async def unresolved_error(ctx:commands.Context, error):
    print("ERROR: message:{} server:{} author:{}".format(ctx.message.content, ctx.message.guild.id, ctx.message.author.id))
    print("ERROR:", error)
    embed = discord.Embed(
        title = "An unresolved error has occured. Make sure you have Administration rights to add/remove a game.",
        color = discord.Color.red()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/219037484531580929/764304895909298206/tenor.gif")
    embed.add_field(name="If you have other issues. You can contact me at:", value="Email: hoyfjeldsbildee@gmail.com\nInstagram: @kirbyydoge", inline=True)
    await ctx.send(embed=embed)

client.run(TOKEN)
