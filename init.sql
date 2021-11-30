CREATE TABLE user_data(
    username VARCHAR NOT NULL,
    password        VARCHAR NOT NULL,
    PRIMARY KEY(username)
);

CREATE TABLE wishlist(
    username  VARCHAR,
    name       VARCHAR NOT NULL,
    price       DECIMAL NOT NULL,
    website     VARCHAR NOT NULL,
    link        VARCHAR NOT NULL,
    rating      DECIMAL NOT NULL,
    img_link    VARCHAR NOT NULL,
    CONSTRAINT userConstraint
        FOREIGN KEY(username) REFERENCES user_data(username)
);

