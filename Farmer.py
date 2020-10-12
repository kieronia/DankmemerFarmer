from discord.ext import commands
import discord
from discord import Embed
import asyncio
import os
from colorama import Fore, init
init(convert=True)
begtime = int(46)

#if you have dank memer premium your time is 25, make it 26 if u wanna, else itll be 45, I like to be just after so I do 46 :)


token = "abc.def.gtokenhereeeeeeeeeeeee"
prefix = "!"
client = commands.Bot(prefix, self_bot=True)
client.remove_command("help")
count = int(0)
os.system("mode 75,40")
os.system("title Auto Begger For Dank Memer, Type !beg")
while True:
    try:
        @client.event
        async def on_connect():
            print(f"""{Fore.GREEN}
                __________████████_____██████
                _________█░░░░░░░░██_██░░░░░░█
                ________█░░░░░░░░░░░█░░░░░░░░░█
                _______█░░░░░░░███░░░█░░░░░░░░░█
                _______█░░░░███░░░███░█░░░████░█
                ______█░░░██░░░░░░░░███░██░░░░██
                _____█░░░░░░░░░░░░░░░░░█░░░░░░░░███
                ____█░░░░░░░░░░░░░██████░░░░░████░░█
                ____█░░░░░░░░░█████░░░████░░██░░██░░█
                ___██░░░░░░░███░░░░░░░░░░█░░░░░░░░███
                __█░░░░░░░░░░░░░░█████████░░█████████
                _█░░░░░░░░░░█████_████___████_█████___█
                _█░░░░░░░░░░█______█_███__█_____███_█___█
                █░░░░░░░░░░░░█___████_████____██_██████
                ░░░░░░░░░░░░░█████████░░░████████░░░█
                ░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█
                ░░░░░░░░░░░░░░░░░░░░██░░░░█░░░░░░██
                ░░░░░░░░░░░░░░░░░░██░░░░░░░███████
                ░░░░░░░░░░░░░░░░██░░░░░░░░░░█░░░░░█
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
                ░░░░░░░░░░░█████████░░░░░░░░░░░░░░██
                ░░░░░░░░░░█▒▒▒▒▒▒▒▒███████████████▒▒█
                ░░░░░░░░░█▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
                ░░░░░░░░░█▒▒▒▒▒▒▒▒▒█████████████████
                ░░░░░░░░░░████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
                ░░░░░░░░░░░░░░░░░░██████████████████
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
                ██░░░░░░░░░░░░░░░░░░░░░░░░░░░██
                ▓██░░░░░░░░░░░░░░░░░░░░░░░░██
                ▓▓▓███░░░░░░░░░░░░░░░░░░░░█
                ▓▓▓▓▓▓███░░░░░░░░░░░░░░░██
                ▓▓▓▓▓▓▓▓▓███████████████▓▓█
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█    

        {Fore.RED}={Fore.WHITE}={Fore.RED}={Fore.WHITE}={Fore.RED}={Fore.WHITE} Dank memer farmer on ={Fore.RED}={Fore.WHITE}={Fore.RED}={Fore.WHITE}={Fore.GREEN}{client.user.name}{Fore.RED}={Fore.WHITE}={Fore.RED}={Fore.WHITE}={Fore.RED}=
            """)




        #might do on message stuff to work with pls work and pls search commands, could even make it use random choices and do slots and blackjack but I wanna see this get a tiny bit of attention first xd


        @client.command()
        async def begoff(ctx):
            global messagefarm
            await ctx.message.delete()
            print(f"{Fore.RED}[{Fore.WHITE}-{Fore.RED}] {Fore.CYAN}Auto begging off!")
            await ctx.send("`Dank memer farmer is now off!`")
            messagefarm="no"



        @client.command()
        async def beg(ctx):
            global count
            global messagefarm 
            messagefarm = "yes"
            print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.CYAN} Auto begging on!")
            await ctx.message.delete()
            while messagefarm=="yes":
                await ctx.send("pls beg")
                print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.CYAN} Sent 'pls beg'")
                count = count + 1
                os.system(f"title Begs Done : [{count}]")
                await asyncio.sleep(begtime)
                

        client.run(token, bot=False)
    except:
        pass
