//ნასწავლი მასალის დახმარებით გააკეთეთ სურათების სლაიდერი , დაუმატეთ რაიმე კარგი დიზაინი თქვენი წარმოსახვით

const images = document.querySelectorAll('#slider img');
let index = 0;

function showImage(i) {
    images.forEach(img => img.classList.remove('active'));
    images[i].classList.add('active');
}

document.getElementById('next').addEventListener('click', () =>{
    index = (index + 1) % images.length;
    showImage(index);
});

document.getElementById('prev').addEventListener('click', () => {
    index = (index - 1 + images.length) % images.length;
    showImage(index);
})
setInterval(() => {
    index = (index + 1) % images.length;
    showImage(index);
},5000);

