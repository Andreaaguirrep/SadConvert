__author__ = 'D. Oumbarek Espinos'
"""
Function to read SAD files and organize to feed into OCELOT
Version - 03/04/2025
"""

import numpy as np
import re as re

def LoadSAD2OCELOTLine(FilePath,Drlines='',BENDlines='',QsLines='',SXTLines='',CavLines='',MonitsLines=''):
    
    
    
    Consonants = "aAIqwrtyplkjhgfdszxcvbnmMNBVCXZLKJHGFDSPYTRWQ"
    
    
    with open(FilePath, 'r') as f:
        content = f.read()
    
    
    hlp = [line.strip() for line in content.split('\n')]
    FileThingsOrder = []
    
    Are_Ds = False
    try:
        Drift_st = [hlp[i].find('DRIFT') for i in range(len(hlp))]
        Drift_st = Drift_st.index(Drift_st==0)
        FileThingsOrder.append(Drift_st)
        Are_Ds = True
    except:
        print('No drifts section found')
    
    Are_Bs = False
    try:
        Bend_st = [hlp[i].find('BEND') for i in range(len(hlp))]
        Bend_st = Bend_st.index(Bend_st==0)
        FileThingsOrder.append(Bend_st)
        Are_Bs = True
    except:
        print('No bends section found')
    
    Are_Qs = False
    try:
        Qs_st = [hlp[i].find('QUAD') for i in range(len(hlp))]
        Qs_st = Qs_st.index(Qs_st==0)
        FileThingsOrder.append(Qs_st)
        Are_Qs = True
    except:
        print('No quads section found')
    
    Are_Ss = False
    try:
        Sxt_st = [hlp[i].find('SEXT') for i in range(len(hlp))]
        Sxt_st = Sxt_st.index(Sxt_st==0)
        FileThingsOrder.append(Sxt_st)
        Are_Ss = True
    except:
        print('No sexts section found')
    
    Are_Ms = False
    try:
        MLTS_st = [hlp[i].find('MULT') for i in range(len(hlp))]
        MLTS_st = MLTS_st.index(MLTS_st==0)
        FileThingsOrder.append(MLTS_st)
        Are_Ms = True
    except:
        print('No multipoles section found')
    
    Are_Cs = False
    try:
        Cavis_st = [hlp[i].find('CAVI') for i in range(len(hlp))]
        Cavis_st = Cavis_st.index(Cavis_st==0)
        FileThingsOrder.append(Cavis_st)
        Are_Cs = True
    except:
        print('No cavities section found')
    
    Are_MONs = False
    try:
        Monits_st = [hlp[i].find('MONI') for i in range(len(hlp))]
        Monits_st = Monits_st.index(Monits_st==0)
        FileThingsOrder.append(Monits_st)
        Are_MONs = True
    except:
        print('No monitors section found')
    
    Are_MAPs = False
    try:
        MAP_st = [hlp[i].find('MAP') for i in range(len(hlp))]
        MAP_st = MAP_st.index(MAP_st==0)
        FileThingsOrder.append(MAP_st)
        Are_MAPs = True
    except:
        print('No map section found')
    
    Are_MKs = False
    try:
        MRKS_st = [hlp[i].find('MARK') for i in range(len(hlp))]
        MRKS_st = MRKS_st.index(MRKS_st==0)
        FileThingsOrder.append(MRKS_st)
        Are_MKs = True
    except:
        print('No marks section found')
    
    Are_LINE = False
    try:
        LINE_st = [hlp[i].find('LINE') for i in range(len(hlp))]
        LINE_st = LINE_st.index(LINE_st==0)
        FileThingsOrder.append(LINE_st)
        Are_LINE = True
    except:
        print('No line section found')
    
    Are_FFS = False
    try:
        FFS_st = [hlp[i].find('FFS') for i in range(len(hlp))]
        FFS_st = FFS_st.index(FFS_st==0)
        FileThingsOrder.append(FFS_st)
        Are_FSS = True
    except:
        print('No FSS line found, chosing the end of the file')
        FFS_st = len(hlp)
        FileThingsOrder.append(FFS_st)
        Are_FSS = True
    
    FileThingsOrder.sort()
    
    if Are_Ds:
        Drift_end   = FileThingsOrder[FileThingsOrder.index(Drift_st)+1]
    if Are_Bs:
        Bend_end    = FileThingsOrder[FileThingsOrder.index(Bend_st)+1]
    if Are_Qs:
        Qs_end      = FileThingsOrder[FileThingsOrder.index(Qs_st)+1]
    if Are_Ss:
        Sxt_end     = FileThingsOrder[FileThingsOrder.index(Sxt_st)+1]
    if Are_Ms:
        MLTS_end    = FileThingsOrder[FileThingsOrder.index(MLTS_st)+1]
    if Are_Cs:
        Cavis_end   = FileThingsOrder[FileThingsOrder.index(Cavis_st)+1]
    if Are_MONs:
        Monits_end  = FileThingsOrder[FileThingsOrder.index(Monits_st)+1]
    if Are_MAPs:
        MAP_end  = FileThingsOrder[FileThingsOrder.index(MAP_st)+1]
    if Are_MKs:
        MRKS_end    = FileThingsOrder[FileThingsOrder.index(MRKS_st)+1]
    if Are_LINE:
        LINE_end    = FileThingsOrder[FileThingsOrder.index(LINE_st)+1]
  
            
    
    if Are_Ms:
        MULTLines = [MLTS_st, MLTS_end]
    else:
        MULTLines = -1
    
    if Are_MAPs:
        MapLines = [MAP_st, MAP_end]
    else:
        MapLines = -1
            
    if Drlines:
        Drift_st   = Drlines[0]
        Drift_end  = Drlines[1]
    else:
        if Are_Ds:
            Drlines = [Drift_st, Drift_end]
        else:
            Drlines = -1
            
    if BENDlines:
        Bend_st    = BENDlines[0]
        Bend_end   = BENDlines[1]
    else:
        if Are_Bs:
            BENDlines = [Bend_st, Bend_end]
        else:
            BENDlines = -1
            
    if QsLines:
        Qs_st      = QsLines[0]
        Qs_end     = QsLines[1]
    else:
        if Are_Qs:
            QsLines = [Qs_st, Qs_end]
        else:
            QsLines = -1
            
    if SXTLines:
        Sxt_st     = SXTLines[0]
        Sxt_end    = SXTLines[1]
    else:
        if Are_Ss:
            SXTLines = [Sxt_st, Sxt_end]
        else:
            SXTLines = -1
            
    if CavLines:
        Cavis_st   = CavLines[0]
        Cavis_end  = CavLines[1]
    else:
        if Are_Cs:
            CavLines = [Cavis_st, Cavis_end]
        else:
            CavLines = -1
            
    if MonitsLines:
        Monits_st  = MonitsLines[0]
        Monits_end = MonitsLines[1]
    else:
        if Are_MONs:
            MonitsLines = [Monits_st, Monits_end]
        else:
            MonitsLines = -1
            
    
    
    #**********************Drifts***************************************
    if np.max(Drlines)!=-1: 
        lines = [line.strip() for line in content.split('\n')[Drift_st:Drift_end]]  
        
        key_bool   = 0
        value_bool = 0
        Drifts = {}
        for line in lines[:]:
            
                    toto=re.split(r'[(),]+|=\(|DRIFT', line)
                    toto = [s for s in toto if s != '']
                    
                    for ii in toto:
                        if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                            ii = ii.replace(' ', '')
                            key = ii
        #                    print(ii)
                            key_bool = 1
                            
                        elif 'L =' in ii:
                            ii = ii.replace(' .', ' 0.')
                            tototo = re.split(r'[ =]+',ii)
                            
                            for ip in range(len(tototo)):
                                try:
                                    val = float(tototo[ip])
        #                            print(val)
                                    value_bool = 1
                                except:
                                    continue
                                        
                        if key_bool == 1 and value_bool==1:   
                            key_bool = 0
                            value_bool = 0
                            Drifts[key] = val
                            del key
                            del val
                            
                            

#**********************BENDS***************************************   
    if np.max(BENDlines)!=-1: 
        lines = [line.strip() for line in content.split('\n')[Bend_st:Bend_end]]  

        key_bool   = 0
        value_bool = 0
        Bends = {} #key: (L,ANGLE,Rotate,E1,E2,F1,Fringe)
         
        for line in lines[:]:  
            
                    toto = line.replace(' E1', '   E1')
                    toto = toto.replace(' ANGLE', '   ANGLE')
                    toto=re.split(r'[(),]+|=\(|  |  R| FR|BEND', toto)
                    toto = [s for s in toto if s != '']
                    toto = [s for s in toto if s != ' '] 
                    
                    val = np.zeros(7)*np.nan #(L,ANGLE,Rotate,E1,E2,F1,Fringe)
                    val[0] = 0.0
                    
                    for ii in toto:
                        if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                            ii = ii.replace(' ', '')
                            key = ii
                            print(ii)
                            key_bool = 1
                            
                        elif 'L =' in ii:
                            ii = ii.replace(' .', '0.')
                            tototo = re.split(r'[ =]+',ii)
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[0] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                            
                        elif 'OTATE =' in ii:
                            deg2rad = 1;
                            if 'DEG' in ii:
                                deg2rad = np.pi/180
                                ii = ii.replace('DEG', '')                        
                            ii = ii.replace(' .', '0.')                        
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'[OTATE=]+',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[2] = float(tototo[ip])*deg2rad
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                            
                        elif 'INGE =' in ii:
                            ii = ii.replace(' .', '0.')                        
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'[INGE=]+',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[6] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                            
                        elif 'ANGLE =' in ii:
                            ii = ii.replace(' .', '0.')                        
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'[ANGLE=]+',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[1] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                            
                        elif 'F1 =' in ii:
                            ii = ii.replace(' .', '0.')                        
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'F1=',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[5] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                            
                        elif 'E1 =' in ii:
                            ii = ii.replace(' .', '0.')                        
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'E1=',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[3] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                            
                        elif 'E2 =' in ii:
                            ii = ii.replace(' .', '0.')                        
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'E2=',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[4] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                                        
                    if key_bool == 1 and value_bool>=1:   
                        key_bool = 0
                        value_bool = 0
                        Bends[key] = val
                        del key
                        del val
                    
                     
   #**********************QUADS***************************************
    if np.max(QsLines)!=-1: 
        lines = [line.strip() for line in content.split('\n')[Qs_st:Qs_end]]  
        
        key_bool   = 0
        value_bool = 0
        Quads = {} #key: (L,K1,F1,FRINGE)
        
        for line in lines[:]:  
                    
                    toto = line.replace(' FRINGE', '   FRINGE')
                    toto = toto.replace(' K1', '   K1')
                    toto = toto.replace(' F1', '   F1')
                    toto=re.split(r'[(),]+|=\(|  |QUAD', toto)
                    toto = [s for s in toto if s != '']
                    toto = [s for s in toto if s != ' '] 
                    
                    val = np.zeros(4)*np.nan #(L,K1,F1,FRINGE)
                    
                    for ii in toto:
                        
                        
                        if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                            ii = ii.replace(' ', '')
                            key = ii
                            print(ii)
                            key_bool = 1    
                            
                        elif 'L =' in ii:
                            ii = ii.replace(' .', '0.')
                            tototo = re.split(r'[ =]+',ii)
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[0] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue    
                            
                        elif 'K1 =' in ii:
                            ii = ii.replace(' .', '0.')
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'K1=',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[1] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue 
                            
                        elif 'F1 =' in ii:
                            ii = ii.replace(' .', '0.')
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'F1=',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[2] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue 
                            
                        elif 'FRINGE =' in ii:
                            ii = ii.replace(' .', '0.')
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'[FRINGE=]+',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[3] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                                        
                    if key_bool == 1 and value_bool>=1:   
                        key_bool = 0
                        value_bool = 0
                        Quads[key] = val
                        del key
                        del val    
    
    
#**********************Sexts***************************************
    if np.max(SXTLines)!=-1: 
        lines = [line.strip() for line in content.split('\n')[Sxt_st:Sxt_end]]  
        
        key_bool   = 0
        value_bool = 0
        Sexts = {} #key: (L,K2,Rotate)
        
        for line in lines[:]:  # skip the first line (assuming it's a header)
                    
                    
                    toto = line.replace(' ROTATE', '   ROTATE')
                    toto = toto.replace(' K2', '   K2')
                    toto=re.split(r'[(),]+|=\(|  |SEXT', toto)
                    toto = [s for s in toto if s != '']
                    toto = [s for s in toto if s != ' '] 
                    
                    val = np.zeros(3)*np.nan #(L,K2,Rotate)
                    
                    for ii in toto:
                        
                        
                        if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                            ii = ii.replace(' ', '')
                            key = ii
                            print(ii)
                            key_bool = 1    
                            
                        elif 'L =' in ii:
                            ii = ii.replace(' .', '0.')
                            tototo = re.split(r'[ =]+',ii)
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[0] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue    
                            
                        elif 'K2 =' in ii:
                            ii = ii.replace('=.', '=0.')
                            ii = ii.replace('=-.', '=-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'K2=',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[1] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue 
                            
                        elif 'ROTATE =' in ii:
                            deg2rad = 1;
                            if 'DEG' in ii:
                                deg2rad = np.pi/180
                                ii = ii.replace('DEG', '')                        
                            ii = ii.replace('=.', '=0.')
                            ii = ii.replace('=-.', '=-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'[ROTATE=]+',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[2] = float(tototo[ip])*deg2rad
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                                        
                    if key_bool == 1 and value_bool>=1:   
                        key_bool = 0
                        value_bool = 0
                        Sexts[key] = val
                        del key
                        del val    
    
#**********************Cavi***************************************
    if np.max(CavLines)!=-1: 
        lines = [line.strip() for line in content.split('\n')[Cavis_st:Cavis_end]]  
        
        key_bool   = 0
        value_bool = 0
        CAVS = {} #key: (L,VOLT,PHI,FREQ)
        
        for line in lines[:]:  # skip the first line (assuming it's a header)
                    
                    
                    toto = line.replace(' FREQ', '   FREQ')
                    toto = toto.replace(' PHI', '    PHI')
                    toto = toto.replace(' VOLT', '   VOLT')
                    toto= re.split(r'[(),]+|=\(|  |CAVI', toto)
                    toto = [s for s in toto if s != '']
                    toto = [s for s in toto if s != ' '] 
                    
                    val = np.zeros(4)*np.nan #(L,VOLT,PHI,FREQ)
                    
                    for ii in toto:
                        
                        
                        if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                            ii = ii.replace(' ', '')
                            key = ii
                            print(ii)
                            key_bool = 1    
                            
                        elif 'L =' in ii:
                            ii = ii.replace('=.', '0.')
                            tototo = re.split(r'[ =]+',ii)
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[0] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue    
                            
                        elif 'VOLT =' in ii:
                            ii = ii.replace('=.', '=0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'VOLT=',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[1] = float(tototo[ip])*1e-9
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue 
                            
                        elif 'PHI =' in ii:
                            ii = ii.replace('=.', '=0.')
                            ii = ii.replace('-.', '-0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'PHI=',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[2] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue 
                            
                        elif 'FREQ =' in ii:
                            ii = ii.replace('=.', '=0.')
                            ii = ii.replace(' ', '')
                            tototo = re.split(r'[FREQ=]+',ii)
                            tototo = [s for s in tototo if s != '']
                            
                            for ip in range(len(tototo)):
                                try:
                                    val[3] = float(tototo[ip])
        #                            print(val)
                                    value_bool += 1
                                except:
                                    continue
                                        
                    if key_bool == 1 and value_bool>=1:   
                        key_bool = 0
                        value_bool = 0
                        CAVS[key] = val
                        del key
                        del val    
    
#**********************MONITOR***************************************
    if np.max(MonitsLines)!=-1: 
        lines = [line.strip() for line in content.split('\n')[Monits_st:Monits_end]]  
        
        key_bool   = 0
        value_bool = 0
        Monits = {} #key: ( )
        
        for line in lines[:]:  # skip the first line (assuming it's a header)
                    
                    
                    toto= re.split(r'[(),]+|=\(|  |MONI', line)
                    toto = [s for s in toto if s != '']
                    toto = [s for s in toto if s != ' '] 
                    
                    val = np.zeros(1)*np.nan #()
                    
                    for ii in toto:
                        
                        
                        if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                            ii = ii.replace(' ', '')
                            key = ii
                            print(ii)
                            key_bool = 1    
                            
                        
                                        
                    if key_bool == 1:   
                        key_bool = 0
                        value_bool = 0
                        Monits[key] = val
                        del key
                        del val   
    

#**********************MULTS***************************************
    if np.max(MULTLines)!=-1: 
        lines = [line.strip() for line in content.split('\n')[MLTS_st:MLTS_end]]  
        
#        key_bool   = 0
#        value_bool = 0
#        Mult = {} #key: (L,VOLT,PHI,FREQ)
        		
        for line in lines[:]:  # skip the first line (assuming it's a header)
            key_bool   = 0
            value_bool = 0
            
            toto = line.replace(' FREQ', '   FREQ')
            toto = toto.replace(' PHI', '    PHI')
            toto = toto.replace(' VOLT', '   VOLT')
            toto = toto.replace(' ROTATE', '   ROTATE')
            toto = toto.replace(' K2', '   K2')
            toto = toto.replace(' K1', '   K1')
            toto = toto.replace(' FRINGE', '   FRINGE')
            toto = toto.replace(' K1', '   K1')
            toto = toto.replace(' F1', '   F1')
            toto = toto.replace(' E1', '   E1')
            toto = toto.replace(' E2', '   E2')
            toto = toto.replace(' ANGLE', '   ANGLE')
            toto= re.split(r'[(),]+|=\(|  |MULT', toto)
            toto = [s for s in toto if s != '']
            toto = [s for s in toto if s != ' '] 
            
            combined_str = ' '.join(toto)            
#            hlpp = [hlp.find('K2') for hlp in toto] #is it a Sext?
            if 'K2' in combined_str:                
                val = np.zeros(3)*np.nan #(L,K2,Rotate)                
                for ii in toto:
                    if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                        ii = ii.replace(' ', '')
                        key = ii
                        print(ii)
                        key_bool = 1    
                        
                    elif 'L =' in ii:
                        ii = ii.replace(' .', '0.')
                        tototo = re.split(r'[ =]+',ii)
                        
                        for ip in range(len(tototo)):
                            try:
                                val[0] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue    
                        
                    elif 'K2 =' in ii:
                        ii = ii.replace('=.', '=0.')
                        ii = ii.replace('=-.', '=-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'K2=',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[1] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue 
                        
                    elif 'ROTATE =' in ii:
                        deg2rad = 1;
                        if 'DEG' in ii:
                            deg2rad = np.pi/180
                            ii = ii.replace('DEG', '')                        
                        ii = ii.replace('=.', '=0.')
                        ii = ii.replace('=-.', '=-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'[ROTATE=]+',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[2] = float(tototo[ip])*deg2rad
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                                    
                if key_bool == 1 and value_bool>=1:   
                    key_bool = 0
                    value_bool = 0
                    Sexts[key] = val
                    del key
                    del val    
    
#            hlpp = [hlp.find('ANGLE') for hlp in toto] #is it a Bend?
            elif 'ANGLE' in combined_str:
                val = np.zeros(7)*np.nan #(L,ANGLE,Rotate,E1,E2,F1,Fringe)
                val[0] = 0.0
                
                for ii in toto:
                    if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                        ii = ii.replace(' ', '')
                        key = ii
                        print(ii)
                        key_bool = 1
                        
                    elif 'L =' in ii:
                        ii = ii.replace(' .', '0.')
                        tototo = re.split(r'[ =]+',ii)
                        
                        for ip in range(len(tototo)):
                            try:
                                val[0] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                        
                    elif 'OTATE =' in ii:
                        deg2rad = 1;
                        if 'DEG' in ii:
                            deg2rad = np.pi/180
                            ii = ii.replace('DEG', '')                        
                        ii = ii.replace(' .', '0.')                        
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'[OTATE=]+',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[2] = float(tototo[ip])*deg2rad
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                        
                    elif 'INGE =' in ii:
                        ii = ii.replace(' .', '0.')                        
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'[INGE=]+',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[6] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                        
                    elif 'ANGLE =' in ii:
                        ii = ii.replace(' .', '0.')                        
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'[ANGLE=]+',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[1] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                        
                    elif 'F1 =' in ii:
                        ii = ii.replace(' .', '0.')                        
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'F1=',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[5] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                        
                    elif 'E1 =' in ii:
                        ii = ii.replace(' .', '0.')                        
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'E1=',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[3] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                        
                    elif 'E2 =' in ii:
                        ii = ii.replace(' .', '0.')                        
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'E2=',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[4] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                                    
                if key_bool == 1 and value_bool>=1:   
                    key_bool = 0
                    value_bool = 0
                    Bends[key] = val
                    del key
                    del val
                
#            hlpp = [hlp.find('VOLT') for hlp in toto] #is it a Cavi?
            elif 'VOLT' in combined_str:                
                val = np.zeros(4)*np.nan #(L,VOLT,PHI,FREQ)                
                for ii in toto:                    
                    if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                        ii = ii.replace(' ', '')
                        key = ii
                        print(ii)
                        key_bool = 1    
                        
                    elif 'L =' in ii:
                        ii = ii.replace('=.', '0.')
                        tototo = re.split(r'[ =]+',ii)
                        
                        for ip in range(len(tototo)):
                            try:
                                val[0] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue    
                        
                    elif 'VOLT =' in ii:
                        ii = ii.replace('=.', '=0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'VOLT=',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[1] = float(tototo[ip])*1e-9
    #                            print(val)
                                value_bool += 1
                            except:
                                continue 
                        
                    elif 'PHI =' in ii:
                        ii = ii.replace('=.', '=0.')
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'PHI=',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[2] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue 
                        
                    elif 'FREQ =' in ii:
                        ii = ii.replace('=.', '=0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'[FREQ=]+',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[3] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                                    
                if key_bool == 1 and value_bool>=1:   
                    key_bool = 0
                    value_bool = 0
                    CAVS[key] = val
                    del key
                    del val    
    
#            hlpp = [hlp.find('K1') for hlp in toto] #is it a Q?
            elif 'K1' in combined_str:                
                val = np.zeros(4)*np.nan #(L,K1,F1,FRINGE)                
                for ii in toto:      
                    if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                        ii = ii.replace(' ', '')
                        key = ii
                        print(ii)
                        key_bool = 1    
                        
                    elif 'L =' in ii:
                        ii = ii.replace(' .', '0.')
                        tototo = re.split(r'[ =]+',ii)
                        
                        for ip in range(len(tototo)):
                            try:
                                val[0] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue    
                        
                    elif 'K1 =' in ii:
                        ii = ii.replace(' .', '0.')
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'K1=',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[1] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue 
                        
                    elif 'F1 =' in ii:
                        ii = ii.replace(' .', '0.')
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'F1=',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[2] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue 
                        
                    elif 'FRINGE =' in ii:
                        ii = ii.replace(' .', '0.')
                        ii = ii.replace('-.', '-0.')
                        ii = ii.replace(' ', '')
                        tototo = re.split(r'[FRINGE=]+',ii)
                        tototo = [s for s in tototo if s != '']
                        
                        for ip in range(len(tototo)):
                            try:
                                val[3] = float(tototo[ip])
    #                            print(val)
                                value_bool += 1
                            except:
                                continue
                                    
                if key_bool == 1 and value_bool>=1:   
                    key_bool = 0
                    value_bool = 0
                    Quads[key] = val
                    del key
                    del val
                    
                    
#            hlpp = [hlp.find('L') for hlp in toto] #is it a Drift?
            elif 'L' in combined_str:                
#                Drifts = {}
                for ii in toto:
                    if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                        ii = ii.replace(' ', '')
                        key = ii
                        key_bool = 1
                        
                    elif 'L =' in ii:
                        ii = ii.replace(' .', ' 0.')
                        tototo = re.split(r'[ =]+',ii)
                        
                        for ip in range(len(tototo)):
                            try:
                                val = float(tototo[ip])
                                value_bool = 1
                            except:
                                continue
                                    
                    if key_bool == 1 and value_bool==1:   
                        key_bool = 0
                        value_bool = 0
                        Drifts[key] = val
                        del key
                        del val
                                    
                
            
        
#**********************MARKS***************************************
    lines = [line.strip() for line in content.split('\n')[MRKS_st:MRKS_end]]  
    
    key_bool   = 0
    value_bool = 0
    MRKS = {} #key: ( )
    
    for line in lines[:]:  # skip the first line (assuming it's a header)
                
                
                toto= re.split(r'[(),]+|=\(|  |MARK', line)
                toto = [s for s in toto if s != '']
                toto = [s for s in toto if s != ' '] 
                
                val = np.zeros(1)*np.nan #()
                
                for ii in toto:
                    
                    
                    if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                        ii = ii.replace(' ', '')
                        key = ii
                        print(ii)
                        key_bool = 1    
                        
                    
                                    
                if key_bool == 1:   
                    key_bool = 0
                    value_bool = 0
                    MRKS[key] = val
                    del key
                    del val     
    
#**********************MAP***************************************
    if np.max(MapLines)!=-1: 
        lines = [line.strip() for line in content.split('\n')[MAP_st:MAP_end]]  
        
        key_bool   = 0
        value_bool = 0
        MAP = {} #key: ( )
        
        for line in lines[:]:  # skip the first line (assuming it's a header)
                    
                    
                    toto= re.split(r'[(),]+|=\(|  |MAP', line)
                    toto = [s for s in toto if s != '']
                    toto = [s for s in toto if s != ' '] 
                    
                    val = np.zeros(1)*np.nan #()
                    
                    for ii in toto:
                        
                        
                        if ii.replace(' ', '')[0] in Consonants and not '=' in ii:
                            ii = ii.replace(' ', '')
                            key = ii
                            print(ii)
                            key_bool = 1    
                            
                        
                                        
                    if key_bool == 1:   
                        key_bool = 0
                        value_bool = 0
                        MAP[key] = val
                        del key
                        del val    
                      
#**********************LINE***************************************
    lines = [line.strip() for line in content.split('\n')[LINE_st:LINE_end]] 
    
    starting = np.array([lines[i].find('=') for i in range(len(lines))])
    if max(starting)>=0:
        starting = np.argwhere(starting >= 0)[0]+1
        starting = starting[0]
    else:
        starting=0
    
    
    lines = "  ".join(lines[starting:-1])    

    toto = lines.replace(' L', '   L')
    toto= re.split(r';[(),]+|=\(|  ', toto)
    toto = [s for s in toto if s != '']
    toto = [s for s in toto if s != ' '] 
    
    for NKey, Nval in MRKS.items():
        [toto.pop(k) for k in range(len(toto)-1,-1,-1) if toto[k].find(NKey)>=0]
    
    if Are_MAPs:
        for NKey, Nval in MAP.items():
            [toto.pop(k) for k in range(len(toto)-1,-1,-1) if toto[k].find(NKey)>=0]
        
    
    [toto.pop(k) for k in range(len(toto)-1,-1,-1) if toto[k].find(')')>=0]
    [toto.pop(k) for k in range(len(toto)-1,-1,-1) if toto[k].find(';')>=0]
                        
    if np.max(CavLines)==-1:  
        return Monits, [], Sexts, Quads, Bends, Drifts, toto
    else:
        return Monits, CAVS, Sexts, Quads, Bends, Drifts, toto