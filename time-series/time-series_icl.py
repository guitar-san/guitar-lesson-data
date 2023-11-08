#上位ラベルの色付け
#conda のpy369環境で実装できる（python=3.9.13）

import pandas as pd
import datetime
import plotly.express as px
import plotly.io as pio
import numpy as np
import plotly.colors
from datetime import timedelta
import matplotlib
import plotly.graph_objects as go
import streamlit as st
import xlwings

df= pd.read_csv('./resource_data/LS1-1.csv')

total_time=sum((df['end']-df['start']).dt.total_seconds()/60) #合計時間
df_m=df[(df['Speaker']=='Music')]
df_t=df[(df['Speaker']=='T-Speech')]
df_s=df[(df['Speaker']=='S-Speech')]   
m_time=sum((df_m['end']-df_m['start']).dt.total_seconds()/60) #演奏時間
t_time=sum((df_t['end']-df_t['start']).dt.total_seconds()/60) #教師の発話時間
s_time=sum((df_s['end']-df_s['start']).dt.total_seconds()/60) #生徒の発話時間
m_ratio=(m_time/total_time)*100 #稼働率
t_ratio=(t_time/total_time)*100 #稼働率
s_ratio=(s_time/total_time)*100 #稼働率

fig= px.timeline(df, x_start="start", x_end="end", y="Speaker",
                 #category_orders={"Speaker":["Music","T-Speech","S-Speech"]},
                 color="ICL", color_discrete_map={'Giving Subjective Information':'blue',
                                                      'Giving Objective Information':'orange',
                                                      'Asking Question':'gray',
                                                      'Giving Feedback':'yellow',
                                                      'Giving Practice':'lightskyblue',
                                                      'Giving Advice':'forestgreen',
                                                      '-':'black'})#色分け
                  
fig.update_traces(textposition="inside", orientation="h", showlegend=False)
fig.update_xaxes(linecolor='black', gridcolor='white',mirror=False, ticks='inside',
                 tickfont=dict(size=16), title='Time')
fig.update_yaxes(categoryorder='total ascending', linecolor='black', gridcolor='lightgray',
                 mirror=False, tickfont=dict(size=16), title_font_size=16)
fig.update_layout(plot_bgcolor="white", width=700, height=450)
fig.update_xaxes(rangeslider_visible=True)
fig.show()