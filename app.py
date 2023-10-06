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
cell_per_ml_vs_time = figure(height=400, width=400, title="E (cells/mL) vs Time (Days)",
                             tools="crosshair,pan,reset,save,wheel_zoom")

#set up plots
cell_per_ml_vs_time.line('t', 'y1', source=source, line_width=3, line_alpha=0.6)

#function to update over time
def update_data(attrname, old, new):
    print(params["pi_E"])
    params["pi_E"] = pi_e_slider.value
    params["mu_E"] = mu_e_slider.value
    print(params["pi_E"])
    results = src.models.run_covid_coinfection_model(src.models.model_covid_influenza,
                                                     Tint_1, Tint_2, y0, params)

    source.data = dict(t = results.t, y1 = results.y[0,], y2 = results.y[1,], 
                       y3 = results.y[2,], y4 = results.y[3,], y5 = results.y[4,], 
                       y6 = results.y[5,], y7 = results.y[6,], y8 = results.y[7,])

for w in [pi_e_slider, mu_e_slider]:
    w.on_change('value', update_data)


inputs = column(pi_e_slider, mu_e_slider, explanation)

plot_column_left = column(cell_per_ml_vs_time)



#make the document
curdoc().add_root(row(inputs, plot_column_left))
curdoc().title = "Coinfection Model of COVID-19 and Influenza"


#push it to server
#session = push_session(curdoc())
#session.show()

#create HTML doc
output_file('plot.html')