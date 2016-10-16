// src/components/DrinkPage.js
import React from 'react';
import { Link } from 'react-router';
import NotFoundPage from './NotFoundPage';
import AthletesMenu from './AthletesMenu';
import DrinksMenu from './DrinksMenu';
import Medal from './Medal';
import Flag from './Flag';
import drinks from '../data/drinkMenu';

export default class DrinkPage extends React.Component {
  render() {
    const id = this.props.params.id;
    const drink = drinks.filter((drink) => drink.id === id)[0];
    if (!drink) {
      return <NotFoundPage/>;
    }
    const headerStyle = { backgroundImage: `url(/img/${drink.cover})` };
    return (
      <div className="athlete-full">
        <DrinksMenu/>
        <div className="athlete">
          <header style={headerStyle}/>
          <div className="picture-container">
            <img src={`/img/${drink.image}`}/>
            <h2 className="name">{drink.name}</h2>
          </div>
          <section className="description">
            (Find out more on <a href={drink.link} target="_blank">Wikipedia</a>).
          </section>
          <section className="medals">
            <p>Contains <strong>{drink.ingredients.length}</strong> ingredients:</p>
            <ul>{
              drink.ingredients.map((ingredient, i) => <Medal key={i} {...ingredient}/>)
            }</ul>
          </section>
        </div>
        <div className="navigateBack">
          <Link to="/">« Back to the index</Link>
        </div>
      </div>
    );
  }
}