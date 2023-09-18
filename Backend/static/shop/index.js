const carousel = document.querySelector('.carousel');
const leftArrow = document.querySelector('.left-arrow');
const rightArrow = document.querySelector('.right-arrow');

let currentIndex = 0;

rightArrow.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % carousel.children.length;
  updateCarouselPosition();
});

leftArrow.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + carousel.children.length) % carousel.children.length;
  updateCarouselPosition();
});

function updateCarouselPosition() {
  const cardWidth = carousel.children[0].offsetWidth + 20; // Including margin
  carousel.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
}
