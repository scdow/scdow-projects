"""
    Create a recipe.
    Initially, it has no element in  recipe dictionary,can invoke setRecipe function to add.
"""
class Recipe:

    def __init__(self):
        self.recipes = {}   # can store all recipes of game
        """dictionary:{(meterial tuple), (product nmae, description)}"""

    def setRecipe(self, material, name, description):
        """
            Adds material, name, description for a recipe. The recipe is stored as a dictionary
            entry of the (key, value) pair (material,(name, description))
        :param material: mix materials tuple to get recipe
        :param name: recipe product name
        :param description: recipe product description
        :return: None
        """
        self.recipes[material] = (name, description)

    def getAllMaterials(self):
        """:return: recipes keys with tuple form"""
        allMaterials = self.recipes.keys()
        return allMaterials

    def getProduct(self,materials):
        """
        :param materials: one key (material1, material2, ...)
        :return: corresponding value (recipe name, recipe description)
        """
        return self.recipes[materials]