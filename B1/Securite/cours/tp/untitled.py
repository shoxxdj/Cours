#! /usr/bin/env python
# -*- coding:Utf­8 ­-*-

import webkit
import gtk
import re

def document_load_finished_cb(webview, webframe):
    #webview.execute_script("document.title=document.documentElement.innerHTML;")
    #for elem in re.findall('<strong>(.*?)</strong>', webframe.get_title()):
    #    try:
    #        eval(elem)
    #        print elem
    #    except: pass
    #gtk.main_quit()

webview = webkit.WebView()
webview.connect("document-load-finished", document_load_finished_cb)
webview.load_uri('http://wlourf.deviantart.com/stats/gallery/')

gtk.main()
gtk.destroy()