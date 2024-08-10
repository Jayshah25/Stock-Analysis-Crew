from crewai_tools import (FileReadTool, 
                          SerperDevTool, 
                          ScrapeWebsiteTool, 
                          CodeInterpreterTool,
                          GithubSearchTool,
                          CodeDocsSearchTool)


search_indicators = FileReadTool(file_path=r'instructions\indicators.md')

search_pandas_ta = FileReadTool(file_path=r'instructions\pandas-ta.md')

search_tool = SerperDevTool()

yfinance_search_tool = CodeDocsSearchTool(docs_url=r'https://python-yahoofinance.readthedocs.io/en/latest/')

scrape_tool = ScrapeWebsiteTool()

code_interpreter_tool = CodeInterpreterTool()