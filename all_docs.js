var ReadJSONStream = require('read-json-stream').default;
ReadJSONStream('results.json')
  .done((err, data) => {
    if(err) {
      // handle error
    } else {
    	//console.log(data);
    }
  });

  refreshData(); // execute function


var counter=0;
  function refreshData()
            {
               
                x = 0.01;  // 5 Seconds
              ReadJSONStream('results.json')
              .done((err, data) => {
    if(err) {
      // handle error
    } else {
    	parseData(data);
    }
  });
                   // $.getJSON('results.json', function(jd) {
                   // $('#stage').append('<p> Using the old language of ' + jd.protocol+ ', they tried to reach out to someone specific. That someone was '+jd.host+' who responded in kind</p>');
                   // });
               // }
               // else
               // {
               //    $.getJSON('results.json', function(jd) {
               //     $('#stage').append('<p> Nothing</p>');
               //     });
               // }
    // Do your thing here

    setTimeout(refreshData, x*1000);
}

function parseData(data)
{
	console.log(data.ip_id);
	counter++;
	// if(counter==1)
	// {
	// 	console.log("A wizard with an arcane tool, " + data.user);	
	// }
	// else if(counter==2)
	// {
	// 	console.log("Sitting on " + data.srcaddr);

	// }
	// else if(counter==3)
	// {
	// 	console.log("Softly whistling towards "+data.host);

	// }
	// else if(counter==4)
	// {
	// 	console.log("They spoke the long forgotten language of "+ data.protocol);
	// }
	// else if(counter==5)
	// {
	// 	console.log("A handshake that was " + data.handshake_length + "had already occurred between them")
	// }
}

// var parser = JSONStream.parse(['rows', true]) //emit parts that match this path (any element of the rows array)
//   , req = request({url: 'http://isaacs.couchone.com/registry/_all_docs'})
//   , logger = es.mapSync(function (data) {  //create a stream that logs to stderr,
//     console.error(data)
//     return data  
//   })

// req.pipe(parser)
// parser.pipe(logger)
