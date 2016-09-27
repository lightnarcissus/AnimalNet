require(['async'], function (async) {
    //foo is now loaded.
});
var frame;
var someText="nothing";
var files="ok.txt";

function setup() {
  createCanvas(windowWidth,windowHeight);
 
  frame = createElement("h2",someText);
}
function draw() {
  frame.remove();
  frame=createElement("h2", someText);
  frame.position(mouseX,mouseY);
  
  readTextFile("ok.txt");
}
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
                someText=allText;
             //   console.log("changed some text to + " + someText);
            }
        }
    }
    rawFile.send(null);
}
