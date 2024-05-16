import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns 
from matplotlib import pyplot as plt

st.set_page_config(
    layout="wide",
    page_title="Freelancer Analytics",
    page_icon="📊"
)

@st.cache_data()
def load_data(path):
    df = pd.read_csv('upwork-jobs.csv')

with st.spinner('Processing upwork data'):
    df=pd.read_csv('upwork-jobs.csv')
with st.container():
    st.title('Freelancer Data-Analysis')
    st.image("https://futureskillsprime.in//sites/default/files/2021-03/Fundamentals%20of%20Data%20Analytics_Desktop_01_1200x630-16-min.jpg", caption='Freelancer Data Analysis')
    st.subheader("Data Summary",divider='red')
c1,c2,c3=st.columns(3)


total_vacancy=df.shape[0]
type_trend="Freelancer Jobs"

c1.metric("Total Post",total_vacancy)
c2.metric("Type",type_trend)
c1.subheader("Insight: ")
c1.text("""This app contains various freelancer 
analysis and its graphs based on total 
53058 number of post.
Total record in 2023 are 7.
Total record in 2024 are 53051.""")

st.header("Top 5 Countries by Number of Titles:",divider='rainbow')

st.subheader('Top 5 Countries:-', divider='blue')
country_counts = df.groupby('country')['title'].count().sort_values(ascending=False)
top_countries = pd.DataFrame(country_counts).head()

fig = px.bar(top_countries, x=top_countries.index, y='title', labels={'Number of Titles': 'Number of Titles'})
st.plotly_chart(fig, use_container_width=True)




st.header("Top 10 Countries by Number of Hourly Jobs:",divider='rainbow')
top_10_countries = df.groupby('country')['is_hourly'].count().sort_values(ascending=False).head(10)
df_plot = pd.DataFrame(top_10_countries)

# Plotting with Plotly Express
fig = px.pie(df_plot, values='is_hourly', names=df_plot.index, labels={'is_hourly': 'Count', 'index': 'Country'})
fig.update_traces(textinfo='percent+label')
fig.update_layout(title='Distribution of Hourly Jobs Across Top 10 Countries')
st.plotly_chart(fig, use_container_width=True)


st.header("Top 20 Titles by Number of Budgets:",divider='green')
top_20_titles = df.groupby('title')['budget'].count().sort_values(ascending=False).head(20)
df_plot = pd.DataFrame(top_20_titles).reset_index()

# Plotting with Plotly Express
fig_violin = px.violin(df_plot, y='title', x='budget',
                        labels={'budget': 'Count', 'title': 'Title'},
                        title='Distribution of Budgets Across Top 20 Titles',
                        orientation='h')
st.plotly_chart(fig_violin, use_container_width=True)

# df_country_count = df['country'].value_counts()
# df_country_count = df_country_count[df_country_count > 1000]
# df_country_count = df_country_count.sort_values(ascending=True)

# # Plotting with Plotly Express: Horizontal Bar Chart
# fig = px.bar(df_country_count, orientation='h', labels={'index': 'Country', 'value': 'Number of job postings'}, title='Number of Job Postings by Country')
# st.plotly_chart(fig, use_container_width=True)


# df_gigs_low = df[(df['is_hourly'] == True) & (df['hourly_low'] > 0)]['hourly_low']
# df_gigs_high = df[(df['is_hourly'] == True) & (df['hourly_low'] > 0)]['hourly_high']

# # Plotting with Plotly Express: Histogram
# fig = px.histogram(df_gigs_low, nbins=100, opacity=0.35, labels={'value': '$ per hour offered'}, title='Distribution of Hourly Rates')
# fig.add_trace(px.histogram(df_gigs_high, nbins=100, opacity=0.35).data[0])
# fig.update_layout(barmode='overlay', legend={'title': 'Rate'})
# st.plotly_chart(fig, use_container_width=True)

# st.markdown('<hr style="border-top: 2px solid red;">', unsafe_allow_html=True)
st.header("Number of Job Postings by Country & Distribution of Hourly Rates:", divider='red')
df_country_count = df['country'].value_counts()
df_country_count = df_country_count[df_country_count > 1000]
df_country_count = df_country_count.sort_values(ascending=True)

# Calculate hourly gigs with positive low hourly rates
df_gigs_low = df[(df['is_hourly'] == True) & (df['hourly_low'] > 0)]['hourly_low']
df_gigs_high = df[(df['is_hourly'] == True) & (df['hourly_low'] > 0)]['hourly_high']

# Split the app into two columns
col1, col2 = st.columns(2)

# Plotting Number of Job Postings by Country in the first column
with col1:
    st.markdown("**Number of Job Postings by Country:**")
    st.markdown('<hr style="border-top: 2px solid black;">', unsafe_allow_html=True)
    fig_country = px.bar(df_country_count, orientation='h', labels={'index': 'Country', 'value': 'Number of job postings'})
    st.plotly_chart(fig_country, use_container_width=True)

# Plotting Distribution of Hourly Rates in the second column
with col2:
    st.markdown("**Distribution of Hourly Rates:**")
    st.markdown('<hr style="border-top: 2px solid black;">', unsafe_allow_html=True)
    fig_hourly = px.histogram(df_gigs_low, nbins=100, opacity=0.35, labels={'value': '$ per hour offered'})
    fig_hourly.add_trace(px.histogram(df_gigs_high, nbins=100, opacity=0.35).data[0])
    fig_hourly.update_layout(barmode='overlay', legend={'title': 'Rate'})
    st.plotly_chart(fig_hourly, use_container_width=True)
