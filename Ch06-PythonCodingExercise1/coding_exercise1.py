def celsius_to_fahrenheit(C):
    """
    Function to convert temperature from Celsius to Fahrenheit.
    
    Parameters:
    C (float): The temperature in Celsius.
    
    Returns:
    float: The temperature in Fahrenheit.
    """
    # Your code here
    F = (9/5 * C) + 32
    return F
    
print(celsius_to_fahrenheit(25))