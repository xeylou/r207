>  :tv: sql querries for third practice session of the r207 course

| course      | teacher       | files                                                           |
| :---        |    :----      |          :---                                                   |
| r207        | munier        | [munier's perso](https://munier.perso.univ-pau.fr/temp/R207/)   |
 

## the start

initial commands after installing [SQlite](https://www.sqlite.org/download.html)

```sql
sqlite3
.read magasin_sqlite.sql
.mode column
.headers on
.sh clear
```

# first practice

## first marks w/ sql

### 1. easy queries

- [x] (a) noms des fournisseurs situés à Paris
```sql
  select nomfour from fournisseur where (origine = 'Paris');
```