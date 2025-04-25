// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './Home';
import About from './About';
import RecipeFinder from './RecipeFinder';

function App() {
  return (
    <Router>
      <div style={{ padding: '20px' }}>
        <h1>Hello from Wasteless Words 🚀</h1>

        <nav style={{ marginBottom: '20px' }}>
          <Link to="/" style={{ marginRight: '10px' }}>Home</Link>
          <Link to="/about" style={{ marginRight: '10px' }}>About</Link>
          <Link to="/recipes">Recipes</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/recipes" element={<RecipeFinder />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
