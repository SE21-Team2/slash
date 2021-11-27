import React, { useEffect, useState } from "react";

function Items({ items, userLoggedIn }) {
    const [wishlist, setWishlist] = useState();

    function loadWishList() {
        if (userLoggedIn) {
            fetch(`/wishlist?user=${userLoggedIn}`)
                .then(res => res.json())
                .then(setWishlist);
        }
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
        loadWishList();
    }

    async function handleRemoveFromWishlist(item) {
        await fetch('/wishlistRemove', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user: userLoggedIn, item })
        });
        loadWishList();
    }

    console.log(wishlist);

    return (
        <table className="item-table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Source</th>
                    <th>Rating</th>
                </tr>
            </thead>
            <tbody>
                {items.map(item =>
                    <Item
                        key={item.link}
                        item={item}
                        wishlist={userLoggedIn && wishlist}
                        onAddToWishlist={handleAddToWishlist}
                        onRemoveFromWishlist={handleRemoveFromWishlist}
                    />
                )}
            </tbody>
        </table>
    );
}

const Item = ({ item, wishlist, onAddToWishlist, onRemoveFromWishlist }) => (
    <tr>
        <td className="name-td"><a href={item.link}>{item.title}</a></td>
        <td>{item.price}</td>
        <td>{item.website}</td>
        <td>{item.rating}</td>
        {wishlist && 
            <td>
                {wishlist.some(wlItem => wlItem.link === item.link)
                    ? <button onClick={() => onRemoveFromWishlist(item)}>Remove from wish list</button>
                    : <button onClick={() => onAddToWishlist(item)}>Add to wish list</button>
                }
            </td>
        }
    </tr>
);

export default Items;
