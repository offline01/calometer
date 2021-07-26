import React from 'react';
import { BrowserRouter, Link, Switch, Route } from 'react-router-dom';
// import './App.css';
import HomePageView from "./components/pages/homePage";
import Login from "./components/pages/loginPage";
import Signup from "./components/pages/mf/Signup";
// import ResetPassword from "./components/pages/mf/ResetPassword";

function App() {
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
            <Route path="/signup" component={Signup}></Route>
            {/*<Route path="/resetpassword" component={ResetPassword} />*/}
          </Switch>
        </BrowserRouter>
      </div>
  );
}

export default App;
