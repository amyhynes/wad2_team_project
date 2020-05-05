import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad2_team_project.settings')
import django
django.setup()
from recipes.models import *
from django.contrib.auth.models import User

cat_objects = {}
admin_objects = {}
bio = "Hello! I enjoy making food the opportunity to upload recipes, share tips, and explore recipes on this website!"
def populate():
	reviews = {"Best pancakes" : {"author" : "q_smart", "recipe" : "Pancakes", "chef" : "lynda_faller", "rating" : 4.25, "comment":"These pancakes are so light and fulffy!"},
		"FABULOUS" : {"author" : "eve_ohagan", "recipe" : "Spaghetti Carbonara", "chef" : "amy_hynes", "rating" : 5 , "comment":" Best i have ever had!"},
		"Quick and effective": {"author" : "eve_ohagan", "recipe" : "Classic Hot Dogs", "chef" : "lynda_faller", "rating" : 4.8, "comment":" Would highly recommend!"},
		"Perfect for the occasion" : {"author" : "eve_ohagan", "recipe" : "All-American Burger", "chef" : "q_smart", "rating" : 4.1, "comment":"a bit too much cheese! "},
		"Hard work but worth it" : {"author" : "amy_hynes", "recipe" : "Chicken Curry", "chef" : "eve_ohagan", "rating" : 3.0, "comment":"This recipe is time consuming but so delicious"},
		"Festive!" : {"author" : "amy_hynes", "recipe" : "St Paddy's Cupcakes", "chef" : "q_smart", "rating" : 4.75, "comment":"These cupcakes are so cute! Kids love them"},
		"Yum!" : {"author" : "amy_hynes", "recipe" : "California Rolls", "chef" : "q_smart", "rating" : 4.5, "comment":"Authentic and delicious"},
		"Authentic!" : {"author" : "q_smart", "recipe" : "Traditional Tiramisu", "chef" : "amy_hynes", "rating" : 5, "comment":"Lovely, reminds me of Italy!"},
		"So creative!" : {"author" : "q_smart", "recipe" : "Easy Chicken Chow Mein", "chef" : "lynda_faller", "rating" : 3.5, "comment":"Not quite China but very close. lovely and quick!"},
		"The best tiramisu": {"author" : "lynda_faller", "recipe" : "Traditional Tiramisu", "chef" : "amy_hynes", "rating" : 5.0, "comment":"This tiramisu reminds me of the one I had in Italy!"},
		"Fabulous Chicken Curry": {"author" : "lynda_faller", "recipe" : "Chicken Curry", "chef" : "eve_ohagan", "rating" : 4.0, "comment":"Really good recipe- would definitely make again. I love the flavours in this!"},
		"You need to try these!": {"author" : "lynda_faller", "recipe" : "St Paddy's Cupcakes", "chef" : "q_smart", "rating" : 4.5, "comment":"I never thought I liked chocolate cupcakes until I ate these. I prefer to use a little less sugar than the recipe calls for, and they still taste amazing."},
	}
	admins = {
		"lynda_faller" : {"email":"lynda@gmail.com", "password":"lyndafaller", "fname":"Lynda", "lname":"Faller", "chef":True, "photo":"profile_pics/lynda.png",},
		"amy_hynes" : {"email":"amy@gmail.com", "password":"amyhynes", "fname":"Amy", "lname":"Hynes", "chef":True, "photo":"profile_pics/amy.png",},
		"eve_ohagan" : {"email":"eve@gmail.com", "password":"eveohagan", "fname":"Eve", "lname":"O'Hagan", "chef":True, "photo":"profile_pics/eve.png",},
		"q_smart" : {"email":"q@gmail.com", "password":"qiufeismart", "fname":"Q", "lname":"Smart", "chef":True, "photo":"profile_pics/q.png",},}
	#EVERY TIME THERE IS A RETURN STATEMENT IN ABOUT/INGREDIENTS/STEPS USE \r\n
	recipes = [
		{"name": "Pancakes",
		"cook_time" : 15,
		"cats" : "Breakfast, American",
		"chef" : "lynda_faller",
		"photo" : "pancakes.jpeg",
		"about": "The fluffiest American pancakes around! Whip these pancakes up in no time for an impromptu pud or an indulgent breakfast treat! Source: http://allrecipes.co.uk/recipe/27002/fluffy-american-pancakes.aspx",
		"ingredients":"150g plain flour\r\n1/2 teaspoon salt\r\n1 tablespoon baking powder\r\n1 teaspoon caster sugar\r\n225ml milk\r\n1 egg\r\n1 knob of butter, melted\r\nbutter or oil for frying",
		"steps":"1. Sift together the flour, salt, baking powder and sugar. Make a well in the centre. Pour in the milk, then add the egg and melted butter. Beat well till the pancake batter is smooth.\r\n2. Heat a frying pan over medium heat. Lightly grease with butter or vegetable oil. To test to see if the pan is hot enough, flick a bit of water on the pan. If it sizzles, it is ready. Ladle the pancake batter into the pan.\r\n3. Cook each pancake till bubbles appear on the surface and the edges have gone slightly dry. Flip each pancake and cook for a minute or two on the reverse side, till golden brown.\r\n4. Serve hot with your favourite toppings, such as maple syrup and fresh berries. Enjoy!",
		},
		{"name": "Chicken Pesto Panini",
		"cook_time" : 10,
		"cats" : "Lunch, American",
		"chef" : "eve_ohagan",
		"photo" : "panini.jpeg",
		"about": "A delicious combination for a chicken sandwich: roast chicken, pesto, veggies and cheese sandwiched between focaccia. Simple, fast and tasty. Source: http://allrecipes.co.uk/recipe/9367/pesto-chicken-panini.aspx",
		"ingredients":"1 focaccia bread, quartered\r\n8 tablespoons prepared basil pesto\r\n150g diced cooked chicken\r\n1/2 green pepper, diced\r\n4 tablespoons diced red onion\r\n120g grated Cheddar, mozzarella or Monterey Jack cheese",
		"steps":"1. Preheat a panini press.\r\n2. Slice each quarter of focaccia bread in half horizontally. Spread each half with pesto. Layer bottom halves with equal amounts chicken, green pepper, onion and cheese. Top with remaining focaccia halves, forming 4 sandwiches.\r\n3. Grill panini 5 minutes in the preheated press, or until focaccia is golden brown and cheese is melted.",
		},
		{"name": "All-American Burger",
		"cook_time" : 25,
		"cats" : "Dinner, American, 4th of July",
		"chef" : "q_smart",
		"photo" : "burger.png",
		"about": "The best-tasting burger is always made using the finest, leanest beef, like this recipe. This really has to be tried - burgers are rarely made like this any more. Try serving with tomato salsa. Source: https://www.saga.co.uk/magazine/food/recipes/meat/beef/lower-cholesterol-classic-american-burger",
		"ingredients":"1 slice brown bread\r\n1kg lean minced Angus beef\r\n1 garlic clove, crushed\r\n1 teaspoon finely chopped fresh thyme\r\n1 tablespoon tomato paste\r\n1 tablespoon Dijon mustard\r\n1 egg\r\nFreshly ground black pepper\r\nDash of Tabasco sauce\r\nSplash of vegetable (rapeseed) oil\r\nToasted sesame-seed burger buns, to serve",
		"steps":"1. Whizz the brown bread in a blender to make crumbs.\r\n2. Place all the remaining ingredients (except for the oil and the buns) in a large mixing bowl and, adding the breadcrumbs, mix with your hands so it all comes together. Make into patties.\r\n3. Heat a little oil in a pan and cook the patties for 2–3 minutes on each side; keep on the medium-rare side.\r\n4. Serve on toasted sesame-seed buns.",
		},
		{"name": "Traditional Tiramisu",
		"cook_time" : 30,
		"cats" : "Dessert, Italian",
		"chef" : "amy_hynes",
		"photo" : "tirimisu.jpeg",
		"about": "Tiramisu is a rich treat blending the bold flavours of cocoa and espresso with savoury mascarpone cheese and wine, layered with ladyfinger biscuits.",
		"ingredients":"568ml pot double cream,\r\n250g tub mascarpone\r\n75ml marsala \r\n 5 tbsp golden caster sugar \r\n300ml strong coffee \r\n75g pack sponge finger \r\n25g chunk dark chocolate \r\n2 tsp cocoa powder.",
		"steps":"1. Put double cream mascarpone, marsala, caster sugar in a large bowl. \r\nWhisk until the cream and mascarpone have completely combined and have the consistency of thickly whipped cream \r\nPour  coffee  into a shallow dish, dipping a few of the sponge fingers at a time, turning for a few secs until they are nicely soaked, but not soggy. \r\nLayer these into your dish until you have used half the sponge fingers, then spread over half of the creamy mixture \r\ngrate over most of the chocolate. Then repeat the layers (using up all the coffee) finishing with the creamy layer. \r\nCover and chill for a few hours or overnight \r\nTo serve, dust with 2 tsp cocoa powder and grate over the remainder of the chocolate.",
		},
		{"name": "Shamrock Shake",
		"cook_time" : 35,
		"cats" : "Dessert, St Patrick's Day",
		"chef" : "eve_ohagan",
		"photo" : "shake.jpeg",
		"about": "Make your own homemade spin on the beloved fast food Shamrock Shake with this quick and easy recipe. Source: https://www.epicurious.com/recipes/food/views/shamrock-shake-51226410",
		"ingredients":"1 1/2 cups vanilla ice cream\r\n1/2 cup whole milk \r\n10 drops green food coloring \r\n1 teaspoon peppermint extract \r\nWhipped cream (optional) \r\n1 maraschino cherry (optional)",
		"steps":"1. In a blender, combine the vanilla ice cream, milk, green food coloring, and peppermint extract, and process until smooth, about 30 seconds \r\n2. Pour the shake into a glass and top with the whipped cream and maraschino cherry. \r\n",
		},
		{"name": "Spaghetti Carbonara",
		"cook_time" : 35,
		"cats" : "Dinner, Italian",
		"chef" : "amy_hynes",
		"photo" : "carbonara.jpeg",
		"about": "This cheesy pasta dish is an italian favourite and with the right technique you can make it perfect every time!",
		"ingredients":"100g pancetta \r\n50g pecorino cheese \r\n50g parmesan \r\n3 large eggs \r\n350g spaghetti \r\n2 plump garlic cloves, peeled and left whole \r\n50g unsalted butter \r\nsea salt and freshly grated black pepper",
		"steps":"1. Put a large saucepan of water on to boil. \r\n2. Finely chop the 100g pancetta, having first removed any rind. Finely grate 50g pecorino cheese and 50g parmesan and mix them together. \r\n3. Beat the 3 large eggs in a medium bowl and season with a little freshly grated black pepper. Set everything aside. \r\n4. Add 1 tsp salt to the boiling water, add 350g spaghetti and when the water comes back to the boil, cook at a constant simmer, covered, for 10 minutes or until al dente (just cooked). \r\n5. Squash 2 peeled plump garlic cloves with the blade of a knife, just to bruise it. \r\n6. While the spaghetti is cooking, fry the pancetta with the garlic. Drop 50g unsalted butter into a large frying pan or wok and, as soon as the butter has melted, tip in the pancetta and garlic. \r\n7. Leave to cook on a medium heat for about 5 minutes, stirring often, until the pancetta is golden and crisp. The garlic has now imparted its flavour, so take it out with a slotted spoon and discard. \r\n8. Keep the heat under the pancetta on low. When the pasta is ready, lift it from the water with a pasta fork or tongs and put it in the frying pan with the pancetta. Don’t worry if a little water drops in the pan as well (you want this to happen) and don’t throw the pasta water away yet. \r\n9. Mix most of the cheese in with the eggs, keeping a small handful back for sprinkling over later. \r\n10. Take the pan of spaghetti and pancetta off the heat. Now quickly pour in the eggs and cheese. Using the tongs or a long fork, lift up the spaghetti so it mixes easily with the egg mixture, which thickens but doesn’t scramble, and everything is coated. \r\n11. Add extra pasta cooking water to keep it saucy (several tablespoons should do it). You don’t want it wet, just moist. Season with a little salt, if needed. \r\n12. Use a long-pronged fork to twist the pasta on to the serving plate or bowl. Serve immediately with a little sprinkling of the remaining cheese and a grating of black pepper. If the dish does get a little dry before serving, splash in some more hot pasta water and the glossy sauciness will be revived.",
		},
		{"name": "Classic Hot Dogs",
		"cook_time" : 30,
		"cats" : "Lunch, American, 4th of July",
		"chef" : "lynda_faller",
		"photo" : "hotdog.jpeg",
		"about": "These hot dogs will be a crowd pleaser at your summer barbecue! Source: https://potatorolls.com/recipes/classic-hot-dog/",
		"ingredients":"Hot Dogs\r\nBuns\r\nCondiments of Choice\r\nToppings of Choice",
		"steps":"1. Cook hot dogs using preferred method:\r\nGrilling Method: Heat hot dogs over medium (or indirect) heat on grill, turning occasionally. Cook until fully heated internally and there is a nice, even char on all sides, being careful not to burn them.\r\nBoiling Method: Fill a saucepan with about 4 cups of water. Bring to a boil. Once boiling, turn heat to low and add hot dogs. Simmer for about 5 minutes, or until hotdogs are fully heated.\r\n2. Once hot dogs are fully heated, remove from heat and set aside, drying them off if necessary.\r\n3. Place each hot dog in a bun and top with desired toppings and condiments, such as cheese, mustard, ketchup, relish, onions, chili, etc.",
		},
		{"name": "Old School Beef Tacos",
		"cook_time" : 30,
		"cats" : "Dinner, Mexican",
		"chef" : "amy_hynes",
		"photo" : "tacos.jpeg",
		"about": "These crispy ground beef tacos are filled with seasoned meat, lettuce, cheese, and tomatoes. An easy dinner recipe that the whole family will enjoy, even your pickiest eaters! Source: https://www.dinneratthezoo.com/ground-beef-tacos/",
		"ingredients":"2 teaspoons vegetable oil\r\n1 pound lean ground beef I use 90% lean\r\n1/2 cup onion finely chopped\r\n1 tablespoon chili powder\r\n1/4 teaspoon garlic powder\r\n1/4 teaspoon onion powder\r\1/4 teaspoon crushed red pepper flakes optional\r\n1/4 teaspoon dried oregano\r\n1/2 teaspoon smoked paprika\r\n1 teaspoon ground cumin\r\n1 teaspoon salt\r\n1/2 teaspoon pepper\r\n1 14 ounce can petite diced tomatoes drained\r\n8 taco shells\r\nassorted toppings such as lettuce, tomato, onion and shredded cheese",
		"steps":"1. Heat the oil in a large pan over medium high heat.\r\n2. Add the ground beef and break up with a spatula.\r\n3. Add the onion to the pan.\r\n4. Cook, stirring occasionally, until beef is done and onion is soft, 5-6 minutes. Drain off any excess fat.\r\n5. Add the chili powder, garlic powder, onion powder, red pepper flakes, oregano, smoked paprika, cumin, salt and pepper to the pan. Stir to coat the meat in the seasonings.\r\n6. Add the tomatoes to the pan and simmer for 2-3 minutes.\r\n7. Spoon the beef into the taco shells and add toppings such as lettuce, tomatoes and cheese. Serve immediately.",
		},
		{"name": "Easy Chicken Chow Mein",
		"cook_time" : 40,
		"cats" : "Dinner, Chinese",
		"chef" : "lynda_faller",
		"photo" : "chowmein.jpeg",
		"about": "This quick and easy chow mein recipe will curb your takeaway cravings! Source: http://iamafoodblog.com/15-minute-easy-chicken-chow-mein-recipe/",
		"ingredients":"8 ounces chow mein egg noodles\r\n1 boneless, skinless chicken thigh cut into small strips\r\n1 teaspoon cornstarch\r\n2 teaspoons light soy sauce\r\n1 teaspoon shaoxing wine\r\noil, for the wok\r\n2 large eggs\r\nsalt and freshly ground pepper\r\n1/2 red onion, sliced\r\n3 green onions, cut into 2 inch lengths\r\n1-2 tablespoons light soy sauce, or to taste\r\n1 tablespoon dark soy sauce, or to taste",
		"steps":"1. Soak the noodles in hot tap water. In a small bowl, mix the chicken with the cornstarch, soy sauce, and shaoxing wine. Set aside.\r\n2. Heat up the oil in a wok or frying pan over medium high heat. When hot and shimmery, crack the eggs into the pan and scramble until cooked but still soft. Season with salt and pepper to taste then scoop out the eggs. The pan should still have a bit of oil in it, but if it’s dry, add a touch more.\r\n3. Add the onions and cook, over medium high heat, until slightly soft – you want them to have some bite to them still. Add the chicken, along with the marinade in the bowl and cook, stirring, until brown and cooked through.\r\n4. Drain the noodles and add them into the pan and toss everything together. Add the eggs back in, along with the green onions. Add the dark and light soy sauce and toss well, frying. Taste, adjust the seasoning, then enjoy!",
		},
		{"name": "Chicken Curry",
		"cook_time" : 45,
		"cats" : "Dinner, Indian",
		"chef" : "eve_ohagan",
		"photo" : "curry.jpeg",
		"about": "This is a traditional North Indian (Punjabi) chicken curry dish. Serve with basmati rice or fresh Indian roti or naan\r\nSource: https://www.allrecipes.com/recipe/80683/traditional-chicken-curry/",
		"ingredients":"1 pound skinless, boneless chicken breast halves - cut into bite-size pieces\r\n1 tablespoon fresh lemon juice\r\nSalt and pepper to taste\r\n3 tablespoons olive oil\r\n1 teaspoon cumin seed\r\n1 large onion, finely chopped\r\n2 cloves garlic, minced\r\n1 teaspoon minced fresh ginger\r\n1 (8 ounce) can peeled, chopped tomatoes\r\n1 teaspoon chili powder\r\n1/2 teaspoon ground turmeric\r\n1 teaspoon garam masala\r\n1/2 teaspoon ground cumin\r\n1 pinch ground coriander\r\n1/2 teaspoon paprika\r\n3 tablespoons plain yogurt\r\n2 medium potatoes, peeled and cut into 1 inch cubes\r\n1 1/2 cups water\r\n1 (5.5 ounce) can tomato juice",
		"steps":"1. In a large bowl, toss the chicken pieces with lemon juice, salt, and pepper to coat. Set aside.\r\n2. Heat oil in a large, heavy saucepan over medium heat. Stir in cumin seed and cook 1 minute, until lightly toasted. Mix in onion, garlic, and ginger. Cook until onion is tender. Add tomatoes, and season with chili powder, turmeric, garam masala, ground cumin, coriander, and paprika. Continue to cook and stir 2 minutes.\r\n3. Mix yogurt into the saucepan until well blended. Add chicken pieces, and potatoes. Mix in water and tomato juice. Reduce heat to medium-low. Cover and simmer about 40 minutes. Adjust seasonings to taste and garnish with fresh cilantro before serving.",
		},
		{"name": "St Paddy's Cupcakes",
		"cook_time" : 25,
		"cats" : "Dessert, St Patrick's Day",
		"chef" : "q_smart",
		"photo" : "cupcakes.jpeg",
		"about": "These cute Irish-themed cupcakes are perfect for sharing and easy enough to whip up the morning of your party. The cakes are made with a flavoursome stout and the icing is mixed with cream liquor for a traditional Irish taste and adult twist.\r\nSource: https://www.goodtoknow.co.uk/recipes/st-patrick-s-day-cupcakes",
		"ingredients":"Cupcakes:\r\n100g soft butter\r\n100ml stout\r\n40g cocoa powder\r\n150g plain flour\r\n1/2 tsp salt\r\n1 tsp baking powder\r\n200g light soft brown sugar\r\n1 egg\r\n75ml sour cream\r\n\r\nFrosting: \r\n200g soft butter\r\n450g icing sugar, sifted\r\n3-4 tbsps Irish cream liquor\r\nGreen sugar sprinkles to decorate (optional)\r\nGreen food colouring (optional)",
		"steps":"1. Preheat the oven to 180 C/350 F/Gas Mark 4. Line a 12 cup muffin tin with paper cases. Place the butter, stout and cocoa powder in a saucepan and place over a gentle heat, stir until the butter has melted and the mixture is smooth. Remove from the heat and allow to cool.\r\n2. In a large bowl sift together the flour, salt, baking powder and sugar. Add the cooled stout mixture and beat for 1 minute using an electric whisk on a medium speed. Add the egg and sour cream and beat for a further 2 minutes.\r\n3. Divide the batter evenly between the prepared tin. Bake for 20-25 minutes until cooked through and springy to the touch. Transfer the cakes to a cooling rack and leave to cool completely.\r\n4. For the frosting, cream the butter in a bowl until light and fluffy. Gradually beat in the icing sugar a little at a time then beat in the Irish cream liquor. Add the food colouring if using (start with a little and add more depending on the shade of green you want). Spoon or pipe the icing on the cooled cakes and sprinkle with green sugar to decorate.",
		},
		{"name": "California Rolls",
		"cook_time" : 50,
		"cats" : "Lunch, Japanese",
		"chef" : "q_smart",
		"photo" : "sushi.jpeg",
		"about": "A California roll is a fresh take on traditional Japanese rice rolls. Filled with avocado, crab, and cucumber, it's fresh and crunchy and makes a filling meal.\r\nSource: https://tasty.co/recipe/california-roll",
		"ingredients":"2 cups  sushi rice, cooked (460 g)\r\n¼ cup  seasoned rice vinegar (60 mL)\r\n4 half sheets sushi grade nori\r\n1 teaspoon  sesame seed, optional\r\n8 pieces imitation crab\r\n1 small cucumber, cut into matchsticks\r\n1 avocado, thinly sliced",
		"steps":"1. Season the sushi rice with the rice vinegar, fanning and stirring until room temperature.\r\n2. On a rolling mat, place one sheet of nori with the rough side facing upwards.\r\n3. Wet your hands and grab a handful of rice and place it on the nori. Spread the rice evenly throughout the nori without mashing the rice down. Season rice with a pinch of sesame seeds, if using, then flip it over so the nori is facing upwards.\r\n4. Arrange, in a horizontal row 1 inch (2.5 cm) from the bottom, the crab followed by a row of avocado and a row of cucumber.\r\n5. Grabbing both nori and the mat, roll the mat over the filling so the extra space at the bottom touches the other side, squeezing down to make a nice tight roll. Squeeze down along the way to keep the roll from holding its shape.\r\n6. Transfer the roll onto a cutting board. Rub a knife on a damp paper towel before slicing the roll into six equal portions.",
		},]
	cuisines = {"Italian": {"likes": 64, "photo":"italian.jpeg"},
		"American": {"likes": 32, "photo":"american.jpeg"},
		"Mexican": {"likes": 16, "photo":"mexican.jpeg"},
		"Chinese": {"likes": 16, "photo":"chinese.jpeg"},
		"Indian": {"likes": 16, "photo":"indian.jpeg"},
		"Japanese": {"likes": 16, "photo":"japanese.png"},}

	specials = {"St Patrick's Day": {"likes": 64, "photo":"stpaddys.jpeg"},
		"Easter": {"likes": 32, "photo":"easter.jpeg"},
		"Christmas": {"likes": 16, "photo":"christmas.jpeg"},
		"Halloween": {"likes": 16, "photo":"halloween.jpeg"},
		"4th of July": {"likes": 16, "photo":"4july.jpeg"},
		"Valentine's Day": {"likes": 16, "photo":"valentines.jpeg"},}

	cats = {"Breakfast": {"likes": 64, "photo":"breakfast.jpeg"},
		"Lunch": {"likes": 32, "photo":"lunch.jpeg"},
		"Dinner": {"likes": 16, "photo":"dinner.jpeg"},
		"Dessert": {"likes": 16, "photo":"dessert.jpeg"},
		"Cuisines": {"likes":160, "photo":"cuisines.jpeg"},
		"Special Occasions": {"likes": 160, "photo":"spec_occ.jpeg"},}

	print(" -Initializing admins . . .")
	for admin, admin_data in admins.items():
		u = add_user(admin,admin_data)
		admin_objects[admin] = u

	print(" -Creating Categories . . .")
	for cat, cat_data in cats.items():
		c = add_cat(cat,cat_data["likes"], 'CAT', None, cat_data["photo"])
		cat_objects[cat] = c

	print(" -Creating Subcategories . . .")
	for cuisine, cuisine_data in cuisines.items():
		c = add_cat(cuisine,cuisine_data["likes"], 'CUS', cat_objects["Cuisines"], cuisine_data["photo"])
		cat_objects[cuisine] = c

	for spec, spec_data in specials.items():
		c = add_cat(spec,spec_data["likes"], 'SPE', cat_objects["Special Occasions"], spec_data["photo"])
		cat_objects[spec] = c

	print(" -Adding recipes . . .")
	for recipe in recipes:
		add_recipe(recipe)

	print(" -Adding reviews . . .")
	for review, review_data in reviews.items():
		r = add_review(review,review_data)

def add_recipe(recipe):
	chef = recipe["chef"]
	name=recipe['name']
	r = Recipe.objects.get_or_create(chef=admin_objects[chef], name=name)[0]
	r.name = recipe['name']
	r.cook_time = recipe["cook_time"]
	cats_lst = recipe["cats"].split(", ")
	print("   ",name,cats_lst)
	for c in cats_lst:
		r.categories.add(cat_objects[c])
	r.photo = "food_pics/"+recipe["photo"]
	r.about = recipe["about"]
	r.ingredients = recipe["ingredients"]
	r.steps = recipe["steps"]
	r.save()
	return r

def add_cat(name, likes, type, supercat, photo):
	print("   ",name, type)
	if type == 'CUS' or type == 'SPE':
		c = Category.objects.get_or_create(name=name, type=type, supercat=supercat)[0]
	else:
		c = Category.objects.get_or_create(name=name, type=type)[0]
	c.likes=likes
	c.photo = "cat_pics/"+photo
	c.save()
	return c

def add_user(username, user_data):
	user = User.objects.get_or_create(username=username)[0]
	user.email = user_data["email"]
	user.set_password(user_data["password"])
	user.first_name = user_data["fname"]
	user.last_name = user_data["lname"]
	user.is_staff = True
	user.save()
	if(user_data["chef"]):
		add_chef(user,user_data)
	return user

def add_chef(user,user_data):
	chef = Chef.objects.get_or_create(user=user)[0]
	chef.photo = user_data["photo"]
	chef.bio = bio
	chef.save()
	return chef

def add_review(title,review_data):
	recipe_chef = review_data["chef"]
	recipe_name = review_data["recipe"]
	author = review_data["author"]
	rating = review_data["rating"]

	recipe = Recipe.objects.get(chef=admin_objects[recipe_chef], name=recipe_name)
	review = Review.objects.get_or_create(recipe=recipe, author=admin_objects[author])[0]
	review.title = title
	review.rating = review_data["rating"]
	review.comment = review_data["comment"]
	review.save()
	return review

if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
	print("Population complete.")
