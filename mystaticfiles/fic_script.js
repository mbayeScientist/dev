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


  document.addEventListener('DOMContentLoaded', (event) => {
    // Attendre 3 secondes après que la page ait chargé
    setTimeout(() => {
      // Utilisez l'instance de Bootstrap pour montrer le modal
      var myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'), {
        keyboard: false,
        backdrop: 'static'
      });
      myModal.show();
    }, 3000);  // 3000 millisecondes correspondent à 3 secondes
  });


  