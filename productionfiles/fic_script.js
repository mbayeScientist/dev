document.addEventListener('DOMContentLoaded', () => {
    // Sélectionner l'élément du carrousel
    const carousel = document.getElementById('carouselExampleControls');
  
    // Gestion des clics sur "Previous"
    document.getElementById('previous-page').addEventListener('click', (e) => {
      e.preventDefault();
      // Déplacer le carrousel vers l'élément précédent
      bootstrap.Carousel.getInstance(carousel).prev();
    });
  
    // Gestion des clics sur "Next"
    document.getElementById('next-page').addEventListener('click', (e) => {
      e.preventDefault();
      // Déplacer le carrousel vers l'élément suivant
      bootstrap.Carousel.getInstance(carousel).next();
    });
  });
  