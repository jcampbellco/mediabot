from slackwrapper import SlackWrapper
from invoker import Invoker
from parser import Parser
from configparser import ConfigParser
from os.path import exists
from command import getip

# Get the config

if not exists('config.ini'):
    raise RuntimeError('`config.ini` file not found. Must exist next to `main.py`')

config = ConfigParser()
config.read('config.ini')

# Invoker

invoker = Invoker()

# Parser setup

parser = Parser()

# Slack settings

slack = SlackWrapper(config)

# Command creation/adding

parser.add_command(getip.GetIp(slack))

# Finally, start watching for new messages (pattern is a regex string for initial message filtering)

slack.watch(lambda message: parser.parse(message["text"]))
