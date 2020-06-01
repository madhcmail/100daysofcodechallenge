import research


def main():
    # Initialize the data
    print("Analysis on Thanksgiving holiday dishes:")
    research.init()

    # Print the available unique regions for users to select
    us_regions, us_income_range = research.get_regions_and_income()
    print("Regions:")
    print(us_regions)
    print()
    # Print the available unique income ranges for users to select
    print("Income_Ranges:")
    print(us_income_range)
    print()

    # Ask user to input teh key of specific region
    user_input_region = input("Select your region key from the above available regions(Example: 1): ")

    while True:
        if user_input_region == '' or user_input_region not in us_regions.keys():
            user_input_region = input("Select your region key from the above available regions(Example: 1): ")
        else:
            break

    # Ask user for input the  key of specific income_range
    user_input_income = input("Select the key for Income range from the above available regions(Example: 1): ")
    while True:
        if user_input_income == '' or user_input_income not in us_income_range.keys():
            user_input_income = input("Select the key for Income range from the above available regions(Example: 1): ")
        else:
            break
    print()

    # Predict the region specific main dish and 5 side dishes
    main_dishes, sides_dish = research.get_menu(us_regions[user_input_region], us_income_range[user_input_income])

    if len(main_dishes) > 0 and len(sides_dish) > 0:
        print(f"Thanksgiving dishes in the region '{us_regions[user_input_region]}' "
              f"with income range of ({us_income_range[user_input_income]}):")
        print()
        print(f"Main dish is: {main_dishes[0][0]}")
        print("Side dishes are:")
        for idx, s_dish in enumerate(sides_dish):
            print(idx + 1, s_dish[0])
    else:
        print(f"No Menu available for the region {us_regions[user_input_region]} and "
              f"with income range between {us_income_range[user_input_income]}.")


if __name__ == '__main__':
    main()

