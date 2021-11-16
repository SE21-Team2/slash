import React, { useState } from "react";
import Search from "./Search";
import Items from "./Items";

import "./Main.css";

function Main() {
    const [items, setItems] = useState();

    return (
        <div id="main-box">
            {/* <Search onSetItems={items => setItems(items)} /> */}
            <Search onSetItems={setItems} />
            {items && <Items items={items} />}
        </div>
    );
}

export default Main;
