import pathlib


def extract_passport(lines: str) -> dict:
    passport = {}

    fields = lines.split(" ")
    for field in fields:
        k, v = field.split(":")
        passport[k] = v

    return passport


def _is_between(value: int, least: int, most: int) -> bool:
    return least <= value <= most


def is_valid_year(year_type: str, year: int) -> bool:
    validation_rule = {
        "byr": (1920, 2002),
        "iyr": (2010, 2020),
        "eyr": (2020, 2030),
    }

    return _is_between(year, *validation_rule[year_type])


def is_valid_height(value: int) -> bool:
    height, unit = int(value[:-2]), value[-2:]

    if unit == "cm":
        return _is_between(height, 150, 193)
    elif unit == "in":
        return _is_between(height, 59, 76)
    else:
        return False


def is_valid_hair_color(value: str) -> bool:
    return value[0] == "#" and len(value) == 7 and value[1:].isalnum()


def is_valid_field(field_type: str, value: str) -> bool:
    if field_type in ("byr", "iyr", "eyr"):
        return is_valid_year(field_type, int(value))
    elif field_type == "hgt":
        return is_valid_height(value)
    elif field_type == "hcl":
        return is_valid_hair_color(value)
    elif field_type == "ecl":
        return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    elif field_type == "pid":
        return len(value) == 9 and value.isdigit()
    elif field_type == "cid":
        return True
    else:
        raise ValueError(f"Unknown field_type {field_type}")


def solution(file_path: str) -> int:
    valid_passport_count = 0

    # read the file
    with open(file_path, "r") as f:
        for line in f:
            # read a passport
            lines = []
            line = line.strip()
            while line != "":
                lines.append(line)
                line = f.readline().strip()

            # parse passport
            passport = extract_passport(" ".join(lines))

            # validate passport
            mandatory_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
            for field in mandatory_fields:
                if field not in passport or not is_valid_field(field, passport[field]):
                    break
            else:
                valid_passport_count += 1

    return valid_passport_count


if __name__ == "__main__":
    print(solution(f"{pathlib.Path(__file__).parent}/input.txt"))
