const img1 = document.getElementById("img1");
const img1Original = img.src="images/leo2.jpg";
const img1Hover = 'img1-hover.jpg';

img1.addEventListener("mouseenter", () =>{
    img1.src="images/leo2.jpg" = img1Hover;
});
img1.addEventListener('mouseleave' , () => {
    img1.src="images/leo" = img1Original;
});

const img2 = document.getElementById("img2");
const img2Original = img2.src;
const img2Hover = 'img2-hover.jpg';

img2.addEventListener('mouseenter', () => {
    img2.src = img2Hover;
});
img2.addEventListener('mouseleave', () => {
    img2.src = img2Original;
});


const img3 = document.getElementById("img3");
const img3Original = img3.src;
const img3Clicked = "images-clicked.jpg";

img3.addEventListener('click', () => {
    img3.src = img3Clicked;
})
img3.addEventListener('mouseleave', () =>{
    img3.src = img3Original;
});