from crewai import Task
from agents import (data_engineer_agent,
                    technical_analysis_agent,
                    nlp_researcher_agent,
                    risk_analysis_agent,
                    advisor_agent)

gather_data = Task(
    description = "Based on the provided {stock}, {start_date}, and "
    "{end_date}, gather stock price data for the company in this time period.",
    expected_output="A csv file with price data of the {stock} from {start_date} to {end_date}.",
    agent=data_engineer_agent,
    output_file="data.csv",
    )

technical_analysis = Task(
    description = "Based on the output of the previous task, use the gathered data "
    "for technical analysis.",
    expected_output="Long and Short Term performance insights of {stock} based on the technical analysis.",
    agent=technical_analysis_agent,
    context=[gather_data]
    )

fundamental_and_sentimental_analysis = Task(
    description="Perform fundamental analysis from the documents provided in the {data_folder}. "
    "Perform Sentiment Analysis from news articles around {end_date}.",
    expected_output="Long and Short Term performance insights of {stock} based on the fundamental analysis and sentiment analysis.",
    agent=nlp_researcher_agent,
    context=[gather_data]
)

risk_analysis = Task(
    description="Evaluate risk of trading in the {stock} from {start_date} and {end_date}. Consider the oututs of previous tasks too.",
    expected_output="Long and Short Term performance insights of {stock} and possible future investment based on the risk analysis.",
    agent=risk_analysis_agent,
    context=[gather_data,technical_analysis,fundamental_and_sentimental_analysis]
)

investment_advise = Task(
    description="Based on the outputs from the previous tasks, provide an overall performance "
    "insights of the {stock} from {start_date} to {end_date} and future investment strategy in the {stock} stocks.",
    expected_output="A detailed report on the performance of {stock} from {start_date} to {end_date} "
    "based on the techincal analysis, fundamental analysis, sentiment analysis, "
    "and risk analysis.",
    agent=advisor_agent,
    context=[gather_data,technical_analysis,fundamental_and_sentimental_analysis,risk_analysis]
)