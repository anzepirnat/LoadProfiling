from __future__ import barry_as_FLUFL
#from cProfile import run
from typing import Sequence
from pyrsistent import v
import streamlit as st
st.set_page_config(page_title="Elderly Care Demo",page_icon="👵",layout="wide")
from PIL import Image
import time
import matplotlib.pyplot as plt
import numpy as np
import datetime
#import folium
#from streamlit_folium import st_folium







#m=folium.Map(location=[39.949610,-75.150282], zoom_start=16)
#folium.Marker([39.949610,-75.150282], popup="hej brigade", tooltip="hitite").add_to(m)
UserPic = Image.open("UserPic.png")
map = Image.open("map.png")
heatmap1=Image.open('heatmaps/heatmap1.png')
heatmap2=Image.open('heatmaps/heatmap2.png')
heatmap3=Image.open('heatmaps/heatmap3.png')
heatmap4=Image.open('heatmaps/heatmap4.png')
heatmap5=Image.open('heatmaps/heatmap5.png')
heatmap6=Image.open('heatmaps/heatmap6.png')
heatmap7=Image.open('heatmaps/heatmap7.png')
heatmap8=Image.open('heatmaps/heatmap8.png')
heatmap9=Image.open('heatmaps/heatmap9.png')
heatmap10=Image.open('heatmaps/heatmap10.png')
heatmap11=Image.open('heatmaps/heatmap11.png')
heatmap13=Image.open('heatmaps/heatmap13.png')
heatmap14=Image.open('heatmaps/heatmap14.png')
heatmap15=Image.open('heatmaps/heatmap15.png')
heatmap16=Image.open('heatmaps/heatmap16.png')
heatmap18=Image.open('heatmaps/heatmap18.png')
heatmap19=Image.open('heatmaps/heatmap19.png')
heatmap20=Image.open('heatmaps/heatmap20.png')


st.title("Elderly Care Dashboard")
st.subheader("About the app")
st.write("Elderly care dahsboard is a webapp developed to showcase usability of anomaly detection on NILM datasets.")
st.write("It works by studying the routine of the elders' electric device usage and then comparing current state to routine state. If current state deviates by the usual routine state enough on two devices at a time, it is recognised as an anomaly.")
st.write("It is designed to give user an insight into the last anomaly detected, its accuracy and date+time of it as it could mean an elder is unconscious and his life in danger. Accuracy provides the probability of said medical state.")
st.write("To provide help to the elderly there is a phone number, location and some basic personal information that a caregiver can use to aid.")
st.write("Beside that the webapp provides the quality of routine, on which the accuracy of our prediction depends on. It also features the best and worst 3 devices by their impact on the quality of routine. We suggest the elser tries to improve on the worst 3. We give our feedback about them in a user friendly manner, describing them with: excellent, very good, good, quite good, decent, usable, barely usable, useless (adjectives are listed descending by their desirability).")
st.subheader("Please start by choosing the house of interest.")
st.sidebar.header('Choose the house:')


if st.sidebar.button('House 1'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-11 18:00:00"
    chance=58.33
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 4 days ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0,0,0,0,0,1,0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([70.83333333333333, 70.0, 71.875, 61.76470588235294, 53.333333333333336, 50.0, 70.83333333333333])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap1)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='washing machine', value='very good')
    column2.metric(label='computer', value='good')
    column2.metric(label='television', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='washer dryer', value='decent')
    column2.metric(label='fridge', value='useless')
    column2.metric(label='freezer', value='useless')

if st.sidebar.button('House 2'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-11 14:00:00"
    chance=69.29
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 4 days ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0,0,0,0,0,1,0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([78.57142857142857, 78.08219178082192, 84.14634146341463, 82.05128205128206, 88.0, 79.48717948717949, 69.73684210526316])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap2)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='microwave', value='very good')
    column2.metric(label='kettle', value='very good')
    column2.metric(label='television', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='fan', value='quite good')
    column2.metric(label='audio system', value='usable')
    column2.metric(label='fridge freezer', value='useless')


if st.sidebar.button('House 3'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-15 08:00:00"
    chance=79.23
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 14h ago at: ")
    col1.error(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 0, 1, 0, 1, 1, 0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([82.65306122448979, 98.96907216494846, 89.7196261682243, 94.64285714285714, 86.60714285714286, 75.89285714285714, 75.47169811320755])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap3)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='television', value='very good')
    column2.metric(label='toaster', value='very good')
    column2.metric(label='kettle', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='microwave', value='quite good')
    column2.metric(label='fridge freezer', value='useless')
    column2.metric(label='freezer', value='useless')


if st.sidebar.button('House 4'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-15 16:00:00"
    chance=82.93
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 6h ago at: ")
    col1.error(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 0, 1, 1, 1, 1, 1])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([98.36065573770492, 94.91525423728814, 89.70588235294117, 86.66666666666667, 88.73239436619718, 84.28571428571429, 78.78787878787878])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap4)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='television', value='very good')
    column2.metric(label='tumble dryer', value='good')
    column2.metric(label='kettle', value='quite good')
    column2.subheader('Worst 3:')
    column2.metric(label='fridge', value='useless')
    column2.metric(label='freezer', value='useless')
    column2.metric(label='fridge freezer', value='useless')


if st.sidebar.button('House 5'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-08 04:00:00"
    chance=84.33
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 7 days ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 0, 1, 0, 0, 0, 0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([92.70833333333333, 94.68085106382979, 93.20388349514563, 93.85964912280701, 97.32142857142857, 94.64285714285714, 93.51851851851852])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap5)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='television', value='very good')
    column2.metric(label='washing machine', value='good')
    column2.metric(label='kettle', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='dish washer', value='decent')
    column2.metric(label='computer', value='barely usable')
    column2.metric(label='fridge freezer', value='useless')


if st.sidebar.button('House 6'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-13 16:00:00"
    chance=97.6
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 2 days ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 4, 0, 2, 0, 0, 0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([96.25, 93.25842696629213, 98.9247311827957, 87.1559633027523, 86.27450980392157, 91.34615384615384, 96.84210526315789])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap6)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='computer', value='very good')
    column2.metric(label='kettle', value='very good')
    column2.metric(label='washing machine', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='toaster', value='quite good')
    column2.metric(label='television', value='usable')
    column2.metric(label='freezer', value='useless')


if st.sidebar.button('House 7'):    
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-14 16:00:00"
    chance=81.76
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 1 day ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 1, 0, 1, 1, 1, 1])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([82.14285714285714, 73.4375, 91.30434782608695, 76.0, 69.11764705882354, 93.33333333333333, 86.36363636363636])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap7)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='television', value='very good')
    column2.metric(label='dish washer', value='very good')
    column2.metric(label='kettle', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='washing machine', value='good')
    column2.metric(label='fridge', value='useless')
    column2.metric(label='freezer', value='useless')


if st.sidebar.button('House 8'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-13 10:00:00"
    chance=85.33
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 2 days ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 2, 0, 0, 1, 2, 2])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([86.53846153846153, 96.42857142857143, 96.72131147540983, 96.875, 90.0, 78.33333333333333, 77.58620689655173])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap8)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='television', value='very good')
    column2.metric(label='washing machine', value='very good')
    column2.metric(label='microwave', value='quite good')
    column2.subheader('Worst 3:')
    column2.metric(label='fridge', value='useless')
    column2.metric(label='freezer', value='useless')
    column2.metric(label='computer', value='useless')


if st.sidebar.button('House 9'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-14 16:00:00"
    chance=74.78
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 1 day ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 3, 3, 0, 1, 1, 0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([93.18181818181819, 79.24528301886792, 83.33333333333333, 83.92857142857143, 88.46153846153847, 78.84615384615384, 77.55102040816327])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap9)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='kettle', value='very good')
    column2.metric(label='electric space heater', value='good')
    column2.metric(label='dish washer', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='audio system', value='quite good')
    column2.metric(label='television', value='useless')
    column2.metric(label='fridge freezer', value='useless')


if st.sidebar.button('House 10'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-15 18:00:00"
    chance=82.26
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 4h ago at: ")
    col1.error(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 2, 2, 0, 2, 2, 0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([41.666666666666664, 46.15384615384615, 46.42857142857143, 46.666666666666664, 39.285714285714285, 60.714285714285715, 65.38461538461539])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap10)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='dish washer', value='good')
    column2.metric(label='washing machine', value='quite good')
    column2.metric(label='food processor', value='usable')
    column2.subheader('Worst 3:')
    column2.metric(label='toaster', value='useless')
    column2.metric(label='television', value='useless')
    column2.metric(label='freezer', value='useless')


if st.sidebar.button('House 11'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-15 20:00:00"
    chance=78.2
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 2h ago at: ")
    col1.error(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 0, 0, 0, 0, 0, 0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([84.0909090909091, 86.66666666666667, 95.23809523809524, 86.36363636363636, 73.33333333333333, 66.66666666666667, 80.0])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap11)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='audio system', value='quite good')
    column2.metric(label='kettle', value='quite good')
    column2.metric(label='dish washer', value='quite good')
    column2.subheader('Worst 3:')
    column2.metric(label='fridge', value='useless')
    column2.metric(label='microwave', value='useless')
    column2.metric(label='broadband router', value='useless')


if st.sidebar.button('House 13'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-03-10 06:00:00"
    chance=95.53
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 35 days ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0,0,0,0,0,0,0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([77.77777777777777, 92.10526315789474, 97.6470588235294, 91.66666666666667, 91.66666666666667, 86.27450980392157])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap13)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='unknown', value='excellent')
    column2.metric(label='kettle', value='very good')
    column2.metric(label='dish washer', value='very good')
    column2.subheader('Worst 3:')
    column2.metric(label='broadband router', value='very good')
    column2.metric(label='television', value='good')
    column2.metric(label='microwave', value='usable')


if st.sidebar.button('House 14'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-15 20:00:00"
    chance=91.95
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 2h ago at: ")
    col1.error(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0,0,0,0,0,0,0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'])
    y2 = np.array([94.44444444444444, 97.61904761904762, 94.87179487179488, 90.47619047619048, 92.3076923076923, 94.87179487179488])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap14)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='washing machine', value='very good')
    column2.metric(label='toaster', value='very good')
    column2.metric(label='television', value='very good')
    column2.subheader('Worst 3:')
    column2.metric(label='computer', value='decent')
    column2.metric(label='dish washer', value='decent')
    column2.metric(label='fridge freezer', value='useless')


if st.sidebar.button('House 15'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-15 14:00:00"
    chance=86.64
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 8h ago at: ")
    col1.error(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 2, 3, 1, 0, 3, 2])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([67.27272727272727, 63.492063492063494, 67.79661016949153, 55.38461538461539, 66.12903225806451, 46.15384615384615, 61.666666666666664])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap15)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='dehumidifier', value='good')
    column2.metric(label='television', value='good')
    column2.metric(label='washing machine', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='dish washer', value='quite good')
    column2.metric(label='computer', value='useless')
    column2.metric(label='fridge freezer', value='useless')

if st.sidebar.button('House 16'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-14 18:00:00"
    chance=81.19
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 1 day ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0,0,0,0,0,1,0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([78.46153846153847, 82.05128205128206, 90.625, 98.82352941176471, 90.21739130434783, 84.52380952380952])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap16)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='tumble dryer', value='very good')
    column2.metric(label='kettle', value='very good')
    column2.metric(label='washing machine', value='very good')
    column2.subheader('Worst 3:')
    column2.metric(label='microwave', value='useless')
    column2.metric(label='fridge freezer', value='useless')
    column2.metric(label='freezer', value='useless')


if st.sidebar.button('House 18'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-14 16:00:00"
    chance=82.69
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 1 day ago at: ")
    col1.info(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 1, 3, 1, 1, 1, 2])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([75.0, 79.3103448275862, 60.60606060606061, 72.22222222222223, 78.78787878787878, 43.333333333333336, 53.57142857142857])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap18)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='microwave', value='very good')
    column2.metric(label='breadmaker', value='good')
    column2.metric(label='games console', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='audio system', value='decent')
    column2.metric(label='television', value='useless')
    column2.metric(label='fridge freezer', value='useless')


if st.sidebar.button('House 19'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-15 10:00:00"
    chance=93.59
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 12h ago at: ")
    col1.error(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0, 1, 1, 1, 1, 4, 3])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([91.35802469135803, 83.52941176470588, 78.88888888888889, 83.83838383838383, 88.88888888888889, 67.77777777777777, 67.77777777777777])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap19)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='dish washer', value='very good')
    column2.metric(label='computer', value='very good')
    column2.metric(label='tumble dryer', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='microwave', value='barely usable')
    column2.metric(label='freezer', value='useless')
    column2.metric(label='fridge', value='useless')


if st.sidebar.button('House 20'):
    st.header("Last anomaly detected")
    col1,col2,col3=st.columns([2,2,2])
    t="2015-04-15 18:00:00"
    chance=77.78
    #st_data = st_folium(m,width=700,height=200)
    col1.subheader("happened 4h ago at: ")
    col1.error(t)
    col2.subheader('Date & Time')
    col2.metric(label="Date (d/m/y)", value="15.4.2015")
    col2.metric(label="Time", value="22:31")
    col2.subheader("accuracy of the prediction:")
    arr1 = np.array([chance,100-chance])
    fig1, ax1 = plt.subplots()
    ax1.pie(
        arr1,wedgeprops=dict(width=0.5), startangle=0,
        labels=['accurate', 'inaccurate'], explode=(0,0), shadow=False, 
        colors=['#99ff99','#66b3ff'],autopct='%1.1f%%', 
        textprops=dict(color="black", weight='bold', size='12')
    )
    plt.figure(figsize=(3,3))
    col2.pyplot(fig1)

    #col3.date_input("Date", datetime.date(2015,4,15))
    #col3.time_input("Time", datetime.time(22,15))
    col1.subheader('Personal info')
    col1.image(UserPic)
    col1.text('Name: Elizabeth Schwarz')
    col1.text('Age: 89')
    col1.text('Phone numnber: 031 254 985')
    col1.subheader('Location')
    col1.image(map)
    
    #------------------------------------------------------
    col3.header("Anomalies last week")
    x3 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y3 = np.array([0,0,0,0,0,0,0])
    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color='#6dd4a8')
    fig3, ax3 = plt.subplots(facecolor=("#E3F2FD"))
    ax3.bar(x3,y3,color='deepskyblue')
    ax3.set_xlabel('Days of the week', fontsize=13)
    ax3.set_ylabel('Number of anomalies', fontsize=13)
    plt.yticks(np.arange(0,max(y3)+1,1))
    col3.pyplot(fig3)

    col3.header("Routine")
    col3.write("This graph shows the routine over the span of one week. You can see on which days the routine is stronger and on which weaker.")
    x2 = np.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
    y2 = np.array([40.0, 63.63636363636363, 59.09090909090909, 44.0, 54.54545454545455, 45.45454545454545, 36.36363636363637])
    fig2, ax2 = plt.subplots(facecolor=("#E3F2FD"))
    plt.ylim(0,100)
    ax2.bar(x2,y2,color='deepskyblue')
    ax2.set_xlabel('Days of the week', fontsize=13)
    ax2.set_ylabel('Probability of discovering the anomaly [%]', fontsize=13)
    plt.yticks(np.arange(0,100+1,10))
    col3.pyplot(fig2)
    #-------------------------------------------------------
    st.header("Routine suggestions")
    column1,column2=st.columns([4,1])
    column1.write("This heatmap presents the activity of different deivices that are known to be in the household over the span of a day. Each rectangle shows the activity of 2 hours. You can use it to understand the routine on the devices and try improving it.")
    column1.image(heatmap20)
    column2.write("Here are the worst and best 3 devices. Try building a stronger routine on the worst ones and continue with the routine on the best ones.")
    column2.subheader('Best 3:')
    column2.metric(label='television', value='very good')
    column2.metric(label='tumble dryer', value='very good')
    column2.metric(label='washing machine', value='good')
    column2.subheader('Worst 3:')
    column2.metric(label='fridge freezer', value='useless')
    column2.metric(label='appliance', value='useless')
    column2.metric(label='pond pump', value='useless')