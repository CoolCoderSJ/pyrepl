from distutils.core import setup
setup(
  name = 'snow_pyrepl',         # How you named your package folder (MyLib)
  packages = ['snow_pyrepl'],   # Chose the same as "name"
  version = '0.6',      # Start with a small number and increase it with every change you make
  license='GNU GPL v 3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Interact with Replit\'s API',   # Give a short description about your library
  author = 'SnowCoder',                   # Type in your name
  author_email = 'not@available.pleasedontemailme',      # Type in your E-Mail
  url = 'https://github.com/CoolCoderSJ/pyrepl',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/CoolCoderSJ/pyrepl/archive/refs/tags/v0.6.tar.gz',    # I explain this later on
  keywords = ['pyrepl', 'Python', 'Replit'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
		  'protobuf',
		  'google-nucleus',
		  'base36',
		  'websocket_client',
		  'requests'
	  ],
  classifiers=[
	'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
	'Intended Audience :: Developers',      # Define that your audience are developers
	'Topic :: Software Development :: Build Tools',
	'License :: OSI Approved :: MIT License',   # Again, pick a license
	'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
  ],
)
