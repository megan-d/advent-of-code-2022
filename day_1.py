class CountCalories:
    def __init__(self, file_path) -> None:
        raw_data = list(open(file_path).read().split("\n\n"))
        self.calorie_data = self.process_data(raw_data)

    def process_data(self, data):
        processed_data = [item.split("\n") for item in data]
        processed_int_data = [list(map(int, lst)) for lst in processed_data]
        return processed_int_data

    def calculate_individual_elf_calories(self, data):
        return sum(data)

    def calculate_all_elf_sums(self, data):
        total_calories = [self.calculate_individual_elf_calories(elf) for elf in data]
        return total_calories

    def calculate_max_calories(self, data):
        total_calories = [self.calculate_individual_elf_calories(elf) for elf in data]
        max_calories = max(total_calories)
        return max_calories

    def calculate_top_3(self, data):
        total_calories = [self.calculate_individual_elf_calories(elf) for elf in data]
        max_calories = sorted(total_calories, reverse=True)
        top_3 = [max_calories[0], max_calories[1], max_calories[2]]
        total = sum(top_3)
        print(total)
        return total


if __name__ == "__main__":
    calorie_counting = CountCalories("day_1_input.txt")
    calorie_counting.calculate_max_calories(calorie_counting.calorie_data)
    calorie_counting.calculate_top_3(calorie_counting.calorie_data)
