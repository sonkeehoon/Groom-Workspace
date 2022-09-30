var http = require( 'http' );
var content = function( req, res ) {
    res.writeHead( 200 );
    res.end( 'Docker Container - Node.js app' );
};

var web = http.createServer( content );
web.listen( 8080 );
