// src/components/DrinksMenu.js
import React from 'react';
import { Link } from 'react-router';
import drinks from '../data/drinkMenu';

export default class DrinksMenu extends React.Component {
  render() {
    return (
      <nav className="atheletes-menu">
        {drinks.map(menuDrink => {
          return <Link key={menuDrink.id} to={`/drink/${menuDrink.id}`} activeClassName="active">
            {menuDrink.name}
          </Link>;
        })}
      </nav>
    );
  }
}