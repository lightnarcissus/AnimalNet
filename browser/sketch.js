require(['async'], function (async) {
    //foo is now loaded.
});
var frame;
var lines=[];
var someText="nothing";
var files="ok.txt";

function setup() {
  createCanvas(windowWidth,windowHeight);
 
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
  
  readTextFile("ok.txt");
}
/*
async.forever(
    function(readTextFile,files) {
      console.log("sup");
      readTextFile(files);
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
                var allText = rawFile.responseText;
              //  var lines=allText.split("\n");
                someText=allText;
             //   console.log("changed some text to + " + someText);
            }
        }
    }
    rawFile.send(null);
}
