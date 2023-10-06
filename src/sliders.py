from bokeh.models import Slider

covid_sliders = {
"pi_E": Slider(title="Pi E", value=2e7, start=3.9e5, end=1.1e8, step=100000),
"mu_E": Slider(title="Mu E", value=0.1, start=0.0625, end=1, step=0.025),
"beta1": Slider(title="Beta 1", value=2e-8, start=3e-10, end=2.1e-7, step=1e-10),
"mu_Ec": Slider(title="mu Ec", value=1, start=0.61, end=4.5, step=0.1),
"kappa1": Slider(title= "Kappa 1", value = 4e-4, start = 1e-5,  end = 1e-2),
"n1": Slider(title = "N1", value = 100, start = 151,  end= 6591),
"theta_x": Slider(title = "Theta x", value=10, start=0.1, end= 100, step = 0.5),
"mu_c": Slider(title = "Mu c", value = 1.8, start =1.8, end=15.12),
"pi_tc": Slider(title="Pi Tc", value=1e5, start=780, end=137000, step=100),
"mu_tc": Slider(title = "Mu Tc", value=0.34, start = 0.003, end = 37.3, step= 0.01),
"psi_tc": Slider(title = "Psi Tc", value=0.34, start = 0.003, end = 37.3, step= 0.01),
"r_x": Slider(title ="Rx", value=10, start=1, end=10, step=0.5),
"psi_x": Slider(title = "Psi X", value=1e5, start=1e4, end=4e5, step=1e4)
}


flu_sliders = {
"beta2": Slider(title= "Beta 2", value=5.4e-9, start=5.4e-9, end=4.25e-7, step=1e-9),
"mu_Ei": Slider(title="Mu Ei", value=0.5, start=0.5, end=3.9, step=0.1),
"kappa2": Slider(title="Kappa 2", value=1e-5, start=4e-6, end=5e-3, step=1e-5),
"n2": Slider(title = "N2", value=33, start=33, end=13400, step=100),
"mu_i": Slider(value=1, start=1, end=6, step=0.5),
"pi_ti": Slider(title = "Pi Ti", value=2.3e5, start = 2.3e5, end=3.65e6, step =1e6),
"psi_ti": Slider(title = "Psi Ti", value=30, start=0.003, end = 37.3, step = 0.25),
"mu_ti": Slider(title = "Mu Ti", value = 0.33, start = 0.33, end = 0.5, step = 0.01)
}