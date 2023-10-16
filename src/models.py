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

def run_covid_coinfection_model(model, Tint_1, Tint_2, coinfection_inital_conditions, params):
    arg_tuple = (params["n1"], params["n2"], params["pi_tc"], params["pi_ti"],
                 params["beta1"], params["beta2"], params["kappa1"], params["kappa2"],
                 params["mu_E"], params["mu_Ec"], params["mu_Ei"], params["mu_c"], 
                 params["mu_i"], params["mu_tc"], params["mu_ti"], params["pi_E"], 
                 params["psi_tc"], params["psi_ti"], params["psi_x"], params["r_tc"],
                  params["r_ti"], params["r_x"], params["tau_c"], params["tau_i"], 
                  params["theta_x"])

    sol_first_run_coninfection = solve_ivp(model, Tint_1, coinfection_inital_conditions, args=arg_tuple, atol = [1e-20] * 8)

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


def model_covid(t, y, pi_e, mu_e, beta1, mu_ec, kappa1, n1, 
                theta_x, mu_c, pi_tc, r_tc, psi_tc, mu_tc, r_x, 
                psi_x, beta2, mu_ei, kappa2, n2, mu_i, pi_ti, 
                r_ti, psi_ti, mu_ti, tau_i, tau_c):

    dy = list()

    dy.append(pi_e - beta1 * y[0] * y[2] - mu_e * y[0])
    dy.append(beta1 * y[0] * y[2] - mu_ec * y[1] - kappa1 * y[1] * y[3])
    dy.append(n1 * mu_ec * y[1] * (1 - y[4] / (theta_x + y[4])) - mu_c * y[2])
    dy.append(pi_tc + r_tc * y[1] / (psi_tc + y[1]) - mu_tc * y[3])
    dy.append(r_x * y[1] / (psi_x + y[1] - y[4]))

    return dy


def model_flu(t, y, Pi_E, mu_E, beta1, mu_Ec, kappa1, N1, theta_x, 
              mu_c, Pi_tc, r_tc, psi_tc, mu_tc, r_x, psi_x, beta2,
              mu_Ei, kappa2, N2, mu_i, Pi_ti, r_ti, psi_ti, mu_ti,
              TAUi, TAUc):

    dy = list()

    dy.append(Pi_E - beta2*y[0]*y[2] - mu_E*y[0])
    dy.append(beta2*y[0]*y[2] - mu_Ei*y[1] - kappa2*y[1] * y[3])
    dy.append(N2*mu_Ei*y[1]*(theta_x/(theta_x + y[4])) - mu_i*y[2])
    dy.append(Pi_ti + r_ti* y[1]/(psi_ti +y[1]) - mu_ti*y[3])
    dy.append(r_x * (y[1] / ((psi_x + y[1])-y[4])))

    print(dy)

    return dy
