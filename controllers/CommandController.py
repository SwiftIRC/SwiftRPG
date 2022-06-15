import commands.ChopCommand as command_chop
import commands.thieving.PickpocketCommand as command_pickpocket
class CommandController:
    commands = None
    auth = None
    command = None
    target = None
    author = None
    message = None
    character = None
    token = None

    def __init__(self, game):
        self.game = game
        self.commands = {
            "chop": command_chop.exec,
            "pickpocket": command_pickpocket.exec
        }


    async def run(self, command, target, author, message, character, token):
        split = self.message.split()
        command_string = split[0][1:]

        if command_string in self.commands:
            await self.game.process_response(command, target, await self.commands[command_string](self.game, command, target, author, message, character, token))
        else:
            await self.game.process_response(command, target, "Error: command not found")