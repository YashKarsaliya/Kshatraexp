import discord
from discord.ext import tasks, commands
import ctx
from discord import Embed

TOKEN = 'OTQ3NDgxODQ4NTY3NzI2MTAx.Yht5PA.3zzQVqGG6Sql2UZh0F8ab5nFJwI'

# client = discord.Client()
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('we have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    user_content = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == bot.user:
        return

    if message.channel.name == 'test-1':
        ls1 = ["hello", "hi", "hola", "namaste", "hii", "hi bot"]
        ls2 = ["how are you", "how's going"]
        ls4 = ["bye", "good bye"]
        ls5 = ["What are the HR rules", "hr policy", "Tell me about HR policy", "rules", "what are the rules"]
        rules = """ 1. 18 Leaves Per Year And 1.5 Per Month.
        2. Weekly 5 Days Working
        3. Unused Leave Will Be Adding To Next Month But Not Year
        4. Employee Have To Inform At least 10 Days Before (For 1 Leave) and
            15 Days Before (More Than 1 Day).
        5. If Employee Come Late After 9:50 Continue 3 Days Than it Will Count as Half Day.
        6. You Can't Use Company's Device For Your Personal Work.
        7. You Will Be Responsible For Device Damage, Lost or Stolen."""

        if user_message.lower() in ls1:
            await message.channel.send(f'hello {username}')

        elif user_message.lower() in ls2:
            await message.channel.send(f'Fine')

        elif user_message.lower in ls4:
            await message.channel.send(f'have a nice day {username}')

        elif user_message.lower() in ls5:
            await message.channel.send(rules)



        elif user_message.lower() == 'timing':
            embed = discord.Embed(title="Office Time", colour=0x552E12)
            embed.add_field(name='Arrive', value='9:30 AM', inline=True)
            embed.add_field(name='Leave', value='7:00 PM', inline=True)
            embed.add_field(name='Lunch break', value="45 minutes", inline=False)
            embed.add_field(name='Morning break', value='15 minutes', inline=True)
            embed.add_field(name='Evening break', value='15 minutes', inline=True)
            embed.set_footer(text='\u200b', icon_url="https://i.imgur.com/uZIlRnK.png")
            await message.channel.send(embed=embed)


rules = """ 1. 18 Leaves Per Year And 1.5 Per Month.
        2. Weekly 5 Days Working
        3. Unused Leave Will Be Adding To Next Month But Not Year
        4. Employee Have To Inform At least 10 Days Before (For 1 Leave) and
            15 Days Before (More Than 1 Day).
        5. If Employee Come Late After 9:50 Continue 3 Days Than it Will Count as Half Day.
        6. You Can't Use Company's Device For Your Personal Work.
        7. You Will Be Responsible For Device Damage, Lost or Stolen."""


@bot.command(pass_context=True)
async def rules(ctx):
    await ctx.send(rules)

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


bot.run(TOKEN)
