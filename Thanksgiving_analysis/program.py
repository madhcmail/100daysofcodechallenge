import research


def main():
    # Initialize the data
    print("Analysis on Thanksgiving holiday dishes")
    print()
    research.init()

    # ToDO: Print the available regions
    us_regions = research.get_regions()
    print("Available Regions: ")
    for each_region in us_regions:
        print(each_region)

    print()

    # TODO: Get user input on the region
    user_input_region = input("Select your region from the above available regions: ").title()
    print()

    # TODO: Print the income ranges available
    income_ranges = research.get_income_ranges()
    print(f"Income_Ranges: {income_ranges}")
    print()
    # TODO: Ask for income range
    user_input_income = input("How much total combined money did all members of your HOUSEHOLD earn last year?")
    print()
    # TODO: Print out the region specific menu
    menu = research.get_menu(user_input_region,user_input_income)

    print(f"Thanksgiving dishes in the region '{user_input_region}' with income range of ({user_input_income}):")
    print(f"Main dish: {menu[0][0]}")

    # TODO: Print the top 5 side dishes
    sides_dish = research.get_sides(user_input_region, user_input_income)
    print("Side dishes:")
    for idx, s_dish in enumerate(sides_dish):
        print(idx+1,s_dish[0])




if __name__ == '__main__':
    main()

