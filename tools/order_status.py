# This file is part of a customer support bot project.
# It defines the bot agent that interacts with users and provides order status information.

from agents import function_tool

# function tool decorator is used to define a tool that can be called by the agent
@function_tool
def get_order_status(order_id:str) -> str:
    """
    Function to get the status of an order based on the order ID.
    
    Args:
        order_id (str): The ID of the order to check.
    
    Returns:
        str: The status of the order.
    """
    print("order status tool call...")
    
    # Simulated order status retrieval
    order_statuses = {
        "123": "Processing",
        "456": "Shipped",
        "789": "Delivered",
        "101": "Cancelled"
    }
    
    # Check if the order ID is valid and retrieve the status
    order_status = order_statuses.get(order_id)
    # If order ID is not found, return a message
    if not order_id:
        return "Order ID not found"
    # Return the order status or a message if not found
    return f"Order ID {order_id} status: {order_status if order_status else 'Unknown'}"
