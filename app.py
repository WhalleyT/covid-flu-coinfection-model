import src.default_params
import src.models

from bokeh.models import Slider, RangeSlider, ColumnDataSource
from bokeh.io import curdoc, output_file
from bokeh.layouts import column, row
from bokeh.plotting import figure,save
from bokeh.models.widgets import Paragraph
from bokeh.client import push_session


#initialise defaults
params = src.default_params.params

y0 = [params["E0"], params["Ec0"], params["C0"], params["Ei0"],
      params["I0"], params["Tc0"], params["Ti0"], params["H0"]]

if params["tau_i"] > 0:
    tau = params["tau_i"]
elif params["tau_c"] > 0:
    tau = params["tau_c"]
else:
    print("Warning, either tau_i or tau_c must be  greater than zero")

Tint_1 = [0,  tau-0.001]
Tint_2 = [tau, params["t_final"]]

coinfection_sol = src.models.run_covid_coinfection_model(src.models.model_covid_influenza,
                                                         Tint_1, Tint_2, y0, params)

#initialise sliders for user input
pi_e_slider = Slider(title="Pi E", value=2e7, start=3.9e5, end=1.1e8, step=100000)
mu_e_slider = Slider(title="Mu E", value=0.1, start=0.0625, end=1, step=0.025)
beta_1_slider = Slider(title="Beta 1", value=2e-8, start=3e-10, end=2.1e-7, step=1e-10)
mu_ec_slider = Slider(title="mu Ec", value=1, start=0.61, end=4.5, step=0.1)
kappa_1_slider = Slider(title= "Kappa 1", value = 4e-4, start = 1e-5,  end = 1e-2)
n1_slider = Slider(title = "N1", value = 100, start = 151,  end= 6591)
theta_x_slider = Slider(title = "Theta x", value=10, start=0.1, end= 100, step = 0.5)
mu_c_slider = Slider(title = "Mu c", value = 1.8, start =1.8, end=15.12)
Pi_tc_slider = Slider(title="Pi Tc", value=1e5, start=780, end=137000, step=100)
mu_tc_slider = Slider(title = "Mu Tc", value=0.34, start = 0.003, end = 37.3, step= 0.01)
psi_tc_slider = Slider(title = "Psi Tc", value=0.34, start = 0.003, end = 37.3, step= 0.01)
r_x_slider = Slider(title ="Rx", value=10, start=1, end=10, step=0.5)
psi_x_slider = Slider(title = "Psi X", value=1e5, start=1e4, end=4e5, step=1e4)
beta_2_slider = Slider(title= "Beta 2", value=5.4e-9, start=5.4e-9, end=4.25e-7, step=1e-9)
mu_ei_slider = Slider(title="Mu Ei", value=0.5, start=0.5, end=3.9, step=0.1)
kappa2_slider = Slider(title="Kappa 2", value=1e-5, start=4e-6, end=5e-3, step=1e-5)
n2_slider = Slider(title = "N2", value=33, start=33, end=13400, step=100)
mu_i_slider = Slider(value=1, start=1, end=6, step=0.5)
pi_ti_slider = Slider(title = "Pi Ti", value=2.3e5, start = 2.3e5, end=3.65e6, step =1e6)
psi_ti_slider = Slider(title = "Psi Ti", value=30, start=0.003, end = 37.3, step = 0.25)
mu_ti_slider = Slider(title = "Mu Ti", value = 0.33, start = 0.33, end = 0.5, step = 0.01)

#readme
explanation = Paragraph(text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
                                exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
                                irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
                                mollit anim id est laborum""", 
                        width=250, height=100)

#initialise model class and solve system for our parameters
results = src.models.run_covid_coinfection_model(src.models.model_covid_influenza,
                                                         Tint_1, Tint_2, y0, params)

source = ColumnDataSource(data=dict(t = results.t, y1 = results.y[0,], y2 = results.y[1,], 
                                    y3 = results.y[2,], y4 = results.y[3,], y5 = results.y[4,], 
                                    y6 = results.y[5,], y7 = results.y[6,], y8 = results.y[7,]))

#create our plot
e_cell_per_ml_vs_time = figure(height=800, width=800, title="E (cells/mL) vs Time (Days)",
                             tools="crosshair,pan,reset,save,wheel_zoom")
ec_cell_per_ml_vs_time = figure(height=800, width=800, title="E_c (cells/mL) vs Time (Days)",
                             tools="crosshair,pan,reset,save,wheel_zoom")

#set up plots
e_cell_per_ml_vs_time.line('t', 'y1', source=source, line_width=3, line_alpha=0.6)
ec_cell_per_ml_vs_time.line('t', 'y2', source=source, line_width=3, line_alpha=0.6)

#function to update over time
def update_data(attrname, old, new):

    params["N1"] = n1_slider.value
    params["N2"] = n2_slider.value
    params["Pi_tc"] = Pi_tc_slider.value
    params["Pi_ti"] = pi_ti_slider.value
    params["beta1"] = beta_1_slider.value
    params["beta2"] = beta_2_slider.value
    params["kappa1"] = kappa_1_slider.value
    params["kappa2"] = kappa2_slider.value
    params["mu_E"] = mu_e_slider.value
    params["mu_Ec"] = mu_ec_slider.value
    params["mu_Ei"] = mu_ei_slider.value
    params["mu_c"] = mu_c_slider.value
    params["mu_i"] = mu_i_slider.value
    params["mu_tc"] = mu_tc_slider.value
    params["mu_ti"] = mu_ti_slider.value
    params["pi_E"] = pi_e_slider.value
    params["psi_tc"] = psi_tc_slider.value
    params["psi_ti"] = psi_ti_slider.value
    params["psi_x"] = psi_x_slider.value
    params["r_x"] = r_x_slider.value
    params["theta_x"] = theta_x_slider.value


    results = src.models.run_covid_coinfection_model(src.models.model_covid_influenza,
                                                     Tint_1, Tint_2, y0, params)

    source.data = dict(t = results.t, y1 = results.y[0,], y2 = results.y[1,], 
                       y3 = results.y[2,], y4 = results.y[3,], y5 = results.y[4,], 
                       y6 = results.y[5,], y7 = results.y[6,], y8 = results.y[7,])

for w in [pi_e_slider, mu_e_slider]:
    w.on_change('value', update_data)


inputs = column(pi_e_slider, mu_e_slider, beta_1_slider, mu_ec_slider, kappa_1_slider,
                n1_slider, theta_x_slider, mu_c_slider, Pi_tc_slider, mu_tc_slider,
                psi_tc_slider, r_x_slider, psi_x_slider, beta_2_slider, mu_ei_slider, 
                kappa2_slider, n2_slider, mu_i_slider, pi_ti_slider, psi_ti_slider, mu_ti_slider)

plot_column_left = column(e_cell_per_ml_vs_time, ec_cell_per_ml_vs_time)



#make the document
curdoc().add_root(row(inputs, plot_column_left))
curdoc().title = "Coinfection Model of COVID-19 and Influenza"


#push it to server
#session = push_session(curdoc())
#session.show()

#create HTML doc
output_file('plot.html')