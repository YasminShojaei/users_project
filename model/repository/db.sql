INSERT INTO users
(user_id, username, password)
values
(1, "yasminshojaei@gmail.com", "yasmin12");

SELECT * FROM users
WHERE user_id = 1;

UPDATE users
SET
    username = "yasminshojaei@gmail.com",
    password = "yasmin1234"
WHERE user_id = 1;

DELETE FROM users
WHERE user_id = 1;

-- SELECT *  FROM users;