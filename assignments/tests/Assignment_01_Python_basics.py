"""
EST 389/371: Special topics in TSM (Data Science)
Spring, 2026
Instructor: Dr. Jieshu Wang (jieshu.wang@stonybrook.edu)

HW 1: Python Basics (5 points)

Rules:
- Please add your answers under each TODO comment line.
- Do NOT change the file name when you submit the assignment
- Do NOT change any variable or function names.
- Do NOT add print statements.
"""

# --------------------------------------------------
# Problem 1 (1 point)
# Assign exact values
# --------------------------------------------------

# TODO: define a variable named 'city' with the value "Stony Brook"
# Example of defining a variable:
# state: str = "NY"
city: str = 'Stony Brook'

# TODO: define a variable named 'season' with the value "winter"
season: str = 'winter'

# TODO: define a variable named 'weather' with the value "snow"
weather: str = 'snow'

# --------------------------------------------------
# Problem 2 (1 point)
# String formatting
# --------------------------------------------------

# TODO: create an f-string named 'sentence' using the variables defined above
# The final string must be EXACTLY:
# "In Stony Brook, winter often brings snow."
sentence: str = f"In {city}, {season} often brings {weather}."

# --------------------------------------------------
# Problem 3 (1 point)
# Work with a list
# --------------------------------------------------

ny_seasons = ["spring", "summer", "fall", "winter"]

# TODO: store the number of seasons in a variable named 'num_seasons'
num_seasons: int = len(ny_seasons)

# TODO: retrieve the first season from the list using an index
# and store it in a variable named 'first_season'
first_season = ny_seasons[1]

# --------------------------------------------------
# Problem 4 (1 point)
# Working with a dictionary
# --------------------------------------------------

season_months = {"spring": (1, 2, 3)}

# TODO: add three more key–value pairs to the dictionary 'season_months'
# representing summer, fall, and winter
# (each value should be a tuple of three integers)
season_months["summer"] = (4, 5, 6)
season_months["fall"] = (7, 8, 9)
season_months["winter"] = (10, 11, 12)

# --------------------------------------------------
# Problem 5 (1 point)
# Simple function with fixed logic
# --------------------------------------------------

def is_winter(season_name: str) -> bool:
    """
    Return True if season_name is "winter".
    Otherwise, return False.
    """
    # TODO: implement the function
    if season_name == "winter":
        return True
    else:
        return False

