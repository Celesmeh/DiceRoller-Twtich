from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='jzhbx6n3ube8fp33o1txvxdcjnkvdg', client_id='j1jnt9v9s4fmvl05v9gqamuf2si5p8', nick='thedicegodssay', prefix='!',
                         initial_channels=['celesmeh'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()
