from reportlab.lib.pagesizes import *
from reportlab.lib.colors import *
from reportlab.lib.units import cm, mm, pica


class CanvasSpec:
    def __init__(self, obj):
        self.filename = obj.filename
        self.size = obj.size
        self.width = obj.size[0]
        self.height = obj.size[1]
        self.xgap = obj.xgap
        self.ygap = obj.ygap
        self.xlist = []
        self.ylist = []
        self.xStart = 0
        self.yStart = 0


def draw(obj, detail_tf, canvas, color, line_width):
    def xylist(start_point, list_, max_, gap, detail_tf):
        i = start_point * cm
        if detail_tf == 1:
            while i < max_ - 5 * gap * cm:
                for j in range(0, 5):
                    list_.append(i + j * gap * cm)
                i += 5 * gap * cm
            list_.append(list_[-1] + gap * cm)

    def align(max_, gap):
        return converter(max_) % 5 * gap / 2

    def gridB(obj, canvas, color, line_width, xlist, ylist):
        canvas.setStrokeColor(color)
        canvas.setLineWidth(line_width)
        for y in ylist:
            for x in xlist:
                width = x + 0.5
                height = y + 0.5
                canvas.ellipse(x, y, width, height, stroke=0, fill=1)
            canvas.ellipse(x, y, width, height, stroke=0, fill=1)

        obj.xStart = xlist[0]
        obj.yStart = ylist[0]
        obj.xlist = []
        obj.ylist = []

    def converter(px):
        return px * 2.54 / 72

    xylist(align(obj.width, obj.xgap), obj.xlist, obj.width,
           obj.xgap, detail_tf)
    xylist(align(obj.height, obj.ygap), obj.ylist, obj.height,
           obj.ygap, detail_tf)
    gridB(obj, canvas, color, line_width, obj.xlist, obj.ylist)
