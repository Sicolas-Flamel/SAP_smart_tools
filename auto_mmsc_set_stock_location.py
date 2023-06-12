# after the login, you could using this function to set lot materials' multiple stock location- SL.


stock_location_FG = [
"A",
"B",
"C",
]   # use stock_location_FG list to involve the finished materials which needs to set in SL series of finished goods

stock_location_RM = [ 
  "P",
  "X",
  "Y",
]    # use stock_location_RM list to involve the raw materials which needs to set in SL series of raw materials

sl_FG_lists = ["SL_001","SL_002","SL_003"]   #  suppose that SL_003 is a specially SL for raw materials
sl_RM_lists = ["SL_001","SL_002","SL_009"]   #  suppose that SL_009 is a specially SL for raw materials

plant_code = "fangtech"

# main code
def maintain_sl(require_setting_list, plant_code, sl_lists):     # please change the plant code and sl_lists in your context
  check_later = []    # store the unsuccessful materials which wasn't set due to the wrong material number of the stock location has not been maintained.
  for i in require_setting_list[0:]:
      session.FindById("wnd[0]/tbar[0]/okcd").text = "/nmmsc"   #  Tcode for maintain the stock location
      session.findById("wnd[0]").sendVKey(0) 
      session.findById("wnd[0]/usr/ctxtRM03M-MATNR").text = i
      session.findById("wnd[0]/usr/ctxtRM03M-WERKS").text = plant_code
      session.findById("wnd[0]").sendVKey(0)
      temp = 9
      try:
          for j in sl_lists:           # set location one by one
            session.findById("wnd[0]/usr/sub:SAPMM03M:0195/ctxtRM03M-LGORT[9,0]").text = j
            session.findById("wnd[0]/usr/sub:SAPMM03M:0195/ctxtRM03M-LGORT[9,0]").caretPosition = 4
            session.findById("wnd[0]").sendVKey(0)
    
          session.findById("wnd[0]/tbar[0]/btn[11]").press()      # click the save button
      except:
          check_later.append(i)
  return check_later      # afterwards, you could manually check the item in the check_later one by one to see the failed reason


# example of call the maintain_sl:
FG_check_later = maintain_sl(stock_location_FG, plant_code, sl_FG_lists)
RM_check_later = maintain_sl(stock_location_RM, plant_code, sl_RM_lists)


