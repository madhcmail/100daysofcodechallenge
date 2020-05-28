import program


def main():
    print("Weather  research for seattle, 2014-2015")
    print()
    program.init()

    # TODO: Find top 5 hottest days
    print("The top 5 hottest days:")
    days = program.hot_days()
    for idx,d in enumerate(days[:5]):
        print(f"{idx+1}. {d.actual_max_temp} F on {d.date}")
    # TODO: Find top 5 coolest days
    print("The top 5 coldest days:")
    days = program.cold_days()
    for idx,d in enumerate(days[:5]):
        print(f"{idx+1}. {d.actual_min_temp} F on {d.date}")
    # TODO: FInd top 5 wettest days
    print("The top 5 wettest days: ")
    days = program.wet_days()
    for idx, d in enumerate(days[:5]):
        print(f"{idx+1}. {d.actual_precipitation} inches of rain on {d.date}")


if __name__ == '__main__':
    main()