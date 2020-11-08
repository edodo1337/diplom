from tkinter import Tk, Canvas, Frame, BOTH
import numpy as np


def nugol(x1, y1, x2, y2):
    xf = x2 - x1
    yf = y2 - y1
    result = 0

    if xf != 0:
        result = np.arctan(yf / xf)
    else:
        if yf > 0:
            result = 3.14 / 2
        else:
            result = 3.14 * 3 / 2
    if xf < 0:
        result += 3.14
    if result < 0:
        result += 3.14 * 2
    if result >= 3.14 * 2:
        result -= 3.14 * 2

    return result


class Approximator:
    def __init__(self, frame: 'Example'):
        self.points = []
        self.frame = frame

    @staticmethod
    def line_builder(f):
        def wrapper(*args):
            # print('ARGS', args)
            f(*args)

            this = args[0].approximator

            if len(this.points) % 3 == 0:
                p1 = this.points.pop()  # мышь
                p2 = this.points.pop()  # вторая
                p3 = this.points.pop()  # центр

                p1, p2, p3 = p3, p2, p1

                _points = [p2]

                rad1 = np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
                rad2 = np.sqrt((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2)

                if rad1 <= 0 or rad2 <= 0:
                    return

                un = nugol(p1[0], p1[1], p2[0], p2[1])
                uk = nugol(p1[0], p1[1], p3[0], p3[1])

                if uk <= un:
                    uk += 2 * 3.14

                L = uk - un
                step1 = 20 / rad1
                step2 = 20 / rad2

                q = None
                nt = None

                if step1 < L and step2 < L:
                    q = (L - step1) / (L - step2)

                if q == 1:
                    nt = round(L / step1)
                    nt = 1 if nt < 1 else nt
                    step1 = L / nt
                else:
                    nt = round(np.log10(step2 / step1) / np.log10(q) + 1)
                    nt = 1 if nt < 1 else nt
                    if nt > 1:
                        step1 = L * (q - 1) / (q ** nt - 1)

                du = 0
                for j in range(nt):
                    du += step1
                    u = un + du
                    rad = rad1 + (rad2 - rad1) / L * du

                    x = p1[0] + rad * np.cos(u)
                    y = p1[1] + rad * np.sin(u)

                    _points.append((x, y))

                    step1 *= q

                _points.append(p3)

                this.frame.canvas.create_line(*_points)

        return wrapper


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.approximator = Approximator(self)
        self.figs = []
        self.initUI()

    @Approximator.line_builder
    def create_circle(self, x, y, r, canvasName):  # center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvas_id = canvasName.create_oval(x0, y0, x1, y1)
        self.figs.append(canvas_id)
        return canvas_id

    def b1(self, event, canvas):
        self.approximator.points.append((event.x, event.y))
        self.create_circle(event.x, event.y, 15, canvas)

    def b2(self, event, canvas):
        if self.figs:
            canvas_id = self.figs.pop()
            canvas.after(100, canvas.delete, canvas_id)

    def initUI(self):
        self.master.title("Рисуем линии")
        self.pack(fill=BOTH, expand=1)

        self.canvas.bind('<Button-1>', lambda event, arg=self.canvas: self.b1(event, arg))
        self.canvas.bind('<Button-3>', lambda event, arg=self.canvas: self.b2(event, arg))

        self.canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("500x500+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
