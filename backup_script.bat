@ECHO OFF

IF EXIST fisier.sql DEL fisier.sql
SET PGPASSWORD=2005

ECHO Realizam procesarea tabelelor


(FOR %%t IN ("aplicatie_Categorie" "aplicatie_Articol" "aplicatie_Marime" "aplicatie_MarimeArticol" "aplicatie_VanzariZilnice" "aplicatie_Depozit" "aplicatie_Stoc") DO (
    ECHO Tabelul %%t

    pg_dump --column-inserts --data-only --inserts -h localhost -U carina -p 5432 -d dj2025 -t %%t >> fisier.sql
))

SET PGPASSWORD=

