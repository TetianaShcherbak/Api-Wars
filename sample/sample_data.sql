ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS pk_user_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.planet_votes DROP CONSTRAINT IF EXISTS pk_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.planets DROP CONSTRAINT IF EXISTS pk_name CASCADE;
ALTER TABLE IF EXISTS ONLY public.planet_residents DROP CONSTRAINT IF EXISTS pk_name CASCADE;

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

DROP TABLE IF EXISTS public.planet_residents;
CREATE TABLE planet_residents (
    id serial NOT NULL,
    name VARCHAR,
    height VARCHAR,
    mass VARCHAR,
    skin_color VARCHAR,
    hair_color VARCHAR,
    eye_color VARCHAR,
    birth_year VARCHAR,
    gender VARCHAR,
    planet_name VARCHAR,
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

ALTER TABLE ONLY planet_residents
    ADD CONSTRAINT fk_planet_name FOREIGN KEY (planet_name) REFERENCES planets(name);
