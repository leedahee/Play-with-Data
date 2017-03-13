import numpy as np
import pandas as pd
import csv
import glob
import os

def daff(raw):
    # extract row data from each columns
    vid=df1.loc[:,'VidTime']
    vel=df1.loc[:,'Velocity']
    bra=df1.loc[:,'Brake']
    lan=df1.loc[:,'LaneOffset']
    xpo=df1.loc[:,'XPos']
    ypo=df1.loc[:,'YPos']
    sce=df1.loc[:,'Scenario_Area']
    fra=df1.loc[:,'FRAME_NUM']
    gad=df1.loc[:,'GAZE_DIR_QUAL']
    gah=df1.loc[:,'GAZE_HEADING']
    gap=df1.loc[:,'GAZE_PITCH']
    fil=df1.loc[:,'FILTERED_GAZE_OBJ_NAME']
    evt=df1.loc[:,'EVT_Events']
    #dictionary for new dataframe
    ext_data={'VidTime': vid,'Velocity':vel, 'Brake':bra, 'LaneOffset':lan, 'XPos':xpo, 'YPos':ypo, 'Scenario_Area':sce, 'FRAME_NUM':fra, 'GAZE_DIR_QUAL':gad,'GAZE_HEADING':gad ,'GAZE_PITCH':gap, 'FILTERED_GAZE_OBJ_NAME':fil, 'EVT_Events': evt}
    df2=pd.DataFrame(ext_data, columns = ext_data.keys())
    return df2


# open files from folder
path='/Users/daheelee/BoxSync/Honda_data_Dahee/data/'
for df in glob.glob(os.path.join(path, '*.csv')):
    n=0
    #data frame
    df1=pd.read_csv(df)
    #extract certain columns
    df2=daff(df1)
    #split by scenario area
    for i in range(1,10):
        df3=df2.loc[df2['Scenario_Area']==i].reset_index(drop=False)
        try:
            if df3['Scenario_Area'][0] is not False:
                df3.to_csv('%s scenario %s.csv' % (df, i))
        except:
            df2.loc[df2['Scenario_Area']==str(i)].reset_index(drop=False).to_csv('%s scenario %s.csv' % (df, i))
        n+=1
        print ('\t','scenario',n,'\t') # should be 72
    print ('===========',df,'============')
