# PyRepl
The repl.it API is very good, if you know JS. If you don't want to use JS, you're out
of luck. But now you can use Python too! PyRepl is a library for interacting with the
repl.it API through Python. It is similar to Crosis, the JS version. Sound interesting?
Read on for a basic tutorial.
# Installation
First you have to install the library. Simply clone this repo and run `pip3 install -r requirements.txt`,
and you'll be good to go.
# The Basics
To use this library, you first need a replit session id. You can find your connect.sid value by checking the cookie named connect.sid found when accessing Replit.
Once you have that, you need a repl. Go ahead and create one. Then create file. In that file, write:
```
import pyrepl
```
Then move on to the next step.
# IDs and Tokens
Each time you access a repl, you need a one-time token for it. To get that, you need a session id (see previous step)
and the repl ID. The repl ID can be retrieved in the following way:
```
id = pyrepl.get_json(<user>, <repl>)['id']
```
`<user>` being your username (no @) and `<repl>` being the name of the repl you created earlier. `pyrepl.get_json`
is a function that returns some useful JSON data about a repl, including the ID. Then you need a token. To get a token,
use:
```
token = pyrepl.get_token(id, <key>)
```
`<key>` being your session id. You probably want to use `dotenv` or something similar to keep it secret.
# Connecting
Now that you have a token for a repl, you need to connect to it. To do that, you can use the following code:
```
url = pyrepl.get_url(token, 'eval.repl.it', 80)
client = pyrepl.Client(token, id, url)
```
First we get the URL to connect to using `pyrepl.get_url`. Then we create an instance of `client`. Now we can
move on to the final step!
# Usage
Now all that's left to do is open a channel and send messages to it! For this example, we'll run the `ls` command.
First, to get a channel, we use:
```
channel = client.open('exec', 'execer')
```
The first argument is the service, and the second the name of the channel. Then, we have three options for sending data:

1. We can use `channel.run`, which sends the data and ignores the output. This is not what we want here,
   but it can be useful for some channels.
2. We can use `channel.get_json` to get a list of dictionaries representing all the responses to the command.
   This is not what we want here, but if we wanted to examine the results in more detail, we would use this.
3. We can use `channel.get_output` to get the output of the response as a string. In this case, we want the output,
   so let's use that!

```
print(channel.get_output({
	'exec':{
		'args':['ls']
	}
}))
```
This should list all the files in your repl! For complete documentation on the services and how to format messages to
them, see [here](http://protodoc.turbio.repl.co/services).
# Closing Notes
Some final notes:

- This code is licensed under the MIT license. Feel free to do with it what you please, but credit would be nice!

Thanks for using PyRepl!
