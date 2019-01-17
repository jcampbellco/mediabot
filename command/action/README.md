##Actions

Actions represent a way to decouple commands from the actual actions they perform.

In the case of a really simple command, maybe like fetching the system time, we could just throw the logic straight into the command, it wouldn't be that bad!

But say we had a longer lived command, something that required time, or performed a few different steps.

Actions can let us break up and share that functionality among other commands.
