// src/components/Layout.js
import React from 'react';
import { Link } from 'react-router';

export default class Layout extends React.Component {
  render() {
    return (
      <div className="app-container">
        <header>
          <Link to="/">
            <img className="logo" src="/img/main_banner.jpg"/>
          </Link>
        </header>
        <div className="app-content">{this.props.children}</div>
        <footer>
          <p>
            This is an application intended for interacting with the SQUID (Self-served Queueless Unjudging Intoxication Device).
          </p>
        </footer>
      </div>
    );
  }
}