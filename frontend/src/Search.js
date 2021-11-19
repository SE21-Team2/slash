import React, { useState } from "react";
import "./Search.css";

import { IconContext } from "react-icons";
import { FaSearch } from "react-icons/fa";

function Search({ onSetItems }) {
    const [numProducts, setNumProducts] = useState();
    const [sortBy, setSortBy] = useState("relevance");
    const [displayOrder, setDisplayOrder] = useState("asc");
    const [currency, setCurrency] = useState("usd");

    function handleSearch(e) {
        e.preventDefault();
        const queryParams = new URLSearchParams({ numProducts, sortBy, displayOrder, currency });
        // const items = await fetch("/search?" + queryParams.toString());
        const items = [
            {name: "An item", price: 13.9, link: 'http://google.com', website: 'amazon', rating: 3.5},
            {name: "An item 2", price: 13.9, link: 'http://google.com', website: 'amazon', rating: 4.2},
            {name: "An item 3", price: 13.9, link: 'http://google.com', website: 'amazon', rating: 5.0},
            {name: "An item 4", price: 13.9, link: 'http://google.com', website: 'amazon', rating: 1.5}
        ]
        onSetItems(items);
    }

    return (
        <React.Fragment>
            <h2>Search For Items</h2>
            <form onSubmit={handleSearch}>
                <div id="options-group">
                    <div className="option">
                        <h4>Number of products:</h4>
                        <input type="text" onChange={e => setNumProducts(e.target.value)} />
                    </div>

                    <div className="option">
                        <h4>Sort By:</h4>
                        <select value={sortBy} onChange={e => setSortBy(e.target.value)}>
                            <option value="relevance">Relevance</option>
                            <option value="price">Price</option>
                        </select>
                    </div>

                    <div className="option">
                        <h4>Display Order:</h4>
                        <select value={displayOrder} onChange={e => setDisplayOrder(e.target.value)}>
                            <option value="asc">Ascending Order</option>
                            <option value="desc">Descending Order</option>
                        </select>
                    </div>

                    <div className="option">
                        <h4>Currency:</h4>
                        <select value={currency} onChange={e => setCurrency(e.target.value)}>
                            <option value="usd">US Dollar</option>
                            <option value="eu">Euro</option>
                            <option value="aud">Australian Dollar</option>
                            <option value="yuan">Yuan</option>
                            <option value="yen">Yen</option>
                            <option value="bp">British Pound</option>
                        </select>
                    </div>
                </div>

                <div id="search">
                    <div className="icon-text-container" id="search-text-container">
                        <IconContext.Provider value={{ className: "text-icon" }}><FaSearch /></IconContext.Provider>
                        <input id="search-text" type="text" size="60" />
                    </div>
                    <input type="submit" value="Search" />
                </div>
            </form>
        </React.Fragment>
    );
}

export default Search;