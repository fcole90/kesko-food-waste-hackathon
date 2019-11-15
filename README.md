# Green K - Vihreä K
K-group app for reducing food waste by optimising consumer consumption and maket store optimisation.

## Kesko, kustomer, kestävä
The apps aims at food sustainability by reducing food waste. This is done in a double way:
- directing customers to buy *expire-soon* food;
- gathering customers data habits for K-markets to better optimise future store updates.

## How does it work?
The app is a webapp that suggests users the best K-markets to go to buy the products they desire. The user will provide a position and a grocery list. The app will hence find the closest K-market that has the greatest amount of *expire-soon* food among the items in the user's grocery list, and taking into account the selling probability of an item given the popularity of the item and the shop.

## Frontend
Simple mobile-first webapp, with few screens. The workflow is the following:
1. User selects grocery list (input 1)
2. User receives a list of ranked K-market according to optimisation (output 1)
3. User selects a market (input 2)
4. User receives a link to map (output 2) (map can be any in Google Maps, OpenStreetMap, Reittiopass)

## K-market advantage
We can gather data on user consumptions habits from this simple app, which K-group can then use for improving the store selection. 

## Why the user wants to use it?
Target users care for environment and want to reduce food waste. In addition users might want to use the app to try to save money on *close-to-expiry* products.

## Backend
Implemented in Django using the Restful APIs plugin. It also interacts with a simpple optimisation algorithm for returning the markets ranking list.

## Expiry date workaround
We have no expiry date API available, so we estimate the amount of *close-expiry* items. We know that K-group has such API internally, so it can be implemented later.

## Future ideas (aka Wishlist)
- Return a group of K-markets to cover all food items (like if K1 doesn't have fish, also optimise for a K2)
- Gamify the app to make users compete on sustinability
- Group items brandless (like just *milk*, then autoselect a brand which many items on close expiry)
