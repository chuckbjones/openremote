Openremote
==========

#### A chrome extension that lets you open a link in a remote browser. ####

Have you ever been sitting on the couch, laptop on your...lap, watching a 
YouTube video on a tiny screen with a fancy 60 inch flatscreen sitting just a 
few feet away? If only there was a way to watch that video the way FSM intended,
with just a few clicks.

This is my attempt. Openremote is a chrome extension, which, when paired with a 
server running on a remote machine, can open a page or link on that remote
machine. If that machine is connected to a big screen tv, you'll be watching 
videos in all their 1080p glory in no time.


Setting up the server
---------------------

* Install python, if necessary: http://www.python.org. I've
  tested the script with python 2.6 on Ubuntu 10.04 and Mac OS 10.6,
  and with python 2.7.1 on Windows XP and Windows 7.
* Download `openremote.py` from `openremote-server-python`.
* Execute `openremote.py`
* Currently, the server runs on port 8080. Edit the source to change it.
* On Windows, you will have to click `allow` for the server to run.   
  


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
* Install packages, error logging, and configuration screens for server.
* Browser options such as opening in full-screen or incognito mode
* Allow definition of multiple renote hosts
* Firefox extension
* Safari extension
* Anything else?

