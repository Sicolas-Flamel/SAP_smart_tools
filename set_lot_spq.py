def set_SPQ(plant, material_number, SPQ):
    session.findById("wnd[0]").resizeWorkingPane(152, 34, 0)
    session.findById("wnd[0]/tbar[0]/okcd").text = "/nmm02"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = material_number
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[1]").sendVKey(0)
    session.findById("wnd[1]/usr/ctxtRMMG1-WERKS").text = plant
    session.findById("wnd[1]").sendVKey(0)
    session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP12/ssubTABFRA1:SAPLMGMM:2000/subSUB4:SAPLMGD1:2483/txtMARC-BSTRF").text = SPQ
    session.findById("wnd[0]/tbar[0]/btn[11]").press()

    
#  use like this: set_SPQ("plant_name", "material_number", "spq")
#  also could use a dict to set a series of PN: SPQ 
