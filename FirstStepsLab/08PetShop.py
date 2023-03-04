DOG_FOOD = 2.50
CAT_FOOD = 4

package_dog_food = int(input())
package_cat_food = int(input())

total_cost = (DOG_FOOD * package_dog_food) + (CAT_FOOD * package_cat_food)

if package_dog_food in range(101) and package_cat_food in range(101):
    print(f"{total_cost} lv.")