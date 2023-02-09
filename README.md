# r107

| course      | teacher       | link                                                            |
| :---        |    :----      |          :---                                                   |
| r207        | munier        | [munier's perso](https://munier.perso.univ-pau.fr/temp/R207/)   |


initial commands
```sql
sqlite3.exe
.read magasin_sqlite.sql
.mode column
.headers on
.shell cls
```


- [x] (a) noms des fournisseurs situés à Paris
```sql
  select nomfour from fournisseur where (origine = 'Paris');
```


(b) numéros des produits provenant de Paris et dont le poids est supérieur ou égal à
```sql
select nomprod from produit where (origine = 'Paris') and (poids >= 0.3);
```

(c) idem précédent, mais triés par poids décroissant
```sql
select nomprod from produit where (origine = 'Paris') and (poids >= 0.3) order by poids asc;
```

(d) correspondance entre les numéros de fournisseurs et les numéros de produits de la même ville
```sql
select numfour, numprod from produit, fournisseur where (fournisseur.ville = produit.origine);
```

(e) correspondance entre les numéros de produits de la même ville
```sql
select numprod, origine from produit where origine in (select origine from produit group by origine having count(*) > 1);
```

(f) noms des produits dont le numéro est p1, p2, p3 ou p4
```sql
select nomprod from produit where (numprod <= 'p4');
```
```sql
select nomprod from produit where numprod in ('p1', 'p2', 'p3', 'p4');
```


(a) noms des fournisseurs ayant livré des produits de couleur rouge
```sql
select fournisseur.nomfour from fournisseur, produit where produit.couleur = 'rouge';
```

(b) noms des fournisseurs ayant livré le produit p2
```sql
select fournisseur.nomfour from fournisseur, produit where produit.numprod = 'p2';
```

(c) numéros des fournisseurs ayant livré au moins un article identique à ceux livrés par f2
```sql
select * from stock where numprod in (select numprod from stock where (numfour = 'f2'));
```
```sql
select * from stock where numprod in ('p1', 'p2', 'p6', 'p7');
```
```sql
select distinct numfour from stock where numprod in (select numprod from stock where (numfour = 'f2'));
```

(d) numéros des produits originaires de la même ville que p1
```sql
select * from produit where origine in (select origine from produit where (numprod = 'p1'));
```


(a) noms des fournisseurs ayant livré le produit p2
```sql
select nomfour from fournisseur where numfour in (select numfour from stock where (numprod = 'p2'));
```
```sql
select nomfour from fournisseur where exists (select numfour from stock where (numprod = 'p2'));
```



(b) noms des fournisseurs n'ayant pas livré le produit p2
```sql
select nomfour from fournisseur where numfour not in (select numfour from stock where (numprod = 'p2'));
```
```sql
select nomfour from fournisseur where not exists (select numfour from stock where (numprod = 'p2'));
```

(c) noms des fournisseurs tels qu'il n'y ait pas de produit qu'ils n'aient pas livré (. . .)

je comprends: donner le nom des fournisseurs ayant livrés tous leur produit
```sql
select nomfour from fournisseur where numfour not in (select distinct numfour from stock where numprod in (select numprod from produit));
```

```sql
 select nomfour from fournisseur where not exists (select 1 from produit, stock where produit.numprod = stock.numprod) and not exists (select 1 from fournisseur, stock where fournisseur.numfour = stock.numfour);
 ```
renvoie rien car tous les fournisseurs ont livrés leur produit