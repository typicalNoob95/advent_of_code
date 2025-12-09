import re
import math
from typing import List, Tuple, Dict, Any

# Définition de type pour les coordonnées d'une boîte de jonction
JunctionBox = Tuple[int, int, int] 
# Définition de type pour une arête : (Boîte1, Boîte2, Distance_Carrée)
Edge = Tuple[JunctionBox, JunctionBox, int]

# --- Fonctions Union-Find ---

def Find(box: JunctionBox, parent: Dict[JunctionBox, JunctionBox]) -> JunctionBox:
    """Trouve la racine du circuit de la boîte (avec compression de chemin)."""
    if parent[box] == box:
        return box
    # Compression de chemin : rattache directement à la racine
    parent[box] = Find(parent[box], parent)
    return parent[box]

def Union(box1: JunctionBox, box2: JunctionBox, parent: Dict[JunctionBox, JunctionBox], sizes: Dict[JunctionBox, int]) -> bool:
    """Fusionne les circuits de deux boîtes (avec union par taille)."""
    root1 = Find(box1, parent)
    root2 = Find(box2, parent)

    if root1 != root2:
        # Union par Taille : Attacher le circuit le plus petit au plus grand
        if sizes[root1] < sizes[root2]:
            root1, root2 = root2, root1 # root1 devient toujours la plus grande
        
        # Fusion
        parent[root2] = root1
        
        # Mise à jour de la taille
        sizes[root1] += sizes[root2]
        return True
    return False

# --- Fonctions de préparation des données ---

def parse_input(filepath: str) -> List[JunctionBox]:
    """Lit le fichier et retourne la liste des positions des boîtes de jonction."""
    junction_boxes_positions = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            x, y, z  = re.findall(r"\d+", line)
            junction_boxes_positions.append((int(x), int(y), int(z)))
    return junction_boxes_positions

def generate_and_sort_edges(positions: List[JunctionBox]) -> List[Edge]:
    """Génère toutes les paires uniques et les trie par carré de distance."""
    junction_boxes_distances: List[Edge] = []
    
    for i in range(len(positions) - 1):
        p1 = positions[i]
        for j in range(i + 1, len(positions)):
            p2 = positions[j]
            
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            dz = p1[2] - p2[2]
            
            # Calcul du carré de la distance
            distance_squared = dx*dx + dy*dy + dz*dz
            
            junction_boxes_distances.append((p1, p2, distance_squared))

    # Tri par distance (carrée)
    return sorted(junction_boxes_distances, key=lambda x: x[2])

def initialize_union_find(positions: List[JunctionBox]) -> Tuple[Dict[JunctionBox, JunctionBox], Dict[JunctionBox, int]]:
    """Initialise les structures Union-Find (parent et sizes)."""
    parent = {}
    sizes = {}
    for jb in positions:
        parent[jb] = jb
        sizes[jb] = 1
    return parent, sizes

# ----------------------------------------
## 🧩 Partie 1: Connexion des 1000 paires les plus courtes
# ----------------------------------------

def solve_part_one(positions: List[JunctionBox], sorted_edges: List[Edge], num_connections: int) -> int:
    """Connecte le nombre d'arêtes spécifié et calcule le produit des 3 plus grandes tailles de circuits."""
    
    # Réinitialisation de l'état Union-Find
    parent, sizes = initialize_union_find(positions)

    # Processus de connexion
    for i in range(num_connections):
        if i >= len(sorted_edges):
            break
            
        jb1, jb2, _ = sorted_edges[i]
        Union(jb1, jb2, parent, sizes)

    # Récupérer les tailles finales des circuits
    circuit_sizes = []
    # On itère sur toutes les boîtes, mais on ne garde que les tailles de celles qui sont des racines
    for box in positions:
        if Find(box, parent) == box: # Vérifier si la boîte est la racine
            circuit_sizes.append(sizes[box])

    # Trier les tailles et multiplier les trois plus grandes
    circuit_sizes.sort(reverse=True)
    
    # Assurez-vous d'avoir au moins 3 tailles (si moins, math.prod gérera)
    lengths = circuit_sizes[0:3]
    
    return math.prod(lengths)

# ----------------------------------------
## 🧩 Partie 2: Dernière connexion pour un circuit unique
# ----------------------------------------

def solve_part_two(positions: List[JunctionBox], sorted_edges: List[Edge]) -> int:
    """Continue la connexion jusqu'à ce que toutes les boîtes forment un seul circuit et retourne le produit des coordonnées X de la dernière paire."""
    
    # Réinitialisation de l'état Union-Find
    parent, sizes = initialize_union_find(positions)

    N = len(positions)
    num_circuits = N
    derniere_connexion_jb1 = None
    derniere_connexion_jb2 = None

    # Processus de connexion jusqu'à ce que num_circuits == 1
    for jb1, jb2, _ in sorted_edges:
        
        if Union(jb1, jb2, parent, sizes):
            num_circuits -= 1
            
            if num_circuits == 1:
                # La dernière arête qui connecte tout!
                derniere_connexion_jb1 = jb1
                derniere_connexion_jb2 = jb2
                break

    # Calcul du résultat
    if derniere_connexion_jb1 and derniere_connexion_jb2:
        x1 = derniere_connexion_jb1[0]
        x2 = derniere_connexion_jb2[0]
        return x1 * x2
    else:
        # Ceci ne devrait pas arriver si le graphe est connexe
        return 0

# ----------------------------------------
## 🚀 Exécution principale
# ----------------------------------------

if __name__ == "__main__":
    # NOTE : Changer le chemin du fichier pour votre puzzle input complet!
    FILEPATH = "2025/python/day_08/input.txt"
    
    positions = parse_input(FILEPATH)
    sorted_edges = generate_and_sort_edges(positions)
    
    # --- Résolution Partie 1 ---
    # Pour l'exemple, c'est 10 connexions. Pour le puzzle réel, ce sera 1000.
    NUM_CONNECTIONS_PART_ONE = 10 if FILEPATH.endswith("sample.txt") else 1000
    
    result_part_one = solve_part_one(positions, sorted_edges, NUM_CONNECTIONS_PART_ONE)
    
    print("--- Résultat Partie 1 ---")
    print(f"Connexions : {NUM_CONNECTIONS_PART_ONE}")
    print(f"Produit des 3 plus grandes tailles de circuits : {result_part_one} (Attendu pour l'exemple: 40)")
    
    # --- Résolution Partie 2 ---
    result_part_two = solve_part_two(positions, sorted_edges)
    
    print("\n--- Résultat Partie 2 ---")
    print(f"Produit des coordonnées X de la dernière connexion : {result_part_two} (Attendu pour l'exemple: 25272)")