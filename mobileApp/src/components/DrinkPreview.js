// src/components/DrinkPreview.js
import React from 'react';
import { Link } from 'react-router';

export default class DrinkPreview extends React.Component {
  render() {
    return (
      <Link to={`/drink/${this.props.id}`}>
        <div className="athlete-preview">
          <img src={`img/${this.props.image}`}/>
          <h2 className="name">{this.props.name}</h2>
          <span className="medals-count"><img src="/img/potion.png"/> {this.props.ingredients.length}</span>
        </div>
      </Link>
    );
  }
}