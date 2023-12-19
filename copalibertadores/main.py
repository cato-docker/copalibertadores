import random
import tkinter as tk
from paises import *




Bolillero_1 = ["Palmeiras(Br)","River(Ar)","Flamengo(Br)","Nacional (U)","Gremio(Br)","Peñarol(U)","Sao Pablo(Br)"]
Bolillero_2 = ["Atletico Mineiro(Br)",
"Independiente del Valle(Ecu)","Cerro Porteño(Par)","Libertad(Par)",
"Atletico Nacional(Col)","Barcelona(Ecu)","Liga de Quito(Ecu)","Estudiantes de La Plata(Ar)"]
Bolillero_3 = ["Junior(Col)","Colo Colo(Chi)","San Lorenzo(Ar)", "Bolivar(Bol)","Sporting Cristal(Per)","The Stongests(Bol)","Rosario Central(Arg)","J Wilsterman(Bol)"]
Bolillero_4 = ["Melgar(Per)","Bragantino(Br)","Universitarios(Per)","Talleres(Ar)","Alianza Lima(Per)","Caracas(Ven)","Botafogo(Br)","Defensor Sporting(U)"]



# Grupos



Grupo_A = []
Grupo_B = []
Grupo_C = []
Grupo_D = []
Grupo_E = []
Grupo_F = []
Grupo_G = []
Grupo_H = []

grupos = [Grupo_A, Grupo_B, Grupo_C, Grupo_D, Grupo_E, Grupo_F, Grupo_G, Grupo_H]

def mismo_pais(equipo, grupo, equipos_por_pais):
    pais_equipo = None
    for pais, equipos in equipos_por_pais.items():
        if equipo in equipos:
            pais_equipo = pais
            break
    
    for e in grupo:
        for pais, equipos in equipos_por_pais.items():
            if e in equipos and pais == pais_equipo:
                return True
    return False

equipos_por_pais = {
    'Argentina': Argentina,
    'Bolivia': Bolivia,
    'Brasil': Brasil,
    'Colombia': Colombia,
    'Chile': Chile,
    'Ecuador': Ecuador,
    'Paraguay': Paraguay,
    'Peru': Peru,
    'Uruguay': Uruguay,
    'Venezuela': Venezuela
}

# Asignar Fluminense al Grupo A
Grupo_A.append('Fluminese(Br)')
equipos_asignados = ['Fluminese']  # Lista para llevar registro de los equipos asignados

# Mezclar los equipos del Bolillero_1 (excluyendo a Fluminense)
bolillero_sin_fluminense = [equipo for equipo in Bolillero_1 if equipo != 'Fluminese']
random.shuffle(bolillero_sin_fluminense)

# Asignar los equipos restantes a los grupos
for grupo in grupos[1:]:
    equipo_asignado = False
    for equipo in bolillero_sin_fluminense:
        if equipo not in equipos_asignados and not mismo_pais(equipo, grupo, equipos_por_pais):
            grupo.append(equipo)
            equipos_asignados.append(equipo)
            equipo_asignado = True
            break
    if not equipo_asignado:
        # Si no se puede asignar a ningún grupo, se agrega al último grupo
        grupos[-1].append(equipo)
        equipos_asignados.append(equipo)
        
def asignar_equipos(bolillero, grupos, equipos_por_pais, fase_preliminar):
    equipos_asignados = []
    
    for equipo in bolillero:
        repetido = any(equipo in grupo for grupo in grupos)
        if not repetido:
            grupo_vacio = next((grupo for grupo in grupos if len(grupo) < 4), None)
            if grupo_vacio:
                pais_equipo = next((pais for pais, equipos in equipos_por_pais.items() if equipo in equipos), None)
                repetido_pais_grupo = any(pais_equipo in equipos_por_pais[pais_grupo] for pais_grupo in [pais for equipo_grupo in grupo_vacio for pais, equipos in equipos_por_pais.items() if equipo_grupo in equipos])
                
                if repetido_pais_grupo:
                    # Si hay un equipo del mismo país en el grupo, reemplacemos uno por un equipo de la fase preliminar
                    idx = grupos.index(grupo_vacio)
                    for equipo_grupo in grupo_vacio:
                        pais_equipo_grupo = next((pais for pais, equipos in equipos_por_pais.items() if equipo_grupo in equipos), None)
                        if pais_equipo == pais_equipo_grupo:
                            equipos_preliminar = [eq for eq in fase_preliminar if eq not in equipos_asignados]
                            if equipos_preliminar:
                                equipo_reemplazo = random.choice(equipos_preliminar)
                                equipos_asignados.remove(equipo_grupo)
                                equipos_asignados.append(equipo_reemplazo)
                                grupo_vacio[grupo_vacio.index(equipo_grupo)] = equipo_reemplazo
                                equipos_asignados.append(equipo_reemplazo)
                                break
                else:
                    grupo_vacio.append(equipo)
                    equipos_asignados.append(equipo)
                    
    return equipos_asignados

root = tk.Tk()
root.title("Fase de grupos libertadores 2024")

# asignar_equipos(Bolillero_1,grupos,equipos_por_pais)


root = tk.Tk()
root.title("Fase de grupos Libertadores 2024")

def mostrar_equipos():
    for widget in root.winfo_children():
        widget.destroy()
    
    fase_preliminar = ["Equipo 1", "Equipo 2", "Equipo 3", "Equipo 4"]
    
    asignar_equipos(Bolillero_1, grupos, equipos_por_pais, fase_preliminar)
    asignar_equipos(Bolillero_2, grupos, equipos_por_pais, fase_preliminar)
    asignar_equipos(Bolillero_3, grupos, equipos_por_pais, fase_preliminar)
    asignar_equipos(Bolillero_4, grupos, equipos_por_pais, fase_preliminar)

    grupos_frame = tk.Frame(root)
    grupos_frame.pack()

    for i, grupo in enumerate(grupos):
        grupo_frame = tk.Frame(grupos_frame)
        grupo_frame.pack(side=tk.LEFT, padx=10)

        tk.Label(grupo_frame, text=f"Grupo {chr(65 + i)}", font=("Arial", 14, "bold")).pack(anchor="w")

        for equipo in grupo:
            tk.Label(grupo_frame, text=equipo).pack(anchor="w")

    boton_regenerar = tk.Button(root, text="Regenerar", command=mostrar_equipos)
    boton_regenerar.pack()

mostrar_equipos()

root.mainloop()