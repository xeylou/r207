>  :tv: sql querries for the r207 course

| course      | teacher       | files                                                           |
| :---        |    :----      |          :---                                                   |
| r207        | munier        | [munier's perso](https://munier.perso.univ-pau.fr/temp/R207/)   |
 

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

- [x] (b) numéros des produits provenant de Paris et dont le poids est supérieur ou égal à 0.3
```sql
select nomprod from produit where (origine = 'Paris') and (poids >= 0.3);
```

- [x] (c) idem précédent, mais triés par poids décroissant
```sql
select nomprod from produit where (origine = 'Paris') and (poids >= 0.3) order by poids desc;
```

- [x] (d) correspondance entre les numéros de fournisseurs et les numéros de produits de la même ville
```sql
select numfour, numprod from produit, fournisseur where (fournisseur.ville = produit.origine);
```

- [x] (e) correspondance entre les numéros de produits de la même ville
```sql
select distinct a.numprod, b.numprod 
from produit a, produit b 
where (A.origine = b.origine) and (a.numprod < b.numprod);
```
dernière condition car distinct ne peut pas fonction+
ner
inférieur strict ou supérieur strict pour garder que l'un des deux (mêmes)

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
select nomfour 
from fournisseur 
where numfour 
in (select numfour from stock where numprod 
in (select numprod from produit where (couleur = 'rouge')));
```

- [x] (b) noms des fournisseurs ayant livré le produit p2
```sql
select nomfour 
from fournisseur 
where numfour 
in (select numfour from stock where (numprod = 'p2'));
```

- [x] (c) numéros des fournisseurs ayant livré au moins un article identique à ceux livrés par f2
```sql
select distinct numfour 
from stock 
where numprod 
in (select numprod from stock where (numfour = 'f2'));
```

- [x] (d) numéros des produits originaires de la même ville que p1
```sql
select numprod 
from produit 
where origine 
in (select origine from produit where (numprod = 'p1'));
```

### 3. "exists" and "not exists"

- [x] (a) noms des fournisseurs ayant livré le produit p2
```sql
select nomfour 
from fournisseur 
where exists (select a.numfour from stock a where (numprod = 'p2') 
and fournisseur.numfour = a.numfour);
```

- [x] (b) noms des fournisseurs n'ayant pas livré le produit p2
```sql
select nomfour 
from fournisseur 
where not exists (select a.numfour from stock a where (numprod = 'p2') 
and fournisseur.numfour = a.numfour);
```

- [] (c) noms des fournisseurs tels qu'il n'y ait pas de produit qu'ils n'aient pas livré (. . .)
```sql
```


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
select nomfour 
from fournisseur 
where numfour 
in (select numfour from stock group by numfour having count(*) >= 2);
```