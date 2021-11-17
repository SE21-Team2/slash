import React, { useEffect, useState } from "react";

import "./Items.css";

function Items({ items, userLoggedIn }) {
    const [wishlist, setWishlist] = useState();

    async function loadWishList() {
        const wl = await fetch('/wishlist', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user: userLoggedIn })
        }).then(res => res.json());
        setWishlist(wl);
    }

    useEffect(() => {
        loadWishList();
    }, [userLoggedIn]);


    async function handleAddToWishlist(item) {
        await fetch('/wishlistAdd', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user: userLoggedIn, item })
        });
        await loadWishList()
    }

    async function handleRemoveFromWishlist(item) {
        await fetch('/wishlistRemove', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user: userLoggedIn, item })
        });
        await loadWishList();
    }

    return (
        <table id="item-table">
            <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Website</th>
                <th>Link</th>
                <th>Rating</th>
            </tr>
            {items.map(item =>
                <Item
                    key={item.link}
                    item={item}
                    wishlist={userLoggedIn && wishlist}
                    onAddToWishlist={handleAddToWishlist}
                    onRemoveFromWishlist={handleRemoveFromWishlist}
                />
            )}
        </table>
    );
}

const Item = ({ item, wishlist, onAddToWishlist, onRemoveFromWishlist }) => (
    <tr>
        <td>{item.name}</td>
        <td>{item.price}</td>
        <td>{item.website}</td>
        <td><a href={item.link}>{item.link}</a></td>
        <td>{item.rating}</td>
        {wishlist && 
            <td>
                {wishlist.any(wlItem => wlItem.link === item.link)
                    ? <button onClick={() => onRemoveFromWishlist(item)}>Remove from wish list</button>
                    : <button onClick={() => onAddToWishlist(item)}>Add to wish list</button>
                }
            </td>
        }
    </tr>
);

export default Items;
