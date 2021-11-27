import React, { useEffect, useState } from "react";

function Wishlist({ userLoggedIn }) {
    const [wishlist, setWishlist] = useState(null);

    function handleRemoveFromWishlist(item) {
        fetch('/wishlistRemove', {
            method: "POST",
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
        return null;
    }

    return (
        <React.Fragment>
            <h2>Wish List</h2>
            {wishlist.length === 0
                ? <h3>Wish List is empty</h3>
                : (
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
                            {wishlist.map(wlItem =>
                                <WishlistItem
                                    key={wlItem.link}
                                    item={wlItem}
                                    onRemoveFromWishlist={handleRemoveFromWishlist}
                                />
                            )}
                        </tbody>
                    </table>
                )}
        </React.Fragment>
    );
}

const WishlistItem = ({ item, onRemoveFromWishlist }) => (
    <tr>
        <td className="name-td"><a href={item.link}>{item.title}</a></td>
        <td>{item.price}</td>
        <td>{item.website}</td>
        <td>{item.rating}</td>
        <td><button onClick={() => onRemoveFromWishlist(item)}>Remove from wish list</button></td>
    </tr>
);

export default Wishlist;