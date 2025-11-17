--
-- PostgreSQL database dump
--

\restrict OHuNGWz7ZvWwEU8obukgW4HCjTx4fFUybftFlVdCcg9vpecb1sBROowzht3wLZj

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_categorie; Type: TABLE DATA; Schema: django; Owner: carina
--

INSERT INTO django.aplicatie_categorie (id, nume, icon) VALUES (5, 'Cardigane', 'categorii_icon/cardigane.png');
INSERT INTO django.aplicatie_categorie (id, nume, icon) VALUES (4, 'Rochii', 'categorii_icon/rochii.png');
INSERT INTO django.aplicatie_categorie (id, nume, icon) VALUES (3, 'Blugi', 'categorii_icon/blugi.png');
INSERT INTO django.aplicatie_categorie (id, nume, icon) VALUES (2, 'Hanorace', 'categorii_icon/hanorace.png');
INSERT INTO django.aplicatie_categorie (id, nume, icon) VALUES (1, 'Tricouri', 'categorii_icon/tricouri.png');


--
-- Name: aplicatie_categorie_id_seq; Type: SEQUENCE SET; Schema: django; Owner: carina
--

SELECT pg_catalog.setval('django.aplicatie_categorie_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict OHuNGWz7ZvWwEU8obukgW4HCjTx4fFUybftFlVdCcg9vpecb1sBROowzht3wLZj

--
-- PostgreSQL database dump
--

\restrict 2d1QHaLu0ww7GOisv8WF0KUUoIpmG1jzE1ePkEMqWZFbWY7vVDcgyhdHpBwoWAj

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_articol; Type: TABLE DATA; Schema: django; Owner: carina
--

INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (5, 'Hanorac negru murder on my mind', 199.99, 2, 'produse/hoodie_murder_on_my_mind.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (2, 'Hanorac fever dream', 190.99, 2, 'produse/hoodie_fever_dream.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (4, 'Blugi baggy gri', 189.99, 3, 'produse/blugi_baggy_gri.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (3, 'Blugi baggy bleu', 160.90, 3, 'produse/blugi_baggy_bleu.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (8, 'Tricou rosu dalmatieni', 119.99, 1, 'produse/tricou_dalmatieni.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (6, 'Tricou another cirese', 99.99, 1, 'produse/tricou_another_cirese.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (10, 'Tricou alb umar gol', 90.90, 1, 'produse/tricou_umar_gol.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (1, 'Tricou negru agrafa Saint', 80.90, 1, 'produse/tricou_agrafa_saint.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (9, 'Tricou spirits of a dreamer', 79.90, 1, 'produse/tricou_spirits_of_a_dreamer.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (7, 'Tricou boys lie', 68.90, 1, 'produse/tricou_boys_lie.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (11, 'Hanorac tell her you love her', 169.00, 2, 'produse/hoodie_tell_her.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (12, 'Tricou catel cu perle', 79.99, 1, 'produse/tricou_dachund_perle.jpeg');
INSERT INTO django.aplicatie_articol (id, nume, pret, categorie_id, imagine) VALUES (13, 'Tricou cal roz', 75.90, 1, 'produse/tricou_cal_roz.jpeg');


--
-- Name: aplicatie_articol_id_seq; Type: SEQUENCE SET; Schema: django; Owner: carina
--

SELECT pg_catalog.setval('django.aplicatie_articol_id_seq', 13, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 2d1QHaLu0ww7GOisv8WF0KUUoIpmG1jzE1ePkEMqWZFbWY7vVDcgyhdHpBwoWAj

--
-- PostgreSQL database dump
--

\restrict cZzb2U7i5k1vVZ3ScaZOnkRcRe6LuA5fKbvW0DxvYbXsb7fBwtR0qbZVedmAHY2

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_marime; Type: TABLE DATA; Schema: django; Owner: carina
--

INSERT INTO django.aplicatie_marime (id, nume, descriere) VALUES (1, 'XS', 'BUST: 84-87cm, TALIE: 64-67cm, SOLD: 89-92cm');
INSERT INTO django.aplicatie_marime (id, nume, descriere) VALUES (2, 'S', 'BUST: 88-92cm, TALIE: 68-72cm, SOLD: 92-96cm');
INSERT INTO django.aplicatie_marime (id, nume, descriere) VALUES (3, 'M', 'BUST: 93-97cm, TALIE: 73-77cm, SOLD: 97-101cm');
INSERT INTO django.aplicatie_marime (id, nume, descriere) VALUES (4, 'L', 'BUST: 98-102cm, TALIE: 78-82cm, SOLD: 102-106cm');
INSERT INTO django.aplicatie_marime (id, nume, descriere) VALUES (5, 'XL', 'BUST: 103-107cm, TALIE: 83-87cm, SOLD: 107-111cm');


--
-- Name: aplicatie_marime_id_seq; Type: SEQUENCE SET; Schema: django; Owner: carina
--

SELECT pg_catalog.setval('django.aplicatie_marime_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict cZzb2U7i5k1vVZ3ScaZOnkRcRe6LuA5fKbvW0DxvYbXsb7fBwtR0qbZVedmAHY2

--
-- PostgreSQL database dump
--

\restrict R2vismfZCWgCsCyHyLRmkDTFpOi46PPJ34kHZIbBwLyOdaVltI3kLtI87OJbOCp

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_marimearticol; Type: TABLE DATA; Schema: django; Owner: carina
--

INSERT INTO django.aplicatie_marimearticol (id, articol_id, marime_id) VALUES (1, 1, 1);
INSERT INTO django.aplicatie_marimearticol (id, articol_id, marime_id) VALUES (2, 1, 2);
INSERT INTO django.aplicatie_marimearticol (id, articol_id, marime_id) VALUES (3, 1, 4);
INSERT INTO django.aplicatie_marimearticol (id, articol_id, marime_id) VALUES (4, 1, 5);
INSERT INTO django.aplicatie_marimearticol (id, articol_id, marime_id) VALUES (5, 5, 2);
INSERT INTO django.aplicatie_marimearticol (id, articol_id, marime_id) VALUES (6, 5, 1);
INSERT INTO django.aplicatie_marimearticol (id, articol_id, marime_id) VALUES (7, 5, 3);
INSERT INTO django.aplicatie_marimearticol (id, articol_id, marime_id) VALUES (8, 4, 1);
INSERT INTO django.aplicatie_marimearticol (id, articol_id, marime_id) VALUES (9, 10, 4);


--
-- Name: aplicatie_marimearticol_id_seq; Type: SEQUENCE SET; Schema: django; Owner: carina
--

SELECT pg_catalog.setval('django.aplicatie_marimearticol_id_seq', 9, true);


--
-- PostgreSQL database dump complete
--

\unrestrict R2vismfZCWgCsCyHyLRmkDTFpOi46PPJ34kHZIbBwLyOdaVltI3kLtI87OJbOCp

--
-- PostgreSQL database dump
--

\restrict bUKnVjFbifJukMtYBZ54z0wy2s5TjOYE75igHvhlB3HLy0eqvGkeeNjPVVqO5He

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_vanzarizilnice; Type: TABLE DATA; Schema: django; Owner: carina
--

INSERT INTO django.aplicatie_vanzarizilnice (id, data, cantitate, venit_total, articol_id) VALUES (2, '2025-11-09', 5, 454, 10);
INSERT INTO django.aplicatie_vanzarizilnice (id, data, cantitate, venit_total, articol_id) VALUES (3, '2025-11-09', 3, 507, 2);
INSERT INTO django.aplicatie_vanzarizilnice (id, data, cantitate, venit_total, articol_id) VALUES (4, '2025-11-09', 7, 699, 10);
INSERT INTO django.aplicatie_vanzarizilnice (id, data, cantitate, venit_total, articol_id) VALUES (5, '2025-11-09', 5, 345, 7);
INSERT INTO django.aplicatie_vanzarizilnice (id, data, cantitate, venit_total, articol_id) VALUES (6, '2025-11-09', 3, 600, 5);


--
-- Name: aplicatie_vanzarizilnice_id_seq; Type: SEQUENCE SET; Schema: django; Owner: carina
--

SELECT pg_catalog.setval('django.aplicatie_vanzarizilnice_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

\unrestrict bUKnVjFbifJukMtYBZ54z0wy2s5TjOYE75igHvhlB3HLy0eqvGkeeNjPVVqO5He

--
-- PostgreSQL database dump
--

\restrict A24pQHjKI5KYSLc8InuGdnQYTd0lFcqZyqvU1nJ1hVyTUDslDwB3bQjJpNM7pR9

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_depozit; Type: TABLE DATA; Schema: django; Owner: carina
--

INSERT INTO django.aplicatie_depozit (id, nume, adresa, oras, activ) VALUES (1, 'Depozit A', 'Strada Dumbrava Rosie 18', 'Bucuresti', true);
INSERT INTO django.aplicatie_depozit (id, nume, adresa, oras, activ) VALUES (2, 'Depozit B', 'Strada Soarelui 5', 'Bucuresti', true);
INSERT INTO django.aplicatie_depozit (id, nume, adresa, oras, activ) VALUES (3, 'Depozit C', 'Str. Independentei 17', 'Cluj', true);
INSERT INTO django.aplicatie_depozit (id, nume, adresa, oras, activ) VALUES (4, 'Depozit D', 'Strada Lalelelor', 'Iasi', true);
INSERT INTO django.aplicatie_depozit (id, nume, adresa, oras, activ) VALUES (5, 'Depozit E', 'Strada Frumoasa 3', 'Constanta', true);


--
-- Name: aplicatie_depozit_id_seq; Type: SEQUENCE SET; Schema: django; Owner: carina
--

SELECT pg_catalog.setval('django.aplicatie_depozit_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict A24pQHjKI5KYSLc8InuGdnQYTd0lFcqZyqvU1nJ1hVyTUDslDwB3bQjJpNM7pR9

--
-- PostgreSQL database dump
--

\restrict 7TG8hN1fdCbmgYUZBvee05inLZ3PCiYsRN15akSpMzgQitGuTBIyrTkE3cS4Ip7

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_stoc; Type: TABLE DATA; Schema: django; Owner: carina
--

INSERT INTO django.aplicatie_stoc (id, cantitate, actualizat, articol_id, depozit_id) VALUES (6, 15, '2025-11-09 13:23:06.15622+02', 1, 1);
INSERT INTO django.aplicatie_stoc (id, cantitate, actualizat, articol_id, depozit_id) VALUES (7, 20, '2025-11-09 13:23:25.539141+02', 2, 2);
INSERT INTO django.aplicatie_stoc (id, cantitate, actualizat, articol_id, depozit_id) VALUES (8, 25, '2025-11-09 13:23:39.409465+02', 3, 3);
INSERT INTO django.aplicatie_stoc (id, cantitate, actualizat, articol_id, depozit_id) VALUES (9, 10, '2025-11-09 13:25:09.899763+02', 4, 4);
INSERT INTO django.aplicatie_stoc (id, cantitate, actualizat, articol_id, depozit_id) VALUES (10, 12, '2025-11-09 13:25:22.453374+02', 5, 5);
INSERT INTO django.aplicatie_stoc (id, cantitate, actualizat, articol_id, depozit_id) VALUES (11, 8, '2025-11-09 13:25:34.206022+02', 10, 2);
INSERT INTO django.aplicatie_stoc (id, cantitate, actualizat, articol_id, depozit_id) VALUES (12, 7, '2025-11-09 13:25:49.301861+02', 1, 4);


--
-- Name: aplicatie_stoc_id_seq; Type: SEQUENCE SET; Schema: django; Owner: carina
--

SELECT pg_catalog.setval('django.aplicatie_stoc_id_seq', 12, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 7TG8hN1fdCbmgYUZBvee05inLZ3PCiYsRN15akSpMzgQitGuTBIyrTkE3cS4Ip7

