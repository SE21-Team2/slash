import React, { useState } from "react";
import "./Search.css";

function Search({ onSetItems }) {
    const [numProducts, setNumProducts] = useState();
    const [sortBy, setSortBy] = useState("Relevance");
    const [displayOrder, setDisplayOrder] = useState("Ascending Order");
    const [currency, setCurrency] = useState("US Dollar");

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
        <form onSubmit={handleSearch}>
            <div>
                <div id="options-group">
                    <div className="option">
                        <h4>Number of products:</h4>
                        <input type="text" onChange={e => setNumProducts(e.target.value)} />
                    </div>

                    <div className="option">
                        <h4>Sort By:</h4>
                        <select value={sortBy} onChange={e => setSortBy(e.target.value)}>
                            <option value="Relevance">Relevance</option>
                            <option value="Price">Price</option>
                        </select>
                    </div>

                    <div className="option">
                        <h4>Display Order:</h4>
                        <select value={displayOrder} onChange={e => setDisplayOrder(e.target.value)}>
                            <option value="Ascending Order">Ascending Order</option>
                            <option value="Descending Order">Descending Order</option>
                        </select>
                    </div>

                    <div className="option">
                        <h4>Currency:</h4>
                        <select value={currency} onChange={e => setCurrency(e.target.value)}>
                            <option value="US Dollar">US Dollar</option>
                            <option value="Euro">Euro</option>
                            <option value="Australian Dollar">Australian Dollar</option>
                            <option value="Yuan">Yuan</option>
                            <option value="Yen">Yen</option>
                            <option value="British Pound">British Pound</option>
                        </select>
                    </div>
                </div>
            </div>

            <div id="search">
                <input type="text" size="50" />
                <input type="submit" value="Search" />
            </div>
        </form>
    );
}

export default Search;