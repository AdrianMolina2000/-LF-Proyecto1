from graphviz import Digraph

t = Digraph('Automata1', filename='automata1.gv', format="pdf")


t.attr('node', shape='doublecircle', fixedsize='true', width="1", color="black",style= "filled", fillcolor="grey")
t.node("q0")
t.node("q5")
t.attr('node', shape='circle', fixedsize='true', height= "1", color="black",style= "filled", fillcolor="grey")
t.node("q1")
t.node("q2")
t.node("q3")
t.node("q4")

t.edge(tail_name="q0", head_name="q0",label="b,c")
t.edge(tail_name="q0", head_name="q1",label="a")

t.edge(tail_name="q1", head_name="q2",label="c")
t.edge(tail_name="q1", head_name="q3",label="b")
t.edge(tail_name="q1", head_name="q5",label="a")
t.edge(tail_name="q2", head_name="q2",label="a,b,c")
t.edge(tail_name="q3", head_name="q3",label="b,c")
t.edge(tail_name="q3", head_name="q5",label="a")
t.edge(tail_name="q3", head_name="q5",label="a")
t.edge(tail_name="q4", head_name="q3",label="b,c")
t.edge(tail_name="q4", head_name="q5",label="a")
t.edge(tail_name="q5", head_name="q4",label="b")
t.edge(tail_name="q5", head_name="q5",label="a")



t.attr(overlap='false')
t.attr(fontsize='20')
t.attr(label= "Automata Parcial")
t.attr(rankdir="LR")
t.view()