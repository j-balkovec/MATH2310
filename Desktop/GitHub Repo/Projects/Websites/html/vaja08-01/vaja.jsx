import React from 'react';
import './style.css';

function App() {
  return (
    <div className="container">
      <h1 className="main-heading">SEZNAMI V HTML</h1>

      <div className="list-section">
        <h2 className="list-heading">S kvadratki</h2>

        <ul className="square-list">
          <li> Jabolka</li>
          <li> Banane</li>
          <li> Limone</li>
          <li> Pomarance</li>
        </ul>
      </div>

      <div className="list-section">
        <h2 className="list-heading">S pikami</h2>
        <ul className="circle-list">
          <li>Jabolka</li>
          <li>Banane</li>
          <li>Limone</li>
          <li>Pomarance</li>
        </ul>
      </div>

      <div className="list-section">
        <h2 className="list-heading">S številkami</h2>
        <ol className="numbered-list">
          <li>Uvod v svetovni splet</li>
          <li>Matematika</li>
          <li>Uvod v Racunalnistvo</li>
          <li>Uporabniska programska oprema</li>
        </ol>
      </div>

      <div className="list-section">
        <h2 className="list-heading">Uporaba velikih črk za alineje</h2>
        <ol className="alpha-list">
          <li>Jabolka</li>
          <li>Banane</li>
          <li>Limone</li>
          <li>Pomarance</li>
        </ol>
      </div>

      <div className="list-section">
        <h2 className="list-heading">Uporaba rimskih številk za alineje</h2>
        <ol className="roman-list">
          <li>Jabolka</li>
          <li>Banane</li>
          <li>Limone</li>
          <li>Pomarance</li>
        </ol>
      </div>
    </div>
  );
}

export default App;
