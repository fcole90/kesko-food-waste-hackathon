import React from 'react';

import MenuItem from '../menu-item/menu-item.component';

import './directory.styles.scss';

class Directory extends React.Component {
  constructor() {
    super();

    this.state = {
      sections: [
        {
          title: 'dairy',
          imageUrl: 'https://images.wallpaperscraft.com/image/cheese_different_delicious_dairy_70737_1280x720.jpg',
          id: 1,
          linkUrl: 'hats'
        },
        {
          title: 'meat',
          imageUrl: 'https://images.wallpaperscraft.com/image/meat_sliced_tasty_86945_1280x720.jpg',
          id: 2,
          linkUrl: ''
        },
        {
          title: 'chocolates',
          imageUrl: 'https://images.wallpaperscraft.com/image/chocolate_nuts_tasty_88252_1280x720.jpg',
          id: 3,
          linkUrl: ''
        },
        {
          title: 'fruits',
          imageUrl: 'https://images.wallpaperscraft.com/image/fruit_lemon_orange_kiwi_banana_apple_113092_3840x2400.jpg',
          size: 'large',
          id: 4,
          linkUrl: ''
        },
        {
          title: 'vegetables',
          imageUrl: 'https://c.wallhere.com/photos/6b/3b/vegetables_rice_still_life_dark-631636.jpg!d',
          size: 'large',
          id: 5,
          linkUrl: ''
        }
      ]
    };
  }

  render() {
    return (
      <div className='directory-menu'>
        {this.state.sections.map(({ id, ...otherSectionProps }) => (
          <MenuItem key={id} {...otherSectionProps} />
        ))}
      </div>
    );
  }
}

export default Directory;
