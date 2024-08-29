def read_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        current_age_group = None
        current_education_level = None
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("21 to") or line.startswith("55 to"):
                age_group = line.split("  ")[0]  # Split by double space
                data[age_group] = {}
                current_age_group = age_group
            elif line.startswith("Not a") or line.startswith("High school") or line.startswith("Some college") or line.startswith("Bachelor degree") or line.startswith("Advanced degree"):
                education_level = line
                data[current_age_group][education_level] = {}
                current_education_level = education_level
            else:
                if current_education_level:
                    values = line.split()
                    data[current_age_group][current_education_level] = {
                        "Total": {
                            "Number": int(values[0].replace(",", "")),
                            "Perc. dist.": float(values[1]),
                            "Worked year-round Employed full-time in 1999": {
                                "Number": int(values[2].replace(",", "")),
                                "Percent": float(values[3]),
                                "Median earnings": values[6],
                                "Relative earnings (US Med=100)": float(values[7])
                            }
                        }
                    }
    return data

# Example usage:
file_path = "census.txt"  # Replace with your file path
data = read_data(file_path)
print(data)
