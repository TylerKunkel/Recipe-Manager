class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"{self.name}: {self.ingredients}\n{self.instructions}"


class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def search_recipe(self, keyword):
        found_recipes = []
        for recipe in self.recipes:
            if keyword.lower() in recipe.name.lower():
                found_recipes.append(recipe)
        return found_recipes

    def __str__(self):
        recipes_str = ""
        for recipe in self.recipes:
            recipes_str += f"{recipe}\n"
        return recipes_str


# Example usage
recipes = []
while True:
    # Ask user for recipe details
    name = input("Enter recipe name (or 'q' to quit): ")
    if name.lower() == "q":
        break
    ingredients = input("Enter ingredients, separated by commas: ")
    instructions = input("Enter instructions: ")
    
    # Create a new recipe object and add it to the list
    recipe = Recipe(name, ingredients, instructions)
    recipes.append(recipe)

# Create a RecipeManager and add all the recipes to it
manager = RecipeManager()
for recipe in recipes:
    manager.add_recipe(recipe)

# Print the list of recipes
print(manager)

# Search for a recipe
keyword = input("Enter a keyword to search for: ")
found_recipes = manager.search_recipe(keyword)
for recipe in found_recipes:
    print(recipe)
