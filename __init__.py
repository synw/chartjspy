import json


class Chart():

    def _format_list(self, data):
        dtype = type(data[0])
        dataset = "["
        i = 1
        for el in data:
            if dtype == int or dtype == float:
                dataset += str(el)
            else:
                dataset += '"' + el + '"'
            if i < len(data):
                dataset += ', '
        dataset += "]"
        return dataset

    def bar(self, slug, xdata, ydata, label=None, opts={}, style={}, **kwargs):
        data = json.dumps(xdata)
        xdataset = self._format_list(xdata)
        ydataset = self._format_list(ydata)
        html = '<script src="/static/js/chartjs/Chart.min.js"></script>\n'
        html += '<div><canvas id="canvas_' + slug + '"></canvas></div>\n'
        html += '<script>\n'
        html += 'var barChartData = {\n'
        html += 'labels: ' + xdataset + ',\n'
        html += 'datasets:[{\n'
        if label is not None:
            html += '\t"label": "' + label + '",'
        # html += '"backgroundColor": ["#3e95cd",
        # "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],\n'
        html += '"backgroundColor": "firebrick",\n'
        html += '"data": ' + ydataset + ',\n'
        html += '}]\n'
        html += '}\n'
        html += 'window.onload = function() {\n'
        html += 'var ctx = document.getElementById("canvas_' + \
            slug + '").getContext("2d");\n'
        html += 'window.myBar = new Chart(ctx, {\n'
        html += 'type: "bar",\n'
        html += 'data: barChartData,\n'
        html += 'options: {\n'
        html += 'responsive: true,\n'
        html += 'legend: {\n'
        html += 'position: "top",\n'
        html += '},\n'
        html += 'title: {\n'
        html += 'display: true,\n'
        html += 'text: "Title"\n'
        html += '}\n'
        html += '}\n'
        html += '}); \n'
        html += '};\n'
        html += 'window.onload = function() {'
        html += 'var ctx = document.getElementById("canvas_' + \
            slug + '").getContext("2d");'
        html += 'window.myBar = new Chart(ctx, {'
        html += 'type: "bar",'
        html += 'data: barChartData,'
        html += 'options: {'
        html += 'responsive: true,'
        html += 'legend: {'
        html += 'position: "top",'
        html += '},'
        html += 'title: {'
        html += 'display: true,'
        html += 'text: "Chart.js Bar Chart"'
        html += '}'
        html += '}'
        html += '});'
        html += '};'
        html += '</script>\n'
        return html


chart = Chart()
