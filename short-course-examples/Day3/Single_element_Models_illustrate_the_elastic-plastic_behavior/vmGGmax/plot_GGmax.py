import numpy as np
import matplotlib.pyplot as plt  

# target
# userInput1= [0,1E-6,1E-5,5E-5,1E-4, 0.0005, 0.001, 0.005, 0.01];  
# userInput2= [1,0.99563892,0.96674888,0.87318337,0.78735192,0.46719464,0.32043423,0.10940113,0.06347752];
userInput1= [0,1E-6,1E-5,5E-5,1E-4, 0.0005, 0.001];  
userInput2= [1,0.99563892,0.96674888,0.87318337,0.78735192,0.46719464,0.32043423];
Gmax = 3E8;
poisson = 0.0;
# #################################
gamma = userInput1
GGmax = userInput2
G=[Gmax * item for item in GGmax]

tau = np.zeros(len(gamma))
for it in xrange(1,len(gamma)):
	tau[it] = gamma[it] * G[it]

print tau

epsilon = [item/2. for item in gamma]

# # ============================================
# # Figure 1
# # Plot the stress-strain
# # ============================================
strain = np.loadtxt("strain.feioutput")
stress = np.loadtxt("stress.feioutput")

essiGamma = [2*item for item in strain]

# plt.plot(gamma, tau, 'b-^', label='Input' )
# plt.plot(essiGamma, stress, 'r-*', label=' ESSI')
# plt.legend(loc=2)
# plt.xlabel('Strain / (unitless)')
# plt.ylabel('Stress / (Pa)')
# plt.title('Material Behavior: Stress-Strain')
# plt.grid()
# plt.box()
# plt.savefig('backbone.pdf', transparent=True, bbox_inches='tight')
# plt.show()



# # ============================================
# # Figure 3
# # Plot the G/Gmax
# # ============================================
# avoid the divide by zero
fontSIZE = 21
import matplotlib as mpl
label_size = fontSIZE
mpl.rcParams['xtick.labelsize'] = label_size 
mpl.rcParams['ytick.labelsize'] = label_size 


stress[0]=stress[1]
strain[0]=strain[1]
essiG = [a/b/2. for a,b in zip(stress, strain)]
essiGGmax = [item/Gmax for item in essiG]

# strain_plot = [100* x for x in strain]
# stress_plot = [1./1000* x for x in stress]
plt.semilogx(essiGamma, essiGGmax, 'k-', label='ESSI', linewidth = 5.0 )
plt.semilogx(gamma , GGmax , 'r--', label='Input', linewidth = 5.0 )

# plt.legend(loc=3)
plt.legend(loc=3, prop={'size':fontSIZE})
plt.title('Multi-Yield-Surface vonMises G/Gmax',fontsize=fontSIZE)
plt.xlabel('Strain / (unitless)',fontsize=fontSIZE)
plt.ylabel('G/Gmax / (unitless)',fontsize=fontSIZE)
plt.grid()
plt.box()
plt.savefig('GGmax.pdf', transparent=True, bbox_inches='tight')
plt.show()






# strain_stress = np.loadtxt('strain_stress.txt')
# strain = strain_stress[:,0]
# stress = strain_stress[:,1]
# # vol_s = strain_stress[:,3]
# strain_plot = [100* x for x in strain]
# stress_plot = [1./1000* x for x in stress]

# plt.plot(strain_plot,stress_plot,linewidth=3.0)
# # plt.plot(vol_s, stress)
# minY = min(stress_plot)*1.05
# maxY = max(stress_plot)*1.05
# minX = min(strain_plot)*1.05
# maxX = max(strain_plot)*1.05
# plt.ylim([minY, maxY])
# plt.xlim([minX, maxX])

# plt.xlabel('Shear Strain (%) ',fontsize=fontSIZE)
# plt.ylabel('Shear Stress (kPa)',fontsize=fontSIZE)

# plt.grid()
# # plt.show()
# plt.savefig('multiSurface.pdf', dpi=1200, transparent=True, bbox_inches='tight')
# # plt.savefig('multiSurface', format='svg', dpi=1200, transparent=True, bbox_inches='tight')

