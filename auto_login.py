# one way is to record the log in process, save it as login.vbs, using Python to call it at a certain time
# another way is below:
import win32com.client
import pandas as pd
import time

def log(username, userpassword):
    SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine
    conn = SapGui.OpenConnection("sap_name", True)  # sap_name is the Name value on the SAP Logon Interface
    session = conn.Children(0)
    session.FindById("wnd[0]/usr/txtRSYST-BNAME").text = username
    session.FindById("wnd[0]/usr/pwdRSYST-BCODE").text = userpassword
    session.FindById("wnd[0]").sendVKey(0)
    return session

session = log("5mvq6j", "xx222222")
  
