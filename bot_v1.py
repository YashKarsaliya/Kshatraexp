import discord, asyncio
import time
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from datetime import datetime
from typing import Optional
from discord.ext import commands, tasks
from discord import Embed, Member
import requests
import json
import random
import aiohttp

bot1_id = "OTQ3NDgxODQ4NTY3NzI2MTAx.Yht5PA.3zzQVqGG6Sql2UZh0F8ab5nFJwI"


bot = commands.Bot(command_prefix='$')

channel1_id = 947153745526013963
#channel2_id = 946715452678225960


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def get_news():
    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=769460c57bcf43598eb1363916731f7c')
    data = json.loads(r.content)
    i = random.randrange(20)
    a = data['articles'][i]['title']
    b = data['articles'][i]['url']
    return (f'{a} \n {b}')





@tasks.loop(seconds=3)
async def auto_msg():
    channel1 = bot.get_channel(channel1_id)
    # channel2 = bot.get_channel(channel2_id)
    auto_response = ["Hello...", "Anyone Is Here ?!", "Where Are Everyone??", "Hello Everyone.. I Am Here.."]
    message = random.choice(auto_response)
    await channel1.send(message)
    # await channel2.send("test")
    print("sending auto message success.../")


@bot.event
async def on_connect():
    print("Connection Established!!!......")


@bot.event
async def on_ready():
    print("Bot is started......////")
    # await asyncio.sleep(3)
    # channel1 = bot.get_channel(channel1_id)
    # await channel1.send("Auto Message Started.....//")
    # auto_msg.start()

    # await asyncio.sleep(10)
    # test.cancel()
    # print("quit...")
    # time.sleep(10)
    # print("after 10 second")


# @bot.event
# async def on_typing(channel, user, when):
#     print("User Typing...", channel, user)




@bot.listen()
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)

    quote = ["send quote", "give quote", "quote", "send me quote"]

    greeting = ["hello", "hi", "hola", "namaste", "hii", "hi bot", "hey", "hi"]
    greeting_reply = ["hello..", "oh! Hey.."]

    unknown = ["who are you", "who is this", "who"]
    bot_reply = ["I am here to assist you", "i am bot", "I am Your Friend"]

    ask_time = ["time", "What is time", "current time"]

    tutorial = ["python tutorial", "python playlist", "python"]
    tutorial_response = ['https://www.youtube.com/watch?v=hEgO047GxaQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3',
                         'https://youtu.be/gfDE2a7MKjA',
                         'https://www.tutorialspoint.com/python/index.htm',
                         'https://www.w3schools.com/python/']

    bad_words = ["bad", "stop", "45", "basterd", "mental"]

    if user_message.lower() in quote:
        new_quote = get_quote()
        await message.channel.send(new_quote)

    elif user_message.lower() in greeting:
        r = random.choice(greeting_reply)
        await message.channel.send(f'{r} {username}')

    elif user_message.lower() in unknown:
        new_r = random.choice(bot_reply)
        await message.channel.send(f'{new_r} {username}')

    elif user_message.lower() in ask_time:
        time = datetime.now().strftime("%H:%M")
        await message.channel.send(time)


    elif user_message.lower() in tutorial:
        response = random.choice(tutorial_response)
        await message.channel.send(response)

    for word in bad_words:
        if word in user_message.lower():
            await message.channel.send(f"WARNING!!! {username} , PLEASE DO NOT USE THIS TYPE OF WORDS")
            await asyncio.sleep(2)
            await message.channel.purge(limit=1)

    # else:
    #     await message.channel.send(f'sorry! i do not understand {username}')




# @bot.event
# async def on_message(message):
#     username = str(message.author).split("#")[0]
#     user_message = str(message.content)
#     channel = str(message.channel.name)
#
#     print(f"{username}: {user_message} ({channel})")
#     # print(message.author, bot.user)
#     if message.author == bot.user:
#         return
#     if message.channel.name == 'test_channel_2':
#         greeting = ['hello', 'hi', 'hey']
#         if user_message.lower() in greeting:
#             await message.channel.send(f"hello....{username}")





# Delete Multiple Message from last
@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)



news_word = ["news", "latest_news", "give_news", "news_today"]
@bot.command(aliases=news_word)
async def news_invoke(ctx):
    headline = get_news()
    await ctx.send(headline)



@bot.command()
async def fact(ctx):

    start = "Did you know that "
    facts = ["Banging your head against a wall for one hour burns 150 calories.",
             "Snakes can help predict earthquakes.",
             "7% of American adults believe that chocolate milk comes from brown cows.",
             "If you lift a kangaroo’s tail off the ground it can’t hop.",
             "Bananas are curved because they grow towards the sun.",
             "Billy goats urinate on their own heads to smell more attractive to females.",
             "The inventor of the Frisbee was cremated and made into a Frisbee after he died.",
             "During your lifetime, you will produce enough saliva to fill two swimming pools.",
             "Polar bears could eat as many as 86 penguins in a single sitting…",
             "Heart attacks are more likely to happen on a Monday.",
             "In 2017 more people were killed from injuries caused by taking a selfie than by shark attacks.",
             "A lion’s roar can be heard from 5 miles away.",
             "The United States Navy has started using Xbox controllers for their periscopes.",
             "A sheep, a duck and a rooster were the first passengers in a hot air balloon.",
             "The average male gets bored of a shopping trip after 26 minutes.",
             "Recycling one glass jar saves enough energy to watch television for 3 hours.",
             "Approximately 10-20% of U.S. power outages are caused by squirrels."
            ]
    fact_file = open("facts.txt", mode="r", encoding="utf8")
    fact_file_facts = fact_file.read().split("\n")
    fact_file.close()

    for i in fact_file_facts:
        if i == "": fact_file_facts.remove(i)
    facts = facts + fact_file_facts

    await ctx.send(start + random.choice(facts).lower())






@bot.command(pass_context = True)
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)









@bot.command()
@commands.has_permissions(manage_channels=True, administrator=True)
async def delete_channels(ctx, channel_name, *, exceptions='None'):
    deleted_channels = 0
    if exceptions == 'None':
        guild = bot.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            is_exception = False
            if channel.name == channel_name:
                await channel.delete()
                deleted_channels += 1
        if deleted_channels == 0:
            await ctx.send("Couldn't find any channels with that name")
        else:
            try:
                await ctx.send(f'Found and deleted {deleted_channels} channels')
            except Exception:  # If the channel you typed the message is deleted some errors occure
                pass
    else:
        exceptions_cont = exceptions.split(', ')
        guild = bot.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            is_exception = False
            if channel.name == channel_name:

                for exception in exceptions_cont:
                    if int(channel.id) == int(exception):
                        is_exception = True

                if is_exception:
                    pass
                else:
                    await channel.delete()
                    deleted_channels += 1

        if deleted_channels == 0:
            await ctx.send("Couldn't find any channels with that name")
        else:
            try:
                await ctx.send(f'Found and deleted {deleted_channels} channels')
            except Exception:  # If the channel you typed the message is deleted some errors occure
                pass



api_key = "8fd04d46f365fac1a32278f02274bb65"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
@bot.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                                  color=ctx.guild.me.top_role.color,
                                  timestamp=ctx.message.created_at, )
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await channel.send(embed=embed)
    else:
            await channel.send("City not found.")





@bot.command(pass_context=True)
async def meme(ctx):
    '''
    Posts a Meme from r/memes
    '''
    embed = discord.Embed(title="From r/memes")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            async with ctx.channel.typing():
              await asyncio.sleep(2)
            await ctx.send(embed=embed)




@bot.command(name="info_all", aliases=["memberinfo", "ui", "mi", 'userinfo'])
async def user_info(ctx, target: Optional[Member]):
    target = target or ctx.author

    embed = Embed(title="User information",
                  colour=target.colour,
                  timestamp=datetime.utcnow())

    embed.set_thumbnail(url=target.avatar_url)

    fields = [("Name", str(target), True),
              ("ID", target.id, True),
              ("Bot?", target.bot, True),
              ("Top role", target.top_role.mention, True),
              ("Status", str(target.status).title(), True),
              ("Activity",
               f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}",
               True),
              ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
              ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
              ("Boosted", bool(target.premium_since), True)]

    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)

    await ctx.send(embed=embed)




@bot.command(name="slap", aliases=["hit"], help = "Ever felt the need to a the person through the phone?")
async def slap_member(ctx, member: Member, *, reason: Optional[str] = "for no reason lol"):
    await ctx.send(f"{ctx.author.display_name} slapped {member.mention} {reason}!")

@slap_member.error
async def slap_member_error(self, ctx, exc):
    if isinstance(exc, BadArgument):
        await ctx.send("I can't find that member.")





@bot.command(aliases=['corona', 'stats'],
                  help='This command gives you CoViD-19 details of India \n\n(Default is set to Nagpur Maharashtra)\n\nType "all <--state-->"  for total stats of a particular state.',
                  brief='CoVid-19 stats')
async def covid(ctx, district="Nagpur", *, state="Maharashtra"):
    district = district.capitalize()
    state = state.title()

    if str(district) == "All":
        try:
            res = requests.get(
                url="https://api.covid19india.org/state_district_wise.json"
            )
            res = res.json()
            flag = state.title()
            confirm, deceased, recovered, delcon, deldec, delrec = 0, 0, 0, 0, 0, 0
            for i in res[flag]["districtData"]:
                confirm = confirm + \
                          res[flag]["districtData"][i]["confirmed"]
                deceased = deceased + \
                           res[flag]["districtData"][i]["deceased"]
                recovered = recovered + \
                            res[flag]["districtData"][i]["recovered"]
                delrec = delrec + \
                         res[flag]["districtData"][i]["delta"]["recovered"]
                delcon = delcon + \
                         res[flag]["districtData"][i]["delta"]["confirmed"]
                deldec = deldec + \
                         res[flag]["districtData"][i]["delta"]["deceased"]

            await ctx.send(f"Hello {ctx.author.mention}, this command gives you CoViD-19 details of India")
            await ctx.send(
                "**`" + flag + "`**\n\n:red_circle: `confirmed: " +
                str(confirm) + "` :red_circle:\n:muscle: `recovered: " +
                str(recovered) + "` :muscle:\n:blossom: `deceased: " +
                str(deceased) +
                "` :blossom:\n\n`Daily change:` \n\n:red_circle: `confirmed: "
                + (str(delcon) if delcon != 0 else "Not updated yet") +
                "`" + ":red_circle:\n:muscle: `recovered: " +
                (str(delrec) if delrec != 0 else "Not updated yet") + "`" +
                ":muscle:\n:blossom: `deceased: " +
                (str(deldec) if deldec != 0 else "Not updated yet") +
                "`:blossom:")
        except:
            await ctx.send("Please enter the state name correctly")

    else:

        try:
            res = requests.get(
                url="https://api.covid19india.org/state_district_wise.json"
            )
            res = res.json()
            confirm = res[state]["districtData"][district]["delta"][
                "confirmed"]
            deceased = res[state]["districtData"][district]["delta"][
                "deceased"]
            recovered = res[state]["districtData"][district]["delta"][
                "recovered"]

            await ctx.send(
                f"**`Corona stats in {district}`**\n\n:red_circle: `confirmed: "
                + (
                    str(confirm) if confirm != 0 else "Not updated yet") + "`" + " :red_circle:\n:muscle: `recovered: " +
                (
                    str(recovered) if recovered != 0 else "Not updated yet") + "`" + " :muscle:\n:blossom: `deceased: " +
                (str(deceased) if deceased != 0 else "Not updated yet") + "`" + " :blossom:\n\n")

            if str(confirm) == str(recovered) == str(deceased) == "0":
                await asyncio.sleep(1)
                await ctx.send("oopssss!!!")


        except:
            await ctx.send("Please enter the city name correctly")






@bot.command(name="anime")
async def anime(ctx, *, arg):
    argument = str(arg)
    results = requests.get(f"https://api.jikan.moe/v3/search/anime?q={argument}&limit=1")
    for i in results.json()["results"]:
      embed=discord.Embed(title=f'{i["title"]}', url=f'{i["url"]}', description=f'{i["synopsis"]}\n\n**Rating: ** {i["score"]}\n**Episodes:** {i["episodes"]}', color=0x5800db)
      embed.set_image(url=f'{i["image_url"]}')
      await ctx.send(embed=embed)


bot.run(bot1_id)
