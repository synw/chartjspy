import json


class Chart():
    """
    Class to handle Chartjs charts
    """

    def bar(self, slug, xdata, ydata, label=None, opts={}, style={}):
        """
        Returns html for a bar chart
        """
        html = self._chart(slug, xdata, ydata, label, opts, style, "bar")
        return html

    def line(self, slug, xdata, ydata, label=None, opts={}, style={}):
        """
        Returns html for a line chart
        """
        html = self._chart(slug, xdata, ydata, label, opts, style, "line")
        return html

    def _chart(self, slug, xdata, ydata, label, opts, style, ctype):
        """
        Returns html for a chart
        """
        data = json.dumps(xdata)
        xdataset = self._format_list(xdata)
        ydataset = self._format_list(ydata)
        html = '<div><canvas id="canvas_' + slug + '"></canvas></div>\n'
        html += '<script>\n'
        html += 'var chartData = {\n'
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

        html += '$(document).ready(function () {'
        html += 'var ctx = document.getElementById("canvas_' + \
            slug + '").getContext("2d");'
        html += 'window.myChart = new Chart(ctx, {'
        html += 'type: "' + ctype + '",'
        html += 'data: chartData,'
        html += 'options: {'
        html += 'responsive: true,'
        html += 'legend: {'
        html += 'position: "top",'
        html += '},'
        html += 'title: {'
        html += 'display: true,'
        if label is not None:
            html += 'text: "' + label + '"'
        html += '}'
        html += '}'
        html += '});'
        html += '});'
        html += '</script>\n'
        return html

    def _format_list(self, data):
        """
        Format a list to use in javascript
        """
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


chart = Chart()
