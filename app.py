import warnings
warnings.filterwarnings('ignore')

from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import (data_engineer_agent,
                    technical_analysis_agent,
                    nlp_researcher_agent,
                    risk_analysis_agent,
                    advisor_agent)
from tasks import (gather_data,
                   technical_analysis,
                   fundamental_and_sentimental_analysis,
                   risk_analysis,
                   investment_advise)
import streamlit as st

from pathlib import Path
import datetime
import os

st.subheader(":robot_face: Stock Analysis Crew")
st.caption("A Multi-Agentic AI system created by [Jay Shah](https://www.linkedin.com/in/jay-shah-qml) with :heart:")


with st.sidebar:
    
    with st.expander(label='User Inputs', expanded=False):

        OPENAI_API_KEY = st.text_input("OPENAI API KEY", key="key1", type="password")

        SERPER_API_KEY = st.text_input("SERPER API KEY", key="key2", type="password",help="Allows the Agents to do Google Search")

        temperature = st.slider(label='Temperature',min_value=0.0,max_value=2.0,value=0.0,step=0.1,help='Lesser value means less randomness in the output and makes output reproducible.')
        
        company = st.text_input(label='Company Name',value='Deloitte')

        start_date = st.date_input(label='Start Date',value=datetime.date(2024,1,1))

        end_date = st.date_input(label='End Date',value=datetime.date.today())

        uploaded_files = st.file_uploader(label='Upload files for fundamental analysis',
                                          accept_multiple_files=True,type=['pdf'])
        
        if uploaded_files is not None:
            try:
                for uploaded_file in uploaded_files:
                    save_path = Path(r'inhouse data',uploaded_file.name)
                    with open(save_path,'wb') as w:
                        w.write(uploaded_file.getvalue())
            except Exception as e:
                st.error(f'Exception Occured! \n {e}')

    analyze_button = st.button(label='Analyze')

    reset_button = st.button(label='Reset', type='primary')


    st.write('[Github](https://github.com/Jayshah25/Stock-Analysis-Crew)')

    st.write('[Get your Serper API key](https://serper.dev/)')

    st.write('[Get your OpenAI API key](https://platform.openai.com/account/api-keys)')

    st.write('[Connect with Author on LinkedIn](https://www.linkedin.com/in/jay-shah-qml/)')

if reset_button:
    st.rerun()

if analyze_button:

    with st.spinner('Waiting for output...'):

        stock_analysis_crew = Crew(
                                tasks=[gather_data,
                                       technical_analysis,
                                       fundamental_and_sentimental_analysis,
                                       risk_analysis,
                                       investment_advise],
                                agents=[data_engineer_agent,
                                        technical_analysis_agent,
                                        nlp_researcher_agent,
                                        risk_analysis_agent,
                                        advisor_agent],
                                manager_agent=ChatOpenAI(model="gpt-3.5-turbo", 
                                                            temperature=temperature),
                                process=Process.hierarchical,
                                verbose=True
                                )
        
        inputs = {
            'stock': company,
            'start_date': str(start_date),
            'end_date' : str(end_date)
        }

        results = stock_analysis_crew.kickoff(inputs=inputs)

        st.markdown(results)