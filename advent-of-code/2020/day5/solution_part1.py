import pathlib


def extract_passport(lines: str) -> dict:
    passport = {}

    fields = lines.split(" ")
    for field in fields:
        k, v = field.split(":")
        passport[k] = v

    return passport


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
            mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
            for field in mandatory_fields:
                if field not in passport:
                    break
            else:
                valid_passport_count += 1

    return valid_passport_count


if __name__ == "__main__":
    print(solution(f"{pathlib.Path(__file__).parent}/input.txt"))
