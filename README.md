# neural-nets-for-images-py# shopping-cart

# Setup the enviroment and install needed dependencies

`conda create -n shopping-env python=3.0`  
`conda activate shopping-env`  
`pip install -r requirements.txt`  

# How to use the code

To execute the code, open a terminal and type:
 
```sh
 python neural_net.py
```

The person at the counter is provided with the following options (see `table` below) 
and he/she needs to type the `product id` in the command line by typing the corresponding
numerical value between 1 and 20. Only integer values are recognized by the
code. When finished adding products and to calculate the total, one needs to type the word: `DONE`.

`  id                                               name                          aisle       department  price`  
`   1                         Chocolate Sandwich Cookies                  cookies cakes           snacks   3.50`  
`   2                                   All-Seasons Salt              spices seasonings           pantry   4.99`  
`   3               Robust Golden Unsweetened Oolong Tea                            tea        beverages   2.49`  
`   4  Smart Ones Classic Favorites Mini Rigatoni Wit...                   frozen meals           frozen   6.99`  
`   5                          Green Chile Anytime Sauce     marinades meat preparation           pantry   7.99`  
`   6                                       Dry Nose Oil               cold flu allergy    personal care  21.99`  
`   7                     Pure Coconut Water With Orange                  juice nectars        beverages   3.50`  
`   8                  Cut Russet Potatoes Steam N' Mash                 frozen produce           frozen   4.25`  
`   9                  Light Strawberry Blueberry Yogurt                         yogurt       dairy eggs   6.50`  
`  10     Sparkling Orange Juice & Prickly Pear Beverage  water seltzer sparkling water        beverages   2.99`  
`  11                                  Peach Mango Juice                   refrigerated        beverages   1.99`  
`  12                         Chocolate Fudge Layer Cake                 frozen dessert           frozen  18.50`  
`  13                                  Saline Nasal Mist               cold flu allergy    personal care  16.00`  
`  14                     Fresh Scent Dishwasher Cleaner                dish detergents        household   4.99`  
`  15                           Overnight Diapers Size 6                  diapers wipes           babies  25.50`  
`  16                      Mint Chocolate Flavored Syrup             ice cream toppings           snacks   4.50`  
`  17                                  Rendered Duck Fat                poultry counter     meat seafood   9.99`  
`  18                Pizza for One Suprema  Frozen Pizza                   frozen pizza           frozen  12.50`  
`  19   Gluten Free Quinoa Three Cheese & Mushroom Blend        grains rice dried goods  dry goods pasta   3.99`  
`  20     Pomegranate Cranberry & Aloe Vera Enrich Drink                  juice nectars        beverages   4.25`  

# How to change the TAX_RATE

Upon cloning this github repository (i.e., `git clone
git@github.com:lcqsigi/shopping-cart.git`). The user needs to create a `.env`
file in the `main` branch of the repository. The contents of the `.env` need to
be:

`TAX_RATE = 0.0875`  

Note the that the tax rate in NY is 8.75%. The tax rate value needs to be
updated accordingly in the `.env` file.
