import numpy as np
#
sciper = 391884
sciper_list = [int(chiffre) for chiffre in str(sciper)]
print(sciper_list)
b =sciper_list[1]
c =sciper_list[2]
d =sciper_list[3]
e =sciper_list[4]
f =sciper_list[5]
green_roof_load = 1.2 + 0.1*((d +f)%10)
screed_of_the_galery = 40 + 0.4*e
if e%2 ==0:
    concrete_of_the_mast = "C50/60"
else:
    concrete_of_the_mast= "C45/55"

if (d + f)%2 ==0:
    concrete_girder = "C30/37"
else: 
    concrete_girder ="C25/30"

tie_space__s = 250 + 10*((c+d)%5)
Nd_mast_fundation = 2700 + 50*c

force_in_one_fin_QP__Nqp = 155 + 5*((c+f)%4)
force_fin_ULS__Nd = force_in_one_fin_QP__Nqp +95
final_skage_fin__eps_cs = -(0.25 + 0.01*((b+c+d+e+f)%11))
moment_mast_axis__Md = -(3900 + 50*((c+e)%3))
print(final_skage_fin__eps_cs)

##Part 2
# 2.2)
#Values:
gamma_c=1.5
gamma_s=1.15
if concrete_of_the_mast=="C50/60":
    f_ck=50 #MPa
elif concrete_of_the_mast=="C45/55":
    f_ck=45 #MPa
else: 
    print('ERROR: concrete of mast missing')
f_yk=500
n_t=1


#calculations:
n_fc=(40/f_ck)**(1/3)
if n_fc>1:
    n_fc=1
    print('your n_fc was bigger than 1 so it was changed to 1')
print(f'2.2) n_fc= {n_fc}')
print(f'2.2) n_t= {n_t}')
f_cd=(n_fc*n_t*f_ck)/gamma_c
f_yd=f_yk/gamma_s
print(f'2.2) f_cd= {f_cd} [MPa]')

diameter_longitudinal= 0.016 #m
diameter_tie= 0.01 #m
diameter_cross_tie= 0.01 #m
diameter_mast=0.4 #m

A_s=8*np.pi*diameter_longitudinal**2/4 #m
print(f'2.2) A_s= {A_s*10**6} [mm]')
A_c=diameter_mast**2-A_s #m
print(f'2.2) A_c= {A_c*10**6} [mm]')

N_Rd = (f_cd*A_c+f_yd*A_s)*10**3 #kN
print(f'2.2) N_Rd= {N_Rd} [kN]')
N_d_divided_by_N_Rd = Nd_mast_fundation/N_Rd
print(f'2.2) N_d/N_Rd= {N_d_divided_by_N_Rd} [kN]')

# 2.3)
print(' ')
s_cx= tie_space__s*10**(-3) #m
s_cy=0.152 #m
s_cz=0.152 #m
b_cy=0.304 #m
b_cz=0.304 #m

A_scy= 3*np.pi*diameter_cross_tie**2/4 #m^2
A_scz=3*np.pi*diameter_cross_tie**2/4 #m^2
A_sc=A_scy
between_barspace=0.152 #m

print(f'2.3) A_sc = {A_sc*10**6} [mm^2]')

w_y=A_scy*f_yd/(b_cz*s_cx*f_cd)
w_z=A_scz*f_yd/(b_cy*s_cx*f_cd)
w_c=max(w_y,w_z)
print(f'2.3) w_c = {w_c}')
sigma_c1=-w_c*f_cd*(1-((s_cy**2+s_cx**2)**(1/2))/(2*b_cz))*(1-((s_cz**2+s_cx**2)**(1/2))/(2*b_cy))
print(f'2.3) sigma_c1 = {sigma_c1} [MPa]')
k_c=1-4*sigma_c1/f_cd
if k_c > 4:
    k_c=4
    print('k_c was bigger than 4, so 4 got taken')
print(f'2.3) k_c= {k_c}')

A_cc=(between_barspace*2)**2
N_Rd_of_confined_core=k_c*f_cd*A_cc*10**3 #kN
N_Rd_mast=N_Rd_of_confined_core+f_yd*A_s*10**3 #kN
print(f'2.3) N_Rd of confined core = {N_Rd_of_confined_core} [kN]')
print(f'2.3)  N_Rd of mast = {N_Rd_mast} [kN]')
print(f'2.3)  N_d/N_Rd_mast = {Nd_mast_fundation/N_Rd_mast}')

# 2.5)
print(' ')
s_cx_new=int(input('what is your new value of s_x? (in mm please :) )'))*10**(-3) #m
w_y_new=A_scy*f_yd/(b_cz*s_cx_new*f_cd)
w_z_new=A_scz*f_yd/(b_cy*s_cx_new*f_cd)
w_c_new=max(w_y,w_z)
sigma_c1_new=-w_c_new*f_cd*(1-((s_cy**2+s_cx_new**2)**(1/2))/(2*b_cz))*(1-((s_cz**2+s_cx_new**2)**(1/2))/(2*b_cy))
print(f'2.5) sigma_c1 = {sigma_c1} [MPa]')
k_c_new=1-4*sigma_c1_new/f_cd
if k_c_new > 4:
    k_c_new=4
    print('k_c was bigger than 4, so 4 got taken')
print(f'2.5) k_c new= {k_c_new}')

A_cc=(between_barspace*2)**2
N_Rd_of_confined_core_new=k_c_new*f_cd*A_cc*10**3 #kN
N_Rd_mast_new=N_Rd_of_confined_core_new+f_yd*A_s*10**3 #kN
print(f'2.5) N_Rd of confined core new = {N_Rd_of_confined_core_new} [kN]')
print(f'2.5) N_Rd of mast new = {N_Rd_mast_new} [kN]')


