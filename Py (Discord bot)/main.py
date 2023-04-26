import nextcord
from nextcord.ext import commands
from nextcord import Member
from nextcord.ext.commands import has_permissions , MissingPermissions
from config import *
import random

#---------------------------------------------------------------------------------------ESSENTIALS START

intents = nextcord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix= "!", intents= intents)


@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.invisible , activity=nextcord.Activity(type = nextcord.ActivityType.watching, name=(BotStatus)))
    chars="abcdefghijklmnopqlstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*=+"
    length=40
    passw = ""
    for a in range(length):
        passw+=random.choice(chars)
    print(f"Bot is Opperational and logged in form bot acoount ====> [{client.user}]")
    print(diaxoristiko)
    print(passw)
#---------------------------------------------------------------------------------------ESSENTIALS END

#---------------------------------------------------------------------------------------FUN START
@client.command()
async def status(ctx,self):
    await ctx.send("Bot Status : 🟢")


@client.command()
async def wipedata(ctx):
    wipebed = nextcord.Embed(title="Initiating Data wipe from list\n", description=f"The data assosiated with the following nubers have been wiped from the list \n+306944431032 \n+306907687717\n+306989462217\n+306945443626\n\nStatus: Sucsess🟢 all data in assosiation with theese phone numbers have been wiped from the astropedia.gr database\n\n\n This opparation has been compleated usint the data purge tool provided with the Decryptor pack made by Gvol & Hush Inc." ,color=0x000000)
    await ctx.send(embed = wipebed)
#---------------------------------------------------------------------------------------FUN END
#---------------------------------------------------------------------------------------ADMIN START
@client.command()
@has_permissions(kick_members = True)
async def kick(self,ctx, Member: nextcord.Member = None, *, kickreason=None):  
    await Member.kick(reason= kickreason)
    if (kickreason == None):
        await ctx.send(f"<@{Member.id}> has been kicked from the server")
        KickLogTrigger(ctx=ctx,Member=Member,kickreason="Not Given")
    else:
        await ctx.send(f"<@{Member.id}> has been kicked from the server with Reason ===> [{kickreason}]" )
        await KickLogTrigger(ctx=ctx,Member=Member,kickreason=kickreason)



@client.command()
@has_permissions(ban_members = True)
async def ban(self,ctx, Member: nextcord.Member = None, *, banreason=None):  
    await Member.ban(reason= banreason)
    if (banreason == None):
        await ctx.send(f"<@{Member.id}> has been baned from the server" )
        BanLogTrigger(ctx=ctx,Member=Member,kickreason="Not Given")
    else:
        await ctx.send(f"<@{Member.id}> has been baned from the server with Reason ===> [{banreason}]" )

@client.command()
async def say(self,ctx, msg ,mention=None):
    saybed = nextcord.Embed(title=embsigniture, description=msg, color=0x000000)
    await ctx.send(embed=saybed)
    if mention!=None:
       await ctx.send(f"||{mention}||")


@client.command()
@has_permissions(administrator=True)
async def sos(self,ctx, msg):
    user = await client.fetch_user(831803232014958642)
    sosbed = nextcord.Embed(title="❗❗❗SOS❗❗❗", description=msg, color=0x000000)
    await user.send(embed=sosbed)
    await user.send(f"||<@831803232014958642>||")


#---------------------------------------------------------------------------------------ADMIN END
#---------------------------------------------------------------------------------------ERROR START
@client.event
async def on_command_error(ctx, error,self):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send("You don't have permission to do that" )
#---------------------------------------------------------------------------------------ERROR END
#---------------------------------------------------------------------------------------events start
@client.event
async def on_member_join(self,Member):
    WelcomeChanel= client.get_channel(WelcomeChannelId)
    WelcomeBed = nextcord.Embed(title="🙋‍♂️Welcome", description=(f"Welcome <@{Member.id}> to the server"), color=0x26fc4a)
    WelcomeBed.set_footer(text=embsigniture)
    await WelcomeChanel.send(embed=WelcomeBed)

@client.event
async def on_member_remove(self,Member):
    WelcomeChanel= client.get_channel(LeaveChannelId)
    LeaveBed = nextcord.Embed(title="👋Bye", description=(f"Bye <@{Member.id}>"), color=0xb30909)
    LeaveBed.set_footer(text=embsigniture)
    await WelcomeChanel.send(embed=LeaveBed)
#---------------------------------------------------------------------------------------events end
#---------------------------------------------------------------------------------------Logs start

@client.event
async def on_member_join(Member,self):
    WelcomeLogBed = nextcord.Embed(title="➕Join Logs", description=(f"<@{Member.id}> has Joined the server"), color=0x26fc4a)
    WelcomeLogBed.set_footer(text=embsigniture)
    JoinLeaveLogsChannel = client.get_channel(JoinLeaveLogsChannelID)
    await JoinLeaveLogsChannel.send(embed=WelcomeLogBed)

@client.event
async def on_member_remove(Member,self):
    LeaveLogBed = nextcord.Embed(title="➖Leave Logs", description=(f"<@{Member.id}> has Left the server"), color=0xb30909)
    LeaveLogBed.set_footer(text=embsigniture)
    JoinLeaveLogsChannel = client.get_channel(JoinLeaveLogsChannelID)
    await JoinLeaveLogsChannel.send(embed=LeaveLogBed)

async def KickLogTrigger(ctx, Member: nextcord.Member = None, *, kickreason=None,self):
    KickLogBed = nextcord.Embed(title="👢Kick Logs", description=(f"<@{Member.id}> has been Kicked From the server"), color=0xb30909)
    KickLogBed.add_field(name ="Responsible Modarator", value=f"<@{ctx.author.id}>")
    KickLogBed.add_field(name ="Reason", value=f"{kickreason}" , inline= False)
    KickBanLogsChannel = client.get_channel(KickBanLogsChannelID)
    await KickBanLogsChannel.send(embed=KickLogBed)

async def BanLogTrigger(ctx, Member: nextcord.Member = None, *, banreason=None,self):
    BanLogBed = nextcord.Embed(title="📛Ban Logs", description=(f"<@{Member.id}> has been Banned From the server"), color=0xb30909)
    BanLogBed.add_field(name ="Responsible Modarator", value=f"<@{ctx.author.id}>")
    BanLogBed.add_field(name ="Reason", value=f"{banreason}" , inline= False)
    BanLogBed.set_footer(text=embsigniture)
    KickBanLogsChannel = client.get_channel(KickBanLogsChannelID)
    await KickBanLogsChannel.send(embed=BanLogBed)

#---------------------------------------------------------------------------------------LOGS end



client.run(token)