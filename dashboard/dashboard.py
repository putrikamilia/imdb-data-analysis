import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px


# Load data
df = pd.read_csv('/mount/src/imdb-data-analysis/movies.csv')

## FUNGSI-FUNGSI UNTUK ANALISIS DATA

# fungsi total movie
def total_movie(data):
    return data['primaryTitle'].nunique()

# fungsi rata-rata rating
def average_rating(data):
    return data['averageRating'].mean()

# fungsi total votes
def total_votes(data):
    return data['numVotes'].sum()

# fungsi rata rata durasi
def average_duration(data):
    return data['runtimeMinutes'].mean()

# plot jumlah movie berdasarkan tahun
def plot_movie_count(data):
    movie_count = data['startYear'].value_counts().reset_index()
    movie_count.columns = ['startYear', 'total_movies']
    movie_count = movie_count.sort_values(by='startYear')

    chart = alt.Chart(movie_count).mark_bar().encode(  # Ganti warna bar chart di sini
        x='startYear:O',
        y='total_movies:Q',
        color=alt.Color('total_movies:Q', scale=alt.Scale(scheme='inferno')),  # Gradasi Inferno
        tooltip=['startYear', 'total_movies']
    ).properties(
        width=400,
        height=400,
        title="Movies Count by Year"
    ).configure(
        background='#F5C518'  # Ganti dengan kode warna yang diinginkan
    )
    st.altair_chart(chart, use_container_width=True)

# fungsi pie chart genre
def plot_genre_pie_chart(data):
    # Explode list genre dan hitung frekuensi
    genre_count = data['genres'].explode().value_counts().reset_index()
    genre_count.columns = ['genre', 'count']
    genre_count = genre_count.sort_values(by='count', ascending=False)
    genre_count = genre_count.head(10)  # Ambil 10 genre teratas
    # Hitung total dan tambahkan kolom persentase
    total = genre_count['count'].sum()
    genre_count['percentage'] = (genre_count['count'] / total) * 100
    
    # Buat pie chart
    chart = alt.Chart(genre_count).mark_arc(innerRadius=50).encode(
        theta='count:Q',
        color=alt.Color('genre:N', scale=alt.Scale(scheme='inferno')),
        tooltip=['genre', 'count', alt.Tooltip('percentage:Q', format='.2f', title='Percentage (%)')]
    ).properties(
        width=500,
        height=500,
        title="Genre Distribution"
    ).configure(
        background='#F5C518'  # Warna background kuning IMDB
    ).configure_legend(
        orient='bottom',  
        titleFontSize=14,
        labelFontSize=12
    )
    
    st.altair_chart(chart, use_container_width=True)

# histogram bahasa film
def plot_language_histogram(data):
    language_count = data['language'].value_counts().reset_index()
    language_count.columns = ['language', 'count']
    language_count = language_count.sort_values(by='count', ascending=False)

    chart = alt.Chart(language_count).mark_bar().encode(  # Ganti warna bar chart di sini
        x='count:Q',
        y=alt.Y('language:O', sort='-x'),
        color=alt.Color('language:N', scale=alt.Scale(scheme='inferno')),
        tooltip=['language', 'count']
    ).properties(
        width=700,
        height=200,
        title="Movies Count by Language"
    ).configure(
        background='#F5C518'  # Ganti dengan kode warna yang diinginkan
    )
    st.altair_chart(chart, use_container_width=True)

# top 10 movie by rating
def plot_top_movies(data, n=10):
    top_movies = data.sort_values(by='averageRating', ascending=False).head(n)
    
    chart = alt.Chart(top_movies).mark_bar().encode(
        x=alt.X('averageRating:Q', title='Rating'),
        y=alt.Y('primaryTitle:N', sort='-x', title='Movie Title'),
        color=alt.Color('averageRating:Q', scale=alt.Scale(scheme='inferno')),
        tooltip=['primaryTitle', 'averageRating']
    ).properties(
        width=700,
        height=400,
        title=f"Top {n} Movies by Rating"
    ).configure(
        background='#F5C518'  # Ganti dengan kode warna yang diinginkan
    )
    
    st.altair_chart(chart, use_container_width=True)

# top 10 movie by votes
def plot_top_rated_movies(data, n=10):
    top_movies = data.sort_values(by='numVotes', ascending=False).head(n)
    
    chart = alt.Chart(top_movies).mark_bar().encode(
        x=alt.X('numVotes:Q', title='Rating'),
        y=alt.Y('primaryTitle:N', sort='-x', title='Movie Title'),
        color=alt.Color('numVotes:Q', scale=alt.Scale(scheme='inferno')),
        tooltip=['primaryTitle', 'numVotes']
    ).properties(
        width=700,
        height=400,
        title=f"Top {n} Movies by number of Votes"
    ).configure(
        background='#F5C518'  # Ganti dengan kode warna yang diinginkan
    )
    
    st.altair_chart(chart, use_container_width=True)

# distribusi durasi film
def plot_duration_distribution(data):
    chart = alt.Chart(data).mark_bar().encode(
        alt.X('runtimeMinutes:Q', bin=alt.Bin(maxbins=30), title='Duration (Minutes)'),
        y='count()',
        color=alt.Color('runtimeMinutes:Q', scale=alt.Scale(scheme='inferno')),  # Ganti warna bar chart di sini
        tooltip=['count()']
    ).properties(
        width=700,
        height=400,
        title="Distribution of Movie Durations"
    ).configure(
        background='#F5C518'  # Ganti dengan kode warna yang diing
    )
    
    st.altair_chart(chart, use_container_width=True)

# heatmap genre
def plot_genre_heatmap(data):
    genre_year = data.explode('genres').groupby(['startYear', 'genres']).size().reset_index(name='count')
    
    chart = alt.Chart(genre_year).mark_rect().encode(
        x='startYear:O',
        y='genres:N',
        color=alt.Color('count:Q', scale=alt.Scale(scheme='inferno')),
        tooltip=['startYear', 'genres', 'count']
    ).properties(
        width=700,
        height=400,
        title="Genre Popularity Over the Years"
    ).configure(
        background='#F5C518'  # Ganti dengan kode warna yang diinginkan
    )
    
    st.altair_chart(chart, use_container_width=True)

# hubungkan vote dan rating
def plot_rating_vs_votes(data):
    chart = alt.Chart(data).mark_circle(size=80).encode(
        x='averageRating:Q',
        y='numVotes:Q',
        size='numVotes:Q',
        color=alt.Color('averageRating:Q', scale=alt.Scale(scheme='redpurple')),  # Ganti warna scatter plot di sini
        tooltip=['primaryTitle', 'averageRating', 'numVotes']
    ).properties(
        width=700,
        height=500,
        title="Rating vs Number of Votes"
    ).configure(
        background='#F5C518'  # Ganti dengan kode warna yang diinginkan
    )
    
    st.altair_chart(chart, use_container_width=True)

# Top directors
def plot_top_directors(data, n=10):
    top_directors = data['directorsName'].explode().value_counts().head(n).reset_index()
    top_directors.columns = ['Director', 'Movie Count']
    
    chart = alt.Chart(top_directors).mark_bar().encode(
        x='Movie Count:Q',
        y=alt.Y('Director:N', sort='-x'),
        color=alt.Color('Movie Count:Q', scale=alt.Scale(scheme='inferno')),  # Ganti warna bar chart di sini
        tooltip=['Director', 'Movie Count']
    ).properties(
        width=700,
        height=400,
        title=f"Top {n} Directors by Number of Movies"
    ).configure(
        background='#F5C518'  # Ganti dengan kode warna yang diinginkan
    )
    
    st.altair_chart(chart, use_container_width=True)

# Top directors by rating
def plot_top_directors_rating(data, n=10):
    top_directors = data.groupby('directorsName')['averageRating'].mean().sort_values(ascending=False).head(n).reset_index()
    
    chart = alt.Chart(top_directors).mark_bar().encode(
        x='averageRating:Q',
        y=alt.Y('directorsName:N', sort='-x'),
        color=alt.Color('averageRating:Q', scale=alt.Scale(scheme='inferno')),  # Ganti warna bar chart di sini
        tooltip=['directorsName', 'averageRating']
    ).properties(
        width=700,
        height=400,
        title=f"Top {n} Directors by Average Rating"
    ).configure(
        background='#F5C518'  # Ganti dengan kode warna yang diinginkan
    )
    
    st.altair_chart(chart, use_container_width=True)

# Plot Treemap untuk Genre
def plot_genre_treemap(data):
    genre_df = data.explode('genres')  # Pecah genre list jadi baris terpisah
    genre_votes = genre_df.groupby('genres')['numVotes'].sum().reset_index()
    genre_votes.columns = ['Genre', 'Total Votes']

    fig = px.treemap(
        genre_votes,
        path=['Genre'],
        values='Total Votes',  
        title="Genre by Total Votes",
        color='Total Votes',
        color_continuous_scale='inferno'  # Skema warna merah
    )
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25), paper_bgcolor='#F5C518')
    st.plotly_chart(fig, use_container_width=True)


# wordcloud judul film
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_wordcloud_titles(data):
    text = ' '.join(data['primaryTitle'].dropna())
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='#F5C518',  # Ubah warna di sini (contoh: hitam)
        colormap='autumn'  # Ubah skema warna kata (opsional)
    ).generate(text)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

## DASHBOARD 

st.markdown(
    """
    <style>
    .stApp {
        background-color:#F5C518; /* Ganti dengan warna yang diinginkan */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar
with st.sidebar:
    st.image('imdb_logo-removebg-preview.png')
    
    st.title('Filter Data')

    # Date range selection menggunakan tahun
    min_year = int(df['startYear'].min())
    max_year = int(df['startYear'].max())

    start_year, end_year = st.slider(
        'Select Year Range',
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    # Pilihan genre
    df['genres'] = df['genres'].apply(eval)  # Ubah string seperti list menjadi tipe data list
    all_genres = df['genres'].explode().unique()    
    selected_genres = st.multiselect(
        'Select Genres',
        options=all_genres,
        default=['Drama', 'Comedy', 'Action', 'Horror', 'Romance', 'Thriller', 'Comedy']   # Secara default pilih semua genre
    )

    # Pilihan bahasa
    all_languages = df['language'].unique()
    selected_languages = st.multiselect(
        'Select Languages',
        options=all_languages,
        default=all_languages  # Secara default pilih bahasa Indonesia dan Inggris
    )

    # footer
    with st.sidebar:
        st.markdown('---')
        st.write('Developed by Putri Kamilia')
        st.write('Contact: putrikamilia975@gmail.com')

# Filter data berdasarkan rentang tahun
filtered_df = df[(df['startYear'] >= start_year) & (df['startYear'] <= end_year)]

# Filter data berdasarkan genre
if selected_genres:
    filtered_df = filtered_df[filtered_df['genres'].apply(lambda x: any(genre in x for genre in selected_genres))]

if selected_languages:
    filtered_df = filtered_df[filtered_df['language'].apply(lambda x: any(language in x for language in selected_languages))]

# Judul
st.title('IMDB Indonesian Movie Analysis')
st.write('''  
Welcome to the **IMDB Movies in Indonesia Data Analysis Dashboard**!  
This dashboard provides insights into movies available in Indonesia, including genres, runtime, language, ratings, and reviews.  
Explore interesting trends and patterns in the Indonesian movie industry!  
''')  


# count
def format_number(num):
    if num >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.1f}K"
    else:
        return str(num)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Movies", value=total_movie(filtered_df))
with col2:
    st.metric("Average Duration (Minutes)", value=f"{average_duration(filtered_df):.2f}")
with col3:
    st.metric("Average Rating", value=f"{average_rating(filtered_df):.2f}")
with col4:
    st.metric("Total Votes", value=format_number(total_votes(filtered_df)))

col1, col2 = st.columns([2, 1])
with col1:
    # plot jumlah movie berdasarkan tahun
    st.header("Movies by Year")
    plot_movie_count(filtered_df)

    # plot histogram bahasa film
    st.header("Movies by Language")
    plot_language_histogram(filtered_df)

with col2:
    # plot genre pie chart
    st.header("Movies by Genre")
    plot_genre_pie_chart(filtered_df)

# Top 10 movie
st.markdown("<h2 style='text-align: center;'>Top Movies</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    plot_top_movies(filtered_df, 10)
with col2:
    plot_top_rated_movies(filtered_df, 10)

# Heatmap genre
st.markdown("<h2 style='text-align: center;'>Genre Popularity Over the Years</h2>", unsafe_allow_html=True)
plot_genre_heatmap(filtered_df) 

st.markdown("<h2 style='text-align: center;'>Movie Duration and Genre Distribution</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    # Distribusi durasi film
    plot_duration_distribution(filtered_df) 
with col2:
    # Treemap untuk Directors
    plot_genre_treemap(filtered_df) 

# Hubungan rating dan votes
st.markdown("<h2 style='text-align: center;'>Rating vs Number of Votes</h2>", unsafe_allow_html=True)
plot_rating_vs_votes(filtered_df) 

# Top directors
st.markdown("<h2 style='text-align: center;'>Top Directors</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    plot_top_directors(filtered_df, 10)
with col2:
    plot_top_directors_rating(filtered_df, 10)

# Wordcloud judul film
st.markdown("<h2 style='text-align: center;'>Movie Titles Wordcloud</h2>", unsafe_allow_html=True)
plot_wordcloud_titles(filtered_df) 

