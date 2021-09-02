# Klayout_Sky130_tech_files

The following rules are the newly implemented rules in Klayout DRC deck and the link to their corresponding violator cells:



| Name          | Description                                   | Flags	| Value		|	Magic Rule	 | KLayout Rule	 | Link to violator cell	| Notes         | 
| ------------- | --------------------------------------------- | ------| --------| -------------| ------------- | -----------------------|---------------|   
| (nsd.9)	      | Diff and tap must be enclosed by their corresponding implant layers. Rule exempted forn- diff inside “advSeal_6um* OR cuPillarAdvSeal_6um*” pcell for SKY130P*/SP8P*/SKY130DI-5R-CSMC flowsn- diff rings around the die at min total L>1000 um and W=0.3 umn- gated_npn n- areaid.zer. |	DE		|	|	implemented	| implemented	|[Violator Cell](https://github.com/NouranAbdelaziz/open_pdks/blob/master/sky130/klayout/Violator%20Cells/n_psdm_test.GDS)|	The rule was not tested for the exception|
(psd.9)       	| Diff and tap must be enclosed by their corresponding implant layers. Rule exempted forn- diff inside “advSeal_6um* OR cuPillarAdvSeal_6um*” pcell for SKY130P*/SP8P*/SKY130DI-5R-CSMC flowsn- diff rings around the die at min total L>1000 um and W=0.3 umn- gated_npn n- areaid.zer. |	DE		|	|	implemented	| implemented	|[Violator Cell](https://github.com/NouranAbdelaziz/open_pdks/blob/master/sky130/klayout/Violator%20Cells/n_psdm_test.GDS)|	The rule was not tested for the exception|
(ncm.4)	        | Min enclosure of P+diff within (areaid:ed AndNot areaid:de) by Ncm |	|P	0.18 |	Not implementable	| implemented	|[Violator Cell](https://github.com/NouranAbdelaziz/open_pdks/blob/master/sky130/klayout/Violator%20Cells/ncm_test.GDS) ||
(ct.3)	        | Only min. square mcons are allowed except die seal ring where mcons are… |	|0.170*L  | implementable	| implemented	|[Violator Cell](https://github.com/NouranAbdelaziz/open_pdks/blob/master/sky130/klayout/Violator%20Cells/Ct_test.GDS) |The exception was not implemented|
(licon.3)	        | Only min. square licons are allowed except die seal ring where licons are (licon CD)*L |	|0.170*L  | implementable	| implemented	|[Violator Cell](https://github.com/NouranAbdelaziz/open_pdks/blob/master/sky130/klayout/Violator%20Cells/Licon_test.GDS) |The exception was not implemented|


