import math

# Defina a constante pi com um ponto decimal
pi = 3.14159

# Loop principal
while True:
    # Apresentação das regras
    print("""
REGRAS:
1) Se não souber o número, insira 0.
2) Para raiz quadrada, use a notação "numero**(1/2)" e para raiz cúbica, "numero**(1/3)".
3) Não insira 0 em todas as entradas para evitar erros.
    """)

    # Pergunta para escolher o objetivo
    switch2 = int(input("""
Qual é o seu objetivo?
(1) Poliedro
(2) Sólidos geométricos
(3) Sair
"""))

    # Sair
    if switch2 == 3:
        print("\ntchau até mais\n")
        break

    # Sólidos geométricos
    elif switch2 == 2:
        switch5 = int(input("""
Qual é o seu objetivo?
(1) Cilindro
(2) Cone reto
(3) Esfera
"""))

        # Cilindro
        if switch5 == 1:
            raio = float(input("Valor do raio: "))
            diagonal = float(input("Valor da diagonal: "))
            altura = float(input("Qual é a altura: "))

            raio = diagonal / 2
            circunferencia = 2 * pi * raio
            area_base = pi * raio**2
            area_lateral = circunferencia * altura
            area_total = area_lateral + 2 * area_base
            volume = area_base * altura

            print(f"""Os valores obtidos foram os seguintes:
                Raio: {raio}
                Diagonal: {diagonal}
                Altura: {altura}
                Circunferência: {circunferencia}
                Área da Base: {area_base}
                Área Lateral: {area_lateral}
                Área Total: {area_total}
                Volume: {volume}
                """)

        # Cone reto
        elif switch5 == 2:
            raio = float(input("Valor do raio: "))
            altura = float(input("Qual é a altura: "))
            angulo_central = float(input("Valor do ângulo central do cone: "))

            volume = (pi * raio**2 * altura) / 3
            geratriz = math.sqrt(altura**2 + raio**2)
            altura = math.sqrt(geratriz**2 - raio**2)
            area_lateral = pi * raio * geratriz

            if raio == 0:
                area_lateral = (pi * geratriz * angulo_central) / 360
                raio = area_lateral / (pi * geratriz)

            area_circulo = pi * raio**2
            area_cone = area_lateral + area_circulo
            diametro = raio * 2

            print(f"""Os valores obtidos foram os seguintes:
                Raio: {raio}
                Altura: {altura}
                Ângulo Central: {angulo_central}
                Volume: {volume}
                Geratriz: {geratriz}
                Área Lateral: {area_lateral}
                Área da Base: {area_circulo}
                Área Total: {area_cone}
                Diâmetro: {diametro}
                """)

        # Esfera
        elif switch5 == 3:
            raio = float(input("Qual é o raio da esfera: "))
            angulo_fuso = float(input("Qual é o ângulo do fuso (em graus): "))

            angulo_fuso_radianos = math.radians(angulo_fuso)
            area = 4 * pi * raio**2
            volume = (4/3) * pi * raio**3
            area_fuso = 2 * pi * raio**2 * (1 - math.cos(angulo_fuso_radianos / 2))

            print(f"""Os valores obtidos foram os seguintes:
                Raio: {raio}
                Ângulo do Fuso: {angulo_fuso}
                Área: {area}
                Volume: {volume}
                Área do Fuso: {area_fuso}
                """)

    # Poliedros
    elif switch2 == 1:
        switch3 = int(input("""
Qual é o seu objetivo?
(1) Pirâmide regular
(2) Paralelepípedo
(3) Cubo
"""))

        # Pirâmide regular
        if switch3 == 1:
            switch4 = int(input("""
Qual é o seu objetivo?
(1) Pirâmide de base quadrada
(2) Pirâmide de base triangular equilátera
(3) Pirâmide de base hexagonal
"""))

            # Pirâmide de base quadrada
            if switch4 == 1:
                area_da_base = float(input("Qual a área da base (0 para nada): "))
                aresta = float(input("Tamanho da aresta da base: "))
                altura = float(input("Qual a altura da pirâmide (0 para nada): "))
                numero_de_lados = int(input("Quantos lados tem a sua pirâmide regular: "))
                apotema_lateral = float(input("Valor do apotema lateral: "))

                aresta = area_da_base**(1/2)
                apotema_base = aresta / 2
                area_da_base = aresta * aresta
                apotema_base = aresta / 2
                altura = math.sqrt(apotema_lateral**2 - (aresta / 2)**2)
                apotema_lateral = math.sqrt((aresta / 2)**2 + altura**2)
                aresta_lateral = math.sqrt(apotema_lateral**2 + (aresta / 2)**2)
                volume_PR = (area_da_base * altura) / 3
                area_PR = (area_da_base * altura / 2) * numero_de_lados

                print(f"""Os valores obtidos foram os seguintes:
                    Volume: {volume_PR}
                    Área Total: {area_PR}
                    Área da Base: {area_da_base}
                    Altura: {altura}
                    Número de Lados: {numero_de_lados}
                    Apótema Lateral: {apotema_lateral}
                    Apótema da Base: {apotema_base}
                    Aresta: {aresta}
                    Aresta Lateral: {aresta_lateral}
                """)

            # Pirâmide de base triangular equilátera
            elif switch4 == 2:
                aresta = float(input("Valor da aresta: "))
                aresta_lateral = float(input("Valor da aresta lateral: "))
                altura = float(input("Valor da altura: "))
                apotema_da_base = float(input("Qual a altura: "))
                lados = int(input("Quantos lados tem: "))
                apotema_lateral = float(input("Valor do apotema lateral: "))

                apotema_da_base = aresta * (3**(1/2)) / 6
                apotema_lateral = math.sqrt(aresta_lateral**2 - (aresta / 2)**2)
                altura = math.sqrt(apotema_lateral**2 - apotema_da_base**2)
                aresta_lateral = math.sqrt(altura**2 + (aresta / 2)**2)
                area_da_base = (aresta**2 * (3**(1/2))) / 4
                area_lateral = lados * (aresta * apotema_lateral / 2)
                area_total = area_da_base + area_lateral
                volume = (area_da_base * altura) / 3

                print(f"""Os valores obtidos foram os seguintes:
                    Volume: {volume}
                    Área Total: {area_total}
                    Área da Base: {area_da_base}
                    Altura: {altura}
                    Número de Lados: {lados}
                    Apótema Lateral: {apotema_lateral}
                    Apótema da Base: {apotema_da_base}
                    Aresta: {aresta}
                    Aresta Lateral: {aresta_lateral}
                """)

            # Pirâmide de base hexagonal
            elif switch4 == 3:
                aresta = float(input("Valor da aresta: "))
                altura = float(input("Altura: "))
                apotema_da_base = float(input("Valor do apotema da base: "))
                apotema_lateral = float(input("Valor do apotema da lateral: "))
                area_da_base = float(input("Valor da área da base: "))
                area_lateral = float(input("Valor da área lateral: "))

                apotema_da_base = (aresta * (3**(1/2))) / 2
                aresta = (apotema_da_base / ((3**(1/2)) / 2))
                altura = math.sqrt((apotema_lateral**2) - (apotema_da_base**2))
                apotema_lateral = math.sqrt((apotema_da_base**2) + (altura**2))
                area_lateral = (aresta * apotema_lateral / 2) * 6
                area_da_base = (6 * aresta**2 * (3**(1/2))) / 4
                volume = (area_da_base * altura) / 3

                print(f"""Os valores obtidos foram os seguintes:
                    Volume: {volume}
                    Área Total: {area_lateral}
                    Área da Base: {area_da_base}
                    Altura: {altura}
                    Apótema Lateral: {apotema_lateral}
                    Apótema da Base: {apotema_da_base}
                    Aresta: {aresta}
                """)

        # Paralelepípedo
        elif switch3 == 2:
            aresta_maior = float(input("Qual é o valor da maior aresta: "))
            aresta_menor = float(input("Qual é o valor da menor aresta: "))
            diagonal = float(input("Qual é o valor da diagonal: "))
            altura = float(input("Qual é a altura: "))

            volume = aresta_maior * aresta_menor * altura
            area_total = 2 * ((aresta_maior * aresta_menor) + (aresta_maior * altura) + (aresta_menor + altura))
            diagonal = math.sqrt(aresta_maior**2 + aresta_menor**2 + altura**2)

            print(f"""Os valores obtidos foram os seguintes:
                Maior Aresta: {aresta_maior}
                Menor Aresta: {aresta_menor}
                Diagonal: {diagonal}
                Altura: {altura}
                Volume: {volume}
                Área Total: {area_total}
                """)

        # Cubo
        elif switch3 == 3:
            aresta = float(input("Qual é o valor da aresta: "))
            diagonal = float(input("Qual é o valor da diagonal: "))

            volume = aresta**3
            area_total = 6 * aresta**2
            diagonal = aresta * (3**(1/2))

            print(f"""Os valores obtidos foram os seguintes:
                Aresta: {aresta}
                Diagonal: {diagonal}
                Volume: {volume}
                Área Total: {area_total}
                """)

