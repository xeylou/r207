| course      | teacher       | files                                                           |
| :---        |    :----      |          :---                                                   |
| r207        | munier        | [munier's perso](https://munier.perso.univ-pau.fr/temp/R207/)   |

> :tv: here are my sql querries for the sql practice in the r207 course

## the start

initial commands after installing [SQlite](https://www.sqlite.org/download.html)

```sql
sqlite3.exe
.read magasin_sqlite.sql
.mode column
.headers on
.shell cls
```

## tp1

### 1. easy queries

- [x] (a) noms des fournisseurs situés à Paris
```sql
  select nomfour from fournisseur where (origine = 'Paris');
```

- [x] (b) numéros des produits provenant de Paris et dont le poids est supérieur ou égal à
```sql
select nomprod from produit where (origine = 'Paris') and (poids >= 0.3);
```

- [x] (c) idem précédent, mais triés par poids décroissant
```sql
select nomprod from produit where (origine = 'Paris') and (poids >= 0.3) order by poids asc;
```

- [x] (d) correspondance entre les numéros de fournisseurs et les numéros de produits de la même ville
```sql
select numfour, numprod from produit, fournisseur where (fournisseur.ville = produit.origine);
```

- [x] (e) correspondance entre les numéros de produits de la même ville
```sql
select numprod, origine from produit where origine in (select origine from produit group by origine having count(*) > 1);
```

- [x] (f) noms des produits dont le numéro est p1, p2, p3 ou p4
```sql
select nomprod from produit where (numprod <= 'p4');
```
```sql
select nomprod from produit where numprod in ('p1', 'p2', 'p3', 'p4');
```

### 2. subqueries

- [x] (a) noms des fournisseurs ayant livré des produits de couleur rouge
```sql
select fournisseur.nomfour from fournisseur, produit where produit.couleur = 'rouge';
```

- [x] (b) noms des fournisseurs ayant livré le produit p2
```sql
select fournisseur.nomfour from fournisseur, produit where produit.numprod = 'p2';
```

- [x] (c) numéros des fournisseurs ayant livré au moins un article identique à ceux livrés par f2
```sql
select * from stock where numprod in (select numprod from stock where (numfour = 'f2'));
```
```sql
select * from stock where numprod in ('p1', 'p2', 'p6', 'p7');
```
```sql
select distinct numfour from stock where numprod in (select numprod from stock where (numfour = 'f2'));
```

- [x] (d) numéros des produits originaires de la même ville que p1
```sql
select * from produit where origine in (select origine from produit where (numprod = 'p1'));
```

### 3. "exists" and "not exists"

- [x] (a) noms des fournisseurs ayant livré le produit p2
```sql
select nomfour from fournisseur where numfour in (select numfour from stock where (numprod = 'p2'));
```
```sql
select nomfour from fournisseur where exists (select numfour from stock where (numprod = 'p2'));
```

- [x] (b) noms des fournisseurs n'ayant pas livré le produit p2
```sql
select nomfour from fournisseur where numfour not in (select numfour from stock where (numprod = 'p2'));
```
```sql
select nomfour from fournisseur where not exists (select numfour from stock where (numprod = 'p2'));
```

- [x] (c) noms des fournisseurs tels qu'il n'y ait pas de produit qu'ils n'aient pas livré (. . .)

je comprends: donner le nom des fournisseurs ayant livrés tous leur produit
```sql
select nomfour from fournisseur where numfour not in (select distinct numfour from stock where numprod in (select numprod from produit));
```
```sql
 select nomfour from fournisseur where not exists (select 1 from produit, stock where produit.numprod = stock.numprod) and not exists (select 1 from fournisseur, stock where fournisseur.numfour = stock.numfour);
 ```
renvoie rien car tous les fournisseurs ont livrés leur produit

### 4. "group by" and "having"

- [x] (a) total des quantités livrées pour chaque produit
```sql
select numprod, sum(qte) from stock group by numprod;
```

- [x] (b) idem précédent, mais p1 non pris en compte
```sql
select numprod, sum(qte) from stock where numprod > 'p1' group by numprod;
```
fallait faire avec un count

- [x] (c) numéros des fournisseurs ayant livré au moins deux produits
```sql
select nomfour from fournisseur where numfour in (select numfour from stock group by numfour having count(*) >= 2);
```