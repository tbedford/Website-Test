# Learning JavaScript with HTML5 Canvas

Summary: In this article I decide to learn JavaScript and write a
couple of simple JavaScript programs.

I decided it was high time I learned JavaScript. I have dabbled before but
never really learnt it properly. I decided to write a couple of programs that
use an HTML5 Canvas to test the language out a bit. I use simple
iteration, JavaScript objects, arrays and conditionals. The bread and
butter things you need to write any porogram. Things went really well
and I was able to put together some very simple demos in a couple of
hours.

As a language I'm not a huge fan of JavaScript - at least as it was in
the old days. I prefer Python or C, but the thing is, each language has
certain things it's good at and if you want code running in your
browser JavaScript, or at least code running on a JavaScript engine in
the browser, is the way to go.

I actually found working with JavaScript and the HTMLß5 Canvas great
fun. I would like to see young coders taking this approach on the
basis that JavaScript running in the browser gives you instant
gratification. You can see colours, and objects and it's all good.

I decided to get the ball rolling (ha ha) by getting a ball bouncing
around inside the browser.

As with learning any language your first attempt at writing something
is usually painful and the result horrible and you figure it all
out. But here's my first attempt:

## Code attempt 1

``` html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Ball</title>
    <style>
    	* { padding: 40; margin: 40; }
    	canvas { background: #EEE; display: block; margin: 0 auto; }
    </style>
</head>
<body>
<canvas id="myCanvas" width="480" height="320"></canvas>
<script>
  
  var canvas = document.getElementById("myCanvas");
  var ctx = canvas.getContext("2d");

  var x = canvas.width / 2;
  var y = canvas.height /2;

  var dx = 2;
  var dy = 2;

  var r = Math.floor(Math.random() * 255);
  var g = Math.floor(Math.random() * 255);
  var b = Math.floor(Math.random() * 255);

  var col = "rgb(" + r + "," + g + "," + b + ")";
  console.log("col is: >%s<", col);
  
  var b = {x: x, y: y, rad: 30, color: col};

  function move_ball(ball)
  {
    if (ball.x > (canvas.width - ball.rad) || ball.x < (0 + ball.rad)) {
       dx = -dx;
    }

    if (ball.y > (canvas.height - ball.rad) || ball.y < (0 + ball.rad)) {
       dy = -dy;
    }
          
    ball.x = ball.x + dx;
    ball.y = ball.y + dy;
                                                        
  }
  
  function draw_ball(ball)
  {
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ball.rad, 0, Math.PI*2, false);
    ctx.fillStyle = ball.color;
    ctx.fill();
    ctx.closePath();
  }

  
  function draw()
  {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // draw small static ball at centre (for debugging)
    ctx.beginPath();
    ctx.arc(canvas.width/2, canvas.height/2, 10, 0, Math.PI*2, false);
    ctx.fillStyle = "#FF0022";
    ctx.fill();
    ctx.closePath();

    move_ball(b);
    draw_ball(b);
  }
  setInterval(draw, 30);
  
</script>
</body>
</html>
```

Far from perfect code but neat and simple. I do like the way callbacks
can simplify things. Obviously if you are writing Node code you will
be (or have to get) very familiar with callbacks. They are simple in
that your code gets called back by the underlying engine when its
ready for you. This asynchronous nature of callbacks is of course at
the very heart of Node. In the above code, the `draw` function gets
called back after a 30 milli-second timeout. The callback is set up by
the `setInterval` function.

You can save the above code to a file such as `ball.html` and then
double click it to run it in a browser. You should see a ball bouncing
around the screen.

## Code attempt 2

The main thing I wanted to add in my next attempt was the use of JavaScript objects. JavaScript
doesn't have classes built into the core language, but you can create `objects` in JavaScript. Here's the
`ball` object:

``` javascript
var ball = {
   x: x,
   y: y,
   rad: rad,
   color: col,
   dx: dx,
   dy: dy
}
```

Once the obbject has been created we can pass it to functions and give
its attributes values. I needed to do this for this example because I
want lots of balls bouncing around the screen! Each ball object can
then have its attributes set individually and retain that
state. 

Because there will be lots of balls bouncing around I simply
keep track of them all in an array. I can work my way along the array
updating the attributes of each object. This is a common use case in
games for example, where you have a list of 'baddy' objects stored in
an array and you then check the player object with each item in the
baddy array for a collision. That's just one examples, but the idea of
objects stored in an array is generally very useful.

So armed with this idea I then launched into my second attempt at
writing some fun JavaScript:

``` html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Balls!</title>
  <style>
    * {
      padding: 40;
      margin: 40;
    }

    canvas {
      background: #000000;
      display: block;
      margin: 0 auto;
    }
  </style>
</head>
<body>
  <canvas id="myCanvas" width="960" height="640"></canvas>
  <script>
    function random_int(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function rgba(r, g, b, a) {
      return "rgba(" + r + "," + g + "," + b + "," + a + ")";
    }


    function random_color() {
      var r = random_int(0, 255);
      var g = random_int(0, 255);
      var b = random_int(0, 255);
      var a = Math.round(Math.random() * 10) / 10; // value between 0.1 and 1.0
      if (a == 0.0) {
        a = 0.1;
      } // Hack because 0.0 won't be visible
      return rgba(r, g, b, a);
    }


    function random_ball() {
      var rad = random_int(20, 70);
      var dx = random_int(-8, 8);
      var dy = random_int(-8, 8);
      // Hack - sometimes if dx/dy is zero a ball gets stuck!
      if (dx == 0) {
        dx = 1;
      }
      if (dy == 0) {
        dy = 1;
      }

      var x = canvas.width / 2;
      var y = canvas.height / 2;

      // fudge factor to make sure balls are created within range
      if (x < rad) {
        x = rad;
      }
      if (x > canvas.width - rad) {
        x = canvas.width - (rad * 4);
      }
      if (y < rad) {
        y = rad
      };
      if (y > canvas.height - rad) {
        y = canvas.height - (rad * 4)
      };

      var col = random_color();

      var ball = {
        x: x,
        y: y,
        rad: rad,
        color: col,
        dx: dx,
        dy: dy
      }
      return (ball);
    }

    function draw_ball(ball) {
      ctx.beginPath();
      ctx.arc(ball.x, ball.y, ball.rad, 0, Math.PI * 2, false);
      ctx.fillStyle = ball.color;
      ctx.fill();
      ctx.closePath();
    }

    function move_ball(ball) {
      // check x within bounds
      if (ball.x > (canvas.width - ball.rad) || ball.x < (0 + ball.rad)) {
        ball.dx = -ball.dx;
      }

      // check y within bounds
      if (ball.y > (canvas.height - ball.rad) || ball.y < (0 + ball.rad)) {
        ball.dy = -ball.dy;
      }

      // move ball
      ball.x = ball.x + ball.dx;
      ball.y = ball.y + ball.dy;

    }

    function draw() {
      // clear screen
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      // draw balls
      for (var i = 0; i < Balls.length; i++) {
        draw_ball(Balls[i]);
      }
      // move Balls
      for (var i = 0; i < Balls.length; i++) {
        move_ball(Balls[i]);
      }
    }

    //
    // Main code routine
    //
    var canvas = document.getElementById("myCanvas");
    var ctx = canvas.getContext("2d");

    var Balls = [];
    var NUM_BALLS = 100;

    for (var i = 0; i < NUM_BALLS; i++) {
      Balls.push(random_ball());
    }

    // call drawing routine every x milliseconds
    setInterval(draw, 30);
  </script>
</body>
</html>
```

You can save the code to a file such as `balls.html` and double click
it to run it. You can experiment with the number of balls you bounce
around on screen.

## Emacs let me down

Sadly Emacs did not seem to handle JavaScript code inside HTML very
well. It was fine when I was writing some little JavaScript snippets
and then running them via Node on the command line. I'm sure there is
an Emacs mode that handles this situation more gracefully, but frankly
I didn't want to spend time exploring it. If the above code looks a
bit ropey in terms of layout, that's why. I have since moved mostly 
to VS Code and so no longer experience this issue.

## Summary

This was a really fun experiment and I found I loved the interactivity
of running JavaScript in the browser, and using HTML5 Canvas it was
fairly easy to see Colourful Things. A great way to learn a language!

I had really wanted to progress this and do some fun demos such as a
starfield. I also had a lens demo half done but simply ran of time due
to work/real-world getting in the way.

Still if you are going to learn JavaScript I do recommend it, and
please feel free to use my code as a starting point on your own
learning adventures.

## Resources

* [W3 Schools info on HTML5 Canvas](https://www.w3schools.com/html/html5_canvas.asp)

---

* Published: 2018-07-05 19:56:00 UTC
* Updated: 2018-07-05 19:56:00 UTC
* UUID: 0658BAA4-3D77-40AA-9BAA-7F188924AB0E
