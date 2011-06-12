#!/usr/bin/env python

import sys, wx
import re
import webbrowser
import urlparse
import platform
import threading
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

TOGGLE_SERVER=wx.NewId()
SERVER_STATUS=wx.NewId()
OPEN_PREFS=wx.NewId()

class OpenRemoteFrame(wx.Frame):
    """This is the frame for our application, it is derived from the
    wx.Frame element."""

    def __init__(self, parent, id, title):
        """Initialize, and let the user set any Frame settings"""
        wx.Frame.__init__(self, parent, -1, title, size = (1, 1),  
            style=wx.FRAME_NO_TASKBAR|wx.NO_FULL_REPAINT_ON_RESIZE)
        self.server = None
        self.tbicon = MailTaskBarIcon(self)  
        
    def exitApp(self,event):  
        self.tbicon.RemoveIcon()  
        self.tbicon.Destroy()  
        sys.exit()    
        
    def OpenPreferences(self,event=None):
        pass    
    
    def ToggleServer(self,event=None):  
        if self.server is None:
            self.server = HTTPServer(('', 8080), OpenRemoteHandler)
            server_thread = threading.Thread(target=self.server.serve_forever)
            server_thread.setDaemon(True)
            server_thread.start()
            self.tbicon.menu.SetLabel(TOGGLE_SERVER, "Stop Server")
            self.tbicon.menu.SetHelpString(TOGGLE_SERVER, "Stop listening for remote URLs.")
            self.tbicon.menu.SetLabel(SERVER_STATUS, "Server listening on port 8080") 
        else:
            self.server.shutdown()
            self.server = None
            self.tbicon.menu.SetLabel(TOGGLE_SERVER, "Start Server")
            self.tbicon.menu.SetHelpString(TOGGLE_SERVER, "Start listening for remote URLs.")
            self.tbicon.menu.SetLabel(SERVER_STATUS, "Server not running") 

class MailTaskBarIcon(wx.TaskBarIcon):  

    def __init__(self, parent):  
        wx.TaskBarIcon.__init__(self)  
        self.parentApp = parent  
        self.SetIcon(wx.Icon("openremote-16.png",wx.BITMAP_TYPE_PNG))  
        self.CreateMenu() 

    def CreateMenu(self):  
        self.Bind(wx.EVT_TASKBAR_RIGHT_UP, self.ShowMenu)  
        self.Bind(wx.EVT_TASKBAR_LEFT_UP, self.ShowMenu)  
        self.Bind(wx.EVT_MENU, self.parentApp.ToggleServer, id=TOGGLE_SERVER)  
        self.Bind(wx.EVT_MENU, self.parentApp.OpenPreferences, id=OPEN_PREFS)  
        self.Bind(wx.EVT_MENU, self.parentApp.exitApp, id=wx.ID_EXIT)   
        self.menu=wx.Menu()  
        self.menu.Append(SERVER_STATUS, "Server not running") 
        self.menu.Enable(SERVER_STATUS, False) 
        self.menu.AppendSeparator()  
        self.menu.Append(TOGGLE_SERVER, "Start Server","Start listening for remote URLs.") 
        self.menu.AppendSeparator()  
        self.menu.Append(OPEN_PREFS, "Preferences...","Configure OpenRemote.") 
        self.menu.AppendSeparator()  
        self.menu.Append(wx.ID_EXIT, "Exit")  

    def ShowMenu(self,event):  
        self.PopupMenu(self.menu)  

class OpenRemoteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = ''
        try:
            request_url = urlparse.urlsplit(self.path)
            if re.search('openurl', request_url.path):
                query = urlparse.parse_qs(request_url.query)            
                url = query["url"][0]
                webbrowser.open_new_tab(url) 
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("Opened %s on %s" % (url, platform.node()))    
            else:
                self.send_error(404)
        except:
            self.send_error(500,'Failed to open url: %s, error: %s' % (url, str(sys.exc_info()[1])))
                      
def main(argv=None):  
    app = wx.App(False)  
    frame = OpenRemoteFrame(None, -1, ' ')  
    frame.Center(wx.BOTH)  
    frame.ToggleServer()
    frame.Show(False)  
    app.MainLoop()  

if __name__ == '__main__':  
    main()