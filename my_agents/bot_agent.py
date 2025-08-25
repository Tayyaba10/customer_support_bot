from agents import Agent,ModelSettings
from my_config.gemini_config import MODEL
from tools.order_status import get_order_status
from guardrail_function.guardrail import guardrail_input
from my_agents.human_agent import human_agent

bot_agent = Agent(
    name="BotAgent",
    instructions="""You are a helpful assistant that provides information and answers questions 
    to the best of your ability. If you encounter any issues or negative language in the user's input, 
    you can hand off to a human agent. 
    You can also check the status of an order using the provided tool.
    answer product FAQS and use the get_order_status tool to fetch order.
    
    
    """,
    model=MODEL,
    tools=[get_order_status],
    model_settings=ModelSettings(tool_choice="auto"),
    input_guardrails=[guardrail_input],
    handoffs=[human_agent]
    
    
)