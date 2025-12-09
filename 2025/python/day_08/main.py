import re
import math
import collections # Peut être utile pour une structure plus propre, mais non obligatoire

# --- Fonctions Union-Find ---

def Find(box, parent):
    """Trouve la racine du circuit de la boîte (avec compression de chemin)."""
    if parent[box] == box:
        return box
    # Compression de chemin
    parent[box] = Find(parent[box], parent)
    return parent[box]

def Union(box1, box2, parent, sizes):
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

# --- Fonction principale ---

if __name__ == "__main__":
    junction_boxes_positions = []

    # Le parsing du fichier semble correct.
    with open("2025/python/day_08/input.txt", "r") as file:
        for line in file.readlines():
            x, y, z  = re.findall(r"\d+", line)
            junction_boxes_positions.append((int(x), int(y), int(z)))

    # Utiliser une liste de triplets (boîte1, boîte2, distance_carrée) pour le tri
    junction_boxes_distances = []
    
    # Remplacer la distance euclidienne par le carré de la distance
    for i in range(len(junction_boxes_positions) - 1):
        p1 = junction_boxes_positions[i]
        for j in range(i + 1, len(junction_boxes_positions)):
            p2 = junction_boxes_positions[j]
            
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            dz = p1[2] - p2[2]
            
            # Calcul du carré de la distance
            distance_squared = dx*dx + dy*dy + dz*dz
            
            # On utilise les coordonnées des boîtes comme clés dans l'Union-Find
            junction_boxes_distances.append((p1, p2, distance_squared))

    # Tri par distance (carrée)
    sorted_junction_boxes_distances = sorted(junction_boxes_distances, key=lambda x: x[2])

    # Initialisation Union-Find
    parent = {} # Qui est le parent/représentant de cette boîte
    sizes = {}  # Taille du circuit, stockée uniquement à la racine
    
    for jb in junction_boxes_positions:
        parent[jb] = jb
        sizes[jb] = 1

    # Processus de connexion : 10 connexions pour l'exemple, 1000 pour le puzzle
    # L'exemple demande les 10 plus courtes arêtes.
    NUM_CONNECTIONS = 1000
    
    for i in range(NUM_CONNECTIONS):
        jb1, jb2, _ = sorted_junction_boxes_distances[i]
        
        # Utiliser la fonction Union
        Union(jb1, jb2, parent, sizes)

    # Récupérer les tailles finales des circuits
    circuit_sizes = []
    
    # On itère sur toutes les boîtes, mais on ne garde que les tailles de celles qui sont des racines
    # En pratique, on peut itérer sur le dictionnaire sizes et ne garder que les clés qui sont des racines
    
    # Solution 1: Filtrer les racines
    for box in junction_boxes_positions:
        if parent[box] == box:
            circuit_sizes.append(sizes[box])
    
    # Solution 2: Filtrer le dictionnaire sizes (plus direct car on sait que la clé est la racine)
    # circuit_sizes = [size for box, size in sizes.items() if Find(box, parent) == box]

    
    # Trier les tailles et multiplier les trois plus grandes
    circuit_sizes.sort(reverse=True)

    # L'exemple demande de multiplier les trois plus grandes, même si elles sont moins de trois
    # (Bien que l'exemple de 20 boîtes et 10 connexions donnera 11 circuits, donc 11 tailles)
    
    if len(circuit_sizes) < 3:
        # Gérer le cas où il y a moins de 3 circuits, si besoin (peu probable avec le puzzle réel)
        print("Moins de 3 circuits trouvés.")
        lengths = circuit_sizes
    else:
        lengths = circuit_sizes[0:3]

    result = math.prod(lengths)
    print(f"Les trois plus grandes tailles de circuits sont : {lengths}")
    print(f"Le résultat (produit des trois plus grandes tailles) est : {result}")

    # Le résultat attendu pour l'exemple est 40 (5 * 4 * 2)