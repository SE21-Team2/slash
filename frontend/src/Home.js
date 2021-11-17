import React, { useState } from "react";
import Search from "./Search";
import Items from "./Items";

function Home({ userLoggedIn }) {
    const [items, setItems] = useState();

    return (
        <div>
            <Search onSetItems={setItems} />
            {items && <hr />}
            {items && <Items userLoggedIn={userLoggedIn} items={items} />}
        </div>
    );
}

export default Home;
