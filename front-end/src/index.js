import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App'
import Login from './Admin/login'
import {
  BrowserRouter as Router,
  Route,
  // Link,
  // Switch,
  // Redirect
} from 'react-router-dom'


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

ReactDOM.render((
  <Router>
    <Route path='/index' component={App}>
    </Route>
    <Route path="/excel">
    </Route>
    <Route path='/login' component={Login}>
    </Route>
  </Router>),
  document.getElementById('root'))