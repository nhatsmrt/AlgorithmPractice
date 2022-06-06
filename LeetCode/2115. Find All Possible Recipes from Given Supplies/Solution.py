class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Time and Space Complexity: O(V + E)
        # where V = number of recipes and ingredients
        # and E = number of recipe-to-requirement connections

        ingredient_to_recipe = {}
        recipe_to_ingredient = {}
        recipes_set = set(recipes)

        for recipe, ingredient_lst in zip(recipes, ingredients):
            recipe_to_ingredient[recipe] = set(ingredient_lst)

            for ingredient in ingredient_lst:
                if ingredient not in ingredient_to_recipe:
                    ingredient_to_recipe[ingredient] = []

                ingredient_to_recipe[ingredient].append(recipe)

        ret = []
        complete = supplies

        while complete:
            next_done = supplies.pop()

            if next_done in recipes_set: # complete recipe
                ret.append(next_done)

            for req_recipe in ingredient_to_recipe.get(next_done, []):
                recipe_to_ingredient[req_recipe].remove(next_done)

                if not recipe_to_ingredient[req_recipe]: # complete recipe:
                    complete.append(req_recipe)

        return ret
