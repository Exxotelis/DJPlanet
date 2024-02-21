
import streamlit as st
import base64

st.set_page_config(page_title='DJ Planet', page_icon='🎧',
                   layout='wide', initial_sidebar_state='auto')
img_path = str(st.image('images/button.png', width=1, output_format="auto",))

logo_path = "images/button.png"

# Function to encode image file to base64


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Encode the logo image to base64
logo_base64 = get_base64_of_bin_file(logo_path)

st.markdown(f"""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<nav class="navbar sticky-top navbar-expand-lg bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
        <img src="data:image/png;base64,{logo_base64}" alt="DJPlanet" width="30" height="24" class="d-inline-block align-text-top">
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="Home" onclick="navigateTo('Home')">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="Techno" onclick="navigateTo('Techno')">Techno & Progressive House</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#" onclick="navigateTo('DeepHouse')">Deep House</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#" onclick="navigateTo('TechnoMusic')">Techno Music</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#" onclick="navigateTo('TranceMusic')">Trance Music</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#" onclick="navigateTo('DubstepMusic')">Dubstep Music</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)

# JavaScript function to handle navigation based on the clicked link
jscode = """
<script>
function navigateTo(page) {
    window.location.href = "/#"+page;
}
</script>
"""
# Render JavaScript code
st.markdown(jscode, unsafe_allow_html=True)

# Define the pages content


def home():
    pass


def techno():
    st.title('Techno & Progressive House Page')
    st.write('Welcome to the Techno & Progressive House Page!')


def deep_house():
    st.title('Deep House Page')
    st.write('Welcome to the Deep House Page!')


def techno_music():
    st.title('Techno Music Page')
    st.write('Welcome to the Techno Music Page!')


def trance_music():
    st.title('Trance Music Page')
    st.write('Welcome to the Trance Music Page!')


def dubstep_music():
    st.title('Dubstep Music Page')
    st.write('Welcome to the Dubstep Music Page!')


# Define a dictionary to map pages to their corresponding functions
pages = {
    'Home': home,
    'Techno': techno,
    'DeepHouse': deep_house,
    'TechnoMusic': techno_music,
    'TranceMusic': trance_music,
    'DubstepMusic': dubstep_music
}

# Get the page name from the URL hash
page_name = st.query_params.get('page', ['Home'])[0]

# Render the page content based on the page name
page_content = pages.get(page_name, home)
page_content()

col1, col2, col3 = st.columns([1, 4, 1.5])
with col2:

    st.title('DJ Planet')
    st.write('''Welcome to DJ Planet! This is a simple web app that allows you to explore the world of electronic music. 
        You can listen to music, read about the history of electronic music, 
        and even learn about some of the most famous DJs in the world.''')
    img_path = 'images/426721476_1566643367428971_6949001200681099155_n.jpg'
    st.image(img_path, width=480, output_format="auto",
             caption='DJ Planet', use_column_width=True)
st.divider()
audio_path = 'audio/deep-house-112301.mp3'
with col3:
    st.write('')
    st.write('')

    st.write('Deep House Music')
    st.audio(audio_path, format='audio/mp3')

    img_path = 'images/consola2.jpg'
    st.image(img_path, width=240, output_format="auto",
             caption='Deep House', use_column_width=True)
    st.write('Anatolia - Ethno Soul (Ambient Organic House) ')
    st.video('https://www.youtube.com/watch?v=HzRO1tnv49w')
    # prompt = st.chat_input("Say something")
    # if prompt:
    #     st.write(f"User has sent the following prompt: {prompt}")
with col1:
    st.write('')

    st.write('')


col4, col5, col6 = st.columns([1, 4, 1.5])

with col5:
    st.title('Melodic Techno & Progressive House Mix')
    st.write('''Electronic music is music that employs electronic musical instruments, digital instruments, or circuitry-based music technology in its creation. It includes both music made using electronic and electromechanical means (electroacoustic music).''')
    img_path = 'images/djplanet1_n.jpg'
    st.image(img_path, width=480, output_format="auto",
             caption='Electronic Music', use_column_width=True)
    st.write('Electronic music was a 20th-century development involving the reproduction of traditional performance mediums through electronic means, while it also evolved composition and performance of music that is not possible using traditional instruments. ')

with col6:
    st.write('Melodic Techno & Progressive House Mix')
    audio_path = 'audio/vocal-deep-house-denied-melancholic-summer-deep-original-mix-116078.mp3'
    st.audio(audio_path, format='audio/mp3')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.video('https://www.youtube.com/watch?v=XJktaXYRWBg')
    img_path = 'images/423944271_724895959751238_6038802035877936412_n.jpg'
    st.image(img_path, width=480, output_format="auto",
             caption='Electronic Music', use_column_width=True)
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
st.divider()
col7, col8, col9 = st.columns([1, 4, 1.5])
with col8:
    st.title('Techno Music')
    st.write('''Techno is a genre of electronic dance music that is characterized by a repetitive beat which is generally produced for use in a continuous DJ set. The central rhythm is often in common time (4/4), while the tempo typically varies between 120 and 150 beats per minute (bpm).''')
    img_path = 'images/techno.jpg'
    st.image(img_path, width=480, output_format="auto",
             caption='Techno Music', use_column_width=True)
    st.write('Techno is a form of electronic dance music that emerged in Detroit, Michigan, in the United States during the mid-to-late 1980s. ')
with col9:
    st.write('Techno Music')
    audio_path = 'audio/techno-music.mp3'
    st.audio(audio_path, format='audio/mp3')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.video('https://www.youtube.com/watch?v=E0Is_IL2_tc')
    img_path = 'images/techno2.jpg'
    st.image(img_path, width=480, output_format="auto",
             caption='Techno Music', use_column_width=True)

st.divider()
col10, col11, col12 = st.columns([1, 4, 1.5])
with col11:
    st.title('Trance Music')
    st.write('''Trance is a genre of electronic music that emerged from the British new-age music scene and the early 1990s German techno and hardcore scenes. At the same time, the genre was developing in the United Kingdom, it was also gathering a following in the Indian state of Goa. ''')
    img_path = 'images/trance.jpg'
    st.image(img_path, width=480, output_format="auto",
             caption='Trance Music', use_column_width=True)
    st.write('Trance music is characterized by a tempo generally lying between 120 and 150 bpm (BPM), repeating melodic phrases and a musical form that distinctly builds tension and elements throughout a track often culminating in 1 to 2 "peaks" or "drops". ')

with col12:
    st.write('Trance Music')
    audio_path = 'audio/trance-music.mp3'
    st.audio(audio_path, format='audio/mp3')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.video('https://www.youtube.com/watch?v=h9L-U-hg8x4')
    img_path = 'images/trance2.jpg'
    st.image(img_path, width=480, output_format="auto",
             caption='Trance Music', use_column_width=True)

st.divider()
col13, col14, col15 = st.columns([1, 4, 1.5])
with col14:
    st.title('Dubstep Music')
    st.write('''Dubstep is a genre of electronic dance music that originated in South London in the late 1990s. It is generally characterized by sparse, syncopated rhythmic patterns with prominent sub-bass frequencies
             !''')
    img_path = 'images/dubstep.jpg'
    st.image(img_path, width=480, output_format="auto",
             caption='Dubstep Music', use_column_width=True)
    st.write('The music website Allmusic has described Dubstep as "tightly coiled productions with overwhelming bass lines and reverberant drum patterns, clipped samples, and occasional vocals". ')
with col15:
    st.write('Dubstep Music')
    audio_path = 'audio/dubstep.mp3'
    st.audio(audio_path, format='audio/mp3')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.video('https://www.youtube.com/watch?v=0-1jEhT3umA')
    img_path = 'images/dubstep2.jpg'
    st.image(img_path, width=480, output_format="auto",
             caption='Dubstep Music', use_column_width=True)
