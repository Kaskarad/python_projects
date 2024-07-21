#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Создаем пустой словарь для хранения пар "значение - индекс"
        tracker = dict()

        # Проходим по каждому элементу списка nums
        for i, val in enumerate(nums):
            # Вычисляем разницу между target и текущим элементом списка
            rem = target - val

            # Проверяем, есть ли разница в словаре tracker
            if rem in tracker:
                # Если да, возвращаем индексы элементов, сумма которых равна target
                return [tracker[rem], i]

            # Добавляем пару "значение - индекс" в словарь tracker
            tracker[val] = i

        # Если мы дошли до конца цикла без нахождения решения, возвращаем пустой список
        return []
        
# @lc code=end

