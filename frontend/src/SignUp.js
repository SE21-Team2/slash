import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { IconContext } from "react-icons";
import { BiUser } from "react-icons/bi";
import { AiOutlineLock } from "react-icons/ai";

import "./auth.css";

function SignUp() {
    const [username, setUsername] = useState();
    const [password, setPassword] = useState();

    const [invalidSignUp, setInvalidSignUp] = useState(false);

    const navigate = useNavigate();

    async function handleSignUp(e) {
        e.preventDefault();

        const { valid } = await fetch("/signup", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        }).then(res => res.json());

        if (valid) {
            navigate("/loginpage");
        } else {
            setInvalidSignUp(true);
        }
    }

    return (
        <React.Fragment>
            {invalidSignUp && <p style={{ color: "#800" }}>A user with this user name already exists</p>}
            <h2>Sign Up</h2>
            <form onSubmit={handleSignUp}>
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
                <input type="submit" className="login-signup-button" value="Sign Up" />
            </form>
            <h4>Already have an account? <Link to="/loginpage" className="login-signup-link">Login</Link></h4>
        </React.Fragment>
    );
}

export default SignUp;