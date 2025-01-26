def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    full_rounds = n // capacity
    if n % capacity != 0:
        return full_rounds + 1
    else:
        return full_rounds
    
print(calculate_lift_rounds(11, 3))
print(calculate_lift_rounds(7, 4))
print(calculate_lift_rounds(13, 3))
print(calculate_lift_rounds(15, 4))

    
    