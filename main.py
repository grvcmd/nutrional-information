
class FoodItem:
    def __init__(self, name = 'None', fat = 0.00, carbs = 0.00, protein = 0.00, servings = 0.00):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.servings = servings

    def print_example_nutrition_info(self):
        print('Nutritional information per serving of None:')
        print('   Fat: 0.00 g')
        print('   Carbohydrates: 0.00 g')
        print('   Protein: 0.00 g')
        print('Number of calories for {:.2f} serving(s): 0.00\n'.format(self.servings))

    def get_calories(self):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * self.servings
        return calories

    def print_nutrition_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print('Number of calories for {:.2f} serving(s): {:.2f}'.format(self.servings, self.get_calories()))


name = str(input())
fat = float(input())
carbs = float(input())
protein = float(input())
servings = float(input())

lunch = FoodItem(name, fat, carbs, protein, servings)

lunch.print_example_nutrition_info()
lunch.get_calories()
lunch.print_nutrition_info()