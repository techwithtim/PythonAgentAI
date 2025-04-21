from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, coffee_context, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

from pdf import canada_engine
from coffee_scraper import coffee_scraper

load_dotenv()

population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})

coffee_scraper.scrape_nearby_coffee()
coffee_query_engine = coffee_scraper.get_query_engine()

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information at the world population and demographics",
        ),
    ),
    QueryEngineTool(
        query_engine=canada_engine,
        metadata=ToolMetadata(
            name="canada_data",
            description="this gives detailed information about canada the country",
        ),
    ),
    QueryEngineTool(
        query_engine=coffee_query_engine,
        metadata=ToolMetadata(
            name="ottawa_coffee",
            description=(
                "Coffee shops near National Gallery of Canada. "
                "Includes price levels (1-3), ratings (1-5) and distances."
            )
        )
    )
]

# llm = OpenAI(model="gpt-3.5-turbo")
llm = OpenAI(model="gpt-4o-mini-2024-07-18")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context + "\n" + coffee_context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
