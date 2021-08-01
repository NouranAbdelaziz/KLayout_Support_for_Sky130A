#Test Cases for Klayout LVS
The table below shows the status of each macro tested. 

|**Macro** | **LVS status** | **Notes** |
|DFFRAM    | Clean except for conb cell | Has an n-diode device |
|digital_pll | Clean except for conb cell ||
|gpio_logic_high | Clean except for conb cell ||
|gpio_control_block (includes gpio_logic_high) | Clean except for conb cell|Has an n-diode device |
|mgmt_protect_hv | Clean except for conb cell and sky130_fd_sc_hvl__lsbufhv2lv_1 | Had to use the spice of the original sky130_fd_sc_hvl__lsbufhv2lv_1 cell and not the one provided + extra VGND and VPWR exists |
mprj_logic_high| Clean except for conb cell||
mprj2_logic_high|Clean except for conb cell||
user_id_programming|Problem with extraction |It does not contain labels |
Mgmt_protect (includes mgmt_protect_hv, mprj_logic_high, and mprj2_logic_high)|Clean except for conb cell and sky130_fd_sc_hvl__lsbufhv2lv_1|Had to use the spice of the original sky130_fd_sc_hvl__lsbufhv2lv_1 cell and not the one provided + extra VGND and VPWR exists |







