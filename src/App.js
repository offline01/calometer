import React, { useState, useEffect } from 'react';
import { BrowserRouter, Link, Switch, Route } from 'react-router-dom';
import './App.css';
import HomePageView from "./components/pages/homePage";
import Login from "./components/pages/loginPage";

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
      <div className="App">
        <BrowserRouter>
          <div>
            <Link className="App-link" to="/">Home</Link>
            &nbsp;|&nbsp;
            <Link className="App-link" to="/login">Login</Link>
          </div>
          <Switch>
            <Route exact path="/" component={HomePageView}></Route>
            <Route path="/login" component={Login}></Route>
          </Switch>
        </BrowserRouter>
      </div>
  );
}

export default App;
