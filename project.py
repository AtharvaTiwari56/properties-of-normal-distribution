import statistics as st
import pandas as pd
import plotly.figure_factory as pff
import plotly.graph_objects as pgo

data = pd.read_csv(r'C:\Users\vedat\OneDrive\Documents\My Coding Stuff\Python\Class109\project\ok.csv')
mathsList = data['math score'].to_list()
mean = st.mean(mathsList)

stddev = st.stdev(mathsList)
lowstdev1, highstdev1 = mean - stddev, mean+stddev

lowstdev2, highstdev2 = mean - (2*stddev), mean + (2*stddev)

lowstdev3, highstdev3 = mean - (3*stddev), mean + (3* stddev)

stdev1data = [i for i in mathsList if i > lowstdev1 and i < highstdev1]
stdev2data = [k for k in mathsList if k > lowstdev1 and k < highstdev1]
stdev3data = [l for l in mathsList if l > lowstdev1 and l < highstdev1]

stdev1percent = ((len(stdev1data))*100)/len(mathsList)
stdev2percent = ((len(stdev2data))*100)/len(mathsList)
stdev3percent = ((len(stdev3data))*100)/len(mathsList)

figure = pff.create_distplot([mathsList], ['heightS'])
figure.add_trace(pgo.Scatter(x = [mean, mean], y = [0, 0.2], mode ='lines', name = 'Mean'))
figure.add_trace(pgo.Scatter(x = [lowstdev1, lowstdev1], y = [0, 0.2], mode ='lines', name = 'STDDEV1'))
figure.add_trace(pgo.Scatter(x = [highstdev1, highstdev1], y = [0, 0.2], mode ='lines', name = 'STDDEV1'))
figure.add_trace(pgo.Scatter(x = [lowstdev2, lowstdev2], y = [0, 0.2], mode ='lines', name = 'STDDEV2'))
figure.add_trace(pgo.Scatter(x = [highstdev2, highstdev2], y = [0, 0.2], mode ='lines', name = 'STDDEV2'))
figure.add_trace(pgo.Scatter(x = [lowstdev3, lowstdev3], y = [0, 0.2], mode ='lines', name = 'STDDEV3'))
figure.add_trace(pgo.Scatter(x = [highstdev3, highstdev3], y = [0, 0.2], mode ='lines', name = 'STDDEV3'))

figure.show()