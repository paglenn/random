using System.Net;
using System.Text;

namespace DayTwo {

  class Server {
     HttpListener listener ; 

     public Server() {
      listener = new HttpListener(); 
      listener.Prefixes.Add("http://localhost:8080/"); 

     }
    public void Start( ) {
      // making a new http listener 
      listener.Start(); 
      Console.WriteLine("Listening on port 8080...."); 

      while (true ) {
        // start witth context
        var ctx = listener.GetContext(); // get request and responses in one object 
        var resp = ctx.Response; 

        Console.WriteLine("Received request..."); 
        resp.Headers.Set("Content-Type","text/plain");

        // create plain text response and set to buffer 
        var text = " Hello there!"; 
        var buffer = Encoding.UTF8.GetBytes(text); 
        resp.ContentLength64 = buffer.Length; 

        var output = resp.OutputStream; 
        output.Write(buffer,0,buffer.Length);


        resp.StatusCode = (int) HttpStatusCode.OK; 
        resp.StatusDescription = "Success" ;

      
      }
    }
  }
}