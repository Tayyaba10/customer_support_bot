from agents import Runner,set_tracing_disabled,InputGuardrailTripwireTriggered
from my_agents.bot_agent import bot_agent
from my_agents.human_agent import human_agent

set_tracing_disabled(True)

try:
    user_input = input("Please enter your query: ")
    result = Runner.run_sync(bot_agent,user_input,context={"user_input": user_input})
    print(f"Bot response: {result.final_output}")
    
except InputGuardrailTripwireTriggered:
    #user_input = input("Please rephrase your query: ")
    result = Runner.run_sync(human_agent, user_input, context={"user_input": user_input})
    print(f"Human agent response: {result.final_output}")