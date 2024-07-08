import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Christopher Zeuch",
    page_icon="👋",
    layout="wide"
)

st.title('Hello 👋 I\'m :orange[Christopher], a :blue[QA Engineer] from South Africa 🇿🇦')

# col1, col2, col3, col4 = st.columns(4)
# with col1:
#     if col1.button("🗃️ GitHub", key='button1'):
#         js = """
#         <script>
#         window.open("https://github.com/Hiccup-za?tab=repositories", "_blank").focus();
#         </script>
#         """
#         components.html(js)
# with col2:
#     if col2.button("💼 LinkedIn", key='button2'):
#         js = """
#         <script>
#         window.open("https://www.linkedin.com/in/christopher-zeuch", "_blank").focus();
#         </script>
#         """
#         components.html(js)
# with col3:
#     if col3.button("🗞️ Substack", key='button3'):
#         js = """
#         <script>
#         window.open("https://qualityengineering.substack.com/", "_blank").focus();
#         </script>
#         """
#         components.html(js)
# with col4:
#     st.empty()

containerAbout = st.container()
containerAbout1, containerAbout2 = containerAbout.columns(2)

with containerAbout1:
    containerAbout1Content = containerAbout1.container()
    containerAbout1Content.markdown('''                          
                                    ## About Me

                                    I'm a hardworking and highly autonomous individual with a very deep passion for Quality Assurance and Engineering.
                                    I've worked for various companies and startups; with products ranging from PoCs and MVPs to large production systems in fintech and financial forecasting.

                                    Having spent the last few years working exclusively with startups; my go-to "style" is lean and lightweight, enabling me to adjust test strategies as the business grows.

                                    I can work solo or as part of a team, both are enjoyable.
                                    I've also had the privilege of leading a small QA team that worked on various start-ups, where I gained experience in leading and mentoring.

                                    I love learning new things and keep my eyes open for new and exciting tech via X (formerly Twitter) and YouTube.
                                    I spend my spare time working on side projects and gaming.
                                    ''')

with containerAbout2:
    containerAbout2Content = containerAbout2.container()
    containerAbout2Content.markdown('''
                                    ## Current Tech Stack

                                    - 🎟️ ClickUp
                                    - ✨ Cursor with gpt-4o
                                    - ⌨️  iTerm2
                                    - 🐙 GitKraken
                                    - 🌻 Loom
                                    - 🐍 Python
                                    - 🐉 SeleniumBase
                                    - 🔭 Streamlit
                                    ''')

st.divider()

content1, content2, content3 = st.columns(3)

with content1:
    container1 = content1.container()
    container1.markdown('## 👨‍💻 Work Experience')
    container1.markdown('''
                        #### :orange[<u>Kohort</u>]
                        - **Lead QA Engineer** · Apr 2023 - Present
                        ''', unsafe_allow_html=True)
    container1.markdown('''
                        #### :orange[<u>The Delta</u>]
                        - **Lead QA Engineer** · Apr 2022 - Apr 2023  
                        - **Senior QA Engineer** · May 2021 - March 2022
                        ''', unsafe_allow_html=True)
    container1.markdown('''
                        #### :orange[<u>Entersekt</u>]
                        - **Senior Quality Engineer** · Mar 2021 - Apr 2021  
                        - **Senior Quality Engineering Analyst** · Dec 2019 - Feb 2021  
                        - **Quality Engineering Analyst** · Jun 2017 - Nov 2019  
                        - **Quality Assurance Analyst** · Feb 2016 - May 2017  
                        ''', unsafe_allow_html=True)
    container1.markdown('''
                        #### :orange[<u>Inspire Testing</u>]
                        - **Junior SQA Analyst** · Jun 2015 - Jan 2016
                        ''', unsafe_allow_html=True)

with content2:
    container2 = content2.container()
    container2.markdown('## 🧠 Technical Experience')
    container2.markdown('''
                        - API testing and automation
                        - Bare-metal server & applications testing
                        - Process roll-out and improvements
                        - Release planning and co-ordination
                        - TestOps
                        - Test plan creation, execution and reporting
                        - Testing environment setup & maintenance
                        - Manual & Automated test suite creation & maintenance
                        - Web application testing & automation
                        ''')

with content3:
    container3 = content3.container()
    container3Heading = container3.container()
    container3Heading.markdown('## 🖥️ Side Projects')

    container3Content1 = container3.container()
    container3Content1.markdown('#### :blue[<u>Testing Toolbox</u>]', unsafe_allow_html=True)
    if container3Content1.button("🔗 Click here to view the application.", key='content1'):
        js = """
        <script>
        window.open("https://testing-toolbox.streamlit.app/", "_blank").focus();
        </script>
        """
        components.html(js)
    container3Content1.markdown('''
                                A Streamlit application where I test out various ideas and concepts.
                                - 🎛️ Config Selector
                                - 💫 Dashboard
                                - 🪄 Generate Test Data
                                ''')