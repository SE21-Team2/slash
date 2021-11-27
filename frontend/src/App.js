import React, { useState } from "react";
import { Link, BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./Home";
import Login from "./Login";
import Wishlist from "./Wishlist";

import "./App.css";
import SignUp from "./SignUp";

function useUserLoggedIn() {
    const [userLoggedIn, setUserLoggedIn] = useState(
        JSON.parse(localStorage.getItem('user'))?.UserLoggedIn
    );
  
    function saveUserLoggedIn(username) {
        if (username) {
            localStorage.setItem('user', JSON.stringify(username));
            setUserLoggedIn(username);
        } else {
            localStorage.removeItem('user');
            setUserLoggedIn(null);
        }
    };
  
    return [userLoggedIn, saveUserLoggedIn];
}

function App() {
    const [userLoggedIn, setUserLoggedIn] = useUserLoggedIn();

    return (
        <Router>
            <div id="top-right-links">
                {userLoggedIn
                    ? (
                        <React.Fragment>
                            <Link to="/wishlist">View Wishlist</Link>
                            <Link to="#" onClick={() => setUserLoggedIn(null)}>Log Out</Link>
                        </React.Fragment>
                    )
                    : <Link to="/login">Log In</Link>
                }
            </div>
            <h1 id="slash-title"><Link to="/">SLASH</Link></h1>
            <main>
                <Routes>
                    <Route path="/" element={<Home userLoggedIn={userLoggedIn} />} />
                    <Route path="/wishlist" element={<Wishlist userLoggedIn={userLoggedIn} />} />
                    <Route path="/login" element={<Login onSetUserLoggedIn={setUserLoggedIn} />} />
                    <Route path="/signup" element={<SignUp />} />
                </Routes>
            </main>
        </Router>
    );
}

export default App;
