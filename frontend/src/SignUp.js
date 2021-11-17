import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

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
        });

        if (valid) {
            navigate("/login");
        } else {
            setInvalidSignUp(true);
        }
    }

    return (
        <React.Fragment>
            {invalidSignUp && <p style={{ color: "red" }}>A user with this user name already exists</p>}
            <h2>Sign Up</h2>
            <form onSubmit={handleSignUp}>
                <h4>Username</h4>
                <input type="text" onChange={e => setUsername(e.target.value)} />
                <h4>Password</h4>
                <input type="password" onChange={e => setPassword(e.target.value)} />
                <br />
                <input type="submit" className="login-signup-button" value="Sign Up" />
            </form>
            <h4>Already have an account? <Link to="/login" className="login-signup-link">Login</Link></h4>
        </React.Fragment>
    );
}

export default SignUp;