from sets import Set
print "Loading Constants..."

def constant(f):
    def fset(self, value):
        raise SyntaxError
    def fget(self):
        return f()
    return property(fget, fset)

class _Const(object):
    @constant
    def listOS():
        return ["69","67","58","40","422","65","63","64","68","28","29","30","31","317"]
    @constant
    def top25():
        return ["89","78","120","79","306","862","798","311","434","807","250","352","22","494","863","829","732","676","327","131","307","601","134","190","759"]
    @constant
    def cweAtts():
        cweAtt=["Owner","User","UI_GUI","Sanitize","Transformation","Transfering","Trust", \
           "DB_DNS_IDS_FW","TimeOut","MaxMin","Thirdparty","Spoofing","Tampering","Encryption",\
           "Attachment","ErrorHandling","Client_Server","WebAppService","Logs"]
        return cweAtt
    @constant
    def listWeb():
        listaWeb=["7","11","12","79","80","81","82","83","84","85","86","87","91","97","112","113","177","202","219",\
    "270","290","293","368","425","433","444","472","473","525","536","539","551","554","565","598","601","611",\
    "613","614","616","618","623","643","644","647","650","651","652","698","776","804","827","830"]
        return listaWeb    
    @constant
    def cwe710():
        cwe=['764', '765', '694', '695', '546', '547', '570', '675', '676', '671', '455', '415', '296', '308', '198', '309', '393', '392', '585', '111', '110', '398', '798', '425', '424', '586', '587', '449', '448', '580', '581', '304', '440', '447', '446', '588', '589', '245', '246', '243', '242', '102', '103', '107', '104', '383', '511', '648', '512', '579', '578', '573', '571', '628', '577', '576', '575', '574', '259', '253', '250', '174', '654', '656', '657', '733', '655', '653', '508', '509', '506', '507', '188', '568', '650', '636', '637', '560', '561', '562', '563', '462', '227', '14', '605', '638', '321', '325', '329', '688', '758', '510', '484', '476', '477', '474', '475', '685', '684', '687', '686', '683', '358']
        return cwe
    @constant
    def cwe118():
        cwe=["119","120","785","123","125","126","127","466","786","124","787","121","122","788","805","806","822","823","824","825","415","416"]
        return cwe
    @constant
    def cwe703():
        cwe=['754', '273', '252', '394', '299', '370', '296', '298', '297', '599', '354', '253', '755', '390', '756', '12', '7', '544', '396', '460', '209', '211', '210', '537', '536', '535', '550', '636', '455', '395', '280', '274', '391', '397', '167', '168', '333', '166', '228', '237', '239', '238', '240', '130', '241', '229', '231', '230', '232', '233', '234', '235', '236', '392', '393', '248', '600']
        return cwe
    @constant
    def cwe664():
        cwe=['216', '214', '215', '212', '213', '210', '668', '762', '763', '665', '761', '766', '767', '764', '765', '498', '499', '804', '494', '495', '496', '497', '491', '492', '493', '24', '25', '26', '27', '669', '22', '428', '211', '28', '29', '542', '406', '540', '541', '403', '402', '401', '451', '281', '8', '548', '549', '348', '284', '409', '408', '400', '414', '672', '673', '263', '262', '261', '260', '267', '266', '521', '346', '269', '574', '520', '59', '58', '415', '55', '57', '53', '51', '62', '619', '52', '537', '378', '535', '534', '533', '532', '531', '530', '825', '370', '827', '826', '375', '374', '377', '538', '591', '775', '593', '56', '708', '594', '774', '704', '598', '197', '196', '618', '192', '270', '271', '386', '776', '397', '275', '276', '277', '278', '279', '667', '770', '832', '379', '830', '836', '773', '536', '772', '605', '416', '798', '524', '525', '526', '527', '666', '288', '522', '523', '421', '420', '422', '528', '529', '427', '426', '308', '410', '303', '582', '583', '580', '290', '300', '301', '441', '299', '305', '588', '307', '244', '384', '385', '243', '298', '302', '784', '821', '39', '38', '843', '842', '782', '33', '32', '31', '23', '37', '36', '35', '419', '640', '642', '663', '539', '647', '648', '434', '291', '515', '514', '820', '623', '459', '620', '612', '71', '590', '572', '453', '454', '455', '456', '457', '404', '258', '592', '64', '65', '66', '178', '69', '250', '413', '256', '257', '407', '613', '268', '543', '662', '405', '195', '732', '306', '651', '340', '502', '706', '500', '501', '568', '473', '638', '833', '562', '545', '565', '566', '550', '98', '789', '289', '294', '226', '309', '412', '223', '222', '221', '220', '11', '424', '13', '282', '15', '771', '863', '862', '61', '272', '273', '287', '274', '551', '286', '54', '283', '396', '224', '607', '30', '601', '558', '603', '602', '555', '749', '556', '609', '608', '553', '552', '292', '285', '67', '34', '259', '48', '356', '46', '47', '44', '45', '42', '43', '40', '41', '322', '321', '219', '324', '639', '9', '645', '201', '200', '203', '202', '205', '204', '207', '206', '209', '208', '610', '611', '779', '778', '615', '73', '72', '489', '488', '487', '486', '485', '567', '293', '194', '425', '49', '433', '472', '829', '470', '471', '689', '460', '479', '681', '359', '50']
        return cwe
    @constant
    def cwe707():
        cwe=['91', '130', '90', '138', '93', '160', '94', '97', '163', '54', '56', '50', '53', '52', '134', '117', '116', '113', '82', '83', '80', '81', '86', '87', '84', '85', '797', '796', '795', '794', '793', '792', '791', '790', '838', '241', '240', '37', '641', '643', '644', '621', '627', '624', '177', '176', '175', '174', '173', '172', '170', '652', '464', '564', '463', '99', '168', '229', '228', '164', '165', '166', '167', '95', '161', '162', '96', '88', '89', '151', '150', '153', '152', '155', '154', '157', '156', '159', '158', '238', '239', '234', '235', '236', '237', '230', '231', '232', '233', '49', '46', '45', '42', '43', '146', '147', '144', '145', '142', '143', '140', '141', '148', '149', '77', '76', '75', '74', '79', '78']
        return cwe
    @constant
    def cwe682():
        cwe=['369', '131', '135', '468', '190', '191', '839', '193', '469', '467', '128']
        return cwe
    @constant
    def cwe697():
        cwe=['486', '595', '597', '372', '185', '186', '625', '777', '596', '478', '187', '839', '184', '183']
        return cwe
    @constant
    def cwe691():
        cwe=['591', '623', '768', '627', '600', '597', '667', '705', '567', '551', '455', '764', '765', '96', '397', '396', '179', '621', '558', '832', '833', '831', '696', '837', '834', '835', '395', '95', '698', '662', '799', '248', '574', '543', '180', '181', '97', '368', '749', '421', '367', '364', '365', '362', '363', '408', '584', '412', '674', '609', '670', '617', '307', '618', '366', '382', '484', '483', '482', '481', '480', '572', '782', '841', '783', '821', '414', '663', '828', '94', '413', '479', '432', '820', '430', '431']
        return cwe
    @constant
    def cwe435():
        cwe=['439', '733', '14', '436', '437', '444', '115', '650', '86', '626', '188', '198']
        return cwe
    @constant
    def cwe693():
        cwe=['318', '760', '219', '692', '690', '20', '289', '288', '346', '347', '281', '5', '283', '549', '348', '284', '287', '286', '263', '262', '261', '260', '267', '266', '129', '269', '268', '183', '425', '441', '297', '294', '292', '293', '290', '291', '593', '592', '708', '599', '312', '311', '317', '316', '315', '314', '270', '271', '272', '273', '274', '276', '277', '278', '279', '836', '798', '520', '521', '522', '523', '247', '422', '424', '360', '308', '309', '300', '301', '302', '303', '305', '306', '307', '108', '109', '384', '106', '105', '784', '780', '842', '789', '640', '645', '647', '646', '649', '648', '433', '623', '622', '620', '626', '450', '319', '258', '259', '179', '250', '256', '257', '656', '345', '181', '654', '182', '313', '180', '732', '653', '184', '757', '638', '639', '759', '565', '566', '781', '13', '282', '114', '285', '863', '862', '349', '354', '606', '603', '602', '555', '554', '556', '551', '357', '112', '322', '321', '326', '327', '9', '353', '328', '613', '616', '778', '614', '655', '472', '471', '689', '352', '351', '350', '358', '807', '680', '804']
        return cwe
    @constant
    def cwe330():
        cwe=['331', '333', '332', '329', '335', '337', '336', '339', '340', '342', '343', '341', '334', '6', '338', '344', '587', '323', '798', '321', '259', '804']
        return cwe
    @constant
    def dummy():
        cwe=['102', '103', '104', '105', '106', '107', '108', '109', '11', '110', '111', '112', '113', '114', '115', '116', '117', '119', '12', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '13', '130', '131', '134', '135', '138', '14', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '15', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '170', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '190', '191', '192', '193', '194', '195', '196', '197', '198', '20', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '219', '22', '220', '221', '222', '223', '224', '226', '227', '228', '229', '23', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '24', '240', '241', '242', '243', '244', '245', '246', '247', '248', '25', '250', '252', '253', '256', '257', '258', '259', '26', '260', '261', '262', '263', '266', '267', '268', '269', '27', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '28', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '29', '290', '291', '292', '293', '294', '296', '297', '298', '299', '30', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '31', '311', '312', '313', '314', '315', '316', '317', '318', '319', '32', '321', '322', '323', '324', '325', '326', '327', '328', '329', '33', '331', '332', '333', '334', '335', '336', '337', '338', '339', '34', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '35', '350', '351', '352', '353', '354', '356', '357', '358', '359', '36', '360', '362', '363', '364', '365', '366', '367', '368', '369', '37', '370', '372', '374', '375', '377', '378', '379', '38', '382', '383', '384', '385', '386', '39', '390', '391', '392', '393', '394', '395', '396', '397', '398', '40', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '41', '410', '412', '413', '414', '415', '416', '419', '42', '420', '421', '422', '424', '425', '426', '427', '428', '43', '430', '431', '432', '433', '434', '436', '437', '439', '44', '440', '441', '444', '446', '447', '448', '449', '45', '450', '451', '453', '454', '455', '456', '457', '459', '46', '460', '462', '463', '464', '466', '467', '468', '469', '47', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '48', '480', '481', '482', '483', '484', '485', '486', '487', '488', '489', '49', '491', '492', '493', '494', '495', '496', '497', '498', '499', '5', '50', '500', '501', '502', '506', '507', '508', '509', '51', '510', '511', '512', '514', '515', '52', '520', '521', '522', '523', '524', '525', '526', '527', '528', '529', '53', '530', '531', '532', '533', '534', '535', '536', '537', '538', '539', '54', '540', '541', '542', '543', '544', '545', '546', '547', '548', '549', '55', '550', '551', '552', '553', '554', '555', '556', '558', '56', '560', '561', '562', '563', '564', '565', '566', '567', '568', '57', '570', '571', '572', '573', '574', '575', '576', '577', '578', '579', '58', '580', '581', '582', '583', '584', '585', '586', '587', '588', '589', '59', '590', '591', '592', '593', '594', '595', '596', '597', '598', '599', '6', '600', '601', '602', '603', '605', '606', '607', '608', '609', '61', '610', '611', '612', '613', '614', '615', '616', '617', '618', '619', '62', '620', '621', '622', '623', '624', '625', '626', '627', '628', '636', '637', '638', '639', '64', '640', '641', '642', '643', '644', '645', '646', '647', '648', '649', '65', '650', '651', '652', '653', '654', '655', '656', '657', '66', '662', '663', '665', '666', '667', '668', '669', '67', '670', '671', '672', '673', '674', '675', '676', '680', '681', '683', '684', '685', '686', '687', '688', '689', '69', '690', '692', '694', '695', '696', '698', '7', '704', '705', '706', '708', '71', '72', '73', '732', '733', '74', '749', '75', '754', '755', '756', '757', '758', '759', '76', '760', '761', '762', '763', '764', '765', '766', '767', '768', '77', '770', '771', '772', '773', '774', '775', '776', '777', '778', '779', '78', '780', '781', '782', '783', '784', '785', '786', '787', '788', '789', '79', '790', '791', '792', '793', '794', '795', '796', '797', '798', '799', '8', '80', '804', '805', '806', '807', '81', '82', '820', '821', '822', '823', '824', '825', '826', '827', '828', '829', '83', '830', '831', '832', '833', '834', '835', '836', '837', '838', '839', '84', '841', '842', '843', '85', '86', '862', '863', '87', '88', '89', '9', '90', '91', '93', '94', '95', '96', '97', '98', '99']
        return cwe
    @constant
    def names():
        names={0:"118",1:"330",2:"435",3:"664",4:"682",5:"691",6:"693",7:"697",8:"703",9:"707",10:"710",11:"all"}
        return names

def cwebase():

    const=_Const()

    a=[]
    a.append(const.cwe118)
    a.append(const.cwe330)
    a.append(const.cwe435)
    a.append(const.cwe664)
    a.append(const.cwe682)
    a.append(const.cwe691)
    a.append(const.cwe693)
    a.append(const.cwe697)
    a.append(const.cwe703)
    a.append(const.cwe707)
    a.append(const.cwe710)
    a.append(const.dummy)

    b=[]
    b.append(const.cwe118)
    b.append(const.cwe330)
    b.append(const.cwe435)
    b.append(const.cwe664)
    b.append(const.cwe682)
    b.append(const.cwe691)
    b.append(const.cwe693)
    b.append(const.cwe697)
    b.append(const.cwe703)
    b.append(const.cwe707)
    b.append(const.cwe710)


    rep={}
    for i in range(0, len(a)):    
        for j in range(0, len(b)):
            if i<j:
                for elem in a[i]:                
                    if elem in b[j]:
                        if elem in rep:                                                
                            if i not in rep[elem]:
                                rep[elem]+=[i]
                            if j not in rep[elem]:
                                rep[elem]+=[j]
                        else:                        
                            rep[elem]=[i,j]    

    return a

def levels(base):
    ""
    if base==0:
        #CWE-118 Improper Access of Indexable Resource ('Range Error')       
        L1 = ["MaxMin","ErrorHandling","Trust","UI_GUI"] 
        L2 = ["Attachment","TimeOut","Sanitize","Logs","Client_Server","Owner","User","DB_DNS_IDS_FW"] 
        L3 = ["Encryption","Spoofing","Tampering","WebAppService","Thirdparty","Transformation","Transfering"]
        return L1, L2, L3
    if base==1:
        #CWE-330 Use of Insufficiently Random Values    
        L1 = ["Encryption","TimeOut"]
        L2 = ["Owner","User","UI_GUI","Spoofing","MaxMin","Trust", "ErrorHandling","WebAppService"]
        L3 = ["Tampering","Sanitize","Transformation","Transfering","DB_DNS_IDS_FW","Attachment","Thirdparty","Client_Server","Logs"]
        return L1, L2, L3
    if base==2:
        #CWE-435 Interaction Error
        L1 = ["UI_GUI","Sanitize","Attachment","ErrorHandling"] 
        L2 = ["WebAppService","Trust","Owner","User","Transformation","Transfering","DB_DNS_IDS_FW","Thirdparty","TimeOut","MaxMin","Client_Server"]
        L3 = ["Spoofing","Tampering","Encryption","Logs"]
        return L1, L2, L3
    if base==3:
        #CWE-664 Improper Control of a Resource Through its Lifetime
        L1 = ["TimeOut","Transfering"] 
        L2 = ["Logs","Owner","User","Attachment","WebAppService","Thirdparty","DB_DNS_IDS_FW","ErrorHandling","Tampering","MaxMin","Trust"] 
        L3 = ["UI_GUI","Spoofing","Encryption","Sanitize","Transformation","Client_Server"]
        return L1, L2, L3
    if base==4:
        #CWE-682 Incorrect Calculation
        L1 = ["Transformation","ErrorHandling","Trust"]  
        L2 = ["MaxMin", "Transfering","Owner","User","TimeOut","DB_DNS_IDS_FW","Thirdparty", "Sanitize","Client_Server","Attachment"] 
        L3 = ["UI_GUI", "WebAppService","Logs""Spoofing","Tampering","Encryption"]
        return L1, L2, L3
    if base==5:
        #CWE-691 Insufficient Control Flow Management
        L1= ["UI_GUI","Sanitize","Transfering"] 
        L2 = ["TimeOut","MaxMin","Owner","User","Transformation","Attachment","Thirdparty","ErrorHandling","Trust","DB_DNS_IDS_FW","Client_Server","WebAppService"]
        L3 = ["Spoofing","Tampering","Encryption","Logs"]
        return L1, L2, L3
    if base==6:
        #CWE-693 Protection Mechanism Failure
        L1 = ["Owner","User","UI_GUI","Sanitize","Spoofing","Tampering","Encryption","Trust"]
        L2 = ["Transformation","Transfering","Attachment","Thirdparty","DB_DNS_IDS_FW","ErrorHandling","Client_Server","WebAppService","Logs"]
        L3 = ["TimeOut","MaxMin"]
        return L1, L2, L3
    if base==7:
        #CWE-697 Insufficient Comparison
        L1 = [""] 
        L2 = ["Transformation","Attachment","Thirdparty","Owner","User","TimeOut","MaxMin","UI_GUI","Sanitize","Trust","DB_DNS_IDS_FW"]
        L3 = ["Spoofing","Tampering","Encryption", "Transfering","Client_Server","WebAppService","Logs"]
        return L1, L2, L3
    if base==8:
        #CWE-703 Improper Check or Handling of Exceptional Conditions
        L1 = ["ErrorHandling","Owner","User"] 
        L2 = ["UI_GUI","Sanitize","Trust","DB_DNS_IDS_FW","Spoofing","Tampering","Encryption","Attachment","Thirdparty","Transformation","Transfering","TimeOut","MaxMin"]
        L3 = ["Client_Server","WebAppService","Logs"]
        return L1, L2, L3
    if base==9:
        #CWE-707 Improper Enforcement of Message or Data Structure
        L1 = ["Sanitize","WebAppService","Attachment"]
        L2 = ["Owner","User","UI_GUI","Spoofing","Tampering","Encryption","Thirdparty","Trust","DB_DNS_IDS_FW","MaxMin","ErrorHandling","Client_Server","Transformation","Transfering"]
        L3 = ["TimeOut","Logs"]        
        return L1, L2, L3
    if base==10:
        #CWE-710 Coding Standards Violation
        L1 = ["Owner","User","DB_DNS_IDS_FW","Thirdparty"]
        L2 = ["UI_GUI","Transformation","Transfering","TimeOut","MaxMin","ErrorHandling","Client_Server","Encryption","Attachment","Trust"]
        L3 = ["Spoofing","Tampering","WebAppService","Logs","Sanitize"]
        return L1, L2, L3
    if base==11:
        #CWE-ALL A More General Classification
        L1 = ["Owner","User","UI_GUI","Sanitize","Trust","Client_Server"]
        L2 = ["DB_DNS_IDS_FW","Thirdparty","Spoofing","Tampering","Encryption","Transfering","TimeOut","MaxMin","ErrorHandling","WebAppService"]
        L3 = ["Transformation","Attachment","Logs"]
        return L1, L2, L3

#all=_Const()
#print sorted(list(Set(all.dummy)))