def recorrer_stats(stats,jugadores):
    """Recorro las stats de la ronda y las sumo a los jugadores"""
    for jugador, stat in stats.items(): 
    # pongo items asi veo las claves y valores y los puedo recorrer
        jugadores[jugador] = aumentar_stats(jugadores[jugador],stat)
    #guardo los mvps
        
    informar_stats_de_jugadores(jugadores)
    jugadores = calcular_MVP_e_informar(stats,jugadores)
    return jugadores

def aumentar_stats(jugador, stat):
    """Guardo las stats de los jugadores para mostrar al final"""

    jugador['kills'] += stat['kills']

    jugador['assists'] += stat['assists']

    jugador['deaths'] += 1 if stat['deaths'] else 0
    jugador['puntos'] += ((stat['kills']*3) + stat['assists']) - (1 if stat['deaths'] else 0)
    
    return jugador

def informar_stats_de_jugadores(jugadores):
    """Imprimo la parte de stats de los jugadores de la tabla ordenados por puntaje"""
    jugadores = dict(sorted(jugadores.items(), key=lambda jugador: jugador[1]['puntos'], reverse=True))
    for jugador,stat in jugadores.items():
        print(f"{jugador:<12}{stat['kills']:<6}{stat['assists']:>10} {stat['deaths']:>7} {stat['puntos']:>7}")
    print("-"*50)

def imprimir_tabla(round):
    """Imprimo la parte de arriba de la tabla"""
    print(f"\nRanking ronda {round}:")
    if round =="Final":
        end=" "
    else:
        end="\n" 
    print(f"{'Jugador':<12}{'Kills':<6}{'Asistencias':>10} {'Muertes':>7} {'Puntos':>7}", end=end)
    if(round == "Final"):  
        print(f"{'MVPs':>6}")        
    print("-"*50)

def calcular_MVP_e_informar(stats,jugadores):
    """Calculo el Mvp de la ronda"""
    
    mvp = max(stats, key = lambda jugador: calcular_puntos(stats[jugador]))

    jugadores[mvp]['MVPs'] += 1
    print(f"EL MVP de la ronda fue: {mvp}")
    print("-"*50)
    return jugadores

def informar_ranking_final(jugadores):
    """Informo todo del ranking final"""
    imprimir_tabla("Final")
    for jugador, stat in jugadores.items():
        print(f"{jugador:<12}{stat['kills']:<6}{stat['assists']:>10} {stat['deaths']:>7} {stat['puntos']:>7}{stat['MVPs']:>6}")
    print("-"*50)

def calcular_puntos(jugador):
    """calculo los puntos totales de cada jugador"""
    return ((jugador['kills']*3) + jugador['assists']) - (1 if jugador['deaths'] else 0)