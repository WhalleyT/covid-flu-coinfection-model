covid_params = {
    "pi_E": 2e7,
    "mu_E": 0.1,
    "beta1": 2e-8,
    "mu_Ec": 1,
    "kappa1": 4e-4,
    "n1": 100,
    "theta_x": 10,
    "mu_c": 1.8,
    "pi_tc": 1e5,
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
"n2": 33,
"mu_i": 1,
"pi_ti":  2.3e5,
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

def init_params_comb(params):

    coinfection_inital_conditions = [params["E0"], params["Ec0"], params["C0"], params["Ei0"],
        params["I0"], params["Tc0"], params["Ti0"], params["H0"]]

    if params["tau_i"] > 0:
        tau = params["tau_i"]
    elif params["tau_c"] > 0:
        tau = params["tau_c"]
    else:
        print("Warning, either tau_i or tau_c must be  greater than zero")
    
    Tint_1 = [0,  tau-0.001]
    Tint_2 = [tau, params["t_final"]]
    
    return coinfection_inital_conditions, tau, Tint_1, Tint_2


def init_params_flu(params):
    flu_initial_conditions = [params["E0"], 0, 1, 0, 0]
    tint_flu = [0, 10]
    flu_params_tuple = (params["pi_E"], params["mu_E"], params["beta1"], params["mu_Ec"], 
                        params["kappa1"], params["n1"], params["theta_x"], params["mu_c"], 
                        params["pi_tc"], params["r_tc"], params["psi_tc"],params["mu_tc"], 
                        params["r_x"], params["psi_x"], params["beta2"], params["mu_Ei"], 
                        params["kappa2"], params["n2"], params["mu_i"], params["pi_ti"], 
                        params["r_ti"],  params["psi_ti"], params["mu_ti"], params["tau_i"], 
                        params["tau_c"])
    return flu_initial_conditions, tint_flu, flu_params_tuple


def init_params_covid(params):
    covid_initial_conditions = [params["E0"], 0, 1, 0, 0]
    tint_covid = [0, 10]
    covid_params_tuple = (params["pi_E"], params["mu_E"], params["beta1"], params["mu_Ec"], params["kappa1"], params["n1"], 
                          params["theta_x"], params["mu_c"], params["pi_tc"], params["r_tc"], 
                          params["psi_tc"], params["mu_tc"], params["r_x"], params["psi_x"], params["beta2"], 
                          params["mu_Ei"], params["kappa2"], params["n2"], params["mu_i"], params["pi_ti"], 
                          params["r_ti"], params["psi_ti"], params["mu_ti"], params["tau_i"], params["tau_c"])
    return covid_initial_conditions, tint_covid, covid_params_tuple