from dcctools.config import Configuration


def validate():
    config = Configuration("config.json")
    validate(config)


def validate(c):
    missing_files = c.validate_all_present()
    if len(missing_files) == 0:
        print("All necessary input is present")
        return "All necessary input is present"
    else:
        print("One or more files missing from data owners:")
        for filename in missing_files:
            print(filename)
        return "One or more files missing from data owners"


if __name__ == "__main__":
    validate()
