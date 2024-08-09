from crewai import Agent
from tools import (search_indicators, 
                   search_pandas_ta,
                   search_tool,
                   scrape_tool,
                   code_interpreter_tool,
                   )


data_engineer_agent= Agent(
            role="Data Engineer",
            goal="Validate the inputs provided by the user. For example, make sure "
            "the  provided company name actually exists, start date and end date are "
            "not the same and so on. After Validation, download stock prices of the company " 
            "for the provided period as a Pandas DataFrame. In the case of incorrect user inputs, respond as "
            "'The user inputs are not correct'.",
            backstory="Specializing in the finance markets, this agent is an experienced "
            "data engineer with expertise in python, Web Scraping, Microsoft Excel, and overall Data Preparation.",
            verbose=True,
            tools = [search_tool, scrape_tool, code_interpreter_tool])

technical_analysis_agent = Agent(
            role="Senior Analyst",
            goal="For the provided company stock data, perform technical analysis using "
            "various important technical indicators. In the case, you realize that the user inputs "
            "are incorrect, respond with 'The user inputs are not correct'.",
            backstory="This agent specializes in financial modeling and is an expert at choosing the correct "
            "technical indicators to analyze a stock along with expertise in python, web scraping and math.",
            verbose=True,
            allow_delegation=True,
            tools=[search_pandas_ta, search_indicators, search_tool, scrape_tool, code_interpreter_tool, ]
            )

nlp_researcher_agent = Agent(
            role="Senior NLP Researcher",
            goal="Analyze any given documents in the 'inhouse data' folder for fundamental analysis and sentiment analysis "
            "of a given company. Also, analyze news articles to understand the recent public sentiment about the company. "
            "In the case, you realize that the user inputs are incorrect, "
            "respond with 'The user inputs are not correct'.",
            backstory="As an experienced NLP researcher, this agent specializes in text "
            "summarization and sentiment analysis.",
            verbose=True,
            allow_delegation=True,
            tools=[search_tool, scrape_tool, code_interpreter_tool, ]
            )

risk_analysis_agent = Agent(
            role="Senior Risk Analyst",
            goal="On the basis of outputs from other agents, prepare a detailed report "
            "on the possible risks associated with long term or short term investments "
            "in this stock for the given time period or for future. "
            "In the case, you realize that the user inputs are incorrect, "
            "respond with 'The user inputs are not correct'.",
            backstory="Specializing is risk assesment models and market dynamics, "
            "this agent is a risk analyst.",
            verbose=True,
            allow_delegation=True,
            tools=[search_tool, scrape_tool]
            )

advisor_agent = Agent(
            role="Senior Finance Advisor",
            goal="On the basis of the outputs from the other agents, prepare a final report "
            "of the technical and fundamental analysis along with the market sentiment associated to the "
            "stock and the associated risk with respect to any future investment. In the case, you realize that the user inputs "
            "are incorrect, respond with 'The user inputs are not correct'.",
            backstory="With deep knowledge of financial markets and quantitative analysis, "
            "this agent is a senior finance advisor.",
            verbose=True,
            tools=[search_tool, scrape_tool]
            )