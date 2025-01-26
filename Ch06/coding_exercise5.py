def calculate_y(slope, intercept, x):
    """
    Function to calculate the value of y using the slope-intercept form of a line.
    
    Parameters:
    slope (float): The slope of the line.
    intercept (float): The y-intercept of the line.
    x (float): The value of x for which y needs to be calculated.
    
    Returns:
    float: The calculated value of y.
    """
    return float(intercept + (slope * x))

print(f"y = b + mx : {calculate_y(2, 3, 4)}")
print(f"y = b + mx : {calculate_y(5, 7, 2)}")