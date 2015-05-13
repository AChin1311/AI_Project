HEAD = '''<!DOCTYPE html>
<html>
<head>
   <meta charset="utf-8" />
   <style>
      #wrapper, #result{
         display: none;
      }
      #text {
         display: inline-block;
         vertical-align: top;
         width: 50%;
      }
      #btn-bar {
         text-align: center;
      }
      #ad {
         background-color: #DA4F49;
      }
      #nad {
         background-color: #5BB75B; 
      }
      .btn {
         color: white;
         font-size: 20px;
         display: inline-block; 
         padding: 6px 0px;
         width: 80px;
         margin: 0px 10px;
         vertical-align: center;
         cursor: pointer;
         border-radius: 5px;
         -moz-border-radius: 5px;
         -webkit-border-radius: 5px;
      }
      #num {
         float: left;
      }
   </style>
</head>
<body>
   <div id="wrapper">
      <div id="btn-bar">
         <span id="num"></span>
         <div class="btn" id="ad">Ad</div>
         <div class="btn" id="nad">Not Ad</div>
      </div>
      <div>
         <img id="img"/>
         <div id="text"></div>
      </div>
   </div>
   <pre id="result">
   </pre>
   <script src="http://code.jquery.com/jquery.min.js"></script>
   <script>
      var json = '''
TAIL = ''';
      var data = json.data;
      var ans = [];
      var len = data.length;
      var i = 0;

      function next(r) {
         //ans.push(r);
         data[i].label = r;
         ++i;
         if (i < len)
            show();
         else {
            $("#wrapper").hide();
            $("#result").text(JSON.stringify(json, null, 2)).show();
         }
      }
      function show() {
         $("#num").text(i);
         $("#img").attr("src", data[i].images.low_resolution.url);
         $("#text").html(data[i].caption.text);
      }

      $(function(){
         $("#ad").click(function() {
            next(1);
         })
         $("#nad").click(function() {
            next(0);
         });
         show();
         $("#wrapper").show();
      });
   </script>
</bodY>
</html>'''
