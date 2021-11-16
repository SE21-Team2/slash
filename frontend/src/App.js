import React from "react";
import { Link, BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Main from "./Main";
import Login from "./Login";

import "./App.css";

const App = () => (
    <Router>
        <main>
            <Link to="/login" id="login-button">Login</Link>
            <h1 id="slash-title">SLASH</h1>
            <Routes>
                <Route path="/" element={<Main />} />
                <Route path="/login" element={<Login />} />
            </Routes>
        </main>
    </Router>
);

export default App;
