import pandas as pd
import plotly.express as px
import pymysql
import json
import os
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#streamlit page creation
st.set_page_config(page_title= "Phonepe Pulse Data Visualization ",                 
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   )
st.title(":violet[:iphone:**Phonepe Pulse Data Visualization**:bar_chart:]")
st.sidebar.title(":red[Overview of the Project]")
st.sidebar.caption(':blue[Phonepe-Pulse-Data-Visualization project is all about in short cloning the data from github repository and utilising the data for visualisation for betterunderstanding of users.Fetched required data using os library and preprocessed stored it into MySql Database using PyMySql.Created different options that user can select and get insights from it.Created Live geo Map, Analysing the data and visualizing it in 5 different charts based on the option which user selects]')

# Creating connection with mysql workbench
mydb = pymysql.connect(host="127.0.0.1",
                   user="root",
                   password="Joel@123",
                   database= "phonepe"
                  )
mydb.cursor()

#option menu
option = option_menu(menu_title=None,
                     options=['Phonepe Map','Analysis','Visualization'],
                     icons=['geo-alt', 'file-bar-graph', 'file-bar-graph'],
                     orientation='horizontal',
                     menu_icon="app-indicator",
                     styles={"nav-link": {"font-size": "25px", "text-align": "center", "margin": "-1px",
                                          "--hover-color": ""},
                             "nav-link-selected": {"background-color": "#9370DB"}})
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

if option =='Phonepe Map':
    col1, col2 = st.columns(2)
    with col1:
        map_type = st.selectbox('', options=['Transactions', 'Users'], label_visibility='collapsed',
                                placeholder='Select Transactions or Users', index=None)
    with col2:
        map_yr = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023], label_visibility='collapsed',
                                placeholder='Select a Year to view',index=None)
        
    # transaction :   
    if map_type == 'Transactions' and map_yr is not None:
        map_query = f'''select states,sum(transaction_count) Transactions,sum(transaction_amount) TotalAmount from map_tran
        where years={map_yr}
        group by states;'''
        df = pd.read_sql_query(map_query, mydb)
        fig = px.choropleth(df,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='states',
                            color="Transactions",
                            title=f'PhonePe India Transactions - {map_yr}',
                            color_continuous_scale='purples',
                            width=800, height=1000, hover_name='states')
        fig.update_geos(fitbounds="locations", visible=False)
        fig.show()
        st.plotly_chart(fig)

    elif map_type == 'Transactions' and map_yr is  None:
        map_query = f'''select states,sum(transaction_count) Transactions,sum(transaction_amount) from map_tran
        group by states;'''
        df = pd.read_sql_query(map_query, mydb)
        fig = px.choropleth(df,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='states',
                            color="Transactions",
                            title='PhonePe India Transactions',
                            color_continuous_scale='purples',
                            width=800, height=1000, hover_name='states')
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)   

    #Users :
        
    elif map_type == 'Users' and map_yr is not None:
        query = f'''select states,sum(Registered_users) Registerduser from map_user 
        where years = {map_yr} 
        group by states;'''
        df = pd.read_sql_query(query, mydb)
        fig = px.choropleth(df,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='states',
                            color="Registerduser",
                            title=f'PhonePe India Transactions - {map_yr}',
                            color_continuous_scale='greens',
                            width=800, height=1000, hover_name='states')
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)

    elif map_type == 'Users' and map_yr is None:
        query = f'''select states,sum(Registered_users) Registerduser from map_user 
        group by states;'''
        df = pd.read_sql_query(query, mydb)
        fig = px.choropleth(df,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='states',
                            color="Registerduser",
                            title='PhonePe India Transactions',
                            color_continuous_scale='greens',
                            width=800, height=1000, hover_name='states')
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)

# Dashboard for Analysis
elif option == 'Analysis':
    # Sidebar Buttons (SelectBox)
    with st.sidebar:
        st.header(":blue[Choose Type,Years and Quarter to do Analysis]")
        st.divider()
        opt, dummy = st.columns([5, 1])
        with opt:
            trans = st.selectbox('', options=['Transactions', 'Users'], index=None, placeholder='Type',
                                 label_visibility='collapsed')
            year = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023], placeholder='Year',
                                label_visibility='collapsed')
            quarter = st.selectbox('', options=[1, 2, 3, 4], placeholder='Quarter', label_visibility='collapsed')
    st.markdown(f'## ANALYSIS BASED ON :red[{year}] - QUARTER - :red[{quarter}]')


# When User selects transactions
    if trans == 'Transactions':
        tab1, tab2, tab3 = st.tabs(['Details', 'Category', 'TOP 10'])
        # Transaction Details Tab
        with tab1:
            st.markdown('#### :orange[PhonePe] :green[India]')
            col1, col2, col3 = st.columns(3)
            with col1:
                query1 = f'''select concat(sum(Transaction_Count)/10000000,' Cr') as trans from aggre_trans 
                where years={year} and quarter = {quarter};'''
                all_trans = pd.read_sql_query(query1, mydb)
                st.dataframe(all_trans, column_config={"trans": "Total Number of Transactions"}, hide_index=True)
            with col2:
                query2 = f'''select concat('₹ ',sum(Transaction_Amount)/10000000,' Cr') as value from aggre_trans 
                where years={year} and quarter={quarter};'''
                trans_val = pd.read_sql_query(query2, mydb)
                st.dataframe(trans_val, column_config={"value": "Total Payment Value"}, hide_index=True)
            with col3:
                query3 = f'''select concat('₹ ',sum(Transaction_Amount)/sum(Transaction_Count)) as avg from aggre_trans 
                where years={year} and quarter={quarter};'''
                avg_val = pd.read_sql_query(query3, mydb)
                st.dataframe(avg_val, column_config={"avg": "Average Payment Value"}, hide_index=True)
             # Transactions Category Tab
        with tab2:
                st.markdown(f"### :grey[Tables on Transaction Count and Payment Value based on the category]")
                col1, col2 = st.columns([4, 4])
                with col1:
                    query4 = f'''select transaction_type as mode , concat(sum(transaction_count)/100000,' lakh') as tc from aggre_trans 
                    where years=years and quarter=quarter group by transaction_type;'''
                    cat_count = pd.read_sql_query(query4, mydb)
                    st.dataframe(cat_count, column_config={"mode": "Type of Transaction", "tc": "No Of Transactions"},
                                hide_index=True)
                with col2:
                    query5 = f'''select transaction_type as mode , concat('₹',sum(transaction_amount)/10000000,' Cr') as amt from aggre_trans 
                    where years=years and quarter=quarter group by transaction_type;'''
                    cat_val = pd.read_sql_query(query5, mydb)
                    st.dataframe(cat_val, column_config={"mode": "Type of Transaction", "amt": "Transaction Value"},
                                hide_index=True)
        # Transaction Top-10 Tab
        with tab3:
            # Creating select box for top 10 based on transaction count and amount transferred
            select = st.selectbox('Select Option To Get TOP 10 :', options=['Number Of Transactions', 'Amount'])
            # Based on Transactions
            if select == "Number Of Transactions":
                # Top 10 States based on transaction
                if st.button("Top 10 States"):
                    st.markdown(
                        f"Top 10 States Based On :blue[Number Of Transactions] Made by :red[{year} - Q{quarter}]:")
                    query6 = f'''select dense_rank()over(order by sum(Transaction_Count) desc) as rnk,states as State,concat(sum(Transaction_Count)/10000000,' Cr') as tc from aggre_trans 
                    where years={year} and quarter={quarter} group by states order by rnk asc limit 10;'''
                    top_state = pd.read_sql_query(query6, mydb)
                    st.dataframe(top_state, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                # Top 10 Districts based on transaction
                if st.button("Top 10 Districts"):
                    st.markdown(
                        f"Top 10 Districts Based On :blue[Number Of Transactions] Made by :red[{year} - Q{quarter}]:")
                    query7 = f'''select dense_rank()over(order by transaction_count desc) as rnk, concat(transaction_count/100000, ' lakh') as tc from top_tran
                    where years={year} and quarter={quarter}  order by rnk asc limit 10;'''
                    top_district = pd.read_sql_query(query7, mydb)
                    st.dataframe(top_district, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                
                 # Based on Amount
            elif select == "Amount":
                # Top 10 states based on Amount
                if st.button("Top 10 States"):
                    st.markdown(f"Top 10 States Based On :blue[Transaction Amount] :red[{year} - Q{quarter}]:")
                    query6 = f'''select dense_rank()over(order by sum(Transaction_Amount) desc) as rnk,states as State,concat('₹ ',sum(Transaction_Amount)/10000000,' Cr') as amt from aggre_trans 
                    where years={year} and quarter={quarter} group by states order by rnk asc limit 10;'''
                    top_state = pd.read_sql_query(query6, mydb)
                    st.dataframe(top_state, column_config={"rnk": "Rank", "amt": "Payment Value"}, hide_index=True)    

                 # Top 10 Districts based on Amount
                if st.button("Top 10 Districts"):
                    st.markdown(f"Top 10 Districts Based On :blue[Transaction Amount] :red[{year} - Q{quarter}]:")
                    query7 = f'''select dense_rank()over(order by transaction_amount desc) as rnk, concat('₹ ',transaction_amount/10000000, ' Cr') as tc from top_tran 
                    where years={year} and quarter={quarter}  order by rnk asc limit 10;'''
                    top_district = pd.read_sql_query(query7, mydb)
                    st.dataframe(top_district, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                

# When the transaction type is Users
    elif trans == 'Users':
        tab1, tab2 = st.tabs(['Details', 'TOP 10'])
        # User Details
        with tab1:
            st.markdown(f'#### :grey[PhonePe Users Data In INDIA by Q{quarter} - {year}]')
            query9 = f'''select concat(sum(Registered_users)/10000000,' Cr') as users from map_user 
            where years={year} and quarter={quarter} group by years,quarter;'''
            usercount = pd.read_sql_query(query9, mydb)
            st.dataframe(usercount, column_config={"users": f"PhonePe users"}, hide_index=True)
            st.markdown("#### Total no of app opens in the selected period of time")
            query10 = f'''select case when sum(App_opens)=0 then 'N/A' else concat(sum(App_opens)/10000000, ' Cr') end as ao from map_user
            where years={year} and quarter ={quarter} group by years, quarter;'''
            app_opens = pd.read_sql_query(query10, mydb)
            st.dataframe(app_opens, column_config={"ao": f"App Opens"}, hide_index=True)   

    # User Top 10
        with tab2:
            # Top 10 User States
            if st.button("Top 10 States"):
                st.markdown(f'#### Top 10 States Based on Registered Users Q{quarter} - {year}:')
                query11 = (f'''select dense_rank()over(order by sum(Registered_users) desc)as rnk,states,concat(sum(Registered_users)/100000,' lakh') as reguser from top_user
                where years={year} and quarter={quarter} group by states order by rnk asc limit 10;''')
                state = pd.read_sql_query(query11, mydb)
                st.dataframe(state, column_config={"reguser": f"Registered Users"}, hide_index=True)
            # Top 10 User Districts
            if st.button("Top 10 Districts"):
                st.markdown(f'#### Top 10 District Based on Registered Users Q{quarter} - {year}:')
                query12 = f'''select dense_rank()over(order by Registered_users desc) as rnk,
                concat(Registered_users/100000,' lakh') as reguser from top_user
                where years={year} and quarter={quarter} order by rnk asc limit 10;'''
                dist = pd.read_sql_query(query12, mydb)
                st.dataframe(dist, column_config={"reguser": f"Registered Users"}, hide_index=True)
                      
elif option =='Visualization':
    col1, col2, col3 = st.columns(3)
    query1 = f'''select years,sum(transaction_amount) trans from aggre_trans
    group by years;'''
    data = pd.read_sql_query(query1, mydb)
    fig = px.pie(data,names='years', values='trans',width=500, height=1000, title='Total  Transaction Year Wise')
    st.plotly_chart(fig)

    st.markdown('#### Animated chart ')
    col1, col2,col3,col4 = st.columns([2,2,2,2])
    with col1:
        query2 = f'''select transaction_type,years,sum(transaction_count) as tc,
                    concat('₹',sum(Transaction_Amount)/10000000,' Cr') as amount from aggre_trans
                    group by transaction_type,years;'''
    df = pd.read_sql_query(query2, mydb)
    fig = px.bar(df, x='years', y='tc', color='transaction_type', hover_name='amount',
                    color_discrete_sequence=px.colors.sequential.Turbo, animation_frame='years', range_x=[2018, 2023],
                    range_y=[0, 50000000000], title='Transaction Count Vs Year')
    st.plotly_chart(fig)

    with col2:
        query3 = f'''select  distinct transaction_type categories,sum(transaction_amount) Amount from aggre_trans
    group by categories ;'''
    data = pd.read_sql_query(query3, mydb)
    fig = px.scatter(data, x='categories', y='Amount',
                    title='Categories Of Transaction Amounts')
    st.plotly_chart(fig)

    with col3:
        query4 = f'''select distinct states states,sum(Registered_users) Registereduser from map_user
        group by states;'''
        data = pd.read_sql_query(query4, mydb)
    fig = px.line(data, x='states', y='Registereduser',width=800, height=400,
    title='State Wise Registered User')
    st.plotly_chart(fig)

    with col4:
        query5 = f'''select years year,avg(transaction_count) avgtransaction from aggre_trans
        group by year;'''
        data = pd.read_sql_query(query5, mydb)
    fig = px.histogram(data,x='year',y='avgtransaction', nbins=30, title='Histogram Example')  
    st.plotly_chart(fig)
