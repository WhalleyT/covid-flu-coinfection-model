from scipy.integrate import solve_ivp

def model_covid_influenza(t, y, N1, N2, Pi_tc, Pi_ti, beta1, beta2, 
                          kappa1, kappa2, mu_E, mu_Ec, mu_Ei, mu_c, 
                          mu_i, mu_tc, mu_ti, pi_E, psi_tc, psi_ti, psi_x, r_tc, 
                          r_ti, r_x, tau_c, tau_i, theta_x):
    dy = list()

    dy.append(pi_E - beta1 * y[0] * y[2] - beta2 * y[0] * y[4]- mu_E*y[0])

    dy.append(beta1 * y[1] * y[2] - mu_Ec * y[1] - kappa1 * y[1]*y[5] )
    
    dy.append(N1 * mu_Ec * y[1] * (1-y[7] / (theta_x +y[7]))-mu_c*y[2])

    dy.append(beta2 * y[0] * y[4] - mu_Ei * y[3] - kappa2 * y[3] * y[6])

    dy.append(N2 * mu_Ei * y[3] * (1-y[7] / (theta_x +y[7])) - mu_i * y[4])

    if t > tau_c - 0.001:
        dy.append(Pi_tc + r_tc * y[1] /( psi_tc + y[1]) - mu_tc * y[5])
    else:
        dy.append(0)

    if t > tau_i - 0.001:
        dy.append(Pi_ti + r_ti * y[3] / (psi_ti + y[3]) - mu_ti * y[6])
    else:
        dy.append(0)

    dy.append(r_x * ((y[1] + y[3] / (psi_x + y[1]+ y[3])- y[7])))

    return dy

def run_covid_coinfection_model(model, Tint_1, Tint_2, y0, params):
    N1 = params["N1"]
    N2 = params["N2"]
    Pi_tc = params["Pi_tc"]
    Pi_ti = params["Pi_ti"]
    beta1 = params["beta1"]
    beta2 = params["beta2"]
    kappa1 = params["kappa1"]
    kappa2 = params["kappa2"]
    mu_E = params["mu_E"]
    mu_Ec = params["mu_Ec"]
    mu_Ei = params["mu_Ei"]
    mu_c = params["mu_c"]
    mu_i = params["mu_i"]
    mu_tc = params["mu_tc"]
    mu_ti = params["mu_ti"]
    pi_E = params["pi_E"]
    psi_tc = params["psi_tc"]
    psi_ti = params["psi_ti"]
    psi_x = params["psi_x"]
    r_tc = params["r_tc"]
    r_ti = params["r_ti"]
    r_x = params["r_x"]
    tau_c = params["tau_c"]
    tau_i = params["tau_i"]
    theta_x = params["theta_x"]

    arg_tuple = (N1, N2, Pi_tc, Pi_ti, beta1, beta2, kappa1, kappa2,
                 mu_E, mu_Ec, mu_Ei, mu_c, mu_i, mu_tc, mu_ti, pi_E, 
                 psi_tc, psi_ti, psi_x, r_tc, r_ti, r_x, tau_c, tau_i, theta_x)

    sol_first_run_coninfection = solve_ivp(model, Tint_1, y0, args=arg_tuple, atol = [1e-20] * 8)

    params_from_first_coinfection = sol_first_run_coninfection.y.T
    y_from_model = params_from_first_coinfection[-1]

    if params["tau_i"] > 0:
        y_from_model[4] = 1
    if params["tau_c"] > 0:
        y_from_model[2] = 1

    q1 = sol_first_run_coninfection.t
    q2 = sol_first_run_coninfection.y

    sol_coninfection = solve_ivp(model_covid_influenza, Tint_2, y_from_model,
                                atol = [1e-20] * 8, args=arg_tuple)

    return sol_coninfection




