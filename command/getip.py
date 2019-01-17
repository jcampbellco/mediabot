from .command import Command
from .action import get_ip


class GetIp(Command):
    def execute(self):
        self.slack.sendmessage(F'My external IP is {get_ip()}')
