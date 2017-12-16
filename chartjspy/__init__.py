import json
import pandas as pd

palette = '["#15527F", "#FF9900", "#FFCC00", "#0099CC", "#999900", "#663366","#FF0000", "#33CC99", "#006600", "#663300", "#99CC00", "#FF0033"]'


class Chart():
    """
    Class to handle Chartjs charts
    """

    def _get_dataset(self, dataset, name, color):
        """
        Encode a dataset
        """
        global palette
        html = "{"
        html += '\t"label": "' + name + '",'
        if color is not None:
            html += '"backgroundColor": "' + color + '",\n'
        else:
            html += '"backgroundColor": ' + palette + ',\n'
        html += '"data": ' + self._format_list(dataset) + ',\n'
        html += "}"
        return html

    def get(self, slug, xdata, ydatasets, label, opts, style, ctype):
        """
        Returns html for a chart
        """
        xdataset = self._format_list(xdata)
        width = "100%"
        height = "300px"
        if opts is not None:
            if "width" in opts:
                width = str(opts["width"])
            if "height" in opts:
                height = str(opts["height"])
        stylestr = '<style>#container_' + slug + \
            ' { width:' + width + ' !important; height:' + \
            height + ' !important}</style>\n'
        html = stylestr
        html += '<div id="container_' + slug + \
            '"><canvas id="canvas_' + slug + '"></canvas></div>\n'
        html += '<script>\n'
        html += 'var data = {\n'
        html += 'labels: ' + xdataset + ',\n'
        html += 'datasets:[\n'
        colors = None
        if "color" in style:
            colors = style["color"]
        i = 0
        for dataset in ydatasets:
            name = dataset["name"]
            data = dataset["data"]
            html += self._get_dataset(data, name, colors)
            if i < len(ydatasets) - 1:
                html += ","
            i += 1
        html += ']\n'
        html += '}\n'

        html += 'window.onload = function() {'
        html += 'var ctx = document.getElementById("canvas_' + \
                slug + '").getContext("2d");'
        html += 'window.myChart = new Chart(ctx, {'
        html += 'type: "' + ctype + '",'
        html += 'data: data,'
        html += 'options: {'
        html += 'spanGaps: false,'
        html += 'responsive: true,'
        html += 'maintainAspectRatio: false,'
        if "legend" in opts:
            html += 'legend: {'
            html += 'position: "' + opts["legend"] + '",'
            html += '},'
        else:
            html += 'legend: {'
            html += 'display: false,'
            html += '},'
        if "title" in opts:
            html += 'title: {'
            html += 'display: true,'
            html += 'text: "' + opts["title"] + '"'
            html += '}'
        html += '}'
        html += '});'
        html += '};'
        html += '</script>\n'
        return html

    def _format_list(self, data):
        """
        Format a list to use in javascript
        """
        dataset = "["
        i = 0
        for el in data:
            if pd.isnull(el):
                dataset += "null"
            else:
                dtype = type(data[i])
                if dtype == int or dtype == float:
                    dataset += str(el)
                else:
                    dataset += '"' + el + '"'
            if i < len(data) - 1:
                dataset += ', '
        dataset += "]"
        return dataset


chart = Chart()
