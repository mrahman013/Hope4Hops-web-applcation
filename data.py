""" store data that are pushed on db """
# included unused Customer and Storeowner incase need later and they have relation
# pylint: disable=unused-import
from hopsapp import db
from hopsapp.models import Beer, Brewery, Store, Customer, Storeowner
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
# pylint: disable=line-too-long, invalid-name, no-member
"""
Note: links to beer imgs
https://cdn.beeradvocate.com/im/beers/16814.jpg (Heady Topper)
https://alchemistbeer.com/ (for Focal Banger & El Jefe imgs)
http://cartonbrewing.com/wp-content/uploads/2015/04/BOAT_can.jpg
http://cartonbrewing.com/wp-content/uploads/2015/08/ID_can.jpg
http://cartonbrewing.com/wp-content/uploads/2015/04/077XX_can.jpg
http://cartonbrewing.com/wp-content/uploads/2016/02/CUPID_can_web.png
https://i.pinimg.com/originals/90/76/79/9076793b07fb7cd58f09ade15f02072f.jpg (Head High)
http://www.businessinsider.in/thumb/msid-59600892,width-640,resizemode-4/NEW-JERSEY-Kane-Brewing-Company-Head-High.jpg?244690 (Head High)
https://bestofnj.com/wp-content/uploads/2017/06/6-kane-brewing.jpg (OVERHEAD)
https://cdn.beeradvocate.com/im/beers/185178.jpg (SNEAKBOX)
https://d33wubrfki0l68.cloudfront.net/951723edd0174e8704ce4b281ee4f49c4b4db5fb/da62a/img/elixirs/bottleswithpints/feastoffools.png (feat of fools)
http://www.williamsdistributing.com/wp-content/uploads/2017/06/CIRCUS.jpg (circus boy)
https://d33wubrfki0l68.cloudfront.net/872fe6d05fcedca21b1ae2cbffb4817ec4396ebe/b69d4/img/elixirs/bottleswithpints/motherlager.png (mother lager)
https://decrescente.net/images/suppliers/north-american-breweries/magic-hat/magic-hat-art-hop/art-hop-can-lg.png (art hop)
https://www.shoppersvineyard.com/images/labels/cricket-hill-east-coast-lager.gif (east coast lager)
http://media.nj.com/food/photo/cricket-hill-american-pale-ale-beer-of-the-weekpng-4885b60b2a8c6894.png (american pale ale)
http://newjerseycraftbeer.com/wp-content/uploads/gravity_forms/5-48b61b129df756afa4ec5393984f2ddf/2015/03/CH_ReleaseEvent_JerseySummer.jpg (jersey summer)
http://nebula.wsimg.com/3704b82109d165d6516e12154eaced81?AccessKeyId=22E47027FF5B90820C12&disposition=0&alloworigin=1 (SIM-NOTIC)
"""



brewery1 = Brewery('The Alchemist', '100 Cottage Rd', 'Stowe', 'VT', '05672', 32.165923, -94.340370)
brewery2 = Brewery('Carton Brewing Company', '6 E Washington Ave', 'Atlantic Highlands', 'NJ', '07716', 40.411777, -74.038177)
brewery3 = Brewery('Kane Brewing Company', '1750 Bloomsbury Ave', 'Ocean', 'NJ', '07712', 40.236504, -74.044961)
brewery4 = Brewery('Magic Hat Brewing Company', '5 Bartlett Bay Rd', 'South Burlington', 'VT', '05403', 44.428961, -73.213401)
brewery5 = Brewery('Cricket Hill Brewery', '24 Kulick Rd', 'Fairfield', 'NJ', '07004', 40.872614, -74.296310)

db.session.add(brewery1)
db.session.add(brewery2)
db.session.add(brewery3)
db.session.add(brewery4)
db.session.add(brewery5)
db.session.commit()

#Beer(name, beer_image, abv, beer_type, seasonal, retail_cost, average_popularity, rarity, brewery)
    # accepts: ['MON' | 'TUE' | 'WED' | 'THU' | 'FRI' | 'SAT' | 'SUN']

# beer1 = Beer('Heady Topper', 'https://i.imgur.com/6ZOFUM3.jpg', 0.08, 'IPA', None, 4.00, 0, 'common', 'TUE', brewery1)
beer1 = Beer('Heady Topper', 'https://i.imgur.com/6ZOFUM3.jpg', 0.08, 'IPA', None, 4.00, 0, 'common', 'TUE', brewery_id=1)
beer2 = Beer('Focal Banger', 'https://i.imgur.com/aH7bZ9G.jpg', 0.07, 'IPA', None, 3.50, 0, 'common', 'THU', brewery_id=1)
beer3 = Beer('El Jefe', 'https://i.imgur.com/J0cHO8s.jpg', 0.07, 'IPA', 'winter', 3.75, 0, 'common', 'MON', brewery_id=1)

beer4 = Beer('Boat', 'https://i.imgur.com/WMEMUn0.jpg', 0.06, 'ale', None, 2.25, 0, 'common', 'TUE', brewery_id=2)
beer5 = Beer('IDIPA', 'https://i.imgur.com/FOtF8r0.jpg', 0.07, 'IPA', None, 3.25, 0, 'common', 'TUE', brewery_id=2)
beer6 = Beer('077XX', 'https://i.imgur.com/gPeh0Lf.jpg', 0.078, 'IPA', None, 3.30, 0, 'common', 'TUE', brewery_id=2)
beer7 = Beer('Cupid', 'https://i.imgur.com/H6sF289.png', 0.066, 'Stout', 'winter', 3.25, 0, 'common', 'FRI', brewery_id=2)

beer8 = Beer('HEAD HIGH', 'https://i.imgur.com/pjp6Hm2.jpg', 0.065, 'IPA', None, 2.00, 0, 'common', 'WED', brewery_id=3)
beer9 = Beer('OVERHEAD', 'https://i.imgur.com/VRcH0wR.jpg', 0.082, 'IPA', None, 4.00, 0, 'common', 'WED', brewery_id=3)
beer10 = Beer('SNEAKBOX', 'https://i.imgur.com/uNTzf0J.jpg', 0.052, 'Ale', None, 2.00, 0, 'common', 'MON', brewery_id=3)

beer11 = Beer('Feast of Fools', 'https://i.imgur.com/2UmyY4Q.png', 0.072, 'Stout', 'winter', 8.00, 0, 'common', 'FRI', brewery_id=4)
beer12 = Beer('Circus Boy', 'https://i.imgur.com/i2yjYql.jpg', 0.045, 'Ale', None, 1.50, 0, 'common', 'MON', brewery_id=4)
beer13 = Beer('Mother Lager', 'https://i.imgur.com/UQ5c5OK.png', 0.05, 'Lager', 'autumn', 1.50, 0, 'common', 'WED', brewery_id=4)
beer14 = Beer('Art Hop Ale', 'https://i.imgur.com/uI6HYaM.png', 0.072, 'Pilsner', 'autumn', 2.50, 0, 'common', 'THU', brewery_id=4)

beer15 = Beer('EAST COAST LAGER', 'https://i.imgur.com/08cDEC8.png', 0.042, 'Lager', None, 1.50, 0, 'common', 'SAT', brewery_id=5)
beer16 = Beer('AMERICAN PALE ALE', 'https://i.imgur.com/EAmWqua.png?1', 0.055, 'Ale', None, 1.74, 0, 'common', 'WED', brewery_id=5)
beer17 = Beer('JERSEY SUMMER BREAKFAST ALE', 'https://i.imgur.com/E3Lu02z.jpg?1', 0.05, 'Ale', 'summer', 1.75, 0, 'common', 'WED', brewery_id=5)
beer18 = Beer('SIM-NOTIC IMPERIAL IPA', 'https://i.imgur.com/5r0Hb0O.jpg', 0.082, 'IPA', 'spring', 3.50, 0, 'common', 'TUE', brewery_id=5)

db.session.add(beer1)
db.session.add(beer2)
db.session.add(beer3)
db.session.add(beer4)
db.session.add(beer5)
db.session.add(beer6)
db.session.add(beer7)
db.session.add(beer8)
db.session.add(beer9)
db.session.add(beer10)
db.session.add(beer11)
db.session.add(beer12)
db.session.add(beer13)
db.session.add(beer14)
db.session.add(beer15)
db.session.add(beer16)
db.session.add(beer17)
db.session.add(beer18)
db.session.commit()


store1 = Store('Good Beer', '422 E 9th St', 'New York', 'NY', '10009', 0, 40.727588, -73.983858)
store2 = Store('Top Hops', '94 Orchard St', 'New York', 'NY', '10002', 0, 40.718403, -73.989943)
store3 = Store('New Beer Distributors', '167 Chrystie St', 'New York', 'NY', '10002', 0, 40.720793, -73.997962)
store4 = Store('Carmine Street Beers', '52 A Carmine St', 'New York', 'NY', '10014', 0, 40.729821, -74.003613)

db.session.add(store1)
db.session.add(store2)
db.session.add(store3)
db.session.add(store4)
db.session.commit()

store1.beers.append(beer1)
store1.beers.append(beer2)
store1.beers.append(beer4)
store1.beers.append(beer5)
store1.beers.append(beer6)
store1.beers.append(beer7)
store1.beers.append(beer11)
store1.beers.append(beer13)
store1.beers.append(beer16)
store1.beers.append(beer18)

store2.beers.append(beer2)
store2.beers.append(beer4)
store2.beers.append(beer6)
store2.beers.append(beer9)
store2.beers.append(beer10)
store2.beers.append(beer12)
store2.beers.append(beer14)
store2.beers.append(beer16)
store2.beers.append(beer18)

store3.beers.append(beer1)
store3.beers.append(beer2)
store3.beers.append(beer3)
store3.beers.append(beer11)
store3.beers.append(beer12)
store3.beers.append(beer13)
store3.beers.append(beer14)

store4.beers.append(beer4)
store4.beers.append(beer5)
store4.beers.append(beer6)
store4.beers.append(beer7)
store4.beers.append(beer8)
store4.beers.append(beer9)
store4.beers.append(beer10)
store4.beers.append(beer15)
store4.beers.append(beer16)
store4.beers.append(beer17)
store4.beers.append(beer18)


beer1 = Beer.query.filter_by(name='Heady Topper').first()
beer2 = Beer.query.filter_by(name='Focal Banger').first()
beer3 = Beer.query.filter_by(name='El Jefe').first()
beer4 = Beer.query.filter_by(name='Boat').first()
beer5 = Beer.query.filter_by(name='IDIPA').first()
beer6 = Beer.query.filter_by(name='077XX').first()
beer7 = Beer.query.filter_by(name='Cupid').first()
beer8 = Beer.query.filter_by(name='HEAD HIGH').first()
beer9 = Beer.query.filter_by(name='OVERHEAD').first()
beer10 = Beer.query.filter_by(name='SNEAKBOX').first()
beer11 = Beer.query.filter_by(name='Feast of Fools').first()
beer12 = Beer.query.filter_by(name='Circus Boy').first()
beer13 = Beer.query.filter_by(name='Mother Lager').first()
beer14 = Beer.query.filter_by(name='Art Hop Ale').first()
beer15 = Beer.query.filter_by(name='EAST COAST LAGER').first()
beer16 = Beer.query.filter_by(name='AMERICAN PALE ALE').first()
beer17 = Beer.query.filter_by(name='JERSEY SUMMER BREAKFAST ALE').first()
beer18 = Beer.query.filter_by(name='SIM-NOTIC IMPERIAL IPA').first()
