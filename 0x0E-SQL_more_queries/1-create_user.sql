-- creates a new user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFY BY "user_0d_1_pwd";
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
