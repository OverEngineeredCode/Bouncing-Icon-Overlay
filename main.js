/*
    Bouncing stream overlay  Copyright (C) 2020 -  Ethan Marshall
    This program comes with ABSOLUTELY NO WARRANTY; for details, see LICENCE.
    This is free software, and you are welcome to redistribute it
    under certain conditions; again, see LICENCE for details.
*/

const icons = ["cpp", "c", "c#", "js-sq", "js-bd", "node", "react", "python", "php", "tux"]

var context;
var img;

var x = config["initial-x"];
var y = config["initial-y"];
var dx = 2;
var dy = 2;

const CANVAS_W = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
const CANVAS_H = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
const ANIM_SPEED = Math.min(Math.max(100 - config["speed"], 0), 100);


function random(max) {
    return Math.floor(Math.random() * (max + 1));
}

function runOverlay() {
    myCanvas = document.getElementById("drawSurface");
    myCanvas.width = CANVAS_W
    myCanvas.height = CANVAS_H

    context = myCanvas.getContext('2d');

    var randint = random(icons.length - 1);
    var randElement = document.getElementById(icons[randint]);
    img = randElement;

    setInterval(draw, ANIM_SPEED);
}

function draw() {
    context.clearRect(0, 0, CANVAS_W, CANVAS_H);
    context.drawImage(img, x, y, 100, 100);

    if (x < 0 || x > CANVAS_W) dx = -dx;
    if (y < 0 || y > CANVAS_H) dy = -dy;
    x += dx;
    y += dy;
}