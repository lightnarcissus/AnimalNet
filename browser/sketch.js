require(['async'], function (async) {
    //foo is now loaded.
});
var frame=[];
var someText="nothing";
var files="ok.txt";
var lines=[];

function setup() {
  readTextFile("ok.txt");
  createCanvas(windowWidth,windowHeight);
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
  
  //readTextFile("ok.txt");
}
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
                lines= allText.split("\n");
                console.log(lines.length);
             //   console.log("changed some text to + " + someText);
            }
        }
    }
    rawFile.send(null);
}
