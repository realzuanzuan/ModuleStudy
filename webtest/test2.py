# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test2.py
# __time__  : 2019/11/14 6:38 PM

a_list = [20010290, 20010228, 20022079, 20371116, 20351001, 20517006, 20514154, 20512013, 20519171, 20451018, 20027132,
          20027227, 20731014, 20731022, 20020149, 20020193, 20755277, 20755223, 20777001, 20898007, 20757022, 20020143,
          20551125, 20551123, 20591005, 20792004, 20574009, 20577001, 20573004, 20571094, 20021029, 20021089, 20021040,
          20021034, 20938005, 20931009, 20029099, 20029083, 20028126, 20028147, 20813139, 20871016, 20022083, 20022078,
          20022090, 20351002, 20351140, 20351003, 20351004, 20451019, 20451020, 20024105, 20010158, 20010226, 20010268,
          20010291, 20712001, 20027187, 20733020, 20731062, 20029127, 20029100, 20029097, 20029004, 20029134, 20029081,
          20029109, 20028129, 20028140, 20028094, 20028115, 20028097, 20871024, 20871021, 20871013, 20871028, 20871015,
          20020204, 20020021, 20020171, 20020185, 20020207, 20898013, 20898011, 20752016, 20757019, 20769140, 20757025,
          20757012, 20755298, 20755027, 20755207, 20755249, 20517004, 20025003, 20515137, 20515143, 20515140, 20512064,
          20512018, 20512022, 20512025, 20512004, 20021030, 20021169, 20021148, 20021022, 20021020, 20021063, 20021048,
          20021164, 20021097, 20021154, 20550074, 20550073, 20558117, 20553027, 20553043, 20591014, 20576002, 20576019,
          20575094, 20574011, 20574026, 20573002, 20571149, 20571012, 20572009, 20573001, 20010169, 20022076, 20022091,
          20022037, 20022077, 20022080, 20536117, 20532065, 20415003, 20415004, 20010227, 20010303, 20010274, 20010310,
          20010213, 20027007, 20027184, 20028104, 20028106, 20028158, 20832004, 20028095, 20662000, 20020192, 20020150,
          20020172, 20020011, 20769162, 20757027, 20752003, 20757026, 20769141, 20755261, 20755222, 20756212, 20756215,
          20760207, 20523169, 20523003, 20523177, 20511001, 20527004, 20512005, 20510024, 20512062, 20510036, 20512001,
          20021095, 20021066, 20021096, 20021046, 20021156, 20021172, 20021059, 20021067, 20558114, 20551143, 20555001,
          20555051, 20552025, 20574052, 20574025, 20577013, 20576012, 20574030, 20571189, 20570003, 20571102, 20571117,
          20571116, 20022040, 20022070, 20022071, 20022054, 20022068, 20010262, 20010238, 20010265, 20010253, 20027142,
          20027145, 20027133, 20028103, 20028117, 20028112, 20028150, 20835001, 20662002, 20020010, 20020194, 20020146,
          20020152, 20758003, 20757018, 20755028, 20020157, 20755256, 20527001, 20516001, 20514003, 20514157, 20513001,
          20512016, 20512065, 20520000, 20510002, 20510017, 20021079, 20021173, 20021213, 20021118, 20021085, 20021084,
          20021094, 20021083, 20557000, 20553029, 20553040, 20559112, 20566051, 20571107, 20571003, 20573097, 20571148,
          20571113, 20010297]

b_list = [20010158, 20010226, 20010228, 20010268, 20010290, 20010291, 20020021, 20020143, 20020149, 20020171, 20020185,
          20020193, 20020204, 20020207, 20021029, 20021030, 20021034, 20021040, 20021089, 20022078, 20022079, 20022083,
          20022090, 20024105, 20025003, 20027132, 20027187, 20027227, 20028094, 20028097, 20028115, 20028126, 20028129,
          20028140, 20028147, 20029004, 20029081, 20029083, 20029097, 20029099, 20029100, 20029109, 20029127, 20029134,
          20351001, 20351002, 20351003, 20351004, 20351140, 20371116, 20451018, 20451019, 20451020, 20512004, 20512013,
          20512018, 20512022, 20512025, 20512064, 20514154, 20515137, 20515140, 20515143, 20517004, 20517006, 20519171,
          20551123, 20551125, 20571094, 20573004, 20574009, 20577001, 20591005, 20712001, 20731014, 20731022, 20731062,
          20733020, 20752016, 20755027, 20755207, 20755223, 20755249, 20755277, 20755298, 20757012, 20757019, 20757022,
          20757025, 20769140, 20777001, 20792004, 20813139, 20871013, 20871015, 20871016, 20871021, 20871024, 20871028,
          20898007, 20898011, 20898013, 20931009, 20938005, 20010169, 20010213, 20010227, 20010238, 20010253, 20010262,
          20010265, 20010274, 20010303, 20010310, 20020010, 20020011, 20020146, 20020150, 20020152, 20020157, 20020172,
          20020192, 20020194, 20021020, 20021022, 20021046, 20021048, 20021059, 20021063, 20021066, 20021067, 20021079,
          20021083, 20021084, 20021085, 20021094, 20021095, 20021096, 20021097, 20021118, 20021148, 20021154, 20021156,
          20021164, 20021169, 20021172, 20021173, 20021213, 20022037, 20022040, 20022054, 20022068, 20022070, 20022071,
          20022076, 20022077, 20022080, 20022091, 20027007, 20027133, 20027142, 20027145, 20027184, 20028095, 20028103,
          20028104, 20028106, 20028112, 20028117, 20028150, 20028158, 20415003, 20415004, 20510002, 20510017, 20510024,
          20510036, 20511001, 20512001, 20512005, 20512016, 20512062, 20512065, 20513001, 20514003, 20514157, 20516001,
          20520000, 20523003, 20523169, 20523177, 20527001, 20527004, 20532065, 20536117, 20550073, 20550074, 20551143,
          20552025, 20553027, 20553029, 20553040, 20553043, 20555001, 20555051, 20557000, 20558114, 20558117, 20559112,
          20566051, 20570003, 20571003, 20571012, 20571102, 20571107, 20571113, 20571116, 20571117, 20571148, 20571149,
          20571189, 20572009, 20573001, 20573002, 20573097, 20574011, 20574025, 20574026, 20574030, 20574052, 20575094,
          20576002, 20576012, 20576019, 20577013, 20591014, 20662000, 20662002, 20752003, 20755028, 20755222, 20755256,
          20755261, 20756212, 20756215, 20757018, 20757026, 20757027, 20758003, 20760207, 20769141, 20769162, 20832004,
          20835001]

# for a in a_list:
#     if a in b_list:
#         continue
#     else:
#         print(a)

c_list = [20010158, 20010169, 20010213, 20010226, 20010227, 20010228, 20010228, 20010228, 20010228, 20010238, 20010253,
          20010262, 20010265, 20010268, 20010274, 20010290, 20010290, 20010290, 20010290, 20010291, 20010297, 20010303,
          20010310, 20020010, 20020011, 20020021, 20020143, 20020143, 20020143, 20020143, 20020146, 20020149, 20020149,
          20020149, 20020149, 20020150, 20020152, 20020157, 20020171, 20020172, 20020185, 20020192, 20020193, 20020193,
          20020193, 20020193, 20020194, 20020204, 20020207, 20021020, 20021022, 20021029, 20021029, 20021029, 20021029,
          20021030, 20021034, 20021034, 20021034, 20021034, 20021040, 20021040, 20021040, 20021040, 20021046, 20021048,
          20021059, 20021063, 20021066, 20021067, 20021079, 20021083, 20021084, 20021085, 20021089, 20021089, 20021089,
          20021089, 20021094, 20021095, 20021096, 20021097, 20021118, 20021148, 20021154, 20021156, 20021164, 20021169,
          20021172, 20021173, 20021213, 20022004, 20022026, 20022037, 20022040, 20022054, 20022068, 20022070, 20022071,
          20022076, 20022077, 20022078, 20022079, 20022079, 20022079, 20022079, 20022080, 20022083, 20022090, 20022091,
          20024075, 20024088, 20024105, 20025003, 20027007, 20027132, 20027132, 20027132, 20027132, 20027133, 20027142,
          20027145, 20027184, 20027187, 20027227, 20027227, 20027227, 20027227, 20028094, 20028095, 20028097, 20028103,
          20028104, 20028106, 20028112, 20028115, 20028117, 20028126, 20028126, 20028126, 20028126, 20028129, 20028140,
          20028147, 20028147, 20028147, 20028147, 20028150, 20028158, 20028164, 20028166, 20028167, 20028179, 20028181,
          20028183, 20029004, 20029081, 20029083, 20029083, 20029083, 20029083, 20029097, 20029099, 20029099, 20029099,
          20029099, 20029100, 20029109, 20029127, 20029134, 20315004, 20351001, 20351001, 20351001, 20351001, 20351002,
          20351003, 20351004, 20351140, 20352011, 20371116, 20371116, 20371116, 20371116, 20371120, 20415003, 20415004,
          20416002, 20418004, 20429045, 20432004, 20432005, 20432006, 20432013, 20437002, 20438080, 20451006, 20451018,
          20451018, 20451018, 20451018, 20451019, 20451020, 20451024, 20452001, 20452003, 20453002, 20454004, 20456000,
          20469002, 20475000, 20510002, 20510017, 20510024, 20510036, 20511001, 20512001, 20512004, 20512005, 20512013,
          20512013, 20512013, 20512013, 20512016, 20512018, 20512022, 20512025, 20512062, 20512064, 20512065, 20513001,
          20514003, 20514154, 20514154, 20514154, 20514154, 20514157, 20515137, 20515140, 20515143, 20516001, 20517004,
          20517006, 20517006, 20517006, 20517006, 20519171, 20519171, 20519171, 20519171, 20520000, 20523003, 20523169,
          20523177, 20527001, 20527004, 20531006, 20531061, 20531069, 20531074, 20531079, 20532058, 20532065, 20533002,
          20535001, 20535006, 20535010, 20535018, 20536117, 20538058, 20539010, 20539011, 20550073, 20550074, 20551123,
          20551123, 20551123, 20551123, 20551125, 20551125, 20551125, 20551125, 20551143, 20552025, 20553027, 20553029,
          20553040, 20553043, 20555001, 20555051, 20557000, 20558114, 20558117, 20559112, 20566051, 20570003, 20571003,
          20571012, 20571094, 20571094, 20571094, 20571094, 20571102, 20571107, 20571113, 20571116, 20571117, 20571148,
          20571149, 20571189, 20572009, 20573001, 20573002, 20573004, 20573004, 20573004, 20573004, 20573097, 20574009,
          20574009, 20574009, 20574009, 20574011, 20574025, 20574026, 20574030, 20574052, 20575094, 20576002, 20576012,
          20576019, 20577001, 20577001, 20577001, 20577001, 20577013, 20591005, 20591005, 20591005, 20591005, 20591014,
          20631003, 20631004, 20633002, 20634004, 20662000, 20662002, 20712001, 20731014, 20731014, 20731014, 20731014,
          20731022, 20731022, 20731022, 20731022, 20731062, 20733020, 20752003, 20752016, 20755027, 20755028, 20755207,
          20755222, 20755223, 20755223, 20755223, 20755223, 20755249, 20755256, 20755261, 20755277, 20755277, 20755277,
          20755277, 20755298, 20756212, 20756215, 20757012, 20757018, 20757019, 20757022, 20757022, 20757022, 20757022,
          20757025, 20757026, 20757027, 20758003, 20760207, 20769140, 20769141, 20769162, 20777001, 20777001, 20777001,
          20777001, 20792004, 20792004, 20792004, 20792004, 20813139, 20813139, 20813139, 20813139, 20832004, 20835001,
          20835002, 20871013, 20871015, 20871016, 20871016, 20871016, 20871016, 20871021, 20871024, 20871028, 20898007,
          20898007, 20898007, 20898007, 20898011, 20898013, 20931009, 20931009, 20931009, 20931009, 20938005, 20938005,
          20938005, 20938005]

d_list = [20835002, 20028167, 20028164, 20028166, 20028183, 20028181, 20028179, 20010290, 20010228, 20022079, 20371116,
          20351001, 20517006, 20514154, 20512013, 20519171, 20451018, 20027132, 20027227, 20731014, 20731022, 20020149,
          20020193, 20755277, 20755223, 20777001, 20898007, 20757022, 20020143, 20551125, 20551123, 20591005, 20792004,
          20574009, 20577001, 20573004, 20571094, 20021029, 20021089, 20021040, 20021034, 20938005, 20931009, 20029099,
          20029083, 20028126, 20028147, 20813139, 20871016, 20022083, 20022078, 20022090, 20351002, 20351140, 20351003,
          20351004, 20451019, 20451020, 20024105, 20010158, 20010226, 20010268, 20010291, 20712001, 20027187, 20733020,
          20731062, 20029127, 20029100, 20029097, 20029004, 20029134, 20029081, 20029109, 20028129, 20028140, 20028094,
          20028115, 20028097, 20871024, 20871021, 20871013, 20871028, 20871015, 20020204, 20020021, 20020171, 20020185,
          20020207, 20898013, 20898011, 20752016, 20757019, 20769140, 20757025, 20757012, 20755298, 20755027, 20755207,
          20755249, 20517004, 20025003, 20515137, 20515143, 20515140, 20512064, 20512018, 20512022, 20512025, 20512004,
          20021030, 20021169, 20021148, 20021022, 20021020, 20021063, 20021048, 20021164, 20021097, 20021154, 20550074,
          20550073, 20558117, 20553027, 20553043, 20591014, 20576002, 20576019, 20575094, 20574011, 20574026, 20573002,
          20571149, 20571012, 20572009, 20573001, 20010169, 20022076, 20022091, 20022037, 20022077, 20022080, 20536117,
          20532065, 20415003, 20415004, 20010227, 20010303, 20010274, 20010310, 20010213, 20027007, 20027184, 20028104,
          20028106, 20028158, 20832004, 20028095, 20662000, 20020192, 20020150, 20020172, 20020011, 20769162, 20757027,
          20752003, 20757026, 20769141, 20755261, 20755222, 20756212, 20756215, 20760207, 20523169, 20523003, 20523177,
          20511001, 20527004, 20512005, 20510024, 20512062, 20510036, 20512001, 20021095, 20021066, 20021096, 20021046,
          20021156, 20021172, 20021059, 20021067, 20558114, 20551143, 20555001, 20555051, 20552025, 20574052, 20574025,
          20577013, 20576012, 20574030, 20571189, 20570003, 20571102, 20571117, 20571116, 20022040, 20022070, 20022071,
          20022054, 20022068, 20010262, 20010238, 20010265, 20010253, 20027142, 20027145, 20027133, 20028103, 20028117,
          20028112, 20028150, 20835001, 20662002, 20020010, 20020194, 20020146, 20020152, 20758003, 20757018, 20755028,
          20020157, 20755256, 20527001, 20516001, 20514003, 20514157, 20513001, 20512016, 20512065, 20520000, 20510002,
          20510017, 20021079, 20021173, 20021213, 20021118, 20021085, 20021084, 20021094, 20021083, 20557000, 20553029,
          20553040, 20559112, 20566051, 20571107, 20571003, 20573097, 20571148, 20571113, 20010297, 20531006, 20539010,
          20022026, 20532058, 20631004, 20371120, 20452001, 20432005, 20432006, 20024075, 20531061, 20533002, 20531069,
          20539011, 20633002, 20022004, 20315004, 20535001, 20535010, 20631003, 20535006, 20535018, 20453002, 20454004,
          20452003, 20432004, 20432013, 20438080, 20437002, 20475000, 20429045, 20416002, 20531074, 20634004, 20538058,
          20531079, 20352011, 20456000, 20451024, 20469002, 20451006, 20024088, 20418004, ]
for c in c_list:
    if c in d_list:
        continue
    else:
        print(c)
