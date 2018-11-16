from sklearn import tree

lisa = 1
irregular = 0
maca = 1
laranja = 0

pomar = [[150, lisa], [130, lisa], [180, irregular], [160, irregular]]

result = [maca, maca, laranja, laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, result)

peso = raw_input("Entre com o peso da fruta: ")
superficie = raw_input("Entre com o tipo de superficia da fruta, 1 - Lisa e 0 - Irregular: ")

resultadoUsuario = clf.predict([[peso, superficie]])

if resultadoUsuario == 1: 
    print("E uma maca")
else:
    print("E uma laranja")

