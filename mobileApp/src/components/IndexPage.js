// src/components/IndexPage.js
import React from 'react';
import AthletePreview from './AthletePreview';
import athletes from '../data/athletes';
import drinks from '../data/drinkMenu';
import DrinkPreview from './DrinkPreview';

export default class IndexPage extends React.Component {
  render() {
    return (
      // <div className="home">
      //   <div className="athletes-selector">
      //     {athletes.map(athleteData => <AthletePreview key={athleteData.id} {...athleteData} />)}
      //   </div>
      // </div>
      <div className="home">
        <div className="drink-selector">
          {drinks.map(drinkData => <DrinkPreview key={drinkData.id} {...drinkData} />)}
        </div>
      </div>
    );
  }
}