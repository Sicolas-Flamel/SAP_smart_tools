# after the login, you could using this function to get a Dataframe for the PO you want to check
# if you want to save it to an excel, you can also 
# it makes copy some values more easier and prepare for future management system co-search

def get_po_infos(po):
    session.FindById("wnd[0]/tbar[0]/okcd").text = "/nme23"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/ctxtRM06E-BSTNR").text = po
    session.findById("wnd[0]").sendVKey(0)

    numbers = len(session.FindById("wnd[0]/usr/tblSAPMM06ETC_0120").Children)/22

    item = []
    material = []
    des = []
    po_qty = []
    price_per_1000pc = []
    plnt = []
    currency = []


    for i in range(int(numbers)):
        item.append(session.FindById("wnd[0]/usr/tblSAPMM06ETC_0120/txtRM06E-BSTPO[0,{}]".format(i)).text)   # Item number
        material.append(session.findById("wnd[0]/usr/tblSAPMM06ETC_0120/ctxtEKPO-EMATN[3,{}]".format(i)).text)   # material number
        des.append(session.FindById("wnd[0]/usr/tblSAPMM06ETC_0120/txtEKPO-TXZ01[4,{}]".format(i)).text) # description
        po_qty.append(session.findById("wnd[0]/usr/tblSAPMM06ETC_0120/txtEKPO-MENGE[5,{}]".format(i)).text)      # PO quantities
        price_per_1000pc.append(session.findById("wnd[0]/usr/tblSAPMM06ETC_0120/txtEKPO-NETPR[9,{}]".format(i)).text)    # PN price/1000 pcs
        currency.append(session.FindById("wnd[0]/usr/ctxtEKKO-WAERS").text)
        plnt.append(session.FindById("wnd[0]/usr/tblSAPMM06ETC_0120/ctxtEKPO-WERKS[13,{}]".format(i)).text)  # plant
    
    infos = {}

    infos['item'] = item
    infos['material'] = material
    infos['des'] = des
    infos['po_qty'] = po_qty
    infos['price_per_1000pc'] = price_per_1000pc
    infos['plnt'] = plnt

    return (pd.DataFrame(infos))

    
