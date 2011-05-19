Openremote
==========

#### A chrome extension that lets you open a link in a remote browser. ####

Have you ever been sitting on the couch, laptop on your...lap, watching a 
YouTube video on a tiny screen with a fancy 60 inch flatscreen sitting just a 
few feet away? If only there was a way to watch that video the way FSM intended,
with just a few clicks.

This is my attempt. Openremote is a chrome extension, which, when paired with a 
webserver running on a remote machine, can open a page or link on that remote
machine. If that machine is connected to a big screen tv, you'll be watching 
videos in all their 1080p glory in no time.


Setting up the server
---------------------

In order to open the desired url on the remote machine, a server component is
required. Currently, the extension uses an XMLHttpRequest to send the url to
the server. Therefore, the remote machine must be running a web server with
some script or application listening for requests from the extension. When
a request arrives, the script should parse the url parameter and make a system
call to open the url in a browser.

A server implementation for Mac OS X can be found in openremote-server-osx. Because 
OS X only lets programs talk to applications on the desktop if they are both run
by the same user, some kludgery was necessary. The request handler consists of
a ruby script that parses the url parameter, then passes it to the OSX `open`
command. Therefore, the url will be opened in the currently logged-in user's 
default browser (I've only tested it in Chrome, so far).

To get around the permissions issues, a wrapper program was written in C that
simply calls the ruby script. When the program's owner is set to the same user
who is logged in to the desktop and the setuid flag is set, the `open` command
should run without errors.

To set up the server on OS X:

* [Enable Apache](http://docs.info.apple.com/article.html?path=Mac/10.6/en/8236.html)
* Copy `openurl.c` and `openurl.rb` to `/Library/Webserver/CGI-Executables/`
* Compile openurl.c: `make openurl`   
* Setup permissions for openurl:
    > sudo chown $USER openurl openurl.rb
    > sudo chmod 4711 openurl
    > sudo chmod 0755 openurl.rb 


Installing the extension
------------------------

* Download the source from `openremote-chrome-extension`.
* In Chrome, open the Tools > Extensions page.
* Click the + to expand the Developer Mode options.
* Click the Load unpacked extension button.
* Browse to the openremote folder you previously downloaded and click OK.
* Click Options.
* Enter the full url to the remote server. If using the included server
  scripts, enter something like `http://servername/cgi-bin/openurl?url=%s`. 
  `%s` is a placeholder that will be replaced with the url to open.
* Optionally enter the text that will be used in the context menus.


Using the extension
-------------------

Right click on any page, link, or image and select 'Open in remote browser'.
You should see the url open up on the remote machine. A status message will
be displayed at the top of the screen denoting success or failure.


Future Enhancements
-------------------
* Linux server implementation
* Windows server implementation
* Remove requirement for webserver (ssh?)
* Browser options such as opening in full-screen or incognito mode
* Allow definition of multiple renote hosts
* Firefox extension
* Safari extension
* Anything else?

