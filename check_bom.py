def check_bom(material_number, plant):
    session.findById("wnd[0]/tbar[0]/okcd").text = "/ncs12"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/ctxtRC29L-MATNR").text = material_number
    session.findById("wnd[0]/usr/ctxtRC29L-WERKS").text = plant
    session.findById("wnd[0]/usr/ctxtRC29L-CAPID").text = "PP01"
    session.findById("wnd[0]/usr/ctxtRC29L-CAPID").setFocus()
    session.findById("wnd[0]/usr/ctxtRC29L-CAPID").caretPosition = 4
    session.findById("wnd[0]/tbar[1]/btn[8]").press()

    
    
