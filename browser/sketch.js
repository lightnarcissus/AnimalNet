require(['async'], function (async) {
    //foo is now loaded.
});
<<<<<<< HEAD
var frame;
var lines=[];
=======
var frame=[];
>>>>>>> 1e91b1c5155cc7e1924a381b113fc877272d39d4
var someText="nothing";
var files="ok.txt";
var lines=[];

function setup() {
  readTextFile("ok.txt");
  createCanvas(windowWidth,windowHeight);
<<<<<<< HEAD
 
  frame = createElement("h4",someText);
}
function draw() {
  frame.remove();
  for(var i=0;i<lines.length;i++)
  {
    console.log("ok");
  }
  frame=createElement("h2", someText);
  frame.position(random(width), random(height));
//  frame.position(mouseX,mouseY);
=======
 // console.log(lines.length);
  //console.log("drawing");
}
function draw() {
 for(var i=0;i<lines.length;i++)
  {
    console.log("sup");
  frame[i]=createElement("h2", lines[i]);
  frame[i].position=(500,500);
  }
 // frame.position(mouseX,mouseY);
>>>>>>> 1e91b1c5155cc7e1924a381b113fc877272d39d4
  
  //readTextFile("ok.txt");
}
/*
async.forever(
    function(readTextFile,files) {
      //console.log("sup");
      //readTextFile(files);
    },
    function(err) {
        // if next is called with a value in its first parameter, it will appear
        // in here as 'err', and execution will stop.
    }
);
*/
function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
              console.log("ok");
                var allText = rawFile.responseText;
<<<<<<< HEAD
              //  var lines=allText.split("\n");
                someText=allText;
=======
                lines= allText.split("\n");
                console.log(lines.length);
>>>>>>> 1e91b1c5155cc7e1924a381b113fc877272d39d4
             //   console.log("changed some text to + " + someText);
            }
        }
    }
    rawFile.send(null);
}
