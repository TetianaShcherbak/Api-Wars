ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS pk_user_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.planet_votes DROP CONSTRAINT IF EXISTS pk_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.planets DROP CONSTRAINT IF EXISTS pk_id CASCADE;

DROP TABLE IF EXISTS public.users;
CREATE TABLE users (
    user_id serial NOT NULL,
    username VARCHAR,
    hashed_password VARCHAR
);

DROP TABLE IF EXISTS public.planet_votes;
CREATE TABLE planet_votes (
    id serial NOT NULL,
    planet_id INTEGER,
    planet_name VARCHAR,
    user_id INTEGER,
    submission_time TIMESTAMP without time zone
);

DROP TABLE IF EXISTS public.planets;
CREATE TABLE planets (
    id serial NOT NULL,
    name VARCHAR,
    diameter VARCHAR,
    climate VARCHAR,
    terrain VARCHAR,
    surface_water VARCHAR,
    population VARCHAR,
    last_update_time VARCHAR
);

ALTER TABLE ONLY users
    ADD CONSTRAINT pk_user_id PRIMARY KEY (user_id);

ALTER TABLE ONLY planet_votes
    ADD CONSTRAINT pk_id PRIMARY KEY (id);

ALTER TABLE ONLY planets
    ADD CONSTRAINT pk_name PRIMARY KEY (name);

ALTER TABLE ONLY planet_votes
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id);

ALTER TABLE ONLY planet_votes
    ADD CONSTRAINT fk_planet_name FOREIGN KEY (planet_name) REFERENCES planets(name);

--INSERT INTO users VALUES (0, 0);
--INSERT INTO question_tag VALUES (7, 4);

