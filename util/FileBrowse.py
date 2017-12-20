import re
import subprocess
import platform
import webbrowser
from util.Global import Global
import os

def explorer(path):

    if not path:
        return

    Global.printStatus("Open: {0}".format(path), 3000)

    if platform.system() == "Darwin":
        # OS X
        subprocess.call(["open", "-R", path])
        Global.printStatus("Open: {0}".format(path), 5000)
    elif platform.system() == "Windows":
        # Win
        refined_path = path.replace('/', '\\')
        subprocess.Popen('explorer /select,{path}'.format(path=refined_path))
        Global.printStatus("Open: {0}".format(refined_path), 5000)
    else:
        Global.printStatus("Not supported.", 5000)

    return

def browse(path):
    if not path:
        return

    st = re.sub('f[0-9]', '', path)

    # todo patch release detection

    url = "http://unity3d.com/unity/whats-new/unity-" + st
    webbrowser.open(url, new=2) # open in new tab

    return