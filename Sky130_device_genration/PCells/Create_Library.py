
# Enter your Python code here
import math

total_width = 510
total_length = 510
licons_plus_spaces_w = total_width / 170.0
licons_plus_spaces_l = total_length / 170.0
      
if (licons_plus_spaces_w/2) - math.floor(licons_plus_spaces_w/2) < 0.5:
  licons_num_w = math.floor(licons_plus_spaces_w/2)
else:
  licons_num_w = math.ceil(licons_plus_spaces_w/2)
        
if (licons_plus_spaces_l/2) - math.floor(licons_plus_spaces_l/2) < 0.5:
  licons_num_l = math.floor(licons_plus_spaces_l/2)
else:
  licons_num_l = math.ceil(licons_plus_spaces_l/2)
      

y_uppers=[]
y_lowers=[]
x_lefts=[]
x_rights=[]
      
y_uppers.append( 85 + ((licons_num_l-1)*170))
y_lowers.append ( y_uppers[0] - 170 )
    
for i in range(licons_num_l-1):
  y_uppers.append(y_lowers[i] - 170)
  y_lowers.append(y_uppers[i+1] - 170)
        
x_lefts.append(85 + ((licons_num_w-1)*170))
x_rights.append(x_lefts[0] - 170)
      
for i in range(licons_num_w-1): 
  x_lefts.append(x_rights[i] - 170)
  x_rights.append( x_lefts[i+1] - 170)
      
  
for i in range(licons_num_w):
  for j in range(licons_num_l):
    #self.cell.shapes(licon).insert(pya.Box(x_rights[i], y_lowers[j], x_lefts[i], y_uppers[j]))
    print(x_lefts[i])
    print (y_lowers[j])
    print(x_rights[i])
    print(y_uppers[j])
    
print(x_lefts)
print(x_rights)

print(y_lowers)
print(y_uppers)

class MyLib(pya.Library):
  """
  The library where we will put the PCell into 
  """

  def __init__(self):
  
    # Set the description
    self.description = "sky130_fd_pr__"
    
    # Create the PCell declarations
    self.layout().register_pcell("sky130_fd_pr__res_generic_nd", sky130_fd_pr__res_generic_nd())
    self.layout().register_pcell("sky130_fd_pr__res_high_po_0p35", sky130_fd_pr__res_high_po_0p35())
    self.layout().register_pcell("sky130_fd_pr__res_generic_m1", sky130_fd_pr__res_generic_m1())
    self.layout().register_pcell("sky130_fd_pr__nfet01v8", sky130_fd_pr__nfet01v8())
    self.layout().register_pcell("sky130_fd_pr__pfet01v8", sky130_fd_pr__pfet01v8())
    self.layout().register_pcell("substrate contact (1.8V)", substrate_contact_1p8V())
    self.layout().register_pcell("substrate contact (5.0V)", substrate_contact_5p0V())
    self.layout().register_pcell("via1", via1())
    self.layout().register_pcell("via2", via2())
    self.layout().register_pcell("via3", via3())
    self.layout().register_pcell("via4", via4())
    self.layout().register_pcell("mcon", mcon())
    self.layout().register_pcell("deep n-well region", deep_n_well_region())
    # That would be the place to put in more PCells ...
    
    # Register us with the name "MyLib".
    # If a library with that name already existed, it will be replaced then.
    self.register("Sky 130")


# Instantiate and register the library
MyLib()