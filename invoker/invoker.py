import command


class Invoker(object):
    commands = []

    def add_command(self, command: command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()
