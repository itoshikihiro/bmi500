# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Jie Lin
# Python 3

#coding=utf-8
"""
@version: 1.0
@author: Jie Lin
@Mail: jlin246@emory.edu
@file: dataUtils.py
@time: 09/27/2018 4:08pm
@purpose: this files contain a class called DataUtils, which is used to clean data
@code environment: ubuntu 18.01
"""
import pandas as pd

class DataUtils:

    #read a file and return a dataframe
    def readFiles(self, addStr):
        data = pd.read_csv(addStr);
        returnDf = pd.DataFrame(data);
        return returnDf;

    #print a column of data without duplicate
    def printCDataWoutDu(self,df,colname):
        return df.groupby(df[colname],as_index=False).size();

    #find a specific date under certain column
    def findDataUnCol(self,df,dataname,colname):
        return df.loc[df[colname].isin([dataname])];

    #rename all data matched oriname to newname in certain colname
    def renameColData(self,df,colname,names):
        returnDf = df;
        for oriname,newname in names.items():
            returnDf = returnDf.replace({colname:{oriname:newname}});
        return returnDf;

    #spliting a column into two without changing the original column, and append two two columns
    def splitColIntoTwo(self,df,colname,newname1,newname2):
        returnDf = df;
        returnDf[newname1],returnDf[newname2]=zip(*returnDf[colname].map(lambda x: [x[0],x[1:]]))
        return returnDf;

    #specifically change time data
    def changeData(self,df,colname,newname):
        returnDf = df;
        returnDf[newname]=pd.to_datetime(returnDf[colname],format='%Y-%m-%dT%H:%M:%SZ').dt.strftime('%m/%d/%Y');
        return returnDf;

    #delete columns
    def deleteCol(self,df,*colnames):
        returnDf = df.drop(*colnames,axis=1);

        return returnDf;
