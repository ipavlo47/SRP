from spyre import server
import pandas as pd
from matplotlib import pyplot as plt


class SimpleApp(server.App):
    
    title = "Лабараторна робота №2"
    inputs = [{ "input_type":"text",
                "variable_name":"freq",
                "label": "Роки",
                "value":1981,
                "action_id":"plot_sine_wave"},
              {
                  "input_type": 'radiobuttons',
                  "label": 'Індекс',
                  "options": [
                      {"label": "VCI", "value": "VCI"},
                      {"label": "VHI", "value": "VHI"},
                      {"label": "TCI", "value": "TCI"}
                      ],
                  "variable_name": 'ind',
                  "action_id": "make_plot"
                },   
              {"input_type": 'checkboxgroup',
               "label": 'Області',
               "options": [
                   {"label": "Вінницька", "value": "Вінницька"},
                   {"label": "Волинська", "value": "Волинська"},
                   {"label": "Дніпропетровська", "value": "Дніпропетровська"},
                   {"label": "Донецька", "value": "Донецька"},
                   {"label": "Житомирська", "value": "Житомирська"},
                   {"label": "Закарпатська", "value": "Закарпатська"},
                   {"label": "Запорізька", "value": "Запорізька"},
                   {"label": "Івано-Франківська", "value": "Івано-Франківська"},
                   {"label": "Київська", "value": "Київська"},
                   {"label": "Кіровоградська", "value": "Кіровоградська"},
                   {"label": "Луганська", "value": "Луганська"},
                   {"label": "Львівська", "value": "Львівська"},
                   {"label": "Миколаївська", "value": "Миколаївська"},
                   {"label": "Одеська", "value": "Одеська"},
                   {"label": "Полтавська", "value": "Полтавська"},
                   {"label": "Рівенська", "value": "Рівенська"},
                   {"label": "Сумська", "value": "Сумська"},
                   {"label": "Тернопільська", "value": "Тернопільська"},
                   {"label": "Харківська", "value": "Харківська"},
                   {"label": "Херсонська", "value": "Херсонська"},
                   {"label": "Хмельницька", "value": "Хмельницька"},
                   {"label": "Черкаська", "value": "Черкаська"},
                   {"label": "Чернівецька", "value": "Чернівецька"},
                   {"label": "Чернігівська", "value": "Чернігівська"},
                   {"label": "Республіка Крим", "value": "Республіка Крим"},
                   {"label": "Київ", "value": "Київ"},
                   {"label": "Севастополь", "value": "Севастополь"}
                   ],
               "variable_name": 'obl',
               "action_id": "make_plot"
                 
                  }]
    controls = [
        {
            "control_type": "button",
            "control_id": "button1",
            "label": "Вивести на екран інформацію",
        }]

    outputs = [
        {
            "type": "plot",
            "id": "plot1",
            "control_id": "button1",
            "tab": "Plot"
        }, {
            "type": "table",
            "id": "table_id",
            "control_id": "button1",
            "tab": "Table"
        }
    ]

    def getPlot(self,params):
        df = self.getData(params)
        print(df[2])
        print(df[6])
        df.plot(x=df[2],y=df[6],style='k--')
        return plt.show()
    
    def getData(self,params):
        df = pd.read_csv('D:\\lab\\All_data.csv', header=None)
        obl = params['obl']
        ind = params['ind']
        f = params['freq']
        print(obl, ind)
        df = df.loc[df[8].isin(obl)].loc[df[1] == f]
        if ind == 'VCI':
            df = df.drop(7, axis=1).drop(6, axis=1)
        elif ind == 'VHI':
            df = df.drop(6, axis=1).drop(5, axis=1)
        else:
            df = df.drop(7, axis=1).drop(5, axis=1)
        df = df.drop(4, axis=1).drop(3, axis=1).drop(0, axis=1)
        
        return df

    



    
app = SimpleApp()
app.launch(port=9097)
