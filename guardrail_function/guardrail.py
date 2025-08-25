from agents import input_guardrail, GuardrailFunctionOutput,RunContextWrapper

# This guardrail function checks for negative language in the input data.
@input_guardrail
def guardrail_input(ctx:RunContextWrapper,agent,input_data:str) -> GuardrailFunctionOutput:
    """ check for offensive or negative language"""
    
    negative_words = ["bad", "hate", "stupid", "dumb", "idiot"]
    
    data = input_data.lower()
    
    if any(word in data for word in negative_words):
        
        # If negative language is detected, trigger the guardrail function
        return GuardrailFunctionOutput(
            output_info="Negative language detected. Please rephrase your input.",
            tripwire_triggered=True
        )
    
    return GuardrailFunctionOutput(
        output_info=None,
        tripwire_triggered=False)
     