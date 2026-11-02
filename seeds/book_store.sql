DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT
);

INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott');
