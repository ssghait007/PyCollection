
### YAML Breakdown
###### datatypes
-   `seq`  - Sequence
-   `map`  - Map
-   `str`  - String
-   `int`  - Integer
-   `float`  - Floating-point decimal
-   `null`  - Null
-   `binary`  - Binary code
-   `omap`  - Ordered map
-   `set`  - Unordered set
###### Mappings
```
host: phl-42
```
###### Sequences
```
roles:
  - webserver
  - wp_database
```
###### Scalars
this include string, number, bool
```
location: philadelphia
```

```
downtime: |
  2018-10-10 - kernel upgrade
  2019-10-10 - kernel downgrade
comments: >
  shabakjsfajfaldhklaDHKad
  ```
###### Structures
```
--- start of block
... end of block
```
###### Comments
```
# comment
```
###### Tags
set uri
```
&TAG ! tag:hostdata:phl:
---
location: !PHL 
```
set datatype
```
cab: !!str 12
```
###### Anchors
```
---
host: phl-42
roles: &wphost
  - webserver
  - wp_database
rbac_role: *wphost
```
