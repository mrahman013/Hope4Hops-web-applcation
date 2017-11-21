"""
Beer(name, abv, beer_type, seasonal, retail_cost, average_popularity, rarity, brewery)
Brewery(name, address, city, state, zip_code)
Storeowner(name, email, phone)
Store(name, address, city, state, zip_code, owner)
Customer(name, phone, email)

To add entries to stock:
        beer1 = Beer()
        beer2 = Beer()
        beer3 = Beer()

        db.session.add(beer1)
        db.session.add(beer2)
        db.session.add(beer3)
        db.session.commit()

        store1 = Store()
        store2 = Store()

        db.session.add(store1)
        db.session.add(store2)
        db.session.commit()

        #adding to the stock table with the realtions we have
        store1.beers.append(beer1)
        store1.beers.append(beer3)
        store2.beers.append(beer2)
        store2.beers.append(beer3)

"""

brewery1 = Brewery('The Alchemist', '100 Cottage Rd', 'Stowe', 'VT', 05672)
brewery2 = Brewery('Carton Brewing Company', '6 E Washington Ave', 'Atlantic Highlands', 'NJ', 07716)
brewery3 = Brewery('Kane Brewing Company', '1750 Bloomsbury Ave', 'Ocean', 'NJ', 07712)
brewery4 = Brewery('Magic Hat Brewing Company', '5 Bartlett Bay Rd', 'South Burlington', 'VT', 05403)

beer1 = Beer('Heady Topper', 0.08, 'IPA', None, 4.00, 0, 'common', brewery1)
beer2 = Beer('Focal Banger', 0.07, 'IPA', None, 3.50, 0, 'common', brewery1)
beer3 = Beer('El Jefe', 0.07, 'IPA', 'winter', 3.75, 0, 'common', brewery1)

beer4 = Beer('Boat', 0.06, 'ale', None, 2.25, 0, 'common', brewery2)
beer5 = Beer('IDIPA', 0.07, 'IPA', None, 3.25, 0, 'common', brewery2)
beer6 = Beer('077XX', 0.078, 'IPA', None, 3.30, 0, 'common', brewery2)
beer7 = Beer('Cupid', 0.066, 'Stout', 'winter', 3.25, 'common', brewery2)

beer8 = Beer('HEAD HIGH', 0.065, 'IPA', None, 2.00, 'common', brewery3)
beer9 = Beer('OVERHEAD', 0.082, 'IPA', None, 4.00, 'common', brewery3)
beer10 = Beer('SINGLE FIN', 0.048, 'Belgian', None, 2.00, 'common', brewery3)

beer11 = Beer('Feast of Fools', 0.072, 'Stout', 'winter', 8.00, 'common', brewery4)
beer12 = Beer('Circus Boy', 0.045, 'Ale', None, 1.50, 'common', brewery4)
beer13 = Beer('Mother Lager', 0.05, 'Lager', 'autumn', 1.50, 'common', brewery4)
beer14 = Beer('Art Hope Ale', 0.072, 'Pilsner', 'autumn', 2.50, 'common', brewery4)


store1 = Store()
store2 = Store()
store3 = Store()
