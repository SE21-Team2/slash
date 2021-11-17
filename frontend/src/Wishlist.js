import React, { useEffect, useState } from "react";

import "./Items.css";

function Wishlist({ userLoggedIn }) {
    const [wishlist, setWishlist] = useState();

    function handleRemoveFromWishlist(item) {
        fetch('/wishlistRemove', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user: userLoggedIn, item })
        });
        setWishlist(wishlist.filter(wlItem => wlItem.link !== item.link));
    }

    useEffect(() => {
        fetch('/wishlist', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user: userLoggedIn })
        }).then(data => data.json()).then(setWishlist);
    }, [userLoggedIn]);

    return (
        <React.Fragment>
            <h2>Wish List</h2>
            <table id="item-table">
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Website</th>
                    <th>Link</th>
                    <th>Rating</th>
                </tr>
                {wishlist.map(wlItem =>
                    <WishlistItem
                        key={wlItem.link}
                        item={wlItem}
                        onRemoveFromWishlist={handleRemoveFromWishlist}
                    />
                )}
            </table>
        </React.Fragment>
    );
}

const WishlistItem = ({ item, onRemoveFromWishlist }) => (
    <tr>
        <td>{item.name}</td>
        <td>{item.price}</td>
        <td>{item.website}</td>
        <td><a href={item.link}>{item.link}</a></td>
        <td>{item.rating}</td>
        <td><button onClick={() => onRemoveFromWishlist(item)}>Remove from wish list</button></td>
    </tr>
);

export default Wishlist;