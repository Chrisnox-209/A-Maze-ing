import time


class Timer:
    """Classe utilitaire pour mesurer le temps d'exécution.
    Permet de chronométrer la génération ou la résolution du labyrinthe.
    Gère le démarrage et le calcul de la durée écoulée.
    """
    def __init__(self) -> None:
        self.start: float = time.perf_counter()

    def restart(self) -> None:
        """Réinitialise le chronomètre à l'instant actuel.
        Met à jour le temps de départ.
        """
        self.start = time.perf_counter()

    def get_time(self) -> float:
        """Calcule et retourne le temps écoulé depuis le démarrage.
        Utile pour afficher les performances à l'utilisateur.
        """
        return time.perf_counter() - self.start
