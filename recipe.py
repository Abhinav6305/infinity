# prompt: main script for the above

# recipes.py (existing code)

recipes_data = [
    {
        "name": "Pancakes",
        "ingredients": ["flour", "milk", "eggs", "sugar", "baking powder"],
        "instructions": "Mix ingredients and cook on a griddle."
    },
    {
        "name": "Spaghetti Bolognese",
        "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onions", "garlic"],
        "instructions": "Cook pasta and mix with sauce and beef."
    }
]

def find_recipe(recipe_name):
    for recipe in recipes_data:
        if recipe["name"].lower() == recipe_name.lower():
            return recipe
    return None

def main():
    recipe_to_find = input("Enter the name of the recipe you're looking for: ")
    found_recipe = find_recipe(recipe_to_find)

    if found_recipe:
        print("\nRecipe Found:")
        print(f"Name: {found_recipe['name']}")
        print(f"Ingredients: {', '.join(found_recipe['ingredients'])}")
        print(f"Instructions: {found_recipe['instructions']}")
    else:
        print(f"Recipe '{recipe_to_find}' not found.")

if __name__ == "__main__":
    main()