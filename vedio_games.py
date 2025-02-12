import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
st.set_page_config(layout="wide")
df = pd.read_csv('Video_Games.csv')

#creata tabs 

tab1,tab2,tab3,tab4=st.tabs(["Platforms","global sales","Genre","Publisher and Developer"])

#------------------------------------------------------------------------------------------

# create fillters

#experience=st.sidebar.multiselect("Choose the experience",df["experience_level"].unique(),default=df["experience_level"].unique())
#msk1 = df["experience_level"].isin(experience)
#experience_fillter = df[msk1]


# ---------------------------------------------------------------------------------------------------------


# jobs tab

with tab1:
    
    st.markdown("""
    <style>
    .centered {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
#-------------------------------------------------------------------------------- 
    
    st.markdown('<h1 class="centered">Platforms</h1>', unsafe_allow_html=True)




    
    st.plotly_chart(px.violin(df, x='Genre', y='Critic_Score', color='Platform',
             hover_name='Name', title='Distribution of Critic Scores by Genre and Platform'))
    st.plotly_chart( px.scatter_matrix(data_frame=df, dimensions=['Global_Sales', 'Critic_Score', 'User_Score'],
                        color='Platform', title='Scatter Matrix of Sales and Scores by Platform'))
        
    col1,col2=st.columns(2)
    
    with col1:
        topglobal = df[['Name', 'Platform', 'Global_Sales']].sort_values(by="Global_Sales", ascending=False)
        topglobal = topglobal.head(30)
        platform_counts = topglobal['Platform'].value_counts().reset_index()
        platform_counts.columns = ['Platform', 'Count']
        st.plotly_chart(px.pie(platform_counts, values='Count', names='Platform', 
             title='Top 30 Games by Global Sales - Platform Distribution',
             labels={'Platform': 'Platform', 'Count': 'Number of Games'}))

    with col2:
            
        platform_pct = df['Platform'].value_counts(normalize=True) * 100
        platform_pct_df = platform_pct.reset_index()
        platform_pct_df.columns = ['Platform', 'Percentage']
        st.plotly_chart(px.bar(platform_pct_df, x='Platform', y='Percentage', 
             title='Percentage of Games Released by Platform',
             labels={'Percentage': 'Percentage of games released', 'Platform': 'Platform'}))
#######################################################################       

#employee tab

with tab2:
    st.markdown("""
    <style>
    .centered {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
#-------------------------------------------------------------------------------- 
    
    st.markdown('<h1 class="global sales</h1>', unsafe_allow_html=True)

    year_counts = df.groupby("Year_of_Release").size().reset_index()
    year_counts.columns = ['Year_of_Release', 'Number_of_Releases']

    st.plotly_chart(px.line(year_counts, x='Year_of_Release', y='Number_of_Releases', 
    title='Number of Video Game Releases per Year',
    labels={'Year_of_Release': 'Year', 'Number_of_Releases': 'Number of Releases'}))


    col1,col2=st.columns(2)

    with col1:
        topeu = df[['Name', 'Platform', 'EU_Sales']].sort_values(by="EU_Sales", ascending=False).head(30)
        st.plotly_chart(px.bar(topeu, x='Name', y='EU_Sales', title='Top 30 Games by EU Sales', labels={'EU_Sales': 'Sales in EU', 'Name': 'Game Name'}))

        topother = df[['Name', 'Platform', 'Other_Sales']].sort_values(by="Other_Sales", ascending=False).head(30)
        st.plotly_chart(px.bar(topother, x='Name', y='Other_Sales', title='Top 30 Games by Other Sales', labels={'Other_Sales': 'Sales in Other Regions', 'Name': 'Game Name'}))



    
    with col2:

        topjap = df[['Name', 'Platform', 'JP_Sales']].sort_values(by="JP_Sales", ascending=False).head(30)
        st.plotly_chart(px.bar(topjap, x='Name', y='JP_Sales', title='Top 30 Games by JP Sales', labels={'JP_Sales': 'Sales in Japan', 'Name': 'Game Name'}))

        topna = df[['Name', 'Platform', 'NA_Sales']].sort_values(by="NA_Sales", ascending=False).head(30)
        st.plotly_chart(px.bar(topna, x='Name', y='NA_Sales', title='Top 30 Games by NA Sales', labels={'NA_Sales': 'Sales in North America', 'Name': 'Game Name'}))

#######################################################################       
    
with tab3:
    st.markdown("""
    <style>
    .centered {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
#-------------------------------------------------------------------------------- 
    
    st.markdown('<h1 class="Genre</h1>', unsafe_allow_html=True)


    st.plotly_chart(px.bar(data_frame=df, x='Genre', y='Global_Sales', color='Platform',hover_name='Name', title='Total Sales by Genre and Platform'))

    st.plotly_chart(px.scatter(data_frame=df, x='Critic_Score', y='Global_Sales', size='EU_Sales',color='Genre', hover_name='Name',title='Relationship between Critic Scores, Global Sales, and Genre'))
#######################################################################################################################

with tab4:
    st.markdown("""
    <style>
    .centered {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
#-------------------------------------------------------------------------------- 
    
    st.markdown('<h1 class="Publisher and Developer</h1>', unsafe_allow_html=True)


    games_per_developer = df['Developer'].value_counts().reset_index()
    games_per_developer.columns = ['Developer', 'Number of Games']
    
    games_per_publisher = df['Publisher'].value_counts().reset_index()
    games_per_publisher.columns = ['Publisher', 'Number of Games']
    
    # الحصول على أفضل 10 مطورين وناشرين
    top_10_developers = games_per_developer.head(10)
    top_10_publishers = games_per_publisher.head(10)
    
    # إنشاء رسم بياني لأفضل 10 مطورين
    fig_developers = px.bar(
        top_10_developers,
        x='Developer',
        y='Number of Games',
        text='Number of Games',
        title='Top 10 Developers by Number of Games',
        labels={'Developer': 'Developer', 'Number of Games': 'Number of Games'},
        color='Developer'
    )
    
    # إنشاء رسم بياني لأفضل 10 ناشرين
    fig_publishers = px.bar(
        top_10_publishers,
        x='Publisher',
        y='Number of Games',
        text='Number of Games',
        title='Top 10 Publishers by Number of Games',
        labels={'Publisher': 'Publisher', 'Number of Games': 'Number of Games'},
        color='Publisher'
    )
    
    # تحديث التخطيط لتحسين القراءة
    fig_developers.update_traces(textposition='outside')
    fig_developers.update_layout(
        xaxis_title='Developer',
        yaxis_title='Number of Games',
        showlegend=False
    )
    
    fig_publishers.update_traces(textposition='outside')
    fig_publishers.update_layout(
        xaxis_title='Publisher',
        yaxis_title='Number of Games',
        showlegend=False
    )
    
    # عرض الرسوم البيانية في Streamlit
    st.plotly_chart(fig_developers, use_container_width=True)
    st.plotly_chart(fig_publishers, use_container_width=True)


    
    

    
