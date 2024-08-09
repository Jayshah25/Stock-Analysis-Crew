import warnings
warnings.filterwarnings('ignore')

import streamlit as st
from pathlib import Path
import datetime
import os

st.subheader(":robot_face: Stock Analysis Crew")
st.caption("A Multi-Agentic AI system created by [Jay Shah](https://www.linkedin.com/in/jay-shah-qml) with :heart:")


with st.sidebar:
    
    with st.expander(label='User Inputs', expanded=False):

        OPENAI_API_KEY = st.text_input("OPENAI API KEY", key="key1", type="password")

        SERPER_API_KEY = st.text_input("SERPER API KEY", key="key2", type="password")

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

    analyze_button = st.button(label='Analyze', type='primary')

    st.text(f'[Github](https://github.com/Jayshah25)')