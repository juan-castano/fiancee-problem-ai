from __future__ import print_function

from simpleai.search import SearchProblem, astar

from simpleai.search.viewers import WebViewer

#from simpleai.search.viewers import  ConsoleViewer


class Novios(SearchProblem):

    def __init__(self):
        super(Novios, self).__init__(initial_state=(3, 3, 0))
        self._acciones = [('1H', (0, 1)),
                          ('1M', (1, 0)),
                          ('2H', (0, 2)),
                          ('2M', (2, 0)),
                          ('1M1H', (1, 1))]

    def actions(self, estado):
        return [accion for accion in self._acciones if self.esValido(self.result(estado, accion))]

    def esValido(self, estado):
        return (estado[0] >= estado[1]) or (estado[0] == 0) and \
               (3 - estado[0]) >= (3 - estado[1]) or (estado[0] == 3) and \
               (0 <= estado[0] <= 3) and \
               (0 <= estado[1] <= 3)

    def is_goal(self, estado):
        return estado == (0, 0, 1)

    def result(self, estado, accion):
        if estado[2] == 0:
            return (estado[0] - accion[1][0], estado[1] - accion[1][1], 1)
        else:
            return (estado[0] + accion[1][0], estado[1] + accion[1][1], 0)

    def heuristic(self, estado):
        return (estado[0] + estado[1]) / 2

    def value(self, estado):
        return 6 - estado[0] - estado[1]


problema = Novios()
visor = WebViewer()
solucion = astar(problema, viewer=visor)
#visor = ConsoleViewer
#solucion = astar(problema, viewer=visor)
print(solucion.path())
