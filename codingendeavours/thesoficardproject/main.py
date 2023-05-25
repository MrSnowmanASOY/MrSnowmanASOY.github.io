import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is botting...')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('scdw:sendmessage'):
        channel = message.channel
        await channel.send('You have triggered the Sofi Card Display Website.')

# Make the bot send an image through URL form on command

    if message.content.startswith('scdw:sendimage'):  # Command to send image
        channel = message.channel
        await channel.send('Here is an image:')
#       await channel.send(file=discord.File('image.png'))  # Send a direct image link
        image_url = 'https://example.com/image.png'  # Url for image goes here 
        await channel.send(image_url)

client.run('MTA5NDUzMjIyMTEzNTc2MTQ0OA.GtEQe4.ogSCE2FtB1PBfvazgsRTzdNJnmEwAw3YAgpwzY')
