var http = require('http');
var dgram = require('dgram');
var socketio = require('socket.io');
var buffer = require('buffer');

var app = http.createServer(handleRequest);
var io = socketio.listen(app);
var socket = dgram.createSocket('udp4');

function handleRequest (req, res) {
	res.writeHead(200);
	res.end('USRP Web - Node.js server');
}

var buf = []
socket.on('message', function(msg, rinfo) {
	
	// 1472 + 1472 + 1152 = 4096. 4096 / 4 = 1024
	
	var sample = [];
	var current = new Buffer(msg);
	
	for (var i = 0; i < current.length; i += 4)
	{
		buf.push(current.readFloatLE(i, true));
	}
	
	if (current.length == 1152)
	{
		// This is the last datagram
		
		if (buf.length == 1024)
		{
			io.sockets.emit('sample', buf);
		}
		
		buf = [];
	}
	else if (current.length != 1472)
	{
		// Discard the entire sample
		buf = [];
	}
	
});

socket.on("listening", function () {
	var address = socket.address();
	console.log("server listening " + address.address + ":" + address.port);
});

socket.bind(65234);
app.listen(1337);
