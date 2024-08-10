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

def run_crew(inputs:dict, temperature:float):

    crew = Crew(
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
                                    manager_llm=ChatOpenAI(model="gpt-3.5-turbo", 
                                                                temperature=temperature),
                                    process=Process.hierarchical,
                                    verbose=True
                                    )
    
    result = crew.kickoff(inputs=inputs)

    return result 
