import os
import json
import pandas as pd
import pymysql
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px


#aggre_transaction

path1 = "D:/visual studio code/phonepe/pulse/data/aggregated/transaction/country/india/state/"
agg_tran_list= os.listdir(path1)

columns1={"States": [], "Years": [], "Quarter": [], "Transaction_type":[], "Transaction_count":[], "Transaction_amount":[]}

for state in agg_tran_list:
    cur_states=path1+state+"/"
    agg_year_list=os.listdir(cur_states)

    for year in agg_year_list:
        cur_year=cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)

        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file, "r")
            
            A=json.load(data)

            for i in A["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                columns1["Transaction_type"].append(name)
                columns1["Transaction_count"].append(count)
                columns1["Transaction_amount"].append(amount)
                columns1["States"].append(' '.join(i.capitalize() for i in state.split('-')))
                columns1["Years"].append(year)
                columns1["Quarter"].append(int(file.strip(".json")))


aggre_trans = pd.DataFrame(columns1)

aggre_trans


#aggre_user

path2="D:/visual studio code/phonepe/pulse/data/aggregated/user/country/india/state/"
agg_user_list = os.listdir(path2)
columns2={"States": [], "Years": [], "Quarter":[], "Brands":[], "Transaction_count":[], "Percentage":[]}

for state in agg_tran_list:
    cur_states=path2+state+"/"
    agg_year_list=os.listdir(cur_states)

    for year in agg_year_list:
        cur_year=cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)


        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            B=json.load(data)

            try:
                for i in B["data"]["usersByDevice"]:
                    brand=i["brand"]
                    count=i["count"]
                    percentage=i["percentage"]
                    columns2["Brands"].append(brand)
                    columns2["Transaction_count"].append(count)
                    columns2["Percentage"].append(percentage)
                    columns2["States"].append(' '.join(i.capitalize() for i in state.split('-')))
                    columns2["Years"].append(year)
                    columns2["Quarter"].append(int(file.strip(".json")))
            
            except:
                pass


aggre_user = pd.DataFrame(columns2)


aggre_user


#map_transaction

path3 = "D:/visual studio code/phonepe/pulse/data/map/transaction/hover/country/india/state/"
map_tran_list = os.listdir(path3)

columns3={"States": [], "Years": [], "Quarter":[], "Districts":[], "Transaction_count":[], "Transaction_amount":[]}


for state in map_tran_list:
    cur_states= path3+state+"/"
    map_year_list= os.listdir(cur_states)
    
    for year in map_year_list:
        cur_year = cur_states+year+"/"
        map_file_list = os.listdir(cur_year)

        for file in map_file_list:
            cur_file = cur_year+file
            data=open(cur_file,"r")

            C= json.load(data)

            for i in C['data']['hoverDataList']:
                name=i["name"]
                count=i["metric"][0]["count"]
                amount=i["metric"][0]["amount"]
                columns3["Districts"].append(name)
                columns3["Transaction_count"].append(count)
                columns3["Transaction_amount"].append(amount)
                columns3["States"].append(' '.join(i.capitalize() for i in state.split('-')))
                columns3["Years"].append(year)
                columns3["Quarter"].append(int(file.strip(".json")))


map_tran=pd.DataFrame(columns3)


map_tran


#map_user

path4 = "D:/visual studio code/phonepe/pulse/data/map/user/hover/country/india/state/"
map_user_list = os.listdir(path4)

columns4={"States": [], "Years": [], "Quarter":[], "Districts":[], "Registered_users":[], "App_opens":[]}


for state in map_user_list:
    cur_states= path4+state+"/"
    map_year_list= os.listdir(cur_states)
    
    for year in map_year_list:
        cur_year = cur_states+year+"/"
        map_file_list = os.listdir(cur_year)

        for file in map_file_list:
            cur_file = cur_year+file
            data=open(cur_file,"r")

            D= json.load(data)

            for i in D["data"]["hoverData"].items():
                name=i[0]
                Users=i[1]['registeredUsers']
                App_opens=i[1]["appOpens"]
                columns4["Districts"].append(name)
                columns4["Registered_users"].append(Users)
                columns4["App_opens"].append(App_opens)
                columns4["States"].append(' '.join(i.capitalize() for i in state.split('-')))
                columns4["Years"].append(year)
                columns4["Quarter"].append(int(file.strip(".json")))


map_user= pd.DataFrame(columns4)


map_user


#top_transaction

path5 = "D:/visual studio code/phonepe/pulse/data/top/transaction/country/india/state/"
top_tran_list = os.listdir(path5)

columns5={"States": [], "Years": [], "Quarter":[], "Districts":[], "Transaction_count":[], "Transaction_amount":[]}


for state in top_tran_list:
    cur_states= path5+state+"/"
    top_year_list= os.listdir(cur_states)
    
    for year in top_year_list:
        cur_year = cur_states+year+"/"
        top_file_list = os.listdir(cur_year)

        for file in top_file_list:
            cur_file = cur_year+file
            data=open(cur_file,"r")

            E= json.load(data)

            for i in E["data"]["districts"]:
                name=i['entityName']
                count=i['metric']['count']
                amount=i['metric']['amount']
                columns5["Districts"].append(name)
                columns5["Transaction_count"].append(count)
                columns5["Transaction_amount"].append(amount)
                columns5["States"].append(' '.join(i.capitalize() for i in state.split('-')))
                columns5["Years"].append(year)
                columns5["Quarter"].append(int(file.strip(".json")))

            
top_tran = pd.DataFrame(columns5)

top_tran


#top_user

path6 = "D:/visual studio code/phonepe/pulse/data/top/user/country/india/state/"
top_user_list = os.listdir(path6)

columns6={"States": [], "Years": [], "Quarter":[], "Districts":[], "Registered_users":[]}


for state in top_user_list:
    cur_states= path6+state+"/"
    top_year_list= os.listdir(cur_states)
    
    for year in top_year_list:
        cur_year = cur_states+year+"/"
        top_file_list = os.listdir(cur_year)

        for file in top_file_list:
            cur_file = cur_year+file
            data=open(cur_file,"r")

            F= json.load(data)

            for i in F['data']['districts']:
                name=i['name']
                Users=i['registeredUsers']
                columns6["Districts"].append(name)
                columns6["Registered_users"].append(Users)
                columns6["States"].append(' '.join(i.capitalize() for i in state.split('-')))
                columns6["Years"].append(year)
                columns6["Quarter"].append(int(file.strip(".json")))
   

top_user=pd.DataFrame(columns6)


top_user


#datainsert agg_trans

mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Joel@123')
cursor=mydb.cursor()
cursor.execute('create database if not exists phonepe')

mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Joel@123',database='phonepe')
cursor=mydb.cursor()

cat='''create table if not exists  aggre_trans (
                       States varchar(100),
                       Years int,
                       Quarter int,
                       Transaction_type varchar(100),
                       Transaction_count  BIGINT,
                       Transaction_amount BIGINT)'''
cursor.execute(cat)
mydb.commit()

for index,row in aggre_trans.iterrows():
    insert_query ='''INSERT into aggre_trans(States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount) VALUES(%s,%s,%s,%s,%s,%s)'''
    values = (row['States'],row['Years'],row['Quarter'],row['Transaction_type'],row['Transaction_count'],row['Transaction_amount'])

    cursor.execute(insert_query,values)
    mydb.commit()


#data insert aggre_user

mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Joel@123',database='phonepe')
cursor=mydb.cursor()

cau='''create table if not exists aggre_user (
                                       States varchar(100),
                                       Years int,
                                       Quarter int,
                                       Brands varchar(100),
                                       Transaction_Count bigint,
                                       Percentage float)'''
cursor.execute(cau)

for index,row in aggre_user.iterrows():
    insert_query = '''INSERT into aggre_user( States, Years, Quarter, Brands, Transaction_count, Percentage) VALUES (%s,%s,%s,%s,%s,%s)'''
    values = (row['States'],row['Years'],row['Quarter'],row['Brands'],row['Transaction_count'],row['Percentage']) 

    cursor.execute(insert_query,values)
    mydb.commit()



#data insert map transaction
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Joel@123',database='phonepe')
cursor=mydb.cursor()

cmt='''create table if not exists map_tran (
                                       States varchar(100),
                                       Years int,
                                       Quarter int,
                                       Districts varchar(100),
                                       Transaction_count bigint,
                                       Transaction_amount float)'''
cursor.execute(cmt)

for index,row in map_tran.iterrows():
    insert_query ='''INSERT into map_tran(States, Years, Quarter, Districts, Transaction_count, Transaction_amount) VALUES(%s,%s,%s,%s,%s,%s)'''
    values = (row['States'],row['Years'],row['Quarter'],row['Districts'],row['Transaction_count'],row['Transaction_amount'])

    cursor.execute(insert_query,values)
    mydb.commit()

#data insert map user
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Joel@123',database='phonepe')
cursor=mydb.cursor()

cmu='''create table if not exists map_user (
                                       States varchar(100),
                                       Years int,
                                       Quarter int,
                                       Districts varchar(100),
                                       Registered_users bigint,
                                       App_opens bigint)'''
cursor.execute(cmu)

for index,row in map_user.iterrows():
    insert_query ='''INSERT into map_user(States, Years, Quarter, Districts, Registered_users, App_opens) VALUES(%s,%s,%s,%s,%s,%s)'''
    values = (row['States'],row['Years'],row['Quarter'],row['Districts'],row['Registered_users'],row['App_opens'])

    cursor.execute(insert_query,values)
    mydb.commit()


#insert top transaction
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Joel@123',database='phonepe')
cursor=mydb.cursor()

ctt='''create table if not exists top_tran (
                                       States varchar(100),
                                       Years int,
                                       Quarter int,
                                       Districts varchar(255),
                                       Transaction_count bigint,
                                       Transaction_amount bigint )'''
cursor.execute(ctt)

for index,row in top_tran.iterrows():
    insert_query ='''INSERT into top_tran(States, Years, Quarter, Districts, Transaction_count, Transaction_amount) VALUES(%s,%s,%s,%s,%s,%s)'''
    values = (row['States'],row['Years'],row['Quarter'],row['Districts'],row['Transaction_count'],row['Transaction_amount'])

    cursor.execute(insert_query,values)
    mydb.commit()

#insert top user
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Joel@123',database='phonepe')
cursor=mydb.cursor()

ctu='''create table if not exists top_user (
                                       States varchar(100),
                                       Years int,
                                       Quarter int,
                                       Districts varchar(255),
                                       Registered_users bigint
                                       )'''
cursor.execute(ctu)

for index,row in top_user.iterrows():
    insert_query ='''INSERT into top_user(States, Years, Quarter, Districts, Registered_users) VALUES(%s,%s,%s,%s,%s)'''
    values = (row['States'],row['Years'],row['Quarter'],row['Districts'],row['Registered_users'])

    cursor.execute(insert_query,values)
    mydb.commit()






