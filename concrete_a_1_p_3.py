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

## Part 3
# 3.1)
#Values
diameter_steel_longitudinal = 14*10**(-3) #m
diameter_steel_ties = 8*10**(-3) #m
cover = 30*10**(-3) #m
k_E=10000
w_lim=0.25*10**(-3) #m
fin_width=0.2 #m
fin_height=0.25 #m
fin_length=5 #m
E_s=205*10**9 #SIA norme pour steel B500B [Pa]
f_cm=38*10**6 #[Pa], SIA norme pour C30/37
f_ctm=2.9*10**6 #Pa, SIA norme pour C30/37


# 3.1)
A_s=np.pi*diameter_steel_longitudinal**2/4*4
A_g=fin_width*fin_height
A_c=A_g-A_s
rho=A_s/A_g


E_c=k_E*(f_cm)**(1/3)
n=E_s/E_c
t=min(fin_width, fin_height)
k_t=1/(1+t/2)


