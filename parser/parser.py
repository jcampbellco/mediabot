from command import Command


class Parser(object):
    available_commands = []

    def add_command(self, command: Command):
        self.available_commands.append(command)

    def parse(self, message):
        print(message)
