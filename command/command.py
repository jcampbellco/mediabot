from slackwrapper import SlackWrapper


class Command(object):
    """
    We hand the SlackWrapper to the commands since they're the ones directly interacting with the Slack instance.
    The abstraction of the wrapper should keep it kinda tidy
    """
    slack = None

    def __init__(self, slack: SlackWrapper):
        self.slack = slack

    def execute(self):
        pass
