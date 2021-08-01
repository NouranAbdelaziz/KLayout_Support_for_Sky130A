# KLayout Sky130 LVS
This readme file is for explaining how to use the LVS scipt to run LVS in kLayout. The LVS script was mainly obtained from [this repo](https://github.com/laurentc2/SKY130_for_KLayout) with some additonal modifications. Please find the test cases and their status [here](https://github.com/NouranAbdelaziz/KLayout_Support_for_Sky130A/tree/main/LVS/Test%20Cases)

**Running LVS using GUI:**
1. Download the lvs_sky130.lylvs file  
2. Place the file in the path : /Klayout/lvs/ 
3. Open Klayout
4. Select “Tools” from the menu bar then select “LVS”, then choose "Edit LVS Script"
    ![image](https://user-images.githubusercontent.com/79912650/125278858-862e5800-e313-11eb-9007-ca351955c37f.png)
  
5. In the lvs script, change the schematic argument to be the path of the cdl, spice or cir file of the layout
    ![image](https://user-images.githubusercontent.com/79912650/125279071-c68dd600-e313-11eb-958d-e1c087e11977.png)
    
6. Run the script using "Run Script from the current tab" or Select “Tools” from the menu bar then select “LVS”, then choose lvs_sky130.lylvs 
    ![image](https://user-images.githubusercontent.com/79912650/125279303-140a4300-e314-11eb-9fe3-8363cf373652.png)

    ![image](https://user-images.githubusercontent.com/79912650/125277907-57fc4880-e312-11eb-9264-24f12b31a282.png)

**Running LVS using CLI:**
1. Download the lvs_sky130.lylvs file  
2. Place the file in the path : /Klayout/lvs/ 
3. Use the command :
```  
klayout -b -rd input=my_layout.gds -rd report=my_report.lyrdb -rd schematic=reference_netlist.cir -rd target_netlist=extracted_netlist.cir -r sky130.lvs
```
Where input is the layout in gds format, schematic is the layout in cdl, spice, or cir format, and target_netlist is the target extraction file and -r argument should be the LVS script

**Notes:**
* Only NMOS, PMOS and ndiode devices are supported in this LVS script
* Currently working on supporting short resistors
* If a spice file was provided, then there is no need to simplify the netlist using the function "netlist.simplify". 
* If a spice file was provided, all transistor devices must begin with an "M" not an "X". This can be done using [this](https://github.com/NouranAbdelaziz/KLayout_Support_for_Sky130A/blob/main/LVS/update_spice.py) simple python script.
* If a cdl file was provided, the lines which begins "+" are not readable so they must be removed. This can be done using [this](https://github.com/NouranAbdelaziz/KLayout_Support_for_Sky130A/blob/main/LVS/update_cdl.py) simple python script.  
* If a cdl file was provided, the simplification (device combining) of the Klayout netlist is not always done correctly. That is why it is better to use spice file. 
