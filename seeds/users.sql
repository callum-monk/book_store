DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ('testuser', '$2b$12$Qr7vqYH9r0qiGpWo4jORBOBiVsm.fDpNA0afJ4P2DGxefvTARqFG2');