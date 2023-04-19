def calculate_weight_on_planet(weight, gravity):
    """Calculates weight on a planet with given gravity."""
    return weight * gravity / 9.81

def main():
    print("Welcome to Weight on Other Planets!")
    weight = float(input("Enter your weight on Earth (in kg): "))
    planets = {
        "Mercury": 3.7,
        "Venus": 8.87,
        "Mars
