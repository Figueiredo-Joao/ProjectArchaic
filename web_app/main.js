const logo = document.getElementById('logo');
const btnBegin = document.getElementById('btnBegin');
const card1 = document.getElementById('card1');
const card2 = document.getElementById('card2');
const card3 = document.getElementById('card3');
const card4 = document.getElementById('card4');
const content1 = document.getElementById('content1');
const content2 = document.getElementById('content2');
const content3 = document.getElementById('content3');
const content4 = document.getElementById('content4');


function getGame1() {
    anime({
        targets: card1,
        translateX: [-700, 0],
        delay: 300,
        begin: function (anim) {
            document.getElementById('card1').style.visibility = "visible";
        }
    })
}

function getGame2() {
    anime({
        targets: card2,
        translateY: [-700, 0],
        delay: 600,
        begin: function (anim) {
            document.getElementById('card2').style.visibility = "visible";
        }
    })
}

function getGame3() {
    anime({
        targets: card3,
        translateY: [-700, 0],
        delay: 900,
        begin: function (anim) {
            document.getElementById('card3').style.visibility = "visible";
        }
    })
}

function getGame4() {
    anime({
        targets: card4,
        translateX: [700, 0],
        delay: 1200,
        begin: function (anim) {
            document.getElementById('card4').style.visibility = "visible";
        },
        complete: function(anim) {
            showDetails1();
            showDetails2();
            showDetails3();
            showDetails4();
        }
    })
}

function showDetails1() {
    anime({
        targets: content1,
        translateY: [300, 0],
        opacity: 1,
    })
}

function showDetails2() {
    anime({
        targets: content2,
        translateY: [300, 0],
        opacity: 1,
        delay: 300
    })
}

function showDetails3() {
    anime({
        targets: content3,
        translateY: [300, 0],
        opacity: 1,
        delay: 600
    })
}

function showDetails4() {
    anime({
        targets: content4,
        translateY: [300, 0],
        opacity: 1,
        delay: 900
    })
}

document.getElementById('btnBegin').onclick = () => {
    anime({
        targets: btnBegin,
        opacity: 0,
        duration: 200,
        easing: 'linear',
    });
    anime({
        targets: logo,
        opacity: 0,
        duration: 400,
        easing: 'linear',
        delay: 200,
        complete: function(anim) {
            document.getElementById('divLogo').style.display = "none";
            document.getElementById('divBegin').style.display = "none";
            document.getElementById('gamesContainer').style.display = "flex";
            getGame1();
            getGame2();
            getGame3();
            getGame4();
        }
    });
}

VanillaTilt.init(document.querySelectorAll(".card"), {
    max: 25,
    speed: 400,
    glare: true,
    "max-glare": 1
});

