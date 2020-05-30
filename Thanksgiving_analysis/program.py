import research

def main():
    # Initialize the data
    print("Analysis on Thanksgiving holiday dishes")
    print()
    research.init()

    # ToDO: Print the available regions
    us_regions = research.get_regions()
    print(f"Available Regions: {us_regions}")

    # TODO: Get user input on the region
    user_input_region = input("Select your region from the above available regions: ").title()

    # TODO: Print the income ranges available
    income_ranges = research.get_income_ranges()
    print(f"Income_Ranges: {income_ranges}")

    # TODO: Ask for income range
    user_input_income = input("How much total combined money did all members of your HOUSEHOLD earn last year?")

    # TODO: Print out the region specific menu
    d = research.data
    for row in d:
        if row.region == user_input_region and row.income_range == user_input_income:
            print(row.main_dish)



if __name__ == '__main__':
    main()

