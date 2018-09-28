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
@purpose: this files contain a main method to call each function in class DataUtils in order to clean data
@code environment: ubuntu 18.01
"""

from dataUtils import DataUtils;

# the main method to call each function in Datautils class
if __name__ == '__main__':
    # to call a DataUtils class
    dataUtil = DataUtils();
    # pass data address to class to get a dataframe
    messyData = dataUtil.readFiles('./SIIM2016_Messy_Fake_EMRdata.csv');
    print(messyData);

    #print data under resource column and show without duplicate with the number of each kind of data
    print("showing data under resource:");
    print(dataUtil.printCDataWoutDu(messyData,"resource"));

    print();
    #select TRCT1 under resource column
    print("showing data with resource name = \'TRCT1\'");
    resourceTRCT1 = dataUtil.findDataUnCol(messyData,"TRCT1","resource");
    print(resourceTRCT1);

    print()
    #pring procedure description for TRCT1
    print("showing TRCT1's procedure description")
    print(dataUtil.printCDataWoutDu(resourceTRCT1,"procedure_description"));


    print();
     #select BRCTRMG under resource column
    print("showing data with resource name = \'BRCTRMG\'");
    print(dataUtil.findDataUnCol(messyData,"BRCTRMG","resource"));

    print();
    #rename BRCTRMG to UMG1 in resource column, names parameter must use dictionary data form
    messyData = dataUtil.renameColData(messyData,"resource",dict([("BRCTRMG","UMG1")]));
    print("showing data under resource:");
    print(dataUtil.printCDataWoutDu(messyData,"resource"));

    print();
    #change the rest resource names
    names = dict([("Mammo-2","CMG1"),("XRAY","UCR1"),("MAINCR","CCR1"),("MRI_MAIN","UMR1"),("newMRI","CMR1"),("FAST_MR","PMR1"),("TRCT1","TCT1")
                  ,("TRCT2","TCT2"),("CT_MAIN","UCT1"),("newCT","CCT1"),("FAST_CT","PCT1")]);
    messyData = dataUtil.renameColData(messyData,"resource",names);
    print("showing data under resource:");
    print(dataUtil.printCDataWoutDu(messyData,"resource"));


    print();
    #split resource into two columns : location and modality
    messyData = dataUtil.splitColIntoTwo(messyData,"resource","location","modality");
    print(messyData);

    print();
    #change arrival_time to arrival_date
    messyData = dataUtil.changeData(messyData,"arrival_time","arrival_date");
    print(messyData);

    print();
    #delete certain columns
    #print(messyData.columns);
    deleteColNames = ["first_final_time","first_image_time","complete_time","patient_gender","arrival_time","dob","id","resource"]
    messyData = dataUtil.deleteCol(messyData,deleteColNames);
    print(messyData);

    print();
    deleteColNames2 = ["accession","MRN","patient_name"];
    messyData = dataUtil.deleteCol(messyData,deleteColNames2);
    print((messyData))

    messyData.to_csv("refined_data.csv",index=False,encoding='utf8');
