import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { IconContext } from "react-icons";
import { BiUser } from "react-icons/bi";
import { AiOutlineLock } from "react-icons/ai";

import "./auth.css"

function Login({ onSetUserLoggedIn }) {
    const [username, setUsername] = useState();
    const [password, setPassword] = useState();

    const [invalidLogin, setInvalidLogin] = useState(false);

    const navigate = useNavigate();

    async function handleLogin(e) {
        e.preventDefault();
        const { valid } = await fetch("/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        }).then(res => res.json());
        
        if (valid) {
            onSetUserLoggedIn(username);
            navigate("/");
        } else {
            setInvalidLogin(true);
        }
    }

    return (
        <React.Fragment>
            {invalidLogin && <p style={{ color: "#800" }}>Invalid login credentials</p>}
            <h2>Log In</h2>
            <form onSubmit={handleLogin}>
                <h4>Username</h4>
                <div className="icon-text-container">
                    <IconContext.Provider value={{ className: "text-icon" }}><BiUser /></IconContext.Provider>
                    <input type="text" size="30" onChange={e => setUsername(e.target.value)} />
                </div>
                <h4>Password</h4>
                <div className="icon-text-container">
                    <IconContext.Provider value={{ className: "text-icon" }}><AiOutlineLock /></IconContext.Provider>
                    <input type="password" size="30" onChange={e => setPassword(e.target.value)} />
                </div>
                <br />
                <input type="submit" className="login-signup-button" value="Log In" />
            </form>
            <h4>Don't have an account? <Link to="/signup" className="login-signup-link">Sign Up</Link></h4>
        </React.Fragment>
    );
}

export default Login;