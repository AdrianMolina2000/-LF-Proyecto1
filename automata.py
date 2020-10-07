from graphviz import Digraph

def graficar_mapa():


    #Graficar
    t = Digraph('Automata', filename='Automata.gv', format="pdf", directory="Automata")
    
    t.attr('node', shape='oval', fixedsize='true', width="2",  height= "1", color="black")
    
    t.node("error", label="error")
    t.node("qo", label="qo",style= "filled", fillcolor="#E3E3E3")
    t.node("q1", label="q1",style= "filled", fillcolor="#E3E3E3")
    t.node("q1 nif", label="q1\nnombre\ninicio\nfin",style= "filled", fillcolor="#E3E3E3")

    # t.node("q1.inicio", label="q1.inicio",style= "filled", fillcolor="#E3E3E3")
    # t.node("q1.fin", label="q1.fin",style= "filled", fillcolor="#E3E3E3")
    t.node("q1.peso", label="q1.peso",style= "filled", fillcolor="#E3E3E3")
    t.node("q2", label="q2",style= "filled", fillcolor="#E3E3E3")
    t.node("q3", label="q3",style= "filled", fillcolor="#E3E3E3")
    t.node("<", label="<")

    t.node("<r", label="<r")
    t.node("<ru", label="<ru")
    t.node("<rut", label="<rut")
    t.node("<ruta", label="<ruta")
    t.node("<ruta>", label="\<ruta\>")

    t.node("<e", label="<e")
    t.node("<es", label="<es")
    t.node("<est", label="<est")
    t.node("<esta", label="<esta")
    t.node("<estac", label="<estac")
    t.node("<estaci", label="<estaci")
    t.node("<estacio", label="<estacio")
    t.node("<estacion", label="<estacion")
    t.node("<estacion>", label="\<estacion\>")

    t.node("<n", label="<n")
    t.node("<no", label="<no")
    t.node("<nom", label="<nom")
    t.node("<nomb", label="<nomb")
    t.node("<nombr", label="<nombr")
    t.node("<nombre", label="<nombre")
    t.node("<nombre>", label="\<nombre\>")

    t.edge(tail_name="qo", head_name="<", label="<")
    t.edge(tail_name="qo", head_name="error",label="^(<)")
    t.edge(tail_name="<", head_name="<r",label="R,r")
    t.edge(tail_name="<r", head_name="<ru", label="U,u")
    t.edge(tail_name="<ru", head_name="<rut", label="T,t")
    t.edge(tail_name="<rut", head_name="<ruta", label="A,a")
    t.edge(tail_name="<ruta", head_name="<ruta>", label=">")
    t.edge(tail_name="<ruta>", head_name="q1")
    t.edge(tail_name="<ruta", head_name="error", label="^(>)")

    t.edge(tail_name="<", head_name="<e",label="E,e")
    t.edge(tail_name="<e", head_name="<es",label="S,s")
    t.edge(tail_name="<es", head_name="<est",label="T,t")
    t.edge(tail_name="<est", head_name="<esta",label="A,a")
    t.edge(tail_name="<esta", head_name="<estac",label="C,c")
    t.edge(tail_name="<estac", head_name="<estaci",label="I,i")
    t.edge(tail_name="<estaci", head_name="<estacio",label="O,o")
    t.edge(tail_name="<estacio", head_name="<estacion",label="N,n")
    t.edge(tail_name="<estacion", head_name="<estacion>",label=">")
    t.edge(tail_name="<estacion>", head_name="q2")
    t.edge(tail_name="<estacion", head_name="error",label="^(>)")

    t.edge(tail_name="<", head_name="<n",label="N,n")
    t.edge(tail_name="<n", head_name="<no",label="O,o")
    t.edge(tail_name="<no", head_name="<nom",label="M,m")
    t.edge(tail_name="<nom", head_name="<nomb",label="B,b")
    t.edge(tail_name="<nomb", head_name="<nombr",label="R,r")
    t.edge(tail_name="<nombr", head_name="<nombre",label="E,e")
    t.edge(tail_name="<nombre", head_name="<nombre>",label=">")
    t.edge(tail_name="<nombre>", head_name="q3")
    t.edge(tail_name="<nombre", head_name="error",label="^(>)")

    #RUTA
    t.node("q1 2", label="q1",style= "filled", fillcolor="#E3E3E3")
    t.node("r<", label="r<")
    t.node("error2", label="error")

    t.node("r<n", label="r<n")
    t.node("r<no", label="r<no")
    t.node("r<nom", label="r<nom")
    t.node("r<nomb", label="r<nomb")
    t.node("r<nombr", label="r<nombr")
    t.node("r<nombre", label="r<nombre")
    t.node("r<nombre>", label="r<nombre>")

    t.node("r<i", label="r<i")
    t.node("r<in", label="r<in")
    t.node("r<ini", label="r<ini")
    t.node("r<inic", label="r<inic")
    t.node("r<inici", label="r<inici")
    t.node("r<inicio", label="r<inicio")
    t.node("r<inicio>", label="r<inicio>")

    t.node("r<f", label="r<f")
    t.node("r<fi", label="r<fi")
    t.node("r<fin", label="r<fin")
    t.node("r<fin>", label="r<fin>")

    t.edge(tail_name="q1 2", head_name="r<", label="<")
    t.edge(tail_name="q1 2", head_name="error2",label="^(<)")
    


    Rnombre = ['','n', 'o', 'm', 'b', 'r', 'e']
    RnombreA = ""
    RnombreB = ""
    for i in range(1,7):
        RnombreA += Rnombre[i-1]
        RnombreB += Rnombre[i]
        t.edge(tail_name=f"r<{RnombreA}", head_name=f"r<{RnombreB}",label=f"{Rnombre[i].upper()},{Rnombre[i]}")

    t.edge(tail_name="r<nombre", head_name="r<nombre>",label=">")
    t.edge(tail_name="r<nombre>", head_name="q1 nif")
    t.edge(tail_name="r<nombre", head_name="error2",label="^(>)")

    
    inicio = ['','i', 'n', 'i', 'c', 'i', 'o']
    inicioA = ""
    inicioB = ""
    for i in range(1,7):
        inicioA += inicio[i-1]
        inicioB += inicio[i]
        t.edge(tail_name=f"r<{inicioA}", head_name=f"r<{inicioB}",label=f"{inicio[i].upper()},{inicio[i]}")
    t.edge(tail_name="r<inicio", head_name="r<inicio>",label=">")
    t.edge(tail_name="r<inicio>", head_name="q1 nif")
    t.edge(tail_name="r<inicio", head_name="error2",label="^(>)")

    fin = ['','f', 'i', 'n']
    finA = ""
    finB = ""
    for i in range(1,4):
        finA += fin[i-1]
        finB += fin[i]
        t.edge(tail_name=f"r<{finA}", head_name=f"r<{finB}",label=f"{fin[i].upper()},{fin[i]}")
    t.edge(tail_name="r<fin", head_name="r<fin>",label=">")
    t.edge(tail_name="r<fin>", head_name="q1 nif")
    t.edge(tail_name="r<fin", head_name="error2",label="^(>)")

    peso = ['','p', 'e', 's', 'o']
    pesoA = ""
    pesoB = ""
    for i in range(1,5):
        pesoA += peso[i-1]
        pesoB += peso[i]
        t.edge(tail_name=f"r<{pesoA}", head_name=f"r<{pesoB}",label=f"{peso[i].upper()},{peso[i]}")
    t.edge(tail_name="r<peso", head_name="r<peso>",label=">")
    t.edge(tail_name="r<peso>", head_name="q1.peso")
    t.edge(tail_name="r<peso", head_name="error2",label="^(>)")


    t.node("error 3", label="error")
    t.node("q1 nif 2", label="q1\nnombre\ninicio\nfin",style= "filled", fillcolor="#E3E3E3")
    # t.node("q1.nombre 2", label="q1.nombre",style= "filled", fillcolor="#E3E3E3")
    t.node("r_pL", label="primera Letra")
    t.node("r_resto_nombre", label="resto")
    t.node("q4 2", label="q4",style= "filled", fillcolor="#E3E3E3")

    t.edge(tail_name="q1 nif 2", head_name="r_pL", label='L')
    t.edge(tail_name="q1 nif 2", head_name="error 3", label='^(L)')
    t.edge(tail_name="r_pL", head_name="r_resto_nombre", label='L,D,_')
    t.edge(tail_name="r_resto_nombre", head_name="r_resto_nombre", label='L,D,_')
    t.edge(tail_name="r_resto_nombre", head_name="r</", label='<')
    t.edge(tail_name="r</", head_name="q4 2", label='/')
    t.edge(tail_name="r_resto_nombre", head_name="error 3", label='^(<)')


    #Peso
    t.node("error 4", label="error")
    t.node("q1.peso 2", label="q1.peso",style= "filled", fillcolor="#E3E3E3")
    t.node("q4 3", label="q4",style= "filled", fillcolor="#E3E3E3")
    t.node("r</ 2", label="r</")
    
    t.edge(tail_name="q1.peso 2", head_name="num", label='D')
    t.edge(tail_name="num", head_name="num", label='D')
    t.edge(tail_name="num", head_name="error 4", label='^(D,.,<)')
    t.edge(tail_name="num", head_name="punto", label='punto')
    t.edge(tail_name="num", head_name="r</ 2", label='<')
    t.edge(tail_name="punto", head_name="num 2", label='D')
    t.edge(tail_name="num 2", head_name="num 2", label='D')
    t.edge(tail_name="num 2", head_name="error 4", label='^(D,<)')
    t.edge(tail_name="num 2", head_name="r</ 2", label='<')
    t.edge(tail_name="r</ 2", head_name="q4 3", label="/")
    t.edge(tail_name="q1.peso 2", head_name="error 4", label='^(D)')



    #penwidth = "5"
    t.attr(overlap='false')
    t.attr(label= "Automata")
    t.attr(fontsize='20')
    t.attr(rankdir="LR")
    t.view()

graficar_mapa()