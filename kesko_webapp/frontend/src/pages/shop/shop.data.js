const SHOP_DATA = [
  {
    id: 1,
    title: 'Dairy',
    routeName: 'dairy',
    items: [
      {
        id: 1,
        name: 'Milk',
        imageUrl: 'https://images.wallpaperscraft.com/image/milk_bottle_field_145756_1280x720.jpg',
        price: 25
      },
      {
        id: 2,
        name: 'Yogurt',
        imageUrl: 'https://images.wallpaperscraft.com/image/strawberries_yogurt_rose_112890_1280x720.jpg',
        price: 18
      },
      {
        id: 3,
        name: 'Cheese',
        imageUrl: 'https://images.wallpaperscraft.com/image/cheeses_sausages_variety_70728_1280x720.jpg',
        price: 35
      },
      {
        id: 4,
        name: 'Butter',
        imageUrl: 'https://images.wallpaperscraft.com/image/pancakes_butter_lots_71522_1280x720.jpg',
        price: 25
      },
      {
        id: 5,
        name: 'Green Beanie',
        imageUrl: 'https://i.ibb.co/YTjW3vF/green-beanie.png',
        price: 18
      },
      {
        id: 6,
        name: 'Palm Tree Cap',
        imageUrl: 'https://i.ibb.co/rKBDvJX/palm-tree-cap.png',
        price: 14
      },
      {
        id: 7,
        name: 'Red Beanie',
        imageUrl: 'https://i.ibb.co/bLB646Z/red-beanie.png',
        price: 18
      },
      {
        id: 8,
        name: 'Wolf Cap',
        imageUrl: 'https://i.ibb.co/1f2nWMM/wolf-cap.png',
        price: 14
      },
      {
        id: 9,
        name: 'Blue Snapback',
        imageUrl: 'https://i.ibb.co/X2VJP2W/blue-snapback.png',
        price: 16
      }
    ]
  },
  {
    id: 2,
    title: 'Meat',
    routeName: 'meat',
    items: [
      {
        id: 10,
        name: 'Meat',
        imageUrl: 'https://images.wallpaperscraft.com/image/meat_rosemary_steak_114150_1280x720.jpg',
        price: 220
      },
      {
        id: 11,
        name: 'Chicken',
        imageUrl: 'https://images.wallpaperscraft.com/image/chicken_baked_food_dinner_82887_1280x720.jpg',
        price: 280
      },
      {
        id: 12,
        name: 'Steak',
        imageUrl: 'https://images.wallpaperscraft.com/image/chicken_baked_food_dinner_82887_1280x720.jpg',
        price: 110
      },
      {
        id: 13,
        name: 'Beef',
        imageUrl: 'https://images.wallpaperscraft.com/image/beef_meat_appetizing_107782_1280x720.jpg',
        price: 160
      },
      {
        id: 14,
        name: 'Nike Red High Tops',
        imageUrl: 'https://i.ibb.co/QcvzydB/nikes-red.png',
        price: 160
      },
      {
        id: 15,
        name: 'Nike Brown High Tops',
        imageUrl: 'https://i.ibb.co/fMTV342/nike-brown.png',
        price: 160
      },
      {
        id: 16,
        name: 'Air Jordan Limited',
        imageUrl: 'https://i.ibb.co/w4k6Ws9/nike-funky.png',
        price: 190
      },
      {
        id: 17,
        name: 'Timberlands',
        imageUrl: 'https://i.ibb.co/Mhh6wBg/timberlands.png',
        price: 200
      }
    ]
  },
  {
    id: 3,
    title: 'Chocolates',
    routeName: 'chocolates',
    items: [
      {
        id: 18,
        name: 'Black Jean Shearling',
        imageUrl: 'https://i.ibb.co/XzcwL5s/black-shearling.png',
        price: 125
      },
      {
        id: 19,
        name: 'Blue Jean Jacket',
        imageUrl: 'https://i.ibb.co/mJS6vz0/blue-jean-jacket.png',
        price: 90
      },
      {
        id: 20,
        name: 'Grey Jean Jacket',
        imageUrl: 'https://i.ibb.co/N71k1ML/grey-jean-jacket.png',
        price: 90
      },
      {
        id: 21,
        name: 'Brown Shearling',
        imageUrl: 'https://i.ibb.co/s96FpdP/brown-shearling.png',
        price: 165
      },
      {
        id: 22,
        name: 'Tan Trench',
        imageUrl: 'https://i.ibb.co/M6hHc3F/brown-trench.png',
        price: 185
      }
    ]
  },
  {
    id: 4,
    title: 'Fruits',
    routeName: 'fruits',
    items: [
      {
        id: 23,
        name: 'Apple',
        imageUrl: 'https://images.wallpaperscraft.com/image/fruit_ripe_apples_75138_1280x720.jpg',
        price: 25
      },
      {
        id: 24,
        name: 'Banana',
        imageUrl: 'https://images.wallpaperscraft.com/image/banana_basket_fruit_77494_1280x720.jpg',
        price: 20
      },
      {
        id: 25,
        name: 'Orange',
        imageUrl: 'https://images.wallpaperscraft.com/image/oranges_citrus_sweet_81983_1280x720.jpg',
        price: 80
      },
      {
        id: 26,
        name: 'Strawberry',
        imageUrl: 'https://images.wallpaperscraft.com/image/strawberries_berries_ripe_106492_1280x720.jpg',
        price: 80
      },
      {
        id: 27,
        name: 'Watermelon',
        imageUrl: 'https://images.wallpaperscraft.com/image/water-melons_half_ripe_cut_5493_1280x720.jpg',
        price: 45
      },
      {
        id: 28,
        name: 'Berries',
        imageUrl: 'https://images.wallpaperscraft.com/image/grapes_berries_ripe_101055_1280x720.jpg',
        price: 135
      },
      {
        id: 29,
        name: 'White Blouse',
        imageUrl: 'https://i.ibb.co/qBcrsJg/white-vest.png',
        price: 20
      }
    ]
  },
  {
    id: 5,
    title: 'Vegetables',
    routeName: 'vegetables',
    items: [
      {
        id: 30,
        name: 'Potato',
        imageUrl: 'https://images.wallpaperscraft.com/image/potatoes_vegetables_a_lot_of_77781_1280x720.jpg',
        price: 325
      },
      {
        id: 31,
        name: 'Carrot',
        imageUrl: 'https://images.wallpaperscraft.com/image/carrots_vegetables_many_110433_1280x720.jpg',
        price: 20
      },
      {
        id: 32,
        name: 'Tomato',
        imageUrl: 'https://images.wallpaperscraft.com/image/tomato_vegetable_ripe_111327_1280x720.jpg',
        price: 25
      },
      {
        id: 33,
        name: 'Mushroom',
        imageUrl: 'https://images.wallpaperscraft.com/image/mushrooms_vegetables_food_106737_1280x720.jpg',
        price: 25
      },
      {
        id: 34,
        name: 'Mushroom',
        imageUrl: 'https://images.wallpaperscraft.com/image/mushrooms_vegetables_food_106737_1280x720.jpg',
        price: 40
      },
      {
        id: 35,
        name: 'Pepper',
        imageUrl: 'https://images.wallpaperscraft.com/image/peppers_vegetables_still_life_111866_1280x720.jpg',
        price: 25
      }
    ]
  }
];

export default SHOP_DATA;
