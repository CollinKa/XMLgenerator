
#'None' represents the ones that are not being used.

#Beboards [first beboard, second beboard, ...]
boardId = ['0', '1']
boardType = ['RD53', 'RD53']
eventType = ['VR', 'VR']



PH2ACF_BASE_DIR = 'GUI'
#Connection [first beboard, second beboard, ...]
address_table = ['file://${PH2ACF_BASE_DIR}/settings/address_tables/CMSIT_address_table.xml',
                 'file://${PH2ACF_BASE_DIR}/settings/address_tables/CMSIT_address_table.xml'] #need to fix this thing with fstring(TBD)
connectionId = ['cmsinnertracker.crate0.slot0',
                'cmsinnertracker.crate0.slot0']
connectionUri = ['chtcp-2.0://localhost:10203?target=192.168.1.80:50001',
                 'chtcp-2.0://localhost:10203?target=192.168.1.81:50001']


#OpticalGroup [first beboard, second beboard, ...]
OpticalGroup_Id = ['0', '1']
FMCId = ['1', '1']


#First Board Hybrid
#These lists should all have equal length
board0_hybridId = ['0', '2', '7', '5']
board0_hybridName = ['zh0018', 'zh0019', None, None] #serial number
board0_enable = ['1', '1', None, None]

#First Board RD53_Files [first hybrid, second hybrid, ...]
board0_RD53File = ['./', 'b', None, None, None, None, None, None]

#Second Board Hybrid
#hybridId, hybridName, enable lists should all have equal length
board1_hybridId = ['5', '4', '7', '3', None, None, None, '2']
board1_hybridName = ['zh0020', 'zh0021', None, None, None, None, None, 'zh0022']
board1_enable = ['1', '1', None, None, None, None, None, '1']

#Second Board RD53_Files [first hybrid, second hybrid, ...]
board1_RD53File = ['c', 'd', None, None, None, None, None, 'e']


#First Board
#Lists should have equal length
board0_hybrid0_Lane = ['0', '1', '2', '3']
board0_hybrid0_RD53AId = ['4', '2', '7', '5']
board0_hybrid0_RD53BId = [None, '4', None, None]
board0_hybrid0_configfile = ['CMSIT_RD53_zh0018_0_4.txt',
                     'CMSIT_RD53_zh0018_0_2.txt',
                     'CMSIT_RD53_zh0018_0_7.txt',
                     'CMSIT_RD53_zh0018_0_5.txt',]

board0_hybrid0_RD53A_Settings = [
    ['839', '63', '0', '0b00', '0b00', '1023', '110', '0', '2', '500', '0', '0',
     '20', '542', '0', '100', '150', '280', '55', '80', '100', '9', '29', '136',
     '20', '130', '5', '12', '350', '512', '511', '300', '1225', '360', '600', '100', '40', '16',
     '16', '900', '450', '700', '100', '150', '400'],
    ['350', '20', '29', '130', '110', '300', '400', '100', '150', '80', '55', '280',
     '100', '360', '150', '450', '2', '511', '542', '512', '1023', '40', '400', '100',
     '20', '0', '600', '100', '0', '136', '0', '0', '0', '16', '16', '0b00', '0b00', '500',
     '0', '0', '5', '12', '63', '839', '1225'],
    ['839', '63', '0', '0b00', '0b00', '1023', '110', '0', '2', '500', '0', '0',
     '20', '542', '0', '100', '150', '280', '55', '80', '100', '9', '29', '136',
     '20', '130', '5', '12', '350', '512', '511', '300', '1225', '360', '600', '100', '40', '16',
     '16', '900', '450', '700', '100', '150', '400'],
    ['350', '20', '29', '130', '110', '300', '400', '100', '150', '80', '55', '280',
     '100', '360', '150', '450', '2', '511', '542', '512', '1023', '40', '400', '100',
     '20', '0', '600', '100', '0', '136', '0', '0', '0', '16', '16', '0b00', '0b00', '500',
     '0', '0', '5', '12', '63', '839', '1225']
]


board0_hybrid1_Lane = ['0', '1', None, '3']
board0_hybrid1_RD53AId = ['4', '8' ,None, '5']
board0_hybrid1_RD53BId = [None, None, None, None]
board0_hybrid1_configfile = ['CMSIT_RD53_zh0018_0_4.txt',
                     'CMSIT_RD53_zh0018_0_8.txt',
                     None,
                     'CMSIT_RD53_zh0018_0_51.txt',]


board0_hybrid2_Lane = ['0', '1', None, '3']
board0_hybrid2_RD53AId = ['4', None ,None, '5']
board0_hybrid2_RD53BId = [None, '4', None, None]
board0_hybrid2_configfile = ['CMSIT_RD53_zh0018_0_42.txt',
                     'CMSIT_RD53_zh0018_0_25.txt',
                     None,
                     'CMSIT_RD53_zh0018_0_5.txt',]


board0_hybrid3_Lane = ['0', '1', None, '3']
board0_hybrid3_RD53AId = ['4', None ,None, '5']
board0_hybrid3_RD53BId = [None, '4', None, None]
board0_hybrid3_configfile = ['CMSIT_RD53_zh0018_0_4.txt',
                     'CMSIT_RD53_zh0018_0_2.txt',
                     None,
                     'CMSIT_RD53_zh0018_0_5.txt',]


#Registers
board0_register0_value = ['2']
board0_register1_value = ['0']
board0_register2_value = ['128']
board0_register3_value = ['128']
board0_register4_value = ['128']
board0_register5_value = ['128']
board0_register6_value = ['128']
board0_register7_value = ['0']
board0_register8_value = ['0']
board0_register9_value = ['10']



#Second Board Lanes
#Lists should have equal length
board1_hybrid0_Lane = ['0', '1', '2', None]
board1_hybrid0_RD53AId = ['1', '7', '9', None]
board1_hybrid0_RD53BId = [None, None, None, None]
board1_hybrid0_configfile = ['CMSIT_RD53_zh0018_0_4.txt',
                     'CMSIT_RD53_zh0018_0_2.txt',
                     'CMSIT_RD53_zh0018_0_7.txt',
                     'CMSIT_RD53_zh0018_0_5.txt',]


board1_hybrid1_Lane = ['0', '1', '2', None]
board1_hybrid1_RD53AId = ['1', '7', '9', None]
board1_hybrid1_RD53BId = [None, None, None, None]
board1_hybrid1_configfile = ['CMSIT_RD53_zh0018_0_4.txt',
                     'CMSIT_RD53_zh0018_0_2.txt',
                     'CMSIT_RD53_zh0018_0_7.txt',
                     'CMSIT_RD53_zh0018_0_5.txt',]


board1_hybrid2_Lane = ['0', '1', '2', None]
board1_hybrid2_RD53AId = ['1', '7', '9', None]
board1_hybrid2_RD53BId = [None, None, None, None]
board1_hybrid2_configfile = ['CMSIT_RD53_zh0018_0_4.txt',
                     'CMSIT_RD53_zh0018_0_2.txt',
                     'CMSIT_RD53_zh0018_0_7.txt',
                     'CMSIT_RD53_zh0018_0_5.txt',]


board1_hybrid3_Lane = ['0', '1', '2', None]
board1_hybrid3_RD53AId = ['1', '7', '9', None]
board1_hybrid3_RD53BId = [None, None, None, None]
board1_hybrid3_configfile = ['CMSIT_RD53_zh0018_0_4.txt',
                     'CMSIT_RD53_zh0018_0_2.txt',
                     'CMSIT_RD53_zh0018_0_7.txt',
                     'CMSIT_RD53_zh0018_0_5.txt',]






# Define the keys for the dictionaries
Beboard_attrib = ['Id', 'boardType', 'eventType']
connection_attrib = ['id', 'uri', 'address_table']
OpticalGroup_attrib = ['Id', 'FMCId']
Hybrid_attrib = ['Id', 'Name', 'enable']
RD53_Files_attrib = ['file']
RD53A_attrib = ['Id', 'Lane', 'configfile']
RD53A_Settings_attrib = [
    'ADC_MAXIMUM_VOLT', 'ADC_OFFSET_VOLT', 'CLK_DATA_DELAY', 'CML_CONFIG_SER_EN_TAP', 
    'CML_CONFIG_SER_INV_TAP', 'COMP_DIFF', 'COMP_LIN', 'CONF_FE_DIFF', 'CONF_FE_SYNC',
    'DAC_CML_BIAS_0', 'DAC_CML_BIAS_1', 'DAC_CML_BIAS_2', 'FC_BIAS_LIN', 'FOL_DIFF', 
    'GP_LVDS_ROUTE', 'IBIASP1_SYNC', 'IBIASP2_SYNC', 'IBIAS_DISC_SYNC', 'IBIAS_KRUM_SYNC',
    'IBIAS_SF_SYNC', 'ICTRL_SYNCT_SYNC', 'INJECTION_SELECT', 'KRUM_CURR_LIN', 'LATENCY_CONFIG', 
    'LCC_DIFF', 'LDAC_LIN', 'MONITOR_CONFIG_ADC', 'MONITOR_CONFIG_BG', 'PA_IN_BIAS_LIN',
    'PRECOMP_DIFF', 'PRMP_DIFF', 'REF_KRUM_LIN', 'TEMPSENS_IDEAL_FACTOR', 'VBL_SYNC', 
    'VCAL_HIGH', 'VCAL_MED', 'VFF_DIFF', 'VOLTAGE_TRIM_ANA', 'VOLTAGE_TRIM_DIG', 'VREF_ADC', 
    'VREF_KRUM_SYNC', 'VTH1_DIFF', 'VTH2_DIFF', 'VTH_SYNC', 'Vthreshold_LIN'
]


Hybrid_Global_attrib = [
    'BITFLIP_ERR_CNT', 'BITFLIP_WNG_CNT', 'CMDERR_CNT', 'EN_CORE_COL_CAL_DIFF_1', 
    'EN_CORE_COL_CAL_DIFF_2', 'EN_CORE_COL_CAL_DIFF_3', 'EN_CORE_COL_CAL_DIFF_4', 
    'EN_CORE_COL_CAL_DIFF_5', 'EN_CORE_COL_CAL_LIN_1', 'EN_CORE_COL_CAL_LIN_2', 
    'EN_CORE_COL_CAL_LIN_3', 'EN_CORE_COL_CAL_LIN_4', 'EN_CORE_COL_CAL_LIN_5', 
    'EN_CORE_COL_CAL_SYNC_1', 'EN_CORE_COL_CAL_SYNC_2', 'EN_CORE_COL_CAL_SYNC_3', 
    'EN_CORE_COL_CAL_SYNC_4', 'EN_CORE_COL_DIFF_1', 'EN_CORE_COL_DIFF_2', 'EN_CORE_COL_LIN_1', 
    'EN_CORE_COL_LIN_2', 'EN_CORE_COL_SYNC', 'HITOR_0_CNT', 'HITOR_0_MASK_DIFF_0', 'HITOR_0_MASK_DIFF_1', 
    'HITOR_0_MASK_LIN_0', 'HITOR_0_MASK_LIN_1', 'HITOR_0_MASK_SYNC', 'HITOR_1_CNT', 'HITOR_1_MASK_DIFF_0', 
    'HITOR_1_MASK_DIFF_1', 'HITOR_1_MASK_LIN_0', 'HITOR_1_MASK_LIN_1', 'HITOR_1_MASK_SYNC', 'HITOR_2_CNT', 
    'HITOR_2_MASK_DIFF_0', 'HITOR_2_MASK_DIFF_1', 'HITOR_2_MASK_LIN_0', 'HITOR_2_MASK_LIN_1', 
    'HITOR_2_MASK_SYNC', 'HITOR_3_CNT', 'HITOR_3_MASK_DIFF_0', 'HITOR_3_MASK_DIFF_1', 'HITOR_3_MASK_LIN_0', 
    'HITOR_3_MASK_LIN_1', 'HITOR_3_MASK_SYNC', 'LOCKLOSS_CNT', 'SKIPPED_TRIGGER_CNT'
]

#Register names
board0_Register0 = ['user', 'ctrl_regs', 'fast_cmd_reg_2', 'trigger_source']
board0_Register1 = ['user', 'ctrl_regs', 'fast_cmd_reg_2', 'HitOr_enable_l12']
board0_Register2 = ['user', 'ctrl_regs', 'ext_tlu_reg1', 'dio5_ch1_thr']
board0_Register3 = ['user', 'ctrl_regs', 'ext_tlu_reg1', 'dio5_ch2_thr']
board0_Register4 = ['user', 'ctrl_regs', 'ext_tlu_reg2', 'dio5_ch3_thr']
board0_Register5 = ['user', 'ctrl_regs', 'ext_tlu_reg2', 'dio5_ch4_thr']
board0_Register6 = ['user', 'ctrl_regs', 'ext_tlu_reg2', 'dio5_ch5_thr']
board0_Register7 = ['user', 'ctrl_regs', 'ext_tlu_reg2', 'tlu_delay']
board0_Register8 = ['user', 'ctrl_regs', 'ext_tlu_reg2', 'ext_clk_en']
board0_Register9 = ['user', 'ctrl_regs', 'fast_cmd_reg_3', 'triggers_to_accept']








RD53B_Settings_attrib = [
    'DAC_PREAMP_L_LIN', 'DAC_PREAMP_R_LIN', 'DAC_PREAMP_TL_LIN', 'DAC_PREAMP_TR_LIN',
    'DAC_PREAMP_T_LIN', 'DAC_PREAMP_M_LIN', 'DAC_FC_LIN', 'DAC_KRUM_CURR_LIN',
    'DAC_REF_KRUM_LIN', 'DAC_COMP_LIN', 'DAC_COMP_TA_LIN', 'DAC_GDAC_L_LIN',
    'DAC_GDAC_R_LIN', 'DAC_GDAC_M_LIN', 'DAC_LDAC_LIN', 'VCAL_HIGH', 'VCAL_MED',
    'GP_LVDS_ROUTE_0', 'GP_LVDS_ROUTE_1', 'TriggerConfig', 'CLK_DATA_DELAY',
    'CAL_EDGE_FINE_DELAY', 'ANALOG_INJ_MODE', 'VOLTAGE_TRIM_DIG', 'VOLTAGE_TRIM_ANA',
    'CML_CONFIG_SER_EN_TAP', 'CML_CONFIG_SER_INV_TAP', 'DAC_CML_BIAS_0',
    'DAC_CML_BIAS_1', 'DAC_CML_BIAS_2', 'MON_ADC_TRIM', 'ToT6to4Mapping', 'ToTDualEdgeCount',
    'ADC_OFFSET_VOLT', 'ADC_MAXIMUM_VOLT', 'TEMPSENS_IDEAL_FACTOR', 'VREF_ADC'
]

RD53B_Global_attrib = [
    'EN_CORE_COL_0', 'EN_CORE_COL_1', 'EN_CORE_COL_2', 'EN_CORE_COL_3',
    'EN_CORE_COL_CAL_0', 'EN_CORE_COL_CAL_1', 'EN_CORE_COL_CAL_2', 'EN_CORE_COL_CAL_3',
    'HITOR_MASK_0', 'HITOR_MASK_1', 'HITOR_MASK_2', 'HITOR_MASK_3',
    'PrecisionToTEnable_0', 'PrecisionToTEnable_1', 'PrecisionToTEnable_2', 'PrecisionToTEnable_3',
    'EnHitsRemoval_0', 'EnHitsRemoval_1', 'EnHitsRemoval_2', 'EnHitsRemoval_3',
    'EnIsolatedHitRemoval_0', 'EnIsolatedHitRemoval_1', 'EnIsolatedHitRemoval_2', 'EnIsolatedHitRemoval_3',
    'HIT_SAMPLE_MODE', 'EN_SEU_COUNT', 'CDR_CONFIG_SEL_PD', 'LOCKLOSS_CNT',
    'BITFLIP_WNG_CNT', 'BITFLIP_ERR_CNT', 'CMDERR_CNT', 'SKIPPED_TRIGGER_CNT',
    'HITOR_0_CNT', 'HITOR_1_CNT', 'HITOR_2_CNT', 'HITOR_3_CNT', 'READTRIG_CNT',
    'RDWRFIFOERROR_CNT', 'PIXELSEU_CNT', 'GLOBALCONFIGSEU_CNT'
]



