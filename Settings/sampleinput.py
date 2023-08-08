chip1 = {
    'Id' : "4",
    'Lane' : "0",
    'configfile' : "CMSIT_RD53_zh0018_0_4.txt",
    'test' : "test",
    'Ph2_ACF_VERSION' : "Ph2_ACF_VERSION",
    'Setting' : "FESetting"
}



chips = {
    'chip1' : "chip1" ,
    'chip2' : "chip2"
}


#single module can have multiple chips inside. One module per Hybrid dictionary
Hybrid = {
    'Id'   :  "4",
    'Name' :  "zh0018",
    'enable' :  "1",
    'chipType' : "chipType",
    'chips' : chips
}


OpticalGroup = {
    'FMCId' : "0",
    'Id' : "0",
    "Hybrid" : Hybrid
}

connection = {
    'address_table' : "/address_tables/CMSIT_address_table.xml",
    'id' : "cmsinnertracker.crate0.slot0",
    'uri' : "chtcp-2.0://localhost:10203?target=192.168.1.80:50001"
}

BeBoard = {
    'connection' : connection,
    'OpticalGroup' : OpticalGroup,
    'Register' : "Register"
}

#--------------------------------------------
Board1info = {
    'BeBoard'  : BeBoard,
    "Settings" : "Settings",
    "MonitoringSettings" : "MonitoringSettings"
}

Board2info = {
    'boardID' : 1,
}

Firmarelist = { 
    "board1" : Board1info,
    "board2" : Board2info
}