@client.command()
async def clear(ctx, user: discord.User, count: int):
   tmp = []
   if count > 50:
      maxDel = "The clear limit is 50 messages."
      e = discord.Embed()
      e.add_field(name="Clear limit.", value=maxDel, inline=False)
      await ctx.send(embed=e)
      return
   async for message in ctx.channel.history(limit=500):
      _user = message.author
      if _user == user:
         tmp.append(message)
   for delete in range(count+1):
      await tmp.pop(0).delete()
