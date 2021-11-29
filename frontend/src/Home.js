import React, { useState } from "react";
import { IconContext } from "react-icons";
import { FaSearch } from "react-icons/fa";

import Items from "./Items";
import CurrencySelect from "./CurrencySelect";

import "./Home.css";

function Home({ userLoggedIn }) {
    const [items, setItems] = useState();

    const [searchQuery, setSearchQuery] = useState("");
    const [numProducts, setNumProducts] = useState(10);
    const [sortBy, setSortBy] = useState("relevance-asc");

    const [currency, setCurrency] = useState("usd");

    function handleSearch(e) {
        e.preventDefault();
        if (searchQuery.trim() !== "") {
            const [sortField, displayOrder] = sortBy.split("-");
            
            const queryParams = new URLSearchParams({
                name: searchQuery,
                numProducts,
                sortBy: sortField,
                displayOrder: displayOrder,
                // currency
            });
            fetch("/search?" + queryParams.toString())
                .then(res => res.json())
                .then(setItems);
        }
    }

    return (
        <div>
            <h2>Search For Items</h2>
            <form onSubmit={handleSearch}>
                <div id="options-group">
                    <div className="option">
                        <h4>Number of products:</h4>
                        <input type="number" min="0" value={numProducts} onChange={e => setNumProducts(e.target.value)} />
                    </div>

                    <div className="option">
                        <h4>Sort By:</h4>
                        <select value={sortBy} onChange={e => setSortBy(e.target.value)}>
                            <option value="relevance-asc">Relevance</option>
                            <option value="rating-desc">Rating (high to low)</option>
                            <option value="rating-asc">Rating (low to high)</option>
                            <option value="price-desc">Price (high to low)</option>
                            <option value="price-asc">Price (low to high)</option>
                        </select>
                    </div>

                    <CurrencySelect currency={currency} setCurrency={setCurrency} />
                </div>

                <div id="search">
                    <div className="icon-text-container" id="search-text-container">
                        <IconContext.Provider value={{ className: "text-icon" }}><FaSearch /></IconContext.Provider>
                        <input id="search-text" type="text" size="60" value={searchQuery} onChange={e => setSearchQuery(e.target.value)} />
                    </div>
                    <input type="submit" value="Search" />
                </div>
            </form>
            {items && <hr />}
            {items && <Items items={items} currency={currency} userLoggedIn={userLoggedIn} />}
        </div>
    );
}

export default Home;
