covid_params = {
    "pi_E": 2e7,
    "mu_E": 0.1,
    "beta1": 2e-8,
    "mu_Ec": 1,
    "kappa1": 4e-4,
    "N1": 100,
    "theta_x": 10,
    "mu_c": 1.8,
    "Pi_tc": 1e5,
    "r_tc": 0.1,
    "psi_tc": 10,
    "mu_tc": 0.340,
    "r_x": 10,
    "psi_x": 1e5
}

influenza_params = {
"beta2": 5.4e-9,
"mu_Ei": 0.5,
"kappa2": 1e-5,
"N2": 33,
"mu_i": 1,
"Pi_ti":  2.3e5,
"r_ti": 0.1,
"psi_ti": 30,
"mu_ti": 0.33
}

tau_i = 0
tau_c = 3
t_final = 10
eps = 0.8

if tau_c > 0:
    time_params = {
        "E0": eps * covid_params["pi_E"] / covid_params["mu_E"],
        "Ec0": 0,
        "C0": 0, 
        "Tc0": 0,
        "H0": 0,
        "Ei0": 0,
        "I0": 1,
        "Ti0":0
    }

if tau_i > 0:
    time_params = {
        "E0": eps * covid_params["pi_E"] / covid_params["mu_E"],
        "Ec0": 0,
        "C0": 1, 
        "Tc0": 0,
        "H0": 0,
        "Ei0": 0,
        "I0": 0,
        "Ti0":0
    }

#because all params have no name clashes, we can combine the dictionaries for the sake of easiness
params = {**covid_params,**influenza_params, **time_params}

params["tau_c"] = tau_c
params["tau_i"] = tau_i
params["t_final"] = 10
params["eps"] = 0.8