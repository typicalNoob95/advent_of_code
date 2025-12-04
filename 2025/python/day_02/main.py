FILE_TO_OPEN: str = "2025/python/day_02/sample.txt"

def count_in_range(start, stop, max_repetition = None):
    """
    Compte les nombres répétitifs dans l'intervalle [A, B] 
    en générant seulement les candidats pertinents.
    """
    count = 0
    max_digits = len(str(stop))
    
    if max_repetition is None:
        max_repetition = max_digits
    
        
    
    # 1. Boucle sur L (Longueur du motif)
    for length in range(1, max_digits):
        
        # 2. Boucle sur R (Nombre de répétitions)
        # On s'assure que la longueur L*R ne dépasse pas la longueur de B
        for R in range(2, (max_digits // length) + 1):
            
            # --- Calcul du Multiplicateur ---
            multiplier = sum(10**(i * length) for i in range(R))
            
            # Déterminer la plage des motifs de base (M) à tester
            min_motif = 10**(length - 1)
            max_motif = 10**length 
            
            # --- Trouver le point de départ intelligent ---
            # Nous voulons que (M * multiplier) >= A.
            # Donc, M doit être au moins (A / multiplier).
            
            # On utilise max() pour s'assurer de ne pas descendre en dessous du plus petit motif possible
            start_motif = max(min_motif, start // multiplier)
            
            # 3. Boucle sur M (Motif de base)
            for M in range(start_motif, max_motif):
                result = M * multiplier
                
                if result > stop:
                    # Si on dépasse B, plus besoin de continuer avec ce L et R, 
                    # car M augmente et tous les résultats suivants dépasseront B.
                    break
                
                if result >= start:
                    # Le nombre est dans l'intervalle [A, B]
                    count += 1
                    print(result)
                    
    return count

if __name__ == "__main__":
    with open(FILE_TO_OPEN, "r") as f:
        line = f.readline()
        string_ranges = line.split(",")

        ranges = []
        for rang in string_ranges:
            start, stop = rang.split("-")
            start = int(start)
            stop = int(stop)

            ranges.append((start, stop))

        for rang in ranges:
            print(count_in_range(rang[0], rang[1], 2))

    print(ranges)