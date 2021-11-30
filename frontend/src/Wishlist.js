import React, { useEffect, useState } from "react";
import CurrencySelect from "./CurrencySelect";

import { convertPrice } from "./shared";

function Wishlist({ userLoggedIn }) {
    const [wishlist, setWishlist] = useState(null);

    const [currency, setCurrency] = useState("usd");

    function handleRemoveFromWishlist(item) {
        fetch('/wishlistRemove', {
            method: "DELETE",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user: userLoggedIn, item })
        });
        setWishlist(wishlist.filter(wlItem => wlItem.link !== item.link));
    }

    useEffect(() => {
        fetch(`/wishlist?user=${userLoggedIn}`)
            .then(res => res.json())
            .then(setWishlist);
    }, [userLoggedIn]);

    if (wishlist === null) {
        return <h3>Loading wishlist...</h3>;
    }

    return (
        <React.Fragment>
            <h2>Wish List</h2>
            {wishlist.length === 0
                ? <h3>Wish List is empty</h3>
                : (
                    <React.Fragment>
                        <CurrencySelect currency={currency} setCurrency={setCurrency} />
                        <table className="item-table">
                            <thead>
                                <tr>
                                    <th>Image</th>
                                    <th>Name</th>
                                    <th>Price</th>
                                    <th>Source</th>
                                    <th>Rating</th>
                                </tr>
                            </thead>
                            <tbody>
                                {wishlist.map(wlItem =>
                                    <WishlistItem
                                        key={wlItem.link}
                                        item={wlItem}
                                        currency={currency}
                                        onRemoveFromWishlist={handleRemoveFromWishlist}
                                    />
                                )}
                            </tbody>
                        </table>
                    </React.Fragment>
                )}
        </React.Fragment>
    );
}

const WishlistItem = ({ item, currency, onRemoveFromWishlist }) => (
    <tr>
        <td>
            <div className="item-img-container">
                <img alt={item.title} src={item.img_link} />
            </div>
        </td>
        <td className="name-td"><a href={item.link}>{item.title}</a></td>
        <td>{convertPrice(item.price, currency)}</td>
        <td>{item.website}</td>
        <td>{item.rating}</td>
        <td><button onClick={() => onRemoveFromWishlist(item)}>Remove from wish list</button></td>
    </tr>
);

export default Wishlist;