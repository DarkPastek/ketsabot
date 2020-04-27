import json

# importer le module discord.py
import discord

from discord.utils import get

# ajouter un composant de discord.py
from discord.ext import commands

# créer le bot
bot = commands.Bot(command_prefix='=')

# détecter quand le bot est pret ("allmué")
@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.idle,
        activity = discord.Game("développer avec Ketsap"))



# détecter quand quelqu'un ajoute un emoji sur un message
@bot.event
async def on_raw_reaction_add(payload):

    emoji = payload.emoji.name # recupere l'emoji
    canal = payload.channel_id # recupere le numero du canal
    message = payload.message_id # recupere le numero du message
    membre_role = get(bot.get_guild(payload.guild_id).roles, name="Membre")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)
    nom = membre.mention
    russe_role = get(bot.get_guild(payload.guild_id).roles, name="Russe")
    espagnol_role = get(bot.get_guild(payload.guild_id).roles, name="Espagnol")
    anniv_role = get(bot.get_guild(payload.guild_id).roles, name="ANNIV")

    booster_role = get(bot.get_guild(payload.guild_id).roles, name="Booster")
    ps4_role = get(bot.get_guild(payload.guild_id).roles, name="PS4")
    xbox_role = get(bot.get_guild(payload.guild_id).roles, name="XBOX")
    mobile_role = get(bot.get_guild(payload.guild_id).roles, name="MOBILE")
    pc_role = get(bot.get_guild(payload.guild_id).roles, name="PC")
    switch_role = get(bot.get_guild(payload.guild_id).roles, name="SWITCH")
    manette_role = get(bot.get_guild(payload.guild_id).roles, name="MANETTE")
    cs_role = get(bot.get_guild(payload.guild_id).roles, name="C/S")
    mc_role = get(bot.get_guild(payload.guild_id).roles, name="Minecraftien")
    fibre_role = get(bot.get_guild(payload.guild_id).roles, name="Fibré btw")
    dresseur_role = get(bot.get_guild(payload.guild_id).roles, name="Dresseur")

    # verifier l'emoji qu'on a ajouté
    if canal == 589165009637081107 and message == 701045522001035274 and emoji == "🆗":
        await membre.add_roles(membre_role)
    elif canal == 595648544426295315 and message == 701047837365895169:
        if emoji == "boost":
            await membre.add_roles(booster_role)
        elif emoji == "ps4":
            await membre.add_roles(ps4_role)
        elif emoji == "xbox":
            await membre.add_roles(xbox_role)
        elif emoji == "mobile":
            await membre.add_roles(mobile_role)
        elif emoji == "pc":
            await membre.add_roles(pc_role)
        elif emoji == "switch":
            await membre.add_roles(switch_role)
        elif emoji == "manette":
            await membre.add_roles(manette_role)
        elif emoji == "claviersouris":
            await membre.add_roles(cs_role)
        elif emoji == "minecraft":
            await membre.add_roles(mc_role)
        elif emoji == "🔌":
            await membre.add_roles(fibre_role)
        elif emoji == "pokemon":
            await membre.add_roles(dresseur_role)
    elif canal == 701723490348433560 and message == 704062935437410455:
        if emoji == "🇷🇺":
            await membre.add_roles(russe_role)
        elif emoji == "🇪🇸":
            await membre.add_roles(espagnol_role)
        elif emoji == "🎂":
            await membre.add_roles(anniv_role)
            channel = bot.get_channel(689781152524795988)
            await channel.send(f"@here Aujourd'hui c'est (normalement) l'anniversaire de {nom} !")


# détecter quand quelqu'un retire un emoji sur un message
@bot.event
async def on_raw_reaction_remove(payload):

    emoji = payload.emoji.name # recupere l'emoji
    canal = payload.channel_id # recupere le numero du canal
    message = payload.message_id # recupere le numero du message
    membre_role = get(bot.get_guild(payload.guild_id).roles, name="Membre")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)
    russe_role = get(bot.get_guild(payload.guild_id).roles, name="Russe")
    espagnol_role = get(bot.get_guild(payload.guild_id).roles, name="Espagnol")
    anniv_role = get(bot.get_guild(payload.guild_id).roles, name="ANNIV")

    booster_role = get(bot.get_guild(payload.guild_id).roles, name="Booster")
    ps4_role = get(bot.get_guild(payload.guild_id).roles, name="PS4")
    xbox_role = get(bot.get_guild(payload.guild_id).roles, name="XBOX")
    mobile_role = get(bot.get_guild(payload.guild_id).roles, name="MOBILE")
    pc_role = get(bot.get_guild(payload.guild_id).roles, name="PC")
    switch_role = get(bot.get_guild(payload.guild_id).roles, name="SWITCH")
    manette_role = get(bot.get_guild(payload.guild_id).roles, name="MANETTE")
    cs_role = get(bot.get_guild(payload.guild_id).roles, name="C/S")
    mc_role = get(bot.get_guild(payload.guild_id).roles, name="Minecraftien")
    fibre_role = get(bot.get_guild(payload.guild_id).roles, name="Fibré btw")
    dresseur_role = get(bot.get_guild(payload.guild_id).roles, name="Dresseur")

    # verifier l'emoji qu'on a ajouté
    if canal == 589165009637081107 and message == 701045522001035274 and emoji == "🆗":
        await membre.remove_roles(membre_role)
    elif canal == 595648544426295315 and message == 701047837365895169:
        if emoji == "boost":
            await membre.remove_roles(booster_role)
        elif emoji == "ps4":
            await membre.remove_roles(ps4_role)
        elif emoji == "xbox":
            await membre.remove_roles(xbox_role)
        elif emoji == "mobile":
            await membre.remove_roles(mobile_role)
        elif emoji == "pc":
            await membre.remove_roles(pc_role)
        elif emoji == "switch":
            await membre.remove_roles(switch_role)
        elif emoji == "manette":
            await membre.remove_roles(manette_role)
        elif emoji == "claviersouris":
            await membre.remove_roles(cs_role)
        elif emoji == "minecraft":
            await membre.remove_roles(mc_role)
        elif emoji == "🔌":
            await membre.remove_roles(fibre_role)
        elif emoji == "pokemon":
            await membre.remove_roles(dresseur_role)
    elif canal == 701723490348433560 and message == 704062935437410455:
        if emoji == "🇷🇺":
            await membre.remove_roles(russe_role)
        elif emoji == "🇪🇸":
            await membre.remove_roles(espagnol_role)
        elif emoji == "🎂":
            await membre.remove_roles(anniv_role)



# créer la commande =regles
@bot.command()
async def regles(ctx):
    await ctx.send("Les règles se trouvent normalement dans le channel tout en haut.")

# créer la commande =bienvenue
@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    # recupere le nom
    pseudo = nouveau_membre.mention

    # executer le message de bienvenue
    await ctx.send(f"Bienvenue à {pseudo} sur le serveur discord !")

# commande =reveiller
@bot.command()
async def reveiller(ctx, membre: discord.Member):
    pseudo = membre.mention
    nom = membre.display_name
    nom2 = ctx.message.author.display_name
    await membre.send(f"Il faut te réveiller {pseudo}")
    await membre.send(f"(de la part de {nom2}).")
    await ctx.send(f"{nom} a été réveillé !")

# commande pour nettoyer un channel =clear
@bot.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx):
    await ctx.channel.purge()
    await ctx.send("Channel nettoyé.")

# verifier les erreurs de commandes
@clear.error
@bienvenue.error
@reveiller.error
async def on_command_error(ctx, error):
    # detecter cet erreur
    if isinstance(error, commands.MissingRequiredArgument):
        # envoyer un message
        await ctx.send("Erreur : =command @pseudo")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Erreur : tu n'as pas la permission.")

# commande =ping
@bot.command()
async def ping(ctx):
    # latence = round(bot.latency,1)
    await ctx.send(f"Pong {round(bot.latency * 1000)}ms !")


# phrase
print("Lancement du bot...")


# connecter au serveur
bot.run(process.env.TOKEN)
