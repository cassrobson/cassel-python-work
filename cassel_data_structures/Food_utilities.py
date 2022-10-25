"""
-------------------------------------------------------
CLass Foods for L01
-------------------------------------------------------
Author:  Cassel Robson
ID:      210507000
Email:   robs7000@mylaurier.ca
__updated__ = "2022-03-19"
-------------------------------------------------------
"""


from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    name = input("Name: ")

    origin = int(input("Origin: "))

    veggie = input("Vegetarian (Y/N): ")

    if veggie == 'Y':
        is_vegetarian = True
    elif veggie == 'N':
        is_vegetarian = False
    else:
        is_vegetarian = None

    calories = int(input("Calories: "))

    food = Food(name, origin, is_vegetarian, calories)

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    # name|origin|is_vegetarian|calories

    list = line.split('|')

    origin = int(list[1])

    name = list[0]
    if list[2] == 'True':
        is_vegetarian = True
    else:
        is_vegetarian = False

    if list[3] == 'None':
        calories = None
    else:
        calories = int(list[3])

    food = Food(name, origin, is_vegetarian, calories)

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """

    foods = []

    for line in file_variable:
        list_object = read_food(line)
        foods.append(list_object)

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    for x in foods:
        x.write(file_variable)

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []
    for i in foods:
        if i.is_vegetarian() == 'True':
            veggies.append(i)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins = []
    for i in foods:
        if i.origin == origin:
            origins.append(i)

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    cals = []
    for i in foods:
        cals.append(int(i.calories))

    avg = sum(cals) // len(cals)

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    origin_cals = []
    for i in foods:
        if i.origin == origin:
            origin_cals.append(int(i.calories))

    avg = sum(origin_cals) // len(origin_cals)
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    count = 0
    sorted_foods = []
    list_names = []
    for i in foods:
        list_names.append(i.name.lower())
    list_names.sort()
    for x in list_names:
        for y in foods:
            if x == y.name.lower():
                sorted_foods.append(y)
        count += 1
    foods = sorted_foods

    # Formatting output

    print(f'Food                                Origin       Vegetarian Calories')
    print(f'----------------------------------- ------------ ---------- --------')
    for z in foods:
        originz = Food.ORIGIN[z.origin]
        if z.is_vegetarian == 1:
            veggie = 'True'
        else:
            veggie = 'False'
        print(
            f"{z.name.capitalize():<36}{originz:<13}{veggie:>10}{z.calories:>9}")

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    valid_origin = []
    valid_calories = []
    result = []
    for i in foods:
        if origin == i.origin or origin == -1:
            valid_origin.append(i)
    for j in valid_origin:
        if max_cals >= int(j.calories) or max_cals == 0:
            valid_calories.append(j)
    for x in valid_calories:
        if is_veg == 'True' and x.is_vegetarian == True or is_veg == 'False':
            result.append(x)

    return result
