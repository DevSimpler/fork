import disnake
from disnake.ext import commands

from utils.bot import OGIROID


class CogName(commands.Cog):
    def __init__(self, bot: OGIROID):
        self.bot = bot

    @commands.slash_command(description="stats about the commands that have been ran")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cmdstats(self, inter):
        cmdsran = self.bot.commands_ran
        sortdict = dict(sorted(cmdsran.items(), key=lambda x: x[1], reverse=True))
        value_iterator = iter(sortdict.values())
        key_iterator = iter(sortdict.keys())
        emby = disnake.Embed(title='edoC command Stats',
                             description=f'{self.bot.total_commands_ran} Commands ran this boot\n',
                             color=disnake.Color.random())
        emby.add_field(name='Top 10 commands ran', value=f'🥇: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n'
                                                         f'🥈: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n'
                                                         f'🥉: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n'
                                                         f'🏅: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n'
                                                         f'🏅: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n'
                                                         f'🏅: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n'
                                                         f'🏅: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n'
                                                         f'🏅: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n'
                                                         f'🏅: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n'
                                                         f'🏅: **/**{next(key_iterator)} ({next(value_iterator)} uses)\n')

        emby.set_author(name=inter.author.name, icon_url=inter.author.display_avatar.url)
        await inter.send(embed=emby)


def setup(bot):
    bot.add_cog(CogName(bot))
