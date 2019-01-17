from slackclient import SlackClient
from configparser import ConfigParser
import time
import re


class SlackWrapper(object):
    slackclient = None
    channel     = None
    bot         = None

    def __init__(self, settings: ConfigParser):
        self.slackclient = SlackClient(settings.get('Slack', 'token'))

        response = self.slackclient.api_call('channels.list')

        if not response["ok"] or not response["channels"]:
            raise RuntimeError("Unable to request channel list")

        channellist = []

        for channel in response["channels"]:
            channellist.append(channel["name"])
            if channel["name"] == settings.get('Slack', 'channel'):
                print(F"Found channel `{channel['name']}` with ID ")
                self.channel = channel
                break

        if self.channel is None:
            raise RuntimeError(
                F"Could not find channel `{settings.get('Slack', 'channel')}` in channel list `{', '.join(channellist)}"
            )

        self.slackclient.api_call(
            'channels.join',
            channel=self.channel['id']
        )

        self.slackclient.api_call(
            'chat.postMessage',
            channel=self.channel["id"],
            text="Connected!"
        )

        self.bot = self.slackclient.api_call('auth.test')  # Store the bot user

    def watch(self, onmessage):
        if self.slackclient.rtm_connect():
            p = re.compile(F'<@{self.bot["user_id"]}>')
            while self.slackclient.server.connected is True:
                sleep = 1
                messages = self.slackclient.rtm_read()

                for message in messages:

                    print(message)

                    if message and message["type"] and message["type"] == 'message' and p.match(message["text"]):
                        print('Message matched!')
                        onmessage(message)

                    time.sleep(sleep)
        else:
            print("Connection unsuccessful")

        print("Connection terminated")

    def setchannel(self, channelid):
        self.channelid = channelid

    def sendmessage(self, message):
        self.slackclient.api_call(
            'chat.postMessage',
            channel=self.channelid,
            text=message
        )
