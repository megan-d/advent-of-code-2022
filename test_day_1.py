import pytest
from day_1 import CountCalories


class TestDay1:
    @pytest.fixture
    def count_calories(self):
        return CountCalories("./day_1_input_test.txt")

    def test_process_data_correctly_processes_data(self, count_calories):
        calories_counted = count_calories.calorie_data
        assert len(calories_counted) == 5
        assert isinstance(calories_counted[0][0], int)

    def test_calculate_individual_elf_calories_sums_calories_for_single_elf(
        self, count_calories
    ):
        calories_counted = count_calories.calorie_data
        single_elf_total = count_calories.calculate_individual_elf_calories(
            calories_counted[0]
        )
        assert single_elf_total == 6000

    def test_calculate_total_elf_calories_sums_all_totals(self, count_calories):
        calories_counted = count_calories.calorie_data
        total_calories = count_calories.calculate_all_elf_sums(calories_counted)
        assert len(total_calories) == 5
        assert total_calories == [6000, 4000, 11000, 24000, 10000]

    def test_calculate_max_calories_calculates_max(self, count_calories):
        calories_counted = count_calories.calorie_data
        max_calories = count_calories.calculate_max_calories(calories_counted)
        assert max_calories == 24000

    def test_calculate_top_3_elf_calories_returns_results(self, count_calories):
        calories_counted = count_calories.calorie_data
        top_calories = count_calories.calculate_top_3(calories_counted)
        assert top_calories == 45000
